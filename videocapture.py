import cv2
import mediapipe as mp
import time
import handtrackingmodule as htm



def main(handno):
    ptime=0
    ctime=0
    cap=cv2.VideoCapture(0)
    detector=htm.handDetetor()
    
    while True:
        istrue ,imgf=cap.read()
        img=cv2.flip(imgf,1)
        
        img = detector.findHands(img,draw=False)
        listlms=detector.findposition(img,handno,draw=False)
        if len(listlms) !=0:
            print(listlms)
        

        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
        cv2.imshow('Img',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        
        
 
