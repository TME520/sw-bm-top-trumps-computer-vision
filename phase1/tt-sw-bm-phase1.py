try:
	import cv2
except ImportError:
	print('Cannot import cv2 computer vision PIP module')

import webbrowser

a = ''
olda = a
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

playername = input('What is your name?\n')
print(f'Hello {playername}')

# current_stage can be: init, start, loop, end
current_stage = 'init'
current_step = 1
# current_player can be: p1, cmp 
current_player = 'p1'
quit_game = False

while quit_game == False:
	try:
		_, img = cap.read()
		# detect and decode
		data, bbox, _ = detector.detectAndDecode(img)
		# check if there is a QRCode in the image
	except Exception as e:
		print(f'Image analysis error: {e}')
		pass
	if data:
		olda = a
		a = data
		if a != olda:
			match a:
				case 'SWTOPTRUMPSBM001':
					print('-> Card: SWTOPTRUMPSBM001\n\t> First Order Stormtrooper (15/2/13/5/5)')
				case 'SWTOPTRUMPSBM002':
					print('-> Card: SWTOPTRUMPSBM002\n\t> Jango Fett (23/15/35/35/11)')
				case 'SWTOPTRUMPSBM003':
					print('-> Card: SWTOPTRUMPSBM003\n\t> Padme Amidala (18/17/38/135/21)')
				case 'SWTOPTRUMPSBM004':
					print('-> Card: SWTOPTRUMPSBM004\n\t> Obi-Wan Kenobi (45/13/32/125/21)')
				case 'SWTOPTRUMPSBM005':
					print('-> Card: SWTOPTRUMPSBM005\n\t> Mace Windu (25/14/33/130/24)')
				case 'SWTOPTRUMPSBM006':
					print('-> Card: SWTOPTRUMPSBM006\n\t> General Grievous (33/17/38/85/19)')
				case 'SWTOPTRUMPSBM007':
					print('-> Card: SWTOPTRUMPSBM007\n\t> Luke Skywalker (8/7/22/70/14)')
				case 'SWTOPTRUMPSBM008':
					print('-> Card: SWTOPTRUMPSBM008\n\t> Leia Organa (42/13/32/150/27)')
				case 'SWTOPTRUMPSBM009':
					print('-> Card: SWTOPTRUMPSBM009\n\t> Han Solo (47/7/22/110/23)')
				case 'SWTOPTRUMPSBM010':
					print('-> Card: SWTOPTRUMPSBM010\n\t> Chewbacca (27/9/25/75/13)')
				case 'SWTOPTRUMPSBM011':
					print('-> Card: SWTOPTRUMPSBM011\n\t> Lando Calrissian (50/22/47/115/24)')
				case 'SWTOPTRUMPSBM012':
					print('-> Card: SWTOPTRUMPSBM012\n\t> Darth Vader (43/24/50/65/19)')
				case 'SWTOPTRUMPSBM013':
					print('-> Card: SWTOPTRUMPSBM013\n\t> Yoda (13/12/30/120/16)')
				case 'SWTOPTRUMPSBM014':
					print('-> Card: SWTOPTRUMPSBM014\n\t> Boba Fett (48/4/17/40/12)')
				case 'SWTOPTRUMPSBM015':
					print('-> Card: SWTOPTRUMPSBM015\n\t> Wicket W. Warrick (35/2/13/60/12)')
				case 'SWTOPTRUMPSBM016':
					print('-> Card: SWTOPTRUMPSBM016\n\t> BB-8 (28/10/27/30/10)')
				case 'SWTOPTRUMPSBM017':
					print('-> Card: SWTOPTRUMPSBM017\n\t> Rose Tico (5/11/28/55/13)')
				case 'SWTOPTRUMPSBM018':
					print('-> Card: SWTOPTRUMPSBM018\n\t> Maz Kanata (30/8/23/105/19)')
				case 'SWTOPTRUMPSBM019':
					print('-> Card: SWTOPTRUMPSBM019\n\t> Jabba The Hutt (3/12/30/50/13)')
				case 'SWTOPTRUMPSBM020':
					print('-> Card: SWTOPTRUMPSBM020\n\t> Rey (12/18/40/90/18)')
				case 'SWTOPTRUMPSBM021':
					print('-> Card: SWTOPTRUMPSBM021\n\t> Finn (22/19/42/140/22)')
				case 'SWTOPTRUMPSBM022':
					print('-> Card: SWTOPTRUMPSBM022\n\t> Poe Dameron (37/20/43/145/26)')
				case 'SWTOPTRUMPSBM023':
					print('-> Card: SWTOPTRUMPSBM023\n\t> Kylo Ren (40/22/47/80/19)')
				case 'SWTOPTRUMPSBM024':
					print('-> Card: SWTOPTRUMPSBM024\n\t> General Hux (10/21/45/100/17)')
				case 'SWTOPTRUMPSBM025':
					print('-> Card: SWTOPTRUMPSBM025\n\t> Clone Troopers (20/6/20/15/7)')
				case 'SWTOPTRUMPSBM026':
					print('-> Card: SWTOPTRUMPSBM026\n\t> Captain Phasma (32/16/37/95/18)')
				case 'SWTOPTRUMPSBM027':
					print('-> Card: SWTOPTRUMPSBM027\n\t> Emperor Palpatine (7/25/52/45/13)')
				case 'SWTOPTRUMPSBM028':
					print('-> Card: SWTOPTRUMPSBM028\n\t> Imperial Stormtrooper (17/3/15/10/6)')
				case 'SWTOPTRUMPSBM029':
					print('-> Card: SWTOPTRUMPSBM029\n\t> C-3PO (2/1/12/25/8)')
				case 'SWTOPTRUMPSBM030':
					print('-> Card: SWTOPTRUMPSBM030\n\t> R2-D2 (53/5/18/20/10)')
				case _:
					print('You are not seeing that message')
	cv2.imshow("QRCODEscanner", img)
	if cv2.waitKey(1) == ord("q"):
		quit_game = True

b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()

