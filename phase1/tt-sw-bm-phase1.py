try:
  import cv2
except ImportError:
  print('Cannot import cv2 computer vision PIP module\nTry: pip3 install opencv-python')

try:
  import webbrowser
except ImportError:
  print('Cannot import the Web browser PIP module')

try:
  import os
except ImportError:
  print('Cannot import the OS PIP module')

try:
  from colorama import Fore, Style
except ImportError:
  print('Cannot import the Colorama PIP module\nTry: pip3 install colorama')

def draw_interface(player_name, stage, step, battle, round, instructions, card):
  os.system('clear')
  print(Fore.BLUE)
  print('--------------------------------------------------------------------------------')
  print(Fore.RED)
  print(f'>> {player_name} <<')
  print(Fore.WHITE)
  print(f'> Stage: {stage} -- Step: {step}')
  print(f'[{battle}/{round}]\n')
  print(f'> Instructions: {instructions}\n\n')
  print(f'> {card}')
  print(Fore.BLUE)
  print('--------------------------------------------------------------------------------')
  print(Style.RESET_ALL)

init_instructions = {
  'init01':{'text':'Shuffle the deck','validation':'Press ENTER','next':'init02'},
  'init02':{'text':'Human Player draws 1 card from the deck and QR-cams it','validation':'QR cam','next':'init03'},
  'init03':{'text':'Computer Player draws 1 card from the deck and QR-cams it','validation':'QR cam','next':'init04'},
  'init04':{'text':'AI compares the Top Trumps Galactic Legend category of both cards','validation':'Auto AI','next':'init05'},
  'init05':{'text':'Return the cards to the deck','validation':'Press ENTER','next':'init06'},
  'init06':{'text':'Shuffle the deck again','validation':'Press ENTER','next':'init01'}
}

cardData = {
  'SWTOPTRUMPSBM001':{'cardName':'First Order Stormtrooper', 'style':15, 'ambition':2, 'pride':13, 'leadership':5, 'ttgl':5},
  'SWTOPTRUMPSBM002':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM003':{'cardName':'Padme Amidala', 'style':18, 'ambition':17, 'pride':38, 'leadership':135, 'ttgl':21},
  'SWTOPTRUMPSBM004':{'cardName':'Obi-Wan Kenobi', 'style':45, 'ambition':13, 'pride':32, 'leadership':125, 'ttgl':21},
  'SWTOPTRUMPSBM005':{'cardName':'Mace Windu', 'style':25, 'ambition':14, 'pride':33, 'leadership':130, 'ttgl':24},
  'SWTOPTRUMPSBM006':{'cardName':'General Grievous', 'style':33, 'ambition':17, 'pride':38, 'leadership':85, 'ttgl':19},
  'SWTOPTRUMPSBM007':{'cardName':'Luke Skywalker', 'style':8, 'ambition':7, 'pride':22, 'leadership':70, 'ttgl':14},
  'SWTOPTRUMPSBM008':{'cardName':'Leia Organa', 'style':42, 'ambition':13, 'pride':32, 'leadership':150, 'ttgl':27},
  'SWTOPTRUMPSBM009':{'cardName':'Han Solo', 'style':47, 'ambition':7, 'pride':22, 'leadership':110, 'ttgl':23},
  'SWTOPTRUMPSBM010':{'cardName':'Chewbacca', 'style':27, 'ambition':9, 'pride':25, 'leadership':75, 'ttgl':13},
  'SWTOPTRUMPSBM011':{'cardName':'Lando Calrissian', 'style':50, 'ambition':22, 'pride':47, 'leadership':115, 'ttgl':24},
  'SWTOPTRUMPSBM012':{'cardName':'Darth Vader', 'style':43, 'ambition':24, 'pride':50, 'leadership':65, 'ttgl':19},
  'SWTOPTRUMPSBM013':{'cardName':'Yoda', 'style':13, 'ambition':12, 'pride':30, 'leadership':120, 'ttgl':16},
  'SWTOPTRUMPSBM014':{'cardName':'Boba Fett', 'style':48, 'ambition':4, 'pride':17, 'leadership':40, 'ttgl':12},
  'SWTOPTRUMPSBM015':{'cardName':'Wicket W. Warrick', 'style':35, 'ambition':2, 'pride':13, 'leadership':60, 'ttgl':12},
  'SWTOPTRUMPSBM016':{'cardName':'BB-8', 'style':28, 'ambition':10, 'pride':27, 'leadership':30, 'ttgl':10},
  'SWTOPTRUMPSBM017':{'cardName':'Rose Tico', 'style':5, 'ambition':11, 'pride':28, 'leadership':55, 'ttgl':13},
  'SWTOPTRUMPSBM018':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM019':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM020':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM021':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM022':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM023':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM024':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM025':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM026':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM027':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM028':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM029':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11},
  'SWTOPTRUMPSBM030':{'cardName':'Jango Fett', 'style':23, 'ambition':15, 'pride':35, 'leadership':35, 'ttgl':11}
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
current_instructions = init_instructions[current_step]['text'] + ' (' + init_instructions[current_step]['validation'] + ')'
current_validation = init_instructions[current_step]['validation']
current_card = ''
quit_game = False
refresh_screen = False
qr_ok = False

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
          qr_ok = True
        case 'SWTOPTRUMPSBM002':
          current_card = 'SWTOPTRUMPSBM002: Jango Fett (23/15/35/35/11)'
          qr_ok = True
        case 'SWTOPTRUMPSBM003':
          current_card = 'SWTOPTRUMPSBM003: Padme Amidala (18/17/38/135/21)'
          qr_ok = True
        case 'SWTOPTRUMPSBM004':
          current_card = 'SWTOPTRUMPSBM004: Obi-Wan Kenobi (45/13/32/125/21)'
          qr_ok = True
        case 'SWTOPTRUMPSBM005':
          current_card = 'SWTOPTRUMPSBM005: Mace Windu (25/14/33/130/24)'
          qr_ok = True
        case 'SWTOPTRUMPSBM006':
          current_card = 'SWTOPTRUMPSBM006: General Grievous (33/17/38/85/19)'
          qr_ok = True
        case 'SWTOPTRUMPSBM007':
          current_card = 'SWTOPTRUMPSBM007: Luke Skywalker (8/7/22/70/14)'
          qr_ok = True
        case 'SWTOPTRUMPSBM008':
          current_card = 'SWTOPTRUMPSBM008: Leia Organa (42/13/32/150/27)'
          qr_ok = True
        case 'SWTOPTRUMPSBM009':
          current_card = 'SWTOPTRUMPSBM009: Han Solo (47/7/22/110/23)'
          qr_ok = True
        case 'SWTOPTRUMPSBM010':
          current_card = 'SWTOPTRUMPSBM010: Chewbacca (27/9/25/75/13)'
          qr_ok = True
        case 'SWTOPTRUMPSBM011':
          current_card = 'SWTOPTRUMPSBM011: Lando Calrissian (50/22/47/115/24)'
          qr_ok = True
        case 'SWTOPTRUMPSBM012':
          current_card = 'SWTOPTRUMPSBM012: Darth Vader (43/24/50/65/19)'
          qr_ok = True
        case 'SWTOPTRUMPSBM013':
          current_card = 'SWTOPTRUMPSBM013: Yoda (13/12/30/120/16)'
          qr_ok = True
        case 'SWTOPTRUMPSBM014':
          current_card = 'SWTOPTRUMPSBM014: Boba Fett (48/4/17/40/12)'
          qr_ok = True
        case 'SWTOPTRUMPSBM015':
          current_card = 'SWTOPTRUMPSBM015: Wicket W. Warrick (35/2/13/60/12)'
          qr_ok = True
        case 'SWTOPTRUMPSBM016':
          current_card = 'SWTOPTRUMPSBM016: BB-8 (28/10/27/30/10)'
          qr_ok = True
        case 'SWTOPTRUMPSBM017':
          current_card = 'SWTOPTRUMPSBM017: Rose Tico (5/11/28/55/13)'
          qr_ok = True
        case 'SWTOPTRUMPSBM018':
          current_card = 'SWTOPTRUMPSBM018: Maz Kanata (30/8/23/105/19)'
          qr_ok = True
        case 'SWTOPTRUMPSBM019':
          current_card = 'SWTOPTRUMPSBM019: Jabba The Hutt (3/12/30/50/13)'
          qr_ok = True
        case 'SWTOPTRUMPSBM020':
          current_card = 'SWTOPTRUMPSBM020: Rey (12/18/40/90/18)'
          qr_ok = True
        case 'SWTOPTRUMPSBM021':
          current_card = 'SWTOPTRUMPSBM021: Finn (22/19/42/140/22)'
          qr_ok = True
        case 'SWTOPTRUMPSBM022':
          current_card = 'SWTOPTRUMPSBM022: Poe Dameron (37/20/43/145/26)'
          qr_ok = True
        case 'SWTOPTRUMPSBM023':
          current_card = 'SWTOPTRUMPSBM023: Kylo Ren (40/22/47/80/19)'
          qr_ok = True
        case 'SWTOPTRUMPSBM024':
          current_card = 'SWTOPTRUMPSBM024: General Hux (10/21/45/100/17)'
          qr_ok = True
        case 'SWTOPTRUMPSBM025':
          current_card = 'SWTOPTRUMPSBM025: Clone Troopers (20/6/20/15/7)'
          qr_ok = True
        case 'SWTOPTRUMPSBM026':
          current_card = 'SWTOPTRUMPSBM026: Captain Phasma (32/16/37/95/18)'
          qr_ok = True
        case 'SWTOPTRUMPSBM027':
          current_card = 'SWTOPTRUMPSBM027: Emperor Palpatine (7/25/52/45/13)'
          qr_ok = True
        case 'SWTOPTRUMPSBM028':
          current_card = 'SWTOPTRUMPSBM028: Imperial Stormtrooper (17/3/15/10/6)'
          qr_ok = True
        case 'SWTOPTRUMPSBM029':
          current_card = 'SWTOPTRUMPSBM029: C-3PO (2/1/12/25/8)'
          qr_ok = True
        case 'SWTOPTRUMPSBM030':
          current_card = 'SWTOPTRUMPSBM030: R2-D2 (53/5/18/20/10)'
          qr_ok = True
        case _:
          current_card = 'That message you see not.'
          qr_ok = False

      draw_interface(current_player, current_stage, current_step, current_battle, current_round, current_instructions, current_card)

  # cv2.imshow("QRCODEscanner", img)

  if cv2.waitKey(1) == ord("q"):
    quit_game = True

  match current_validation:
    case 'Press ENTER':
      input()
      current_step = init_instructions[current_step]['next']
      current_instructions = init_instructions[current_step]['text'] + ' (' + init_instructions[current_step]['validation'] + ')'
      current_validation = init_instructions[current_step]['validation']
      refresh_screen = True
    case 'QR cam':
      if refresh_screen == True:
        draw_interface(current_player, current_stage, current_step, current_battle, current_round, current_instructions, current_card)
        refresh_screen = False
      if qr_ok == True:
        current_step = init_instructions[current_step]['next']
        current_instructions = init_instructions[current_step]['text'] + ' (' + init_instructions[current_step]['validation'] + ')'
        current_validation = init_instructions[current_step]['validation']
        refresh_screen = True
        qr_ok = False
    case 'Auto AI':
      print('Waiting on AI')
    case 'Auto Human':
      print('Waiting on Human')
    case _:
      print('You no see this')

cap.release()
cv2.destroyAllWindows()

