<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-4.x-brightgreen?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-Hands-orange?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/pyautogui-Automation-purple?style=for-the-badge">
</p>

<h1 align="center">
  <img src="https://img.icons8.com/color/96/keyboard.png" width="60"/>
  <span style="color:#4F8EF7">Hand Gesture Virtual Keyboard</span>
</h1>

<p align="center">
  <b>
    Control your computer with just your hands!<br>
    🖐️ Move the mouse, 🖱️ click, and <span style="color:#4F8EF7">type on a virtual keyboard</span> using real-time hand gestures.<br>
    <span style="background:#e0f7fa; color:#00796b; padding:4px 8px; border-radius:8px;">No hardware required — just your webcam!</span>
  </b>
</p>

---

## 🚀 Features

- <span style="color:#43a047">**Real-time hand tracking**</span> with MediaPipe
- <span style="color:#fbc02d">**Virtual keyboard**</span> rendered on your webcam feed
- <span style="color:#1976d2">**Mouse control**</span> with your left hand
- <span style="color:#d32f2f">**Type letters**</span> by pinching your right hand over keys
- <span style="color:#7b1fa2">**Arrow key swipes**</span> and <span style="color:#388e3c">spacebar gesture</span> support
- <span style="color:#0288d1">**No touch, no click, just gestures!**</span>


## 🖥️ How It Works

| Gesture | Action | Visual |
|--------|--------|--------|
| <img src="https://img.icons8.com/ios-filled/48/000000/hand-cursor.png" width="34" height="34" style="margin-right:14px;"/> **Left hand index** | Move mouse cursor | 🖱️ |
| <img src="https://img.icons8.com/ios-filled/48/000000/pinch.png" width="34" height="34" style="margin-right:14px;"/> **Left hand pinch** | Mouse click | 👆 |
| <img src="https://img.icons8.com/ios-filled/48/000000/hand-right.png" width="34" height="34" style="margin-right:14px;"/> **Right hand swipe** | Arrow keys (← ↑ → ↓) | ⬅️⬆️➡️⬇️ |
| <img src="https://img.icons8.com/ios-filled/48/000000/keyboard.png" width="34" height="34" style="margin-right:14px;"/> **Right hand pinch on key** | Type that letter | 🔤 |
| <img src="./readme_images/rock.png" width="34" height="34" style="margin-right:14px;"/> **Rock gesture** | Spacebar | ⬜ |

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/hand-gesture-keyboard.git
cd hand-gesture-keyboard

# 2. Install dependencies
pip install opencv-python mediapipe pyautogui

# 3. Run the main app
python main.py
```

---

## 🎮 Usage

- **Start the app:**  
  <span style="background:#4caf50; color:white; padding:4px 12px; border-radius:6px;">python main.py</span>
- **Show/Hide Keyboard:**  
  The virtual keyboard appears at the bottom of your webcam feed.
- **Mouse Control:**  
  Move your left hand’s index finger to move the mouse. Pinch (index + thumb) to click.
- **Typing:**  
  Use your right hand’s index finger to hover over a key, then pinch (index + thumb) to type.
- **Arrow Keys:**  
  Swipe your right hand’s index finger left/right/up/down for arrow keys.
- **Spacebar:**  
  Make a “rock” gesture (thumb near pinky) to press space.

---

## 🧩 File Structure

```plaintext
.
├── main.py                # Main gesture + keyboard app
├── virtual_keyboard.py    # Virtual keyboard rendering & logic
├── keyboardtest.py        # Minimal gesture test/demo
```

---

## 🧠 How Does It Work?

- **MediaPipe** detects your hands and tracks finger landmarks in real time.
- **OpenCV** displays the webcam feed and draws the virtual keyboard.
- **pyautogui** sends keyboard and mouse events to your OS.
- **Gestures** are mapped to actions:
  - **Left hand:** Mouse movement and click
  - **Right hand:** Virtual keyboard typing and arrow key swipes

---

## 💡 Customization

- Change the keyboard layout in `virtual_keyboard.py` (`KEY_ROWS`)
- Adjust gesture sensitivity thresholds in `main.py` and `keyboardtest.py`
- Add more gestures or keys as you wish!

