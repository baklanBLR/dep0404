#! /usr/bin/env python
# -*- coding: utf-8 -*-
##from smtplib import _Reply
import telebot
import os
import json
import traceback
import requests
import sys
import urllib.request
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
   

class PHOTOGAME:
    MainLink = 'https://oren.en.cx/GameDetails.aspx?gid=74782'
    ind1 = MainLink.find('x/', 0 ,-1)
    ind2 = MainLink.rfind('gid=',0,-1)
    Number = MainLink[ind2 + 4:]
    Typegame = 'photohunt'
    InLink = MainLink[:ind1 + 2] + 'gameengines/' + Typegame + '/play/' +Number
    Tip = ''
    levels  = []
    Number = '1'
    reglink =MainLink[:MainLink.find('.',1,len(MainLink))] + '.en.cx/Login.aspx'
    



def calcluator(marka, dostavka, m3, abn):
    itog = 0
    cena = 0
    abnp = 0
    if (m3 < 18):
        itog = cena * m3 + dostavka * 18 

    return(itog+ abnp)


def dost(mesto):
    wrongname = "Что-то такого названия нет у меня в прайсе"
    baza = ('Антракт',	600,
'алакуль',	800,
'барышево',	1700,
'борисово',	1500,
'мичуринское',	1400,
'красноозерное П',	1250,
'красноозерное В',	800,
'коробицыно',	1200,
'васильево',	1300,
'светлое',	1300,
'правдино',	1200,
'ски хаус',	1200,
'волочаевка',	1000,
'большая медведица',	1100,
'северная корона',	900,
'золотая сотка',	900,
'красносельское',	1200,
'синицыно',	1100,
'кучерово',	1400,
'овсяное',	900,
'адмирал',	900,
'цвелодубово',	700,
'староселье',	1200,
'нагорное',	1100,
'олимпиец',	1400,
'грибное',	1300,
'первомайское',	700,
'черниговка',	900,
'солодово',	900,
'актер',	600,
'галкатика',	600,
'гелиос',	600,
'капелла',	600,
'рощино',	500,
'лебяжье',	600,
'горьковское',	700,
'хуторок',	600,
'флора',	600,
'бойково',	700,
'яковлево',	700,
'семашко',	700,
'сопки',	700,
'серово',	600,
'ушково',	600,
'молодежное',	700,
'зеленогорск',	700,
'решетниково',	600,
'солнечный берег',	1200,
'днп зеркальное',	1100,
'уткино',	900,
'огоньково',	800,
'подгорное',	800,
'рябово',	1200,
'красная долина',	1200,
'поляны',	900,
'краснофлотское',	1100,
'клеверное',	1100,
'клеверная бухта',	1100,
'сосоновый бор',	1200,
'заполье',	1000,
'снт поляна',	1000,
'белокаменка',	700,
'комарово',	800,
'репино',	800,
'солнечное',	900,
'белоостров',	1100,
'акватория',	700,
'алые паруса',	700,
'финский бриз',	700,
'пески',	800,
'золотые пески',	800,
'зеленая роща',	900,
'озерки',	1100,
'парнас',	1000,
'пески 29',	800,
'37 км приморского',	1000,
'чистый ключ',	1000,
'осетрово',	0,
'карпикюля',	1000,
'лесное',	1000,
'стеклянный',	1100,
'зеркальный',	1200,
'яппиля',	1100,
'кирпичное',	900,
'кирилловское',	900,
'ягодное р',	500,
'ягодное с',	900,
'климово',	1400,
'пушное',	900,
'победа',	900,
'каннельярви',	1000,
'счемиозерье',	1000,
'ольшаники',	700,
'краснознаменка',	800,
'старорусское',	1200,
'каменка',	1300,
'владимировка',	1300,
'мамонтовка',	1300,
'парнас',	1000,
'система',	1000,
'крутой берег',	800,
'береговая горка',	1100,
'зеленый холм',	1100,
'три берега',	700,
'озерки р',	999,
'озерки',	1100,
'солнечный  мыс',	1100,
'лужки',	1200,
'ермилово',	1500,
'приморск',	1700,
'снт рощино',	600,
'лебедь 1',	600,
'лебедь 1',	600,
'лебедь 2',	600,
'марченково',	700,
'чуфрино',	700,
'ильичево',	700,
'конта',	600,
'ганино',	900,
'тарасово',	900,
'ленинское',	800,
'глубокое',	1200,
'приветнинское',	800,
'приветное',	800,
'смолячково',	700,
'чайка',	7000,
'чайко',	700,
'гармония',	1200,
'зайчихино',	1400,
'мысовое',	1200,
'александровка',	1200)
    
    if mesto in baza:
        otvet = "Доставка в " + mesto + " равна " + str(baza[baza.index(mesto)+1]) + " рублей за куб"
        return(otvet)
    else:
        return wrongname

def PhotoFromLevel(GameLink, nLevel, delete = 0):
    massiv = []
    
    workurl = GameLink + '/?level=' + nLevel
    if delete !=0:
        workurl='http://demo.en.cx/gameengines/photohunt/delete/30507/?level=3&mediaid=3473'
        print('vse ok!')
    print(workurl) 
    s = requests.Session()
    loging = s.post(PHOTOGAME.reglink,data = datas)
    print(workurl)                
    link = s.get(workurl)
    print(link.text)
    link.encoding = 'utf-8'
    s.close()
             

    filetxt = open('txtfileF.txt', 'wb')
    for line in link:
        filetxt.write(line)
    filetxt.close()               
    with open('txtfileF.txt','r', encoding = 'utf-8') as fp:
        fp2 = fp.read()
        soup = BeautifulSoup(fp2,'html.parser')
        soup.a.encode('utf-8')
        strings = soup.find_all(href=re.compile('http://cdn.endata.cx/data/games'))
        #strings = 'fhgf'
        #strings = soup.find_all(a, class_ = 'thephoto')
        lnk =''
        for txt in strings:                
            print(txt.get('href'))
            lnk = txt.get('href')
            massiv.append(lnk)
    return(massiv)
            



datas = {
    'Login' : 'baklan',
    'Password' : '4644135baklan',
    }

def Loging():
    global s
    s = requests.Session()
    log = s.post(PHOTOGAME.reglink,data = datas)
    
typegame = ''
photo = ''
tagg = ">Фото"

bot = telebot.TeleBot('1694799489:AAENCJXThZJs-obJqyisOgDiViv2nA2VdPI')
@bot.message_handler(content_types=['text'])
def send_text(message):
    
    sss1 = ''
    kkk =''
          
    sss =  message.text.lower()
    if sss == 'пинг':
         bot.send_message(message.chat.id,'пцонг')
    if sss == '/help':
        bot.send_message(message.chat.id,'Cписок команд этого чудо-бота: \n /link - Загрузить ссылку  на игру.\n /login - ввести логин игрока. \n /pass - ввести пароль игрка \n /up N - загрузить текущую фотку в уровень N. \n /levs показать список уровней текущей игры') 
    if sss[0:6] == '/link ':
        slovo ="Гпорпопо"
        PHOTOGAME.MainLink = sss[6:]
        PHOTOGAME.reglink = PHOTOGAME.MainLink[:PHOTOGAME.MainLink.find('.',1,len(PHOTOGAME.MainLink))] + '.en.cx/Login.aspx'
            
        ###### Из HTML страницы с игрой получаем ее тип ########
        link = urllib.request.urlopen(PHOTOGAME.MainLink)
        
        for line in link.readlines():
            if line.find(b'class="white">') != -1 :
                photo = line
                photo = photo.decode('utf-8')
                if photo.find("Фотоо",0, len(photo)-1) !=-1 :
                    PHOTOGAME.Tip = 'Фотоохота'
                    PHOTOGAME.Typegame = 'photohunt'
                if photo.find("Фотоэ",0, len(photo)-1) !=-1 :
                    PHOTOGAME.Typegame = 'photoextreme'
                    PHOTOGAME.Tip = 'Фотоэкстрим'
        bot.send_message(message.chat.id, "Тип игры: " + PHOTOGAME.Tip)
        #######################################
        
        
        # Из ссылки на игру получаем  номер игры и ссылку на уровни
        
    ######################################################################
    
    
    
    
    
    if sss == "/testgame":
       datas['Password'] = '4644135baklan'






    if sss == '/set mainbot':
       datas['Login'] = 'uploader'
       datas['Password'] = '4644135baklan'
       bot.send_message(message.chat.id, 'Добавьте в команду бота под ником uploader (id 1275352)')
    
        
    if sss[0:7] == '/login ':
        datas['Login'] = sss[7:]
        bot.send_message(message.chat.id, datas['Login'])
    if sss[0:6] == '/pass ':
        datas['Password'] = sss[6:]        
       
    if  'tps://yandex.ru/m' in sss:
        browser = webdriver.Chrome()
        browser.get(sss)
        delay = 5 # seconds
        try:
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'zoom-control')))
            print ("Page is ready!")
            browser.save_screenshot('d:/skrin.png')
        except TimeoutException:
            print ("Loading took too much time!")
        browser.save_screenshot('d:/skrin.png')

        browser.quit()
        bot.send_photo(message.chat.id, photo = open("d:/skrin.png","rb"))

    if sss[0:3].lower() == '!д ':
        kudago = sss[3:]
        kudago = kudago.lower()
        bot.send_message(message.chat.id,  str(dost(kudago)))
        ##bot.send_message(message.chat.id,'Доставка в ' + str(kudago) + " равна " + str(dost(kudago)) + " рублей")
    
    if sss[0:4] == '/up ':
        
        
        numero = ''
        ifnumer = sss.find(' ', 4,len(sss)-1) 
        #bot.send_message(message.chat.id, 'ifnumer:  ' + str(ifnumer))
        if ifnumer != -1:
            numero = sss[4:ifnumer]
        else:
            numero = sss[4:]
        #bot.send_message(message.chat.id, 'numero:  ' + numero)
        if numero.isdigit():
            if message.reply_to_message:
                try:                   
                    upcomment = ''
                    if (message.reply_to_message.caption) :
                        upcomment =  message.reply_to_message.caption                    
                    upcomment0 = sss[sss.find(' ', 4,len(sss)-1)+1:]                    
                    if (upcomment0 != sss):
                        upcomment = upcomment0                   
                    if message.reply_to_message.photo :
                        file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
                    if message.reply_to_message.document :
                       file_info = bot.get_file(message.reply_to_message.document.file_id)
                    #bot.send_message(message.chat.id, str(file_info))
                    downloaded_file = bot.download_file(file_info.file_path)
                    src=file_info.file_path;
                    src1=file_info.file_path;            
                    with open('sen2.jpg', 'wb') as new_file:
                        new_file.write(downloaded_file)
                        bot.send_message(message.chat.id, 'Успешно залито в уровень ' + numero)        
                except Exception as e:
                    bot.reply_to(message,e)                
                
                lev = numero   
                url2 = PHOTOGAME.reglink
                urlbase = '/?level=' + lev + '&isadditional=false&operation=add'
                urlmain = PHOTOGAME.InLink
                s = requests.Session()
                loging = s.post(url2,data = datas)
                comm = {'PhotoUploadOperation.Comment': upcomment}
                files = {'PhotoUploadOperation.UploadedPhoto': ('sen2.jpg', open('sen2.jpg', 'rb')) }           
                r = s.post(urlmain + urlbase, files=files, data = comm)
           
    ## По команде получаем список уровней в игре и выдаем пользователю
    if sss == '/levs':
        
        s = requests.Session()
        loging = s.post(PHOTOGAME.reglink,data = datas)
                     
        link = s.get(PHOTOGAME.InLink)
        link.encoding = 'utf-8'
        s.close()
                
        filetxt = open('txtfile.txt', 'wb')
        for line in link:
            filetxt.write(line)
        filetxt.close()
                
        i=0
        with open('txtfile.txt','r', encoding = 'utf-8') as fp:
            fp2 = fp.read()
            soup = BeautifulSoup(fp2,'html.parser')
            soup.a.encode('utf-8')
            strings = soup.find_all(href=re.compile('/?level=30'))
            for txt in strings:                
                txt2 = txt.text
                print(txt2)
                if i < 111:
                    bot.send_message(message.chat.id, 'Слово ' + PhotoFromLevel(3,PHOTOGAME.InLink))
    if sss[0:3] == '/f ':
        numero = ''
        ifnumer = sss.find(' ', 3,len(sss)-1) 
        #bot.send_message(message.chat.id, 'ifnumer:  ' + str(ifnumer))
        if ifnumer != -1:
            numero = sss[3:ifnumer]
        else:
            numero = sss[3:]
        st =  'N' + numero +'N'
        bot.send_message(message.chat.id, st)
        
        
        bot.send_message(message.chat.id,  "Фото из уровня " + numero)

        for LK in PhotoFromLevel(PHOTOGAME.InLink,numero):
            bot.send_message(message.chat.id,  LK)   
    if sss == '/del':
        Loging()
        s = requests.Session()
        print(PhotoFromLevel("fdsfs",'3', delete = 1))
        #deltry = requests.get('http://demo.en.cx/gameengines/photohunt/delete/30507/?level=3&mediaid=3472')




bot.polling()



    
    


