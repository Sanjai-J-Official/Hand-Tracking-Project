import time
import cv2
import mediapipe as mp
cap=cv2.VideoCapture(0)

ptime=0
ctime=0

mphands=mp.solutions.hands
hands=mphands.Hands()
mpdraws=mp.solutions.drawing_utils 
while True:
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime

    out ,imgf=cap.read()
    img=cv2.flip(img,1)
    
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(imgrgb)
   # print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLMS in result.multi_hand_landmarks:
            for (id,lms) in enumerate(handLMS.landmark):
                h,w=img.shape[:2]
                cx,cy=int(lms.x*w),int(lms.y*h)
                print(id,cx,cy)
                if id==8:
                    
                    cv2.circle(img,(cx,cy),25,(0,90,255),cv2.FILLED)
            mpdraws.draw_landmarks(img,handLMS,mphands.HAND_CONNECTIONS)



    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),2)
    cv2.imshow('Img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
         
        
