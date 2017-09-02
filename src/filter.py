# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import numpy as np
def applyCustomColorMap(im_gray) :

    #create lookup table to accomodate maximum of 256 and minimum of 1 pixel value, for 3 streams red, green and blue
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    for i in xrange(256):
        lut[i, 0, 0] = max(min((127 - i) * 2, 255), 0)
        if i < 127 else 0
        lut[i, 0, 1] = max(min((i - 127) * 2, 255), 0)
        if i > 127 else 0
        lut[i, 0, 2] = max(min((127 - i) * 2, 255), 0) if i < 127 else 0    #map the color gradient created using lookup tables for the gray image "im_gray".
    im_color = cv2.LUT(im_gray, lut)
    #return new image created using color gradient
    return im_color;

cap = cv2.VideoCapture(0)


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	#frame = cv2.applyColorMap(frame, cv2.COLORMAP_PINK)

	frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

	frame = applyCustomColorMap(frame)
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
