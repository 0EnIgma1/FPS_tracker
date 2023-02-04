# FPS Tracker

fps_tracker helps to detect and measure the webcam's frame rate per second in any system.

This frame rate depends on both the computational speed and the webcam's capability as usual.

### You can install using pip:

```
pip3 install fpstracker
```

### Import package:

```
import cv2
import time
from fpstracker import Tracker
```

### You can call the module using the syntax:

```
trackfps.FPS(img, pos1, Average_FPS, pos2)
```

- img is the frame in which the FPS will be calculated and displayed
- pos1 is the pixel position of the measured FPS in text
- Average_FPS is the average FPS measured for every 5 seconds. This argument is optional and default is set to True
- pos2 is the pixel postion of the average FPS in text 

### Sample python program:

```
import cv2
import time
from fpstracker import Tracker
cap = cv2.VideoCapture(0)
trackfps = Tracker()
while True:
    ret, image = cap.read()
    img = trackfps.FPS(img = image)
    cv2.imshow('Frames', img)
    k = cv2.waitKey(1)
    if k & 0xFF == 27:
        break
cv2.destroyAllWindows()
```


[!PYPI package Link](https://pypi.org/project/fpstracker/1.0.0/)
