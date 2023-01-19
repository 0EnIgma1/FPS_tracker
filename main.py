import cv2
import time

previous_time = 0

cap = cv2.VideoCapture(0)

avgfps = []

while True:
    ret, img = cap.read()

    current_time = time.time()

    fps = int(1/(current_time - previous_time))

    previous_time = current_time

    avgfps.append(fps)
    cv2.putText(img, f"FPS : {fps}", (10,25), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("frame",img)

    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break

#print(sum(avgfps)/len(avgfps))
cv2.destroyAllWindows()