import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            continue

        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgbFrame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                for point in landmarks.landmark:
                    height, width, _ = frame.shape
                    x, y = int(point.x * width), int(point.y * height)
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
