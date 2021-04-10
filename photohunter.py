#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import os
import json
import traceback
import requests
import sys
class way33:
    pathup = ''
datas = {
    'Login' : 'def',
    'Password' : 'def'
}

bot = telebot.TeleBot('1694799489:AAENCJXThZJs-obJqyisOgDiViv2nA2VdPI')
@bot.message_handler(content_types=['text'])
def send_text(message):
    sss1 = ''
    sss =  message.text.lower()
    
    if sss == 'here?' :
        bot.send_message(message.chat.id,'Aga')    
    if len(sss) > 7 :
        sss1 = sss[0:6]
        if sss1 == 'upload':
            numero = sss[7:]
            if numero.isdigit():
                lev = numero   
                datas['Login'] = 'baklan'
                datas['Password'] = '4644135baklan'
                url2 ='http://minsk.en.cx/Login.aspx'
                url3 = 'http://chita.en.cx/Administration/Games/FileUploader.aspx?gid=71160'
                url = 'http://chita.en.cx/gameengines/photohunt/play/71160/?level='+ lev + '&isadditional=false&operation=add'
                url4 = 'http://minsk.en.cx/gameengines/photoextreme/play/71552/?level=' + lev + '&isadditional=false&operation=add'
                url5 = 'http://gameengines/photoextreme/play/71552/?level=1&mediaid=613494&operation=editcomment'
                s = requests.Session()
                loging = s.post(url2,data = datas)
                f=open('ress.txt', mode = 'w+', encoding='utf-8')
                f.write(loging.text)
                f.close()
                files = {'PhotoUploadOperation.UploadedPhoto': ('sen.jpg', open('sen.jpg', 'rb'))}
                r = s.post(url4, files=files)
                     





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



    
    


