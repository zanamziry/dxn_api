from datetime import datetime
from typing import Final
from bs4 import BeautifulSoup as BS4
import json
import requests
import pytesseract
import matplotlib.image as mpimg

class Collector:
    agent_code = ''
    username = ''
    passwd = ''
    CaptchaFile = "captcha.png"
    HEADERS = {"User-Agent":"ZM API"}
    BASE_URL = "https://obs3.dxn2u.com/gulf"
    captchaNumber = 0
    seasonData = None
    S: requests.Session = None
    def __init__(self, agent_code:str, username:str, passwd:str) -> None:
        self.agent_code = agent_code
        self.username = username
        self.passwd = passwd
        self.S = requests.Session()
        self.seasonData = self.getCaptchaData()
        self.captchaNumber = self.ReadCaptcha().replace('\n','')
        self.Login()
        return
    
    def getCaptchaData(self):
        url = self.BASE_URL + "/module/relod_kecap.php"
        resp = self.S.get(url)
        return json.loads(resp.content)

    def getCID(self) -> str:
        return self.seasonData["cid"]
    
    def getUID(self) -> str:
        return self.seasonData["uid"]
    
    def GetStatus(self,DateOfReport:datetime=datetime.now()) -> bool:
        url = self.BASE_URL + '/module/mnu_pro_check_allow_date.php'
        date = self.DateFormat(DateOfReport)
        data = {
           'txtTgl1': date,
           'txtTgl2': date,
           'txt_scid': 'x',
           'sc_checking': 0,
           'localdate':date
        }
        resp = self.S.get(url, data=data).json()
        if(resp['xstatus'] == 'true'):
            return True
        else:
            return False

    def ReadCaptcha(self) -> str:
        url = self.BASE_URL + f'/captcha2/CaptchaImage.php?uid=54;{self.getUID()}'
        resp = self.S.get(url).content
        __path__
        f = open(self.CaptchaFile, "wb")
        f.write(resp)
        f.close()
        image = mpimg.imread(self.CaptchaFile, 0)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        return pytesseract.image_to_string(image, lang='eng',config='--psm 6')
        
    def Login(self):
        url = self.BASE_URL + '/login.php'
        data = {
            'cmd':'masuk',
            'usertype': 0,
            'txt_user': self.username,
            'txt_pass': self.passwd,
            'uid':self.captchaNumber,
            'cid':self.getCID()
            }
        return self.S.post(url,params=data)

    def GetInventoryReport(self, ProductCode:str="", DateOfReport:datetime=datetime.now()):
        date = self.DateFormat(DateOfReport)
        params = {
            'id': self.agent_code,
            'txt_scid': self.agent_code,
            'txt_code': self.agent_code,
            'txtTgl1' : date,
            'txtTgl2' : date,
            'cbo_prd' : 1,
            'prd_from' : ProductCode,
            'prd_to': ProductCode,
        }
        #url = self.BASE_URL + f"/scenters/sb_prnt.php?id={SC_CODE}&txt_scid={SC_CODE}&txt_code={SC_CODE}&txtTgl1={date}&txtTgl2={date}&cbo_prd=1&prd_from={ProductCode}&prd_to={ProductCode}"
        url = self.BASE_URL + f"/scenters/sb_prnt.php"
        html = self.S.get(url,params=params).content
        count = 1
        table_data:list = []
        for row in BS4(html,'html.parser')("tr"):
            #Filter rows that have less than 11 cells and ignore the first row
            if(len(row('td')) < 11):
                continue
            if(count == 1):
                count = 0
                continue
            table_data.append({
                'ID': row('td')[0].text,
                'Name':row('td')[1].text,
                'OpenBalance':row('td')[2].text,
                'Sold':row('td')[5].text,
                'CloseBalance':row('td')[9].text
              })
        Final:dict = {
        'agent' : self.agent_code,
        'date' : date,
        'list' : table_data,
        }
        return Final

    def DateFormat(self,Date:datetime):
        return datetime.strftime(Date,"%d/%m/%Y")