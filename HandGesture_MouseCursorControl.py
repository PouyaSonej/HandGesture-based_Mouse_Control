import cv2
import mediapipe as mp 
import pyautogui

Capture_hands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
camera = cv2.VideoCapture(0)
x1 = y1 = x2 = y2 = 0
while True:
    _, img = camera.read()
    img_height, img_width , _ = img.shape
    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output_hands = Capture_hands.process(rgb_img)
    all_hands = output_hands.multi_hand_landmarks
    if all_hands:
        for hand in all_hands:
            drawing_option.draw_landmarks(img, hand)
            one_hand_landmarks = hand.landmark
            for id, lm in enumerate(one_hand_landmarks):
                x = int(lm.x * img_width)
                y = int(lm.y * img_height)
                if id ==8:
                    m_x = int(screen_width / img_width * x)
                    m_y = int(screen_height / img_height * y)
                    cv2.circle(img, (x,y), 10, (0,255,255))
                    pyautogui.moveTo(m_x, m_y)
                    x1 = x
                    y1 = y
                if id ==4:                    
                    x2 = x
                    y2 = y
                    cv2.circle(img, (x,y), 10, (0,255,255))
        dist = y2 - y1 
        print(dist)
        if(dist<70):
            pyautogui.click()
            print("Clicked")
    cv2.imshow("Hand movement video capture", img)
    key = cv2.waitKey(100)
    if key == 27:
        break
camera.release()
cv2.destroyAllWindows()