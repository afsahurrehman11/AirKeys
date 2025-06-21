import cv2
import mediapipe as mp
import pyautogui
import virtual_keyboard
from virtual_keyboard import draw_keyboard, handle_virtual_keys

CAM_W, CAM_H, TARGET_FPS = 1280, 720, 60
pyautogui.PAUSE = 0

# ── Mediapipe Hands Init ────────────────────────────────────────────────────
mp_hands = mp.solutions.hands
hands    = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# ── Video Capture Setup ──────────────────────────────────────────────────────
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  CAM_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_H)
cap.set(cv2.CAP_PROP_FPS,          TARGET_FPS)

screen_w, screen_h = pyautogui.size()
# state for right‑hand arrow swipes
prev_rx = prev_ry = None

# Precompute keyboard size & fixed position (center bottom)
ks, kp = virtual_keyboard.KEY_SIZE, virtual_keyboard.KEY_PADDING
rows = virtual_keyboard.KEY_ROWS
kb_w = max(len(r) for r in rows)*(ks+kp)
kb_h = len(rows)*(ks+kp)
# center bottom, with 20px margin
fixed_x0 = (CAM_W - kb_w) // 2
fixed_y0 = CAM_H - kb_h - 20
virtual_keyboard.KB_TOP_LEFT = (fixed_x0, fixed_y0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # -----------------------
    # 1) Preprocess frame
    # -----------------------
    frame = cv2.flip(frame, 1)
    rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    hover = None

    if results.multi_hand_landmarks:
        for lm, handedness in zip(results.multi_hand_landmarks,
                                  results.multi_handedness):
            label = handedness.classification[0].label  # "Left" or "Right"
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

            # common landmarks
            idx_tip   = lm.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = lm.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # -----------------------
            # 2) Left hand → mouse
            # -----------------------
            if label == "Left":
                # map index tip to screen coords
                cx = int(idx_tip.x * screen_w)
                cy = int(idx_tip.y * screen_h)
                pyautogui.moveTo(cx, cy, duration=0)

                # pinch to click
                dist = ((idx_tip.x - thumb_tip.x)**2 +
                        (idx_tip.y - thumb_tip.y)**2)**0.5
                if dist < 0.04:
                    pyautogui.click()

            # -----------------------
            # 3) Right hand → keyboard + arrows
            # -----------------------
            else:  # label == "Right"
                # → typing on fixed keyboard
                frame, hover = handle_virtual_keys(frame, idx_tip, thumb_tip)

                # → arrow swipes
                rx = int(idx_tip.x * screen_w)
                ry = int(idx_tip.y * screen_h)
                if prev_rx is not None:
                    dx, dy = rx - prev_rx, ry - prev_ry
                    if abs(dx) > abs(dy):
                        if dx > 30:    pyautogui.press('right')
                        elif dx < -30: pyautogui.press('left')
                    else:
                        if dy > 30:    pyautogui.press('down')
                        elif dy < -30: pyautogui.press('up')
                prev_rx, prev_ry = rx, ry

    # -----------------------
    # 4) Draw fixed keyboard
    # -----------------------
    draw_keyboard(frame, hover)

    # -----------------------
    # 5) Show & exit
    # -----------------------
    cv2.imshow("Gesture + Virtual Keyboard", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
