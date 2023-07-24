import cv2
import numpy as np

# Set up the video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# Set up the RTSP stream
rtsp_url = "rtsp://your-rtsp-server-ip-address:port/stream_name"  # Replace with your RTSP server details
# stream = cv2.VideoWriter(rtsp_url, cv2.CAP_FFMPEG, 0, (640, 480))

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Failed to open webcam")
    exit()

# Capture and stream frames
while True:
    # Read frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Write frame to the RTSP stream
    # stream.write(frame)

    # Display the frame locally (optional)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
# stream.release()
cv2.destroyAllWindows()

"""
Before running the code, make sure you have OpenCV installed (pip install opencv-python) and 
replace the "rtsp://your-rtsp-server-ip-address:port/stream_name" 
with the appropriate RTSP server details. 
You may need to adjust the resolution ((640, 480)) and other parameters to fit your needs.

Once you run this script, it will capture frames from the webcam and 
stream them through RTSP to the specified server.
"""