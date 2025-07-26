# 🚪🔧 DIY Smart Garage Door Opener – A Learning Journey 🔧🚪

This project started from a simple need: I wanted a garage door opener. But instead of buying one, I chose to build it myself to better understand hardware design, embedded systems, and mechanical integration.

---

## 🛠️ Project Overview

### **Phase 1 – Proof of Concept**
- **ESP32** microcontroller
- **SG90 servo** to press the garage button
- **Powered by a power bank**
- Housed in a simple **3D-printed mount**

This initial prototype worked conceptually, but it lacked structural integrity and sufficient power for reliable operation.

---

### **Version 2 – Improved Design**
- Switched to **LiPo battery power**
- Added a **battery level indicator** (with red, yellow, green LEDs)
- Included a **physical power switch** to prevent idle drain
- Upgraded to an **MG90S servo** (still underpowered for the task)
- Moved to a **perfboard** for permanent soldering (my first time using one!)
- Built a **seamless 3D-printed enclosure** with internal battery compartment

> 🧰 I used **Onshape** for all 3D modeling. The second version was much more planned, with an aim to fully enclose all components except the moving arm.

---

## 📸 Demo and Media

- ▶️ **Version 2 in action:**  
  [YouTube Video](https://youtube.com/shorts/SxfYtOG-8IA?feature=share)

- 🧩 **CAD Models (Onshape):**  
  - [Version 1 Model](https://cad.onshape.com/documents/0aacb74aa05e59e247364e0c/w/c6d8a8912145856f3c92b16d/e/c99ce0e9ce6d822e1db50cd2)  
  - [Version 2 Model](https://cad.onshape.com/documents/1459060a4a21909e479f6e4a/w/def8b11744a731030349f386/e/fe1937bca27357c312be0ec1)

---

## 💡 Key Features

- **Wireless Control via Blynk IoT App**
- **Servo-driven mechanical actuation**
- **Battery voltage sensing using a voltage divider**
- **LED indicators for battery level (red, yellow, green)**
- **Power management switch**
- **Compact, custom enclosure**

---

## 🧠 Lessons Learned

- Soldering perfboards can be tricky — copper pads lifted, and my soldering iron tips wore out quickly.
- Wiring inside a tight enclosure is tough — my first lid didn't close properly due to poor wire layout and tolerance issues.
- 3D modeling in **Onshape** has its quirks, especially coming from a **SOLIDWORKS** background.
- I now have a strong motivation to learn **PCB design** to eliminate messy wiring.

---

## 🔮 Next Steps

- Redesign the enclosure with **better tolerances** and **threaded inserts**
- Move to a **custom PCB** for cleaner assembly
- Test a **stronger servo** for more reliable actuation
- Explore **RF control** to mimic garage remotes directly instead of pressing a physical button

---

## 📂 Source Code

You can find all code and setup instructions in the project directory:
👉 [GitHub Code](https://github.com/Khusanjon-B/Coding-Projects/tree/main/Garage%20Door%20Clicker)

---

This was a great opportunity to apply and grow my skills in **electronics**, **embedded programming**, and **mechanical design**. Thanks for reading!
