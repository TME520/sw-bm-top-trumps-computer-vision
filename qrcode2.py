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
			case 'SWTOPTRUMPSBM002':
				print('SWTOPTRUMPSBM002 - Jango Fett (23/15/35/35/11)')
			case 'SWTOPTRUMPSBM003':
				print('SWTOPTRUMPSBM003 - Padme Amidala (18/17/38/135/21)')
			case 'SWTOPTRUMPSBM004':
				print('SWTOPTRUMPSBM004 - Obi-Wan Kenobi (45/13/32/125/21)')
			case 'SWTOPTRUMPSBM005':
				print('SWTOPTRUMPSBM005 - Mace Windu (25/14/33/130/24)')
			case 'SWTOPTRUMPSBM006':
				print('SWTOPTRUMPSBM006 - General Grievous (33/17/38/85/19)')
			case 'SWTOPTRUMPSBM007':
				print('SWTOPTRUMPSBM007 - Luke Skywalker (8/7/22/70/14)')
			case 'SWTOPTRUMPSBM008':
				print('SWTOPTRUMPSBM008 - Leia Organa (42/13/32/150/27)')
			case 'SWTOPTRUMPSBM009':
				print('SWTOPTRUMPSBM009 - Han Solo (47/7/22/110/23)')
			case 'SWTOPTRUMPSBM010':
				print('SWTOPTRUMPSBM010 - Chewbacca (27/9/25/75/13)')
			case 'SWTOPTRUMPSBM011':
				print('SWTOPTRUMPSBM011 - Lando Calrissian (50/22/47/115/24)')
			case 'SWTOPTRUMPSBM012':
				print('SWTOPTRUMPSBM012 - Darth Vader (43/24/50/65/19)')
			case 'SWTOPTRUMPSBM013':
				print('SWTOPTRUMPSBM013 - Yoda (13/12/30/120/16)')
			case 'SWTOPTRUMPSBM014':
				print('SWTOPTRUMPSBM014 - Boba Fett (48/4/17/40/12)')
			case 'SWTOPTRUMPSBM015':
				print('SWTOPTRUMPSBM015 - Wicket W. Warrick (35/2/13/60/12)')
			case 'SWTOPTRUMPSBM016':
				print('SWTOPTRUMPSBM016 - BB-8 (28/10/27/30/10)')
			case 'SWTOPTRUMPSBM017':
				print('SWTOPTRUMPSBM017 - Rose Tico (5/11/28/55/13)')
			case 'SWTOPTRUMPSBM018':
				print('SWTOPTRUMPSBM018 - Maz Kanata (30/8/23/105/19)')
			case 'SWTOPTRUMPSBM019':
				print('SWTOPTRUMPSBM019 - Jabba The Hutt (3/12/30/50/13)')
			case 'SWTOPTRUMPSBM020':
				print('SWTOPTRUMPSBM020 - Rey (12/18/40/90/18)')
			case 'SWTOPTRUMPSBM021':
				print('SWTOPTRUMPSBM021 - Finn (22/19/42/140/22)')
			case 'SWTOPTRUMPSBM022':
				print('SWTOPTRUMPSBM022 - Poe Dameron (37/20/43/145/26)')
			case 'SWTOPTRUMPSBM023':
				print('SWTOPTRUMPSBM023 - Kylo Ren (40/22/47/80/19)')
			case 'SWTOPTRUMPSBM024':
				print('SWTOPTRUMPSBM024 - General Hux (10/21/45/100/17)')
			case 'SWTOPTRUMPSBM025':
				print('SWTOPTRUMPSBM025 - Clone Troopers (20/6/20/15/7)')
			case 'SWTOPTRUMPSBM026':
				print('SWTOPTRUMPSBM026 - Captain Phasma (32/16/37/95/18)')
			case 'SWTOPTRUMPSBM027':
				print('SWTOPTRUMPSBM027 - Emperor Palpatine (7/25/52/45/13)')
			case 'SWTOPTRUMPSBM028':
				print('SWTOPTRUMPSBM028 - Imperial Stormtrooper (17/3/15/10/6)')
			case 'SWTOPTRUMPSBM029':
				print('SWTOPTRUMPSBM029 - C-3PO (2/1/12/25/8)')
			case 'SWTOPTRUMPSBM030':
				print('SWTOPTRUMPSBM030 - R2-D2 (53/5/18/20/10)')
			case _:
				print('You are not seeing that message')
		break
	cv2.imshow("QRCODEscanner", img)
	if cv2.waitKey(1) == ord("q"):
		break

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()

