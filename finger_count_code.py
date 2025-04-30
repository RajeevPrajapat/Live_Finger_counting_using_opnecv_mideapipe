import cv2
import mediapipe as mp

# Initialize the MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# OpenCV video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 840)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 580)

# Hand tracking configuration
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands
        result = hands.process(rgb_frame)

        # Initialize finger counts
        left_count = 0
        right_count = 0

        if result.multi_hand_landmarks and result.multi_handedness:
            
            for idx, (hand_landmarks, handedness) in enumerate(zip(result.multi_hand_landmarks, result.multi_handedness)):

                # Draw landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks
                landmarks = []
                for lm in hand_landmarks.landmark:
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmarks.append((cx, cy))

                # Finger tips and base points
                tip_ids = [4, 8, 12, 16, 20]
                fingers = []

                # Thumb detection (adjusted for mirrored image)
                label = handedness.classification[0].label
                if label == "Left":
                    if landmarks[tip_ids[0]][0] > landmarks[tip_ids[0] - 1][0]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                else:
                    if landmarks[tip_ids[0]][0] < landmarks[tip_ids[0] - 1][0]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Other 4 fingers
                for id in range(1, 5):
                    if landmarks[tip_ids[id]][1] < landmarks[tip_ids[id] - 2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Count fingers
                finger_count = fingers.count(1)

                # Assign count based on handedness
                if label == "Left":
                    left_count = finger_count
                else:
                    right_count = finger_count

                # Show which fingers are raised
                finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
                raised_fingers = [finger_names[i] for i, f in enumerate(fingers) if f == 1]

                cv2.putText(frame, f'{label} Raised: {", ".join(raised_fingers)}',
                            (10, 200 + 50 * idx),  # Offset per hand
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Total fingers
        total_fingers = left_count + right_count

        # Display the finger count for both hands
        cv2.putText(frame, f'Left Hand: {left_count}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.putText(frame, f'Right Hand: {right_count}', (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the total finger count in red
        cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the frame
        cv2.imshow("Both Hands Finger Counter", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release and close windows
cap.release()
cv2.destroyAllWindows()
