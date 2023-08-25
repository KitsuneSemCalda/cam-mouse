import cv2
import sys
import mediapipe as mp
import logging

is_debug = False

if len(sys.argv) > 1:
    if sys.argv[1] == 'debug':
        is_debug = True

if is_debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(filename="gesture_control.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def main():
    hand_detected_count = 0
    hand_undetected_count = 0
    consecutive_frames_threshold = 5
    max_consecutive_frames_without_hand = 7
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('X','2','6','4'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            continue

        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgbFrame)
        
        if results.multi_hand_landmarks:
            hand_detected_count += 1
            hand_undetected_count = 0
            if hand_detected_count >= consecutive_frames_threshold:
                logging.info("Hand Detected")

            for landmarks in results.multi_hand_landmarks:
                for point in landmarks.landmark:
                    height, width, _ = frame.shape
                    x, y = int(point.x * width), int(point.y * height)
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        else:
            hand_detected_count = 0
            hand_undetected_count += 1
            if hand_undetected_count >= max_consecutive_frames_without_hand:
                logging.info("Hand Out of View")
        if is_debug:
            cv2.imshow("Hand Tracking", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
