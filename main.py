import cv2
import time

previous_time = 0
average_fps = "'/'"

cap = cv2.VideoCapture(0)

avgfps = []

initial_time =time.time()

while True:
    ret, img = cap.read()

    current_time = time.time()

    fps = int(1/(current_time - previous_time))

    avgfps.append(fps)

    previous_time = current_time

    timer = time.time() - initial_time

    if timer > 5:
        average_fps = int(sum(avgfps)/len(avgfps))
        initial_time = time.time()
    
    cv2.putText(img, f"FPS : {fps}", (10,25), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.putText(img, f"Avg FPS : {average_fps}", (420,25), cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
    cv2.imshow("frame",img)

    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break

#print(sum(avgfps)/len(avgfps))
cv2.destroyAllWindows()