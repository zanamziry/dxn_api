from datetime import datetime
from bs4 import BeautifulSoup as BS4
import requests
import random

###Edit MemberInfo
#POST https://obs3.dxn2u.com/gulf/membership/fmnt_edit.php
#DATA del_sign=&_from=LST&_notfill=1&txt_memid=&txt_taxid=&txt_memname=&id=141100033&nsearch=&fpage=0

class Collector:
    agent_code = ''
    username = ''
    passwd = ''
    CaptchaFile = "captcha.png"
    HEADERS = {"User-Agent":"ZM API"}
    BASE_URL = "https://obs3.dxn2u.com/gulf"
    captchaNumber = 0
    seasonData = None
    S: requests.Session

    CID_UID = [
        {'uid': '7355' , 'cid' : 'UdSVLL3s3wysJCFM3bFrz68+2LFiraExo4KVCc0QRyI='},
        {'uid': '5911' , 'cid' : 'aC9EjfYEilGs2iSG2FBXxNNEU5jQk3/jo4fO3OrNjqA='},
        {'uid': '9327' , 'cid' : '6H+/+DcQASIxyDDhSSxAICsKsMNb/DQ6MQd8QWEqZWc='},
        {'uid': '3432' , 'cid' : 'ZYckz9Lyl20SGSYa4h0maPUV2nn5aPY26IReg+otPKU='},
        {'uid': '9186' , 'cid' : 'L8n7wHkIF9zkiYLi5GJ5YWAJKk4A1dSMiNCZbluYK/o='},
        {'uid': '4666' , 'cid' : 'Z72gzzYkh24GZ3esQjxnhNHP/AOQyIeTtXDZzOlNMRE='},
    ]

    def RandomCaptchaSolve(self):
        randint = random.randrange(0,5)
        s = self.CID_UID[randint]
        return s
    
    def __init__(self) -> None:
        self.S = requests.Session()
        return
    
    def Login(self, username:str, passwd:str) -> bool:
        url = self.BASE_URL + '/login.php'
        randomCaptcha = self.RandomCaptchaSolve()
        data = {
            'cmd':'masuk',
            'usertype': 0,
            'txt_user': username,
            'txt_pass': passwd,
            'uid': randomCaptcha['uid'],
            'cid': randomCaptcha['cid']
            }
        res = self.S.post(url,params=data)
        soup = BS4(res.content,'html.parser')
        some = soup.find(id = 'menu1')
        if(some == None):
            return False
        else:
            return True

    def GetInventoryReport(self, agent_id:str, ProductCode:str="", DateOfReport:datetime=datetime.now()):
        date = self.DateFormat(DateOfReport)
        params = {
            'id': agent_id,
            'txt_scid': agent_id,
            'txt_code': agent_id,
            'txtTgl1' : date,
            'txtTgl2' : date,
            'cbo_prd' : 1,
            'prd_from' : ProductCode,
            'prd_to': ProductCode,
        }
        
        url = self.BASE_URL + f"/scenters/sb_prnt.php"
        html = self.S.get(url,params=params).content
        count = 1
        table_data:list = []
        for row in BS4(html,'html.parser')("tr"):
            #Filter rows that have less than 11 cells and ignore the first row
            if(len(row('td')) != 11):
                continue
            #The Count Is To Skip The Header Part
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