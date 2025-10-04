from ultralytics import YOLO
import cv2
import serial
import time

model = YOLO(r'C:\Users\adnan.DESKTOP-Q8SIVEA\Documents\HACK-Rev\env\best.pt')

arduino = serial.Serial(port='COM18 ', baudrate=250000, timeout=1)
time.sleep(2)

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    raise ValueError("Webcam could not be opened. Check your webcam or permissions.")

FRAME_WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
FRAME_HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
FRAME_CENTER_X = FRAME_WIDTH // 2
FRAME_CENTER_Y = FRAME_HEIGHT // 2

TOLERANCE = 20

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video. Exiting.")
        break

    results = model(frame, conf=0.5)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        box_center_x = (x1 + x2) // 2
        box_center_y = (y1 + y2) // 2

        error_x = FRAME_CENTER_X - box_center_x
        error_y = FRAME_CENTER_Y - box_center_y

        arduino.write(f"{error_x},{error_y}\n".encode())

        label = "Drone"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print(f"Error X: {error_x}, Error Y: {error_y}")

    cv2.imshow("Drone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
