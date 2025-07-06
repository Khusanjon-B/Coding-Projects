import pygame
import sys
from pixelObject import pixelObject
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import time
import os

# === Setup ===
pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Classification Game")
clock = pygame.time.Clock()

# === Utilities ===
def color(value):
    gray = int(max(0.0, min(1.0, value)) * 255)
    return (gray, gray, gray)

def draw_title():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Number Classification', True, 'black')
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 12))
    screen.blit(text, text_rect)

def show_text(text, extra=0, size=32):
    font = pygame.font.Font('freesansbold.ttf', size)
    text_surface = font.render(text, True, 'black')
    text_rect = text_surface.get_rect(center=(850, HEIGHT // 2 + extra))
    screen.blit(text_surface, text_rect)

def make_text_button(x, y, width, height, label, pressed, font_size=28):
    color_btn = (200, 200, 200) if pressed else (220, 220, 220)
    pygame.draw.rect(screen, color_btn, (x, y, width, height))
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(label, True, 'black')
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text, text_rect)
    return pygame.Rect(x, y, width, height)

# === Pixel Grid ===
pixels = [pixelObject(20, 20, 50 + (i % 28) * 20, 100 + (i // 28) * 20) for i in range(28*28)]
mouse_held = False

# === Neural Network ===
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.input_layer = nn.Conv2d(1, 32, 5, padding=2)
        self.activation1 = nn.ReLU()
        self.maxpool1 = nn.MaxPool2d(2)
        self.hidden_convolution1 = nn.Conv2d(32, 64, 5, padding=2)
        self.activation2 = nn.ReLU()
        self.maxpool2 = nn.MaxPool2d(2)
        self.hidden_convolution2 = nn.Conv2d(64, 128, 5, padding=2)
        self.activation3 = nn.ReLU()
        self.maxpool3 = nn.MaxPool2d(2)
        self.hidden_convolution3 = nn.Conv2d(128, 256, 5, padding=2)
        self.activation4 = nn.ReLU()
        self.maxpool4 = nn.MaxPool2d(2)
        self.flatten = nn.Flatten()
        self.hidden_linear = nn.Linear(256, 1024)
        self.activation5 = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        self.output_layer = nn.Linear(1024, 10)

    def forward(self, x):
        x = self.maxpool1(self.activation1(self.input_layer(x)))
        x = self.maxpool2(self.activation2(self.hidden_convolution1(x)))
        x = self.maxpool3(self.activation3(self.hidden_convolution2(x)))
        x = self.maxpool4(self.activation4(self.hidden_convolution3(x)))
        x = self.flatten(x)
        x = self.activation5(self.hidden_linear(x))
        x = self.dropout(x)
        return self.output_layer(x)

# === Models and Training Setup ===
goodModel = NeuralNetwork()
goodModel.load_state_dict(torch.load("Coding/Num Class Project/cnn_model_1.pth"))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(goodModel.parameters(), lr=0.001)

def pixels_to_tensor(pixels):
    pixel_values = [[pixel.getValue() * 255 for pixel in pixels[row * 28:(row + 1) * 28]] for row in range(28)]
    return torch.tensor(pixel_values, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

def train_one_step(model, input_tensor, target_tensor):
    model.train()
    optimizer.zero_grad()
    output = model(input_tensor)
    loss = criterion(output, target_tensor)
    loss.backward()
    optimizer.step()
    return loss.item(), torch.argmax(output).item()

def get_input_tensor(pixels):
    pixel_values = []
    for row in range(28):
        row_vals = []
        for col in range(28):
            val = pixels[row * 28 + col].getValue()
            row_vals.append(val * 255)
        pixel_values.append(row_vals)
    input_tensor = torch.tensor(pixel_values, dtype=torch.float32)
    input_tensor = input_tensor.unsqueeze(0).unsqueeze(0)
    return input_tensor

# === State Variables ===
train_mode = False
number = -1
lastPredicted = -1
lasttime = -666
submit_rect = pygame.Rect(800, 280, 160, 50)

# === Main Loop ===
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_held = True
            mx, my = pygame.mouse.get_pos()
            if make_text_button(800, 200, 160, 50, "Train" if not train_mode else "Training", train_mode).collidepoint(mx, my):
                train_mode = not train_mode
            if submit_rect.collidepoint(mx, my) and train_mode and number != -1:
                input_tensor = pixels_to_tensor(pixels)
                target_tensor = torch.tensor([number], dtype=torch.long)
                _, lastPredicted = train_one_step(goodModel, input_tensor, target_tensor)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_held = False
        elif event.type == pygame.KEYDOWN:
            if train_mode and pygame.K_0 <= event.key <= pygame.K_9:
                number = event.key - pygame.K_0

            if event.key == pygame.K_RETURN and train_mode and number != -666:
                goodModel.train()
                input_tensor = get_input_tensor(pixels)
                target_tensor = torch.tensor([number])
                train_one_step(goodModel, input_tensor, target_tensor)
                number = -666  # Reset

            elif event.key == pygame.K_c:
                for pixel in pixels:
                    pixel.value = 0


    screen.fill((255, 255, 255))
    draw_title()

    mx, my = pygame.mouse.get_pos()
    if mouse_held:
        for pixel in pixels:
            pixel.hover(mx, my)

    blank = 0
    for pixel in pixels:
        pygame.draw.rect(screen, color(pixel.getValue()), pixel.getRectangle())
        if pixel.getValue() == 0:
            blank += 1

    # Clear button
    clear_rect = make_text_button(800, 50, 100, 50, "Clear", False)
    if clear_rect.collidepoint(mx, my) and mouse_held:
        for pixel in pixels:
            pixel.value = 0

    # Train mode button
    make_text_button(800, 200, 160, 50, "Train" if not train_mode else "Training", train_mode)

    # Submit button in train mode
    if train_mode:
        make_text_button(800, 280, 160, 50, "Submit", False)
        show_text("Type number", extra=60, size=24)
        if number != -1:
            show_text(f"Current Label: {number}", extra=90, size=24)

    # === Live Prediction (both modes) ===
    if time.time() - lasttime > 0.25 and blank < 28 * 28:
        lasttime = time.time()
        goodModel.eval()
        input_tensor = pixels_to_tensor(pixels)
        with torch.no_grad():
            output = goodModel(input_tensor)
        lastPredicted = torch.argmax(output).item()

    if lastPredicted != -1:
        show_text(f"Predicted: {lastPredicted}")

    pygame.display.flip()
    clock.tick(240)

pygame.quit()
sys.exit()
