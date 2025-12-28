# 🌤️ Raspberry Pi Brightness Overlay (Wayland)

A lightweight **Wayland-native brightness controller** for Raspberry Pi OS that uses `ddcutil` to control external monitor brightness.

---

## ✨ Features

* ✅ Works on **Wayland** (Raspberry Pi OS default)
* ✅ Uses **ddcutil** (hardware-level brightness control)
* ✅ Lightweight (Python + GTK)
* ✅ Clean on-screen brightness overlay

---

## 🧠 How It Works

* Uses **gtk-layer-shell** to display a popup overlay
* Overlay appears on top of all windows
* Brightness is controlled via **DDC/CI**
* Designed for **external monitors**
* Made and tested for Raspberry Pi 4 

---

## 📦 Requirements

### Hardware

* Raspberry Pi 4 
* External monitor that supports **DDC/CI**

### Software

* Raspberry Pi OS (Wayland session)
* Python 3.9+
* `ddcutil`
* GTK 3
* gtk-layer-shell

---

## 🔧 Installation

### 1️⃣ Install dependencies

```bash
sudo apt update
sudo apt install -y \
  python3-gi \
  gir1.2-gtk-3.0 \
  gtk-layer-shell \
  ddcutil
```

---

### 2️⃣ Enable I²C (required for ddcutil)

```bash
sudo usermod -aG i2c $USER
sudo modprobe i2c-dev
reboot
```

After reboot, verify:

```bash
ddcutil detect
```

You should see your monitor listed.

---

## ▶️ Running the Application

```bash
python3 main.py
```

When launched:

* A brightness overlay appears
* You can change brightness
* Overlay stays on top
* Closes automatically when dismissed

---

## 🛠 Troubleshooting

### ❌ Brightness not changing?

✔ Ensure monitor supports DDC
✔ Try:

```bash
ddcutil getvcp 10
```

### ❌ Overlay doesn’t appear?

✔ Ensure you're on **Wayland**

```bash
echo $XDG_SESSION_TYPE
```

Must return:

```
wayland
```

### ❌ Permission error?

Run:

```bash
sudo usermod -aG i2c $USER
reboot
```

---

## 📌 Notes

* This project **does not use tray icons** (Wayland limitation)
* Uses modern Wayland-compatible APIs
* Works independently of desktop environment
* Tested on Raspberry Pi OS (Bookworm / Trixie)

---

## 🚀 Future Enhancements (Optional)

* 🔆 Auto-detect brightness on startup
* ⌨️ Media key support
* 🕒 Auto-hide timeout
* 💾 Save brightness across reboots
* 📦 Package as `.deb`

---

