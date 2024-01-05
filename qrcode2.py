import cv2
import webbrowser

cap = cv2.VideoCapture(0) 
# initialize the cv2 QRCode detector 
detector = cv2.QRCodeDetector()

while True:
	_, img = cap.read()
	# detect and decode 
	data, bbox, _ = detector.detectAndDecode(img) 
	# check if there is a QRCode in the image 
	if data: 
		a=data 
		print(f'a: {a}')
		match a:
			case 'SWTOPTRUMPSBM001':
				print('SWTOPTRUMPSBM001 - First Order Stormtrooper (15/2/13/5/5)')
			case _:
				print('You are not seeing that message')
		break
	cv2.imshow("QRCODEscanner", img)
	if cv2.waitKey(1) == ord("q"):
		break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()

