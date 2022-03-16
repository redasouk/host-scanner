import requests, ssl, socket, sys, os, datetime, platform, time

###################### ABOUT AUTHOR ####################
'''

Scanner Created By Cool-Coder
Telegram contact : @jctacoder
Telegram channel : @godmode_tricks
Version : 1.0
Special Thanx : No 1
--> To modders n claimers : thats soo 2000 

'''
####################### ABOUT END #######################

counter = 1

r = '[0;1;31;91m'
g = '[0;1;32;92m'
k = '[0m'

try:

  os.system('clear') 
  z = open('.auth','r')
  z1 = z.readlines()
  z2 = z1[0].replace('\n','')
  
  if z2 == 'Coolcoder':
    print('safety check ... ')
    time.sleep(0.2)
    print(g+'passed'+k)
    time.sleep(0.2)
    print('auth check ...')
    time.sleep(0.2)
    print('complete')
    time.sleep(0.2)
    print(g+'success'+k)
    time.sleep(0.2)
    os.system('clear')
    time.sleep(0.5)
    print(g+'\nSystem Online'+k)
    time.sleep(0.2)

  else:

    print('safety check ... ')
    time.sleep(0.2)
    print(r+'failed'+k)
    time.sleep(0.2)
    print('Auth validation ...')
    time.sleep(0.2)
    print(r+'unsuccessful'+k)
    time.sleep(0.2)
    os.system('clear')
    time.sleep(0.5)
    print(r+'Modification detected!!'+k+'\nScript Shut Down sequence intiated...'+r+'\nClosed!!\n'+k)
    sys.exit(1)



  print('''
    |  --____ ---    contact : @jctacoder --------------+
    |   / ___|  ___ __ _ _ __  _ __   ___ _ __          |
    |   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|         |
  HOST   ___) | (_| (_| | | | | | | |  __/ | [ V 1.0 LTS ]
    |   |____/ \___\__,_|_| |_|_| |_|\___|_|
    |                                                   |
  CTRL + C : exit ----- channel : @godmode_tricks     --|''')
  print('    |' + ' ' * 32 + 'Coded By: ' + z2 + '|\n')

  file = open('hosts.txt','r')
  x = list(file)
  #print(x)
  print('\nscanning [' + str(len(x)) + '] hosts\n')

  for h in x:
    #print(h.replace('\n',''))
    x2 = h.replace('\n','').replace(' ','')
    y = 'http://'+x2
    y1 = requests.get(y)

    try:
      ctx = ssl.create_default_context()
      with ctx.wrap_socket(socket.socket(), server_hostname = x2 ) as s:
         s.connect((x2, 443))
         cert = s.getpeercert()

      subject = dict(x[0] for x in cert['subject'])
      issued_to = subject['commonName']
      issuer = dict(x[0] for x in cert['issuer'])
      issued_by = issuer['commonName']
    
    except:
      print('Host Error!!')

    #issued_by = issuer['commonName']
    counter2 = str(counter)
    print(counter2 + ".{'" + x2 +"', " + str(y1)  +  ", '" + issued_by + "'}")
    counter = counter + 1
    
  print('')

except KeyboardInterrupt:
  print('Exiting...')
  sys.exit(1)

except:
  print('Unconfirmed Error\n')
