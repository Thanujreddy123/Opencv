import cv2
import time
import posemodel as pm
cap = cv2.VideoCapture(0)
pTime = 0
detector=pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findpose(img,Draw=False)
    lmlist = detector.findPosition(img, Draw=False)
    '''
    if len(lmlist) >= 25:
        print(lmlist[25])
        cv2.circle(img, (lmlist[25][1], lmlist[25][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 26:
        print(lmlist[26])
        cv2.circle(img, (lmlist[26][1], lmlist[26][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 27:
        print(lmlist[27])
        cv2.circle(img, (lmlist[27][1], lmlist[27][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 28:
        print(lmlist[28])
        cv2.circle(img, (lmlist[28][1], lmlist[28][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 29:
        print(lmlist[29])
        cv2.circle(img, (lmlist[29][1], lmlist[29][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 30:
        print(lmlist[30])
        cv2.circle(img, (lmlist[30][1], lmlist[30][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 31:
        print(lmlist[31])
        cv2.circle(img, (lmlist[31][1], lmlist[31][2]), 10, (255, 0, 0), cv2.FILLED)
    if len(lmlist) >= 32:
        print(lmlist[32])
        cv2.circle(img, (lmlist[32][1], lmlist[32][2]), 10, (255, 0, 0), cv2.FILLED)'''
    if len(lmlist) >= 25 and len(lmlist) >= 26 and len(lmlist) >= 27 and len(lmlist) >= 28 and len(lmlist) >= 29 and len(lmlist) >= 30 and len(lmlist) >= 31 and len(lmlist) >= 31:
        cv2.circle(img, (lmlist[25][1], lmlist[25][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[26][1], lmlist[26][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[27][1], lmlist[27][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[28][1], lmlist[28][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[29][1], lmlist[29][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[30][1], lmlist[30][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[31][1], lmlist[31][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (lmlist[32][1], lmlist[32][2]), 10, (0, 0, 255), cv2.FILLED)
        cv2.line(img,(lmlist[28][1], lmlist[28][2]),(lmlist[30][1], lmlist[30][2]),(0,0,255),5)
        cv2.line(img, (lmlist[26][1], lmlist[26][2]), (lmlist[28][1], lmlist[28][2]), (255, 255, 255),5)
        cv2.line(img, (lmlist[25][1], lmlist[25][2]), (lmlist[27][1], lmlist[27][2]), (255, 255, 255), 5)
        cv2.line(img, (lmlist[27][1], lmlist[27][2]), (lmlist[29][1], lmlist[29][2]), (255, 255, 255), 5)
        cv2.line(img, (lmlist[29][1], lmlist[29][2]), (lmlist[31][1], lmlist[31][2]), (255, 255, 255), 5)
        cv2.line(img, (lmlist[28][1], lmlist[28][2]), (lmlist[32][1], lmlist[32][2]), (255, 255, 255), 5)
        cv2.line(img, (lmlist[32][1], lmlist[32][2]), (lmlist[30][1], lmlist[30][2]), (255, 255, 255), 5)
        cv2.line(img, (lmlist[31][1], lmlist[31][2]), (lmlist[27][1], lmlist[27][2]), (255, 255, 255), 5)
    # if results.pose_landmarks:
    # mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    # for id, lm in enumerate(results.pose_landmarks.landmark):
    # h, w, c = img.shape
    # print(id, lm)
    # cx, cy = int(lm.x * w), int(lm.y * h)
    # cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 0), 3)
    cv2.imshow("image", img)
    if cv2.waitKey(10) == 27:
        break