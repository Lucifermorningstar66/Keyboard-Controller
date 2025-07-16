
import cv2

class Key:
    def __init__(self, pos, text, w=60, h=60):
        self.pos = pos
        self.text = text
        self.w, self.h = w, h

    def draw(self, img, color=(200, 200, 200)):
        x, y = self.pos
        cv2.rectangle(img, (x, y), (x + self.w, y + self.h), color, cv2.FILLED)
        cv2.rectangle(img, (x, y), (x + self.w, y + self.h), (50, 50, 50), 2)
        font_scale = 1.5 if len(self.text) == 1 else 1.0
        offset_x = 20 if len(self.text) == 1 else 10
        cv2.putText(img, self.text, (x + offset_x, y + int(self.h * 0.7)),
                    cv2.FONT_HERSHEY_PLAIN, font_scale, (0, 0, 0), 2)

def create_keyboard():
    layout = [
        ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace"],
        ["Tab","Q","W","E","R","T","Y","U","I","O","P","[","]","\\"],
        ["Caps","A","S","D","F","G","H","J","K","L",";","'","Enter"],
        ["Shift","Z","X","C","V","B","N","M",",",".","/","Shift"],
        ["Space"]
    ]

    keys = []
    screen_width = 950
    key_height = 45
    row_spacing = 8
    start_y = 30

    for row_idx, row in enumerate(layout):
        total_row_width = 0
        key_widths = []

        for key in row:
            w = 70 if key in ["Tab", "Caps", "Shift"] else \
                90 if key == "Backspace" else \
                250 if key == "Space" else \
                45
            total_row_width += w + 10
            key_widths.append(w)
        total_row_width -= 10

        start_x = (screen_width - total_row_width) // 2

        cur_x = start_x
        for key, w in zip(row, key_widths):
            keys.append(Key((cur_x, start_y + row_idx * (key_height + row_spacing)), key, w, key_height))
            cur_x += w + 8

    return keys

