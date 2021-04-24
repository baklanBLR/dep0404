#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import os
import json
import traceback
import requests
import sys
import urllib.request
class PHOTOGAME:
    MainLink = ''
    InLink = ''
    Typegame = ''
    Tip = ''
    levels  = []
    Number = ''
    reglink =''
    test = "Нихуя не помню"
datas = {
    'Login' : 'def',
    'Password' : 'def',
    }
slovo = 'Г'
typegame = ''
photo = ''
tagg = ">Фото"

bot = telebot.TeleBot('1694799489:AAENCJXThZJs-obJqyisOgDiViv2nA2VdPI')
@bot.message_handler(content_types=['text'])
def send_text(message):
    
    sss1 = ''
    sss =  message.text.lower()
    if sss == '/help':
        bot.send_message(message.chat.id,'Cписок команд этого чудо-бота: \n /link - Загрузить ссылку  на игру.\n /login - ввести логин игрока. \n /pass - ввести пароль игрка \n /up N - загрузить текущую фотку в уровень N. \n /levs показать список уровней текущей игры') 
    if sss[0:6] == '/link ':
        slovo ="Гпорпопо"
        PHOTOGAME.MainLink = sss[6:]
        PHOTOGAME.reglink = PHOTOGAME.MainLink[:PHOTOGAME.MainLink.find('.',1,len(PHOTOGAME.MainLink))] + '.en.cx/Login.aspx'
       # bot.send_message(message.chat.id,PHOTOGAME.reglink)
       # bot.send_message(message.chat.id,datas['Game'])   
        
     
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
        ind1 = PHOTOGAME.MainLink.find('x/', 0 ,len(PHOTOGAME.InLink) - 1)
        ind2 = PHOTOGAME.MainLink.rfind('gid=',0, len(PHOTOGAME.InLink) - 1)
        PHOTOGAME.Number = PHOTOGAME.MainLink[ind2 + 4:]
        PHOTOGAME.InLink = PHOTOGAME.MainLink[:ind1 + 2] + 'gameengines/' + PHOTOGAME.Typegame + '/play/' +PHOTOGAME.Number
        bot.send_message(message.chat.id, PHOTOGAME.InLink)
    ######################################################################
    if sss == '/set mainbot':
       datas['Login'] = 'uploader'
       datas['Password'] = 'pass4thisbot'
       bot.send_message(message.chat.id, 'Добавьте в команду бота под ником uploader (id 1275352)')
    if sss== 'вспомнить':
        bot.send_message(message.chat.id, PHOTOGAME.test)
    if sss== 'бетон':
        PHOTOGAME.test = "я запомнил слово бетон"
        
    if sss[0:7] == '/login ':
        datas['Login'] = sss[7:]
        bot.send_message(message.chat.id, datas['Login'])
    if sss[0:6] == '/pass ':
        datas['Password'] = sss[6:]        
       
    if sss[0:4] == '/up ':
        numero = ''
        numero = sss[4:]
        if numero.isdigit():
            lev = numero   
            url2 = PHOTOGAME.reglink
            urlbase = '/?level=' + lev + '&isadditional=false&operation=add'
            url5 = 'http://gameengines/photoextreme/play/71552/?level=1&mediaid=613494&operation=editcomment'
            urlmain = PHOTOGAME.InLink
            s = requests.Session()
            loging = s.post(url2,data = datas)
            files = {'PhotoUploadOperation.UploadedPhoto': ('sen2.jpg', open('sen2.jpg', 'rb'))}
            ##bot.send_message(message.chat.id,urlmain + urlbase)
            r = s.post(urlmain + urlbase, files=files)
           
    ## По команде получаем список уровней в игре и выдаем пользователю
    if sss == '/levs':
        li = 0
        lev = 'Нихуя не нашел'
       ## datas['Login'] = 'baklan'
        ##datas['Password'] = '4644135baklan'
        ##PHOTOGAME.InLink = 'http://minsk.en.cx/gameengines/photoextreme/play/71552'
       ## bot.send_message(message.chat.id, datas['Login']  + "   " + datas['Password'])
                ##url2 = PHOTOGAME.InLink
        s = requests.Session()
        loging = s.post(PHOTOGAME.reglink,data = datas)
        ##link = urllib.request.urlopen(PHOTOGAME.InLink)
        link = s.get(PHOTOGAME.InLink)
        key2 = link.text.find('<ul class="level"',1, len(link.text))
        key1 = 0
        key0 = 0
        li = 0
        i = 0
        ur = 0
        while  key0 != -1:
            
            i = 0
            key0 = link.text.find('<li class',key2 + 1, len(link.text))      
            key1 = link.text.find('vel=',key0 + 1, len(link.text)) 
            while link.text[key1 + 5].isdigit():
                key1 = key1 + 1
                i = i + 1
            key2 = link.text.find('</a>',key1 + 1, len(link.text)) 
            if link.text[key1 + 7:key2] :
                ur = ur + 1
                bot.send_message(message.chat.id, str(ur)  + ')   ' + link.text[key1 + 7 + i:key2])
             ##PHOTOGAME.levels.append(link.text[key1:key2])
            li = li + 1
        ##bot.send_message(message.chat.id, PHOTOGAME.levels)
      
        




@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

     try:


        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src=file_info.file_path;
        src1=file_info.file_path;
        
            
        with open('sen2.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        ##bot.reply_to(message,way33.pathup) 
     except Exception as e:
         bot.reply_to(message,e )
bot.polling()



    
    


