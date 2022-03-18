import requests
import time
import os
tokenz = os.environ['acctoken']
def advertise(gameId):
    link222 = f'https://www.roblox.com/games/{gameId}/'
    messageE = f'''
      *2 Player Games*
     {link222}
  '''
    jsonn = {
        'content': f'{messageE}',
        'tts': 'false'
    }

    headers = {
        'authorization': tokenz
    }
    #hentai society
    r5 = requests.post('https://discord.com/api/v9/channels/894272415234945045/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r5.status_code == 429:
        sheesh = r5.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r5.status_code == 200:
        print("   Success sent message ")
    else:
        print(r5.status_code)
        #swift
    r6 = requests.post('https://discord.com/api/v9/channels/948011442773311508/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r6.status_code == 429:
        sheesh = r6.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r6.status_code == 200:
        print("  Success sent message ")
    else:
        #condogames.xyz
        print(r6.status_code)
    r7 = requests.post('https://discord.com/api/v9/channels/947932686603931738/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r7.status_code == 429:
        sheesh = r7.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r7.status_code == 200:
        print("  Success sent message ")
    else:
        #sunset co
        print(r7.status_code)
    r8 = requests.post('https://discord.com/api/v9/channels/945127156349034526/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r8.status_code == 429:
        sheesh = r8.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r8.status_code == 200:
        print("  Success sent message ")
    else:
        print(r8.status_code)
        #pokey
    r9 = requests.post('https://discord.com/api/v9/channels/938975235850518608/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r9.status_code == 429:
        sheesh = r9.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r9.status_code == 200:
        print("  Success sent message ")
    else:
        print(r9.status_code)
    #frost condos
    r10 = requests.post('https://discord.com/api/v9/channels/915430109979234405/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r10.status_code == 429:
        sheesh = r10.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r10.status_code == 200:
        print("  Success sent message ")
    else:
        print(r10.status_code)
     #condohub
    r11 = requests.post('https://discord.com/api/v9/channels/883135560527515678/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r11.status_code == 429:
        sheesh = r11.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r11.status_code == 200:
        print("  Success sent message ")
    else:
        print(r10.status_code)
        #xhub
    r12 = requests.post('https://discord.com/api/v9/channels/908880597915676702/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r12.status_code == 429:
        sheesh = r12.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r12.status_code == 200:
        print("  Success sent message ")
    else:
        print(r12.status_code)
        #lust condos
    r13 = requests.post('https://discord.com/api/v9/channels/949269266769784902/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r13.status_code == 429:
        sheesh = r13.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r13.status_code == 200:
        print("  Success sent message ")
    else:
        print(r13.status_code)
        #thot
    r14 = requests.post('https://discord.com/api/v9/channels/944551851502764032/messages', headers=headers, json = jsonn)
    time.sleep(5)
    if r14.status_code == 429:
        sheesh = r14.json()['retry_after']
        print(f'  Error Slowmode {sheesh}')
    elif r14.status_code == 200:
        print("  Success sent message ")
    else:
        print(r14.status_code)
