# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import numpy as np
import requests
import urllib

def applyCustomColorMap(im_gray) :

    #create lookup table to accomodate maximum of 256 and minimum of 1 pixel value, for 3 streams red, green and blue
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    for i in xrange(256):
        lut[i, 0, 0] = max(min((127 - i) * 2, 255), 0)        if i < 127 else 0
        lut[i, 0, 1] = max(min((i - 127) * 2, 255), 0)        if i > 127 else 0
        lut[i, 0, 2] = max(min((127 - i) * 2, 255), 0) if i < 127 else 0    #map the color gradient created using lookup tables for the gray image "im_gray".
    im_color = cv2.LUT(im_gray, lut)
    #return new image created using color gradient
    return im_color;

cap = cv2.VideoCapture(0)

url = 'https://openapi.npm.gov.tw/v1/rest/collection/search/04000975'
KEY = '04175c5c-33b9-463c-a973-4fd6679d31ae'
params = {'lang': 'eng'}
headers = {"apiKey": "04175c5c-33b9-463c-a973-4fd6679d31ae"}
res = requests.get(url, params=params, headers=headers, verify=False)
data = res.json()
req = urllib.urlopen(data['result'][0]['imgUrl'])
print('ArticleSubject   ='), data['result'][0]['ArticleSubject']


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	#frame = cv2.imdecode(arr,-1)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	frame = cv2.applyColorMap(frame, 8)

	#frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

	#frame = applyCustomColorMap(frame)
	font = cv2.FONT_HERSHEY_SIMPLEX
	
	cv2.putText(frame,data['result'][0]['ArticleSubject'],(10,200), font, 1,(255,255,255),2)
	
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
