import requests
import json
     

url = 'http://20.196.127.192:5006/simpleAPI'
myobj = {'message_key': 'message_val',
         'msg':'ตะวัน'} #json

x = requests.post(url, data = json.dumps(myobj)) #requests ใช้เรียก // data // รับ output จาก webb