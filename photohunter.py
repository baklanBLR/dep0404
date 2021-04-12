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
        bot.send_message(message.chat.id,'Cписок команд этого чудо-бота: \n /link - Загрузить ссылку  на игру.\n /login - ввести логин-пароль игрока. \n /up N - загрузить текущую фотку в уровень N. \n ') 
    if sss[0:6] == '/link ':
        slovo ="Гпорпопо"
        PHOTOGAME.MainLink = sss[6:]
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
    if sss[0:7] == '/login ':
        datas['Login'] = sss[7:]
    if sss[0:6] == '/pass ':
        datas['Password'] = sss[6:]        
        
    if sss[0:4] == '/up ':
        numero = sss[4:]
        if numero.isdigit():
            lev = numero   
            url2 ='http://30.en.cx/Login.aspx'
            url3 = 'http://chita.en.cx/Administration/Games/FileUploader.aspx?gid=71160'
            url = 'http://chita.en.cx/gameengines/photohunt/play/71160/?level='+ lev + '&isadditional=false&operation=add'
            url4 = 'http://minsk.en.cx/gameengines/photoextreme/play/71552/?level=' + lev + '&isadditional=false&operation=add'
            url5 = 'http://gameengines/photoextreme/play/71552/?level=1&mediaid=613494&operation=editcomment'
            urlmain = PHOTOGAME.InLink
            s = requests.Session()
            loging = s.post(url2,data = datas)
            files = {'PhotoUploadOperation.UploadedPhoto': ('sen.jpg', open('sen.jpg', 'rb'))}
            r = s.post(urlmain, files=files)
    if sss[0:4] == '/levs':
        url2 ='http://30.en.cx/Login.aspx'
        s = requests.Session()
        loging = s.post(url2,data = datas)






@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

     try:


        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src=file_info.file_path;
        src1=file_info.file_path;
        way33.pathup = src1;
            
        with open('sen.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message,way33.pathup) 
     except Exception as e:
         bot.reply_to(message,e )
bot.polling()



    
    


