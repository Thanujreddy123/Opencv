import cv2
import mediapipe as mp
import time
mpDraw=mp.solutions.drawing_utils

class poseDetector():

    def __init__(self,mode=False,upBody=False,smooth=True,detectionCon=0.5,trackCon=0.5):

        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)

    def findpose(self,img,Draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if Draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    def findPosition(self,img,Draw=True):
        lmlist=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id,cx,cy])
                if Draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        return lmlist

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector=poseDetector()
    while True:
        success, img = cap.read()
        img=detector.findpose(img)
        lmlist=detector.findPosition(img,Draw=False)
        if len(lmlist)>=25:
            print(lmlist[25])
            cv2.circle(img, (lmlist[25][1], lmlist[25][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=26:
            print(lmlist[26])
            cv2.circle(img, (lmlist[26][1], lmlist[26][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=27:
            print(lmlist[27])
            cv2.circle(img, (lmlist[27][1], lmlist[27][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=28:
            print(lmlist[28])
            cv2.circle(img, (lmlist[28][1], lmlist[28][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=29:
            print(lmlist[29])
            cv2.circle(img, (lmlist[29][1], lmlist[29][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist) >= 30:
                print(lmlist[30])
                cv2.circle(img, (lmlist[30][1], lmlist[30][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=31:
            print(lmlist[31])
            cv2.circle(img, (lmlist[31][1], lmlist[31][2]), 10, (255, 0, 0), cv2.FILLED)
        if len(lmlist)>=32:
            print(lmlist[32])
            cv2.circle(img, (lmlist[32][1], lmlist[32][2]), 10, (255, 0, 0), cv2.FILLED)
        #if results.pose_landmarks:
            #mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
            #for id, lm in enumerate(results.pose_landmarks.landmark):
                #h, w, c = img.shape
                #print(id, lm)
                #cx, cy = int(lm.x * w), int(lm.y * h)
                #cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        #cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 0), 3)
        cv2.imshow("image", img)
        if cv2.waitKey(10) == 27:
            break


if __name__ == "__main__":
    main()