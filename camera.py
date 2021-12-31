import cv2

def video():
    LerCamera = cv2.VideoCapture(0)
    if LerCamera.isOpened():
        while True:
            validacao, frame = LerCamera.read()
            cv2.imshow("", frame)
            teclaefps = cv2.waitKey(1)
            if teclaefps == 27:
                print("a camera será fechada.")
                break
        LerCamera.release()
        cv2.destroyAllWindows()
    else:
        print('nenhuma webcam encpmtrada.')
        
video()