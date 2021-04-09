import requests
datas = {
    'Login' : 'def',
    'Password' : 'def'
}
login = "baklan"
passwd = "4644135baklan"
datas['Login'] = login
datas['Password'] = passwd
url2 ='http://chita.en.cx/Login.aspx'
url = 'http://chita.en.cx/Login.aspx?return=%2fAdministration%2fGames%2fFileUploader.aspx%3fgid%3d71160'
s = requests.Session()
loging = s.post(url,data = datas)
f=open('ress.txt', mode = 'w+', encoding='utf-8')
f.write(loging.text)
f.close()
files = {"inputFile1": ("tig.jpg", open("tig.jpg", "rb"))}
r = s.post("http://chita.en.cx/Administration/Games/FileUploader.aspx?gid=71160", files=files)
print(r.text)
print('Вроде выполнено')
