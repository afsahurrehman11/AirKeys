import cv2
import pyautogui
import time

# Keyboard layout
KEY_ROWS = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM")
]

KEY_SIZE = 60
KEY_PADDING = 15
KB_TOP_LEFT = (100, 500)  # This will be overwritten from main.py

last_pressed_time = {}
press_delay = 0.5  # seconds to wait before allowing another press of same key

# Function to draw the virtual keyboard
def draw_keyboard(frame, hovered_key=None):
    x0, y0 = KB_TOP_LEFT

    # Draw outer frame
    kb_width = max(len(r) for r in KEY_ROWS) * (KEY_SIZE + KEY_PADDING)
    kb_height = len(KEY_ROWS) * (KEY_SIZE + KEY_PADDING)
    cv2.rectangle(frame, (x0 - 10, y0 - 10), (x0 + kb_width + 10, y0 + kb_height + 10), (220, 220, 220), thickness=2)

    for row_idx, row in enumerate(KEY_ROWS):
        for col_idx, key in enumerate(row):
            x = x0 + col_idx * (KEY_SIZE + KEY_PADDING)
            y = y0 + row_idx * (KEY_SIZE + KEY_PADDING)

            # Highlight if hovered
            if hovered_key == (row_idx, col_idx):
                color = (180, 255, 180)  # light green
            else:
                color = (245, 245, 245)  # light gray

            # Draw key background
            cv2.rectangle(frame, (x, y), (x + KEY_SIZE, y + KEY_SIZE), color, -1)
            # Draw key border
            cv2.rectangle(frame, (x, y), (x + KEY_SIZE, y + KEY_SIZE), (160, 160, 160), 2)
            # Put letter
            cv2.putText(frame, key, (x + 18, y + 42), cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 30, 30), 2)

# Function to handle hovering and pressing
def handle_virtual_keys(frame, index_tip, thumb_tip):
    """
    frame        : the current OpenCV image (numpy array)
    index_tip    : mediapipe landmark, x/y in [0..1] relative to frame
    thumb_tip    : same for thumb
    """
    global KB_TOP_LEFT, last_pressed_time

    # 1) map landmarks into FRAME‑pixel coords
    fh, fw = frame.shape[:2]
    fx = int(index_tip.x * fw)
    fy = int(index_tip.y * fh)

    hover = None

    # 2) check each key box
    x0, y0 = KB_TOP_LEFT
    for r, row in enumerate(KEY_ROWS):
        for c, key in enumerate(row):
            key_x = x0 + c * (KEY_SIZE + KEY_PADDING)
            key_y = y0 + r * (KEY_SIZE + KEY_PADDING)
            if key_x <= fx <= key_x + KEY_SIZE and key_y <= fy <= key_y + KEY_SIZE:
                hover = (r, c)

                # 3) detect pinch in normalized space
                pd = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
                if pd < 0.04:
                    now = time.time()
                    kc = key.lower()
                    if kc not in last_pressed_time or (now - last_pressed_time[kc]) > press_delay:
                        pyautogui.press(kc)
                        last_pressed_time[kc] = now
                        cv2.putText(frame, f"Pressed {key}", (50,50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                break
        if hover:
            break

    return frame, hover
