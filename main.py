
import cv2, pyautogui
from hand_tracking import HandDetector
from virtual_keyboard import create_keyboard
from utils import is_inside

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
keys = create_keyboard()
delay_counter, click_delay = 0, 8

while True:
    ret, img = cap.read()
    if not ret: break
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (950, 700))
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)

    for key in keys:
        key.draw(img)

    if lmList:
        ix, iy = lmList[8][1], lmList[8][2]
        cv2.circle(img, (ix, iy), 12, (255, 0, 255), cv2.FILLED)

        for key in keys:
            if is_inside(ix, iy, key):
                key.draw(img, color=(0, 255, 0))
                if delay_counter == 0:
                    if key.text == "Space":
                        pyautogui.press("space")
                    elif key.text in ["Shift", "Caps", "Tab"]:
                        key_map = {
                            "Backspace": "backspace",
                            "Enter": "enter",
                            "Tab": "tab",
                            "Caps": "capslock",
                            "Shift": "shift",
                            "Space": "space",
                            "`": "`",
                            "-": "minus",
                            "=": "equals",
                            "[": "bracketleft",
                            "]": "bracketright",
                            "\\": "backslash",
                            ";": "semicolon",
                            "'": "quote",
                            ",": "comma",
                            ".": "period",
                            "/": "slash"
                        }

                        key_to_press = key_map.get(key.text, key.text.lower())

                        try:
                            pyautogui.press(key_to_press)
                        except Exception as e:
                            print(f"⛔ Error pressing key '{key.text}': {e}")

                    elif key.text == "Backspace":
                        pyautogui.press("backspace")
                    elif key.text == "Enter":
                        pyautogui.press("enter")
                    else:
                        pyautogui.press(key.text.lower())
                    delay_counter = click_delay
                break

    if delay_counter: delay_counter -= 1
    cv2.imshow("Hand Keyboard", img)
    if cv2.waitKey(1) & 0xFF == 27: break
