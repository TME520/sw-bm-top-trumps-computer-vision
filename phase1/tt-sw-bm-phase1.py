try:
  import cv2
except ImportError:
  print('Cannot import cv2 computer vision PIP module')

import webbrowser
import os

def draw_interface(player_name, stage, step, battle, round, instructions, card):
  print('--------------------------------------------------------------------------------')
  print(f'>> {player_name} <<')
  print(f'> Stage: {stage}') 
  print(f'> Step: {step}')
  print(f'[{battle}/{round}]\n')
  print(f'> Instructions: {instructions}\n\n')
  print(f'> {card}')
  print('--------------------------------------------------------------------------------')

init_instructions = {
  'init01':{'text':'Shuffle the deck','validation':'press_space'},
  'init02':{'text':'Human Player draws 1 card from the deck and QR-cams it','validation':'qrcam'},
  'init03':{'text':'Computer Player draws 1 card from the deck and QR-cams it','validation':'qrcam'},
  'init04':{'text':'AI compares the Top Trumps Galactic Legend category of both cards','validation':'auto_ai'},
  'init05':{'text':'Return the cards to the deck','validation':'press_space'},
  'init06':{'text':'Shuffle the deck again','validation':'press_space'}
}

a = ''
olda = a
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

os.system('clear')

playername = input('What is your name?\n')
print(f'\n\t>> Hello {playername}\n')

# current_player can be: Human Player, Computer Player 
current_player = playername
# current_stage can be: init, start, loop, end
current_stage = 'Init'
current_step = 'init01'
current_battle = 1
current_round = 1
current_instructions = init_instructions[current_step]['text']
current_card = ''
quit_game = False

os.system('clear')

draw_interface(current_player, current_stage, current_step, current_battle, current_round, current_instructions, current_card)

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
      os.system('clear')

      match a:
        case 'SWTOPTRUMPSBM001':
          current_card = 'SWTOPTRUMPSBM001: First Order Stormtrooper (15/2/13/5/5)'
        case 'SWTOPTRUMPSBM002':
          current_card = 'SWTOPTRUMPSBM002: Jango Fett (23/15/35/35/11)'
        case 'SWTOPTRUMPSBM003':
          current_card = 'SWTOPTRUMPSBM003: Padme Amidala (18/17/38/135/21)'
        case 'SWTOPTRUMPSBM004':
          current_card = 'SWTOPTRUMPSBM004: Obi-Wan Kenobi (45/13/32/125/21)'
        case 'SWTOPTRUMPSBM005':
          current_card = 'SWTOPTRUMPSBM005: Mace Windu (25/14/33/130/24)'
        case 'SWTOPTRUMPSBM006':
          current_card = 'SWTOPTRUMPSBM006: General Grievous (33/17/38/85/19)'
        case 'SWTOPTRUMPSBM007':
          current_card = 'SWTOPTRUMPSBM007: Luke Skywalker (8/7/22/70/14)'
        case 'SWTOPTRUMPSBM008':
          current_card = 'SWTOPTRUMPSBM008: Leia Organa (42/13/32/150/27)'
        case 'SWTOPTRUMPSBM009':
          current_card = 'SWTOPTRUMPSBM009: Han Solo (47/7/22/110/23)'
        case 'SWTOPTRUMPSBM010':
          current_card = 'SWTOPTRUMPSBM010: Chewbacca (27/9/25/75/13)'
        case 'SWTOPTRUMPSBM011':
          current_card = 'SWTOPTRUMPSBM011: Lando Calrissian (50/22/47/115/24)'
        case 'SWTOPTRUMPSBM012':
          current_card = 'SWTOPTRUMPSBM012: Darth Vader (43/24/50/65/19)'
        case 'SWTOPTRUMPSBM013':
          current_card = 'SWTOPTRUMPSBM013: Yoda (13/12/30/120/16)'
        case 'SWTOPTRUMPSBM014':
          current_card = 'SWTOPTRUMPSBM014: Boba Fett (48/4/17/40/12)'
        case 'SWTOPTRUMPSBM015':
          current_card = 'SWTOPTRUMPSBM015: Wicket W. Warrick (35/2/13/60/12)'
        case 'SWTOPTRUMPSBM016':
          current_card = 'SWTOPTRUMPSBM016: BB-8 (28/10/27/30/10)'
        case 'SWTOPTRUMPSBM017':
          current_card = 'SWTOPTRUMPSBM017: Rose Tico (5/11/28/55/13)'
        case 'SWTOPTRUMPSBM018':
          current_card = 'SWTOPTRUMPSBM018: Maz Kanata (30/8/23/105/19)'
        case 'SWTOPTRUMPSBM019':
          current_card = 'SWTOPTRUMPSBM019: Jabba The Hutt (3/12/30/50/13)'
        case 'SWTOPTRUMPSBM020':
          current_card = 'SWTOPTRUMPSBM020: Rey (12/18/40/90/18)'
        case 'SWTOPTRUMPSBM021':
          current_card = 'SWTOPTRUMPSBM021: Finn (22/19/42/140/22)'
        case 'SWTOPTRUMPSBM022':
          current_card = 'SWTOPTRUMPSBM022: Poe Dameron (37/20/43/145/26)'
        case 'SWTOPTRUMPSBM023':
          current_card = 'SWTOPTRUMPSBM023: Kylo Ren (40/22/47/80/19)'
        case 'SWTOPTRUMPSBM024':
          current_card = 'SWTOPTRUMPSBM024: General Hux (10/21/45/100/17)'
        case 'SWTOPTRUMPSBM025':
          current_card = 'SWTOPTRUMPSBM025: Clone Troopers (20/6/20/15/7)'
        case 'SWTOPTRUMPSBM026':
          current_card = 'SWTOPTRUMPSBM026: Captain Phasma (32/16/37/95/18)'
        case 'SWTOPTRUMPSBM027':
          current_card = 'SWTOPTRUMPSBM027: Emperor Palpatine (7/25/52/45/13)'
        case 'SWTOPTRUMPSBM028':
          current_card = 'SWTOPTRUMPSBM028: Imperial Stormtrooper (17/3/15/10/6)'
        case 'SWTOPTRUMPSBM029':
          current_card = 'SWTOPTRUMPSBM029: C-3PO (2/1/12/25/8)'
        case 'SWTOPTRUMPSBM030':
          current_card = 'SWTOPTRUMPSBM030: R2-D2 (53/5/18/20/10)'
        case _:
          current_card = 'That message you see not.'

      draw_interface(current_player, current_stage, current_step, current_battle, current_round, current_instructions, current_card)

  # cv2.imshow("QRCODEscanner", img)

  if cv2.waitKey(1) == ord("q"):
    quit_game = True

cap.release()
cv2.destroyAllWindows()

