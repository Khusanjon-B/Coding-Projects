# OLED Sensor Display System

This project is a **real-time environmental and volume monitoring system** built using an **Arduino**, an **SSD1306 OLED display**, a **DHT11 sensor**, and a **potentiometer**. The goal was to create a compact and responsive display that continuously shows the current **date**, **time**, **temperature**, **humidity**, and **volume level** (via potentiometer). The idea came from my interest in combining sensors with dynamic visual feedback—and I built the system from scratch, iterating on both hardware layout and software logic.


![image](/Time-Date-Temp%20Display%20Using%20Arduino/Setup.jpg)

---

## ✨ Features

- 📅 **Live date and time** displayed and updated every second  
- 🌡️ **Temperature and humidity** readings via DHT11 sensor (sampled every 3 seconds)  
- 🎚️ **Potentiometer-based volume control** displayed as both a % and a dynamic bar  
- ⚡️ **Optimized OLED rendering** — only redraws what's needed to reduce flicker and lag  
- 🔄 **Serial time sync** support (PC can send time like `Sun May 18 17:21:31 2025`)  

---

## 🛠 Hardware Used

| Component           | Description                         |
|--------------------|-------------------------------------|
| Arduino (Uno/Nano) | Main microcontroller                |
| SSD1306 OLED       | 128x64 I2C display (Adafruit style) |
| DHT11 Sensor       | For temperature and humidity        |
| Potentiometer      | Acts as analog volume controller    |
| Jumper Wires       | Standard prototyping setup          |
| Breadboard         | For wiring everything together      |

---

## 🧠 How It Works

- On boot, the Arduino requests the current time over Serial.  
- Every second, the display updates the on-screen clock using `tickTime()`.  
- Every 3 seconds, the DHT11 is polled and the screen updates its environmental readings.  
- The potentiometer is read in near-real-time (~10–50ms), and its value is displayed both numerically and graphically.  
- To optimize speed, only **sections of the screen are cleared** and redrawn—avoiding a full `clearDisplay()` call unless needed.

---

## 🖼 OLED Display Layout

|-----------------------------|
| Sun May 18 2025 | ← Date

| 17:21:31 | ← Time

| Vol: 72% | ← Potentiometer reading

| [██████████ ] | ← Volume bar

| T: 23.4C | ← Temperature
| H: 48.7% | ← Humidity
|-----------------------------|


---

## 🔧 Code Structure Highlights

- `refreshDisplay(int pot)`: Main function that draws everything to the screen.  
- `tickTime()`: Advances time by 1 second without RTC.  
- `mapValue(...)`: Custom float-friendly map function.  
- `clearLine(x, y, size)`: Clears only one text line instead of whole screen.  
- `drawVolumeBar(...)`: Draws a white bar proportional to volume %.  

---

## 🚧 Future Improvements

- Fix the laggy volume bar
- Add support for a real-time clock (RTC) module  
- Log data to SD card or send over Bluetooth  
- Add weather iconography or scrolling text  
- Touch buttons to set time without PC serial input  

---

## 🤝 Acknowledgments

This project was my own idea, and I led the design and implementation.  
Special thanks to [ChatGPT](https://openai.com/chatgpt) for helping me debug tricky OLED rendering, timing intervals, and structuring my display logic. It was a great way to collaborate, learn, and push the limits of what a small microcontroller can do.
