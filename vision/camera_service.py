import cv2

class CameraService:
    def capture(self):
        camera = cv2.VideoCapture(0)
        success, frame = camera.read()
        if success:
            cv2.imwrite('capture.jpg', frame)
        camera.release()
        return success
