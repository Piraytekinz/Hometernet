# # # from getpass import getpass
# # # import pyrebase

# # # firebaseConfig={
# # #     "apiKey": "AIzaSyDG9LX4CI6Rsef49D1VTMmA_9QHg5zHywo",
# # #     "authDomain": "first-db-77609.firebaseapp.com",
# # #     "databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com",
# # #     "projectId": "first-db-77609",
# # #     "storageBucket": "first-db-77609.appspot.com",
# # #     "messagingSenderId": "820407820543",
# # #     "appId": "1:820407820543:web:62a2c15e88e30ef6346cca",
# # #     "measurementId": "G-NGK0NGTGJX"
# # # }

# # # firebase = pyrebase.initialize_app(firebaseConfig)

# # # auth = firebase.auth()

# # # # auth = firebase.auth()

# # # # Log the user in


# # # # Get a reference to the database service
# # # db = firebase.database()

# # # # data to save
# # # data = {
# # #     "name": "Red Hair"
# # # }

# # # # Pass the user's idToken to the push method



# # # def signup():
# # #     email = input("Enter email: ")
# # #     password = input("Enter Password: ")
    
# # #     user = auth.create_user_with_email_and_password(email, password)
# # #     auth.send_email_verification(user['idToken'])

# # #     # results = db.child("users").child(user['localId']).push(data)
# # #     # print(results)
    


    
# # #     # print("Successfully created account")

# # # def login():
# # #     email = input("Enter Email: ")
# # #     password = getpass("Enter Password: ")
    
# # #     lila = auth.sign_in_with_email_and_password(email, password)
# # #     auth.send_email_verification(lila['idToken'])

    

# # #     # useri = db.child("users").child(user['localId']).get()
# # #     # for i in useri.each():
# # #     #     print(i.val()['name'])
    

# # #     print("Successfully signed in")
    
            

# # # choice = input("Login?: ")
# # # if choice == 'y':
# # #     login()
# # # elif choice == 'n':
    
# # #     signup()

# # # import phonenumbers

# # # phone = '+233276098275'
# # # phone_number  = phonenumbers.parse(phone)
# # # print(phonenumbers.is_valid_number(phone_number))
# # # import smtplib

# # # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# # # server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
# # # server.sendmail("anangjosh8@gmail.com", "ahdwaoidnofnw@gmail.com", "An offer has been made to buy your house.")
# # # server.quit()

# # # import requests
# # # email_address = 'pirateyonko5@gmail.com'
# # # response = requests.get('https://isitarealemail.com/api/email/validate', params= {'email':email_address})

# # # status = response.json()['status']

# # # if status == "valid":
# # #     print('valid')
# # # elif status == 'invalid':
# # #     print('invalid')
# # # else:
# # #     print('Unknown')

# # from kivymd.app import MDApp
# # from kivy.lang import Builder
# # from kivymd.uix.boxlayout import MDBoxLayout
# # from kivymd.uix.label import MDLabel
# # from kivy.uix.label import Label
# # from kivy.uix.image import Image
# # import time
# # from threading import Thread
# # from kivy.clock import mainthread, Clock
# # from kivy.uix.screenmanager import ScreenManager, Screen
# # # screens = """
# # # <Screeni>:
# # #     Ascreen:
# # #         MyLayout:
# # #             id: bis
# # #             md_bg_color: app.theme_cls.primary_color
# # #             MDLabel:
# # #                 id: lol
# # #                 text: 'Working'
# # #                 halign: 'center'
# # # """
# # # Builder.load_string(screens)

# # # class MyLayout(MDBoxLayout):
# # #     def __init__(self, **kwargs):
# # #         super().__init__(**kwargs)
        


# # # class Ascreen(Screen):
# # #     def __init__(self, **kw):
# # #         super().__init__(**kw)
# # #         daemon = Thread(target=self.on_enter, daemon=True, name='added')
# # #         daemon.start()

# # #     @mainthread
# # #     def on_enter(self, *args):
# # #         while MainApp.get_running_app():
# # #             time.sleep(20)
# # #             snack = MDLabel(text='My House', halign='center')
# # #             print('rip right through your center')
# # #             break
# # #         return super().on_enter(*args)
    
        




# # import pycountry
# # import flag
# # from emojiflags.lookup import lookup




# # # flagser = pycountry.countries.get(name='United States')
# # # real = flagser.alpha_2
# # stringi = """
# # <Screeni>:
# #     Screen:
        
# #         Flagsisy:
# #             # text: self.flagser
# #             # halign: 'center'
# #             source: self.flagser


# # """
# # Builder.load_string(stringi)
# # #How to transform flag**** into image in python

# # print(lookup('IL') +  'is the cintry ')


# # class Screeni(ScreenManager):
# #     def __init__(self, **kwargs):
# #         super().__init__(**kwargs)
        

# # class Flagsisy(Image):
# #     flagser = flag.flag('IL')
    

# # class MainApp(MDApp):
# #     def build(self):
# #         screeni = Screeni()
# #         self.screen = screeni
# #         print(flag.flag('IL'))
        
# #         return self.screen
        
# # MainApp().run()



# # import webbrowser

# # webbrowser.open('https://mail.google.com/mail/?view=cm&fs=1&to=anangjosh8@gmail.com&su=SUBJECT&body=BODY')

# # text = '<This is a very long text ya know.>'

# # print(text)
# # input = [19,2,31,45,30,11]
# # for i in range(1,len(input)):
# #     j = i-1

# # ssl._create_default_https_context = ssl._create_unverified_context
# # os.environ['SSL_CERT_FILE'] = certifi.where()
# # Config.set('kivy', 'exit_on_escape', 0)

# # pat = ssl.get_default_verify_paths()
# # print(pat)

# # from datetime import datetime

# # dt = datetime.now()
# # print(dt.time() == dt.time())
# # time = 12:17:45.133003

# import json
# from plyer import filechooser
# import os

# path = os.getcwd()
# print(path)

# with open(f'{path}\\user.json', 'r') as myfile:
#     self = json.load(myfile)
# print(self)

# def select_file():
#     filechooser.open_file(on_selection=selected, multiselect=True)

# def selected(image):
#     print(image)



# select_file()

# with open(f'{path}\\user.json', 'r') as jsonfile:
#     mama = json.load(jsonfile)

# print(mama)
# import DNS
# from validate_email import validate_email

# DNS.defaults['server']=['8.8.8.8', '8.8.4.4']

# status = validate_email('anangjosh8@gmail.com', verify=True)
# print(status)

# import smtplib
# from email.mime.text import MIMEText
import random

# num = random.randint(100000,999999)



# message = MIMEText(f"Your email login code is {num}. \n Warning do not share this code with anyone.")
# message['Subject'] = "Your Hometernet login code."
# message["From"] = "anangjosh8@gmail.com"
# message["To"] = "dawdhlawdald@gmail.com"
# server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
# server.sendmail("anangjosh8@gmail.com", "dawdhlawdald@gmail.com", message.as_string())
# server.quit()

# input = input("> ")
# if input == num:
#     print("Successfully signed in")
# else:
#     print("Wrong input code")

# print(' banana is good for you  '.strip())
# from plyer import filechooser

# def func_name(selection):
#     print(selection)

# filechooser.save_file(open='C:/Users/Yvonne/Pictures', on_selection=func_name)

# import webbrowser

# webbrowser.open("https://fb.me/Dwin Halm")
# name = 'Trafalgar'
# num = 0
# namo = list(name)

# leng = len(namo)-1

# for i in range(len(namo)//2):
#     temp = namo[num]
#     namo[num] = namo[leng-num]
#     namo[leng-num] = temp
#     num += 1
    
# total = ''
# for i in namo:
#     total += i
# print(total)


# import pyrebase
# from datetime import datetime, date, timedelta
# import os
# import json
# #
# import smtplib
# from email.mime.text import MIMEText

# firebaseconfig = {
#     "apiKey": "AIzaSyDG9LX4CI6Rsef49D1VTMmA_9QHg5zHywo",
#     "authDomain": "first-db-77609.firebaseapp.com",
#     "databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com",
#     "projectId": "first-db-77609",
#     "storageBucket": "first-db-77609.appspot.com",
#     "messagingSenderId": "820407820543",
#     "appId": "1:820407820543:web:62a2c15e88e30ef6346cca",
#     "measurementId": "G-NGK0NGTGJX",
#     "type": "service_account",
#     "project_id": "first-db-77609",
#     "private_key_id": "c7599cc9be6de93088877bd6b6db6ea6efd9e3a2",
#     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC9Bycx+4BU4PGp\nDJ5XPpmswcegqk9dkdmB+8PmXdgjWdR9UFAPkE+VXytPMBUVvO1TNju1MwwvrJhT\nuOAjubXZj5euqtFHgaxBiD2CPZGSWMPUyTSLX1uVWwwexOuzhdBr/5aT44I30Go9\nZV3GUVKKlIysb/Fc1Gr7YtIE/6e9YsvN2dJvdCwfmxVaqSgga2xxqM0a6v0vlgDb\ndjDuFdhoPjCoB53cpYvsspMvRNSQ3Xa/lXOTCkOCY0wFad50rQtpito/0YXHIscN\nz5PcxaBpggFvGrV3pN28vxX1LEGBarknMfsgywQ0M9HVB3VoRXDO1LfoG4OkQBJt\n88dUFJTRAgMBAAECggEABeY3UB81j4iT6CsGdcn0izSCv7oS9yRML8sg/3N0MXG+\nMMFA92RhRHPTduGk9dBHLpSzpzV6MtJx0FKVra2//fPGF8eZV5BFpUeshkAYRwNF\nzNIw9WzO35XXZm4uPjR910IDM7c65xWmPCdpxly/PQeS7paBh4xyUIlCbVEifbW9\n64+zYUSFO8LamSGxQdcMcQl0858HXYFY793VWHPybZedZ8CM+xE0dBif1B2mp7kC\n0jwI25BeHfsj4l8V/FwlEtSFtG1Qx+C99a185ocqsmA0Am1BapCKZ7nX4IaJDp92\nbpHKsDKsP2T/o8Ex6dG+zsCCTmep9pG5zczecSq1QQKBgQDr322QPlc6idm9d+9x\ngKFkrRnWyUZzTCa0aiV73WKLN4G4k+DAL19qYwFkK5OutECDPBuweb8VSCYvyl5N\nMZcOMvuV+1DYuYhSuBabDfAE+zJMSmETvrSwJk0xEw0FdLgmm3/9O3WvthK5mX6+\nqbsN2Zks/tgG8re07HgsCAYmQQKBgQDNKGnfROTGrlTN7NfQS1/jGYC/6N33nTTm\nrEfdTw7jxBCWaplQrCHOrDhKz1g3UISR6tUY1PECJEV/W/mVylc/Q4yQPaW42WAt\n9KYJ8hVLoiRSPVdrwJAeSMXZypgiBONRKrRAaAGsIWoRpzguUEBB/j5wBPvA0PTg\nBH4WYEJqkQKBgAs6p8ymKyDuTx9mBlAw/337f69qBaCXj4AnTYGIGJjoG5Td9WUw\n3CoEbJyINo+qpSeaRPcx1Jb+yFKeH78tDTPv2WpafI7Uxlipyum20CZsjwhywgxe\nl9uK90HO1l/cHqg33u//VKr40Atl81LAYddW9KPfvgkWpQhH+bCe8SwBAoGAYapu\nlFJ40rilOI8awldPo449g565JKrbR0EWyR1cykNJXkILEKORSJEmDz8cEOEs60Yv\nAi5FOa7IwvOnIo777+sZXIVsgk5Bgj8oWC29w47B2cDIAEzgjvo37hGLUQ6gpMA+\npTaeLTKPCy5fCXU80e3WDX/h1Y3kNU0ONVrH43ECgYBWimuvPTmGwS5rBWC9Z7OD\nvfVT4uSuAiXrDdPo0N9HqCKunSuJIqihA/NJELmq9DrBWZI1AFDXaLBlz2RqBq3T\n4k/BaE9gsS0Tn+K9Plee/fWFkVO6fFTSiARn128VyF9hqXEm0vnIiyYhTQvIkQKZ\nmC+UyHUSL+EjIg1MXbE2vw==\n-----END PRIVATE KEY-----\n",
#     "client_email": "firebase-adminsdk-ykjt8@first-db-77609.iam.gserviceaccount.com",
#     "client_id": "105639461294547029153",
#     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#     "token_uri": "https://oauth2.googleapis.com/token",
#     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ykjt8%40first-db-77609.iam.gserviceaccount.com"
# }

# cred = credentials.Certificate("first-db-77609-firebase-adminsdk-ykjt8-c7599cc9be.json")
# firebase_admin.initialize_app(cred, {"databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com"})

# firebasei = pyrebase.initialize_app(firebaseconfig)
# # path = os.getcwd()
# db = firebasei.database()
# authi = firebasei.auth()
# storage = firebasei.storage()


# check = db.child('Update').get()
# for i in check.each():
#     print(i.val()['update'])


# users = auth.list_users()

# # try:

# with open(f"{path}/user.json", "r") as jsonfile:
#     curr = json.load(jsonfile)

# dev = authi.sign_in_with_email_and_password(curr['email'], curr['password'])

# with open("New Test/evaluate.json", "r") as jsondude:
#     curri = json.load(jsondude)



# get = db.child("Sale").get()
# for i in get.each():
#     if i.val()['email'] == 'anangjosh8@gmail.com':
        
#         key_data = {
#             "prop_keys": "",
#         }
#         key_data['prop_keys'] = i.key()
#         db.child("People").child(dev['localId']).child("ids").push(key_data, dev['idToken'])
#         print("pushed successfully")


############################################################### From bottom to top
# new = db.child("Sale").order_by_key().limit_to_first(2).get()
# new_list = []
# othr = []
# key1 = new.each()[0].key()
# key2 = new.each()[1].key()



# othe = db.child("Sale").get()
# num = len(othe.each())-1
# print(num)
# num1 = len(othe.each())-2
# print(othe.each()[num].key())
# print(othe.each()[num1].key())
# print(num1)


# db.child("Sale").update()
############################################################## FROM bttom to top



# print(authi.get())
# for user in users.users:
#     if user.email == 'pirateyonko5@gmail.com':
#         print(user.uid)
#         testichiro = db.child("People").child(str(user.uid)).child("ids").get(dev['idToken'])
#         for u in testichiro.each():
#             if u.val()['prop_keys'] == '-NSxOwBmQ-iVDD92Yex-':
#                 db.child("People").child(str(user.uid)).child("ids").child(u.key()).remove(dev['idToken'])
#                 break
#         print('successfully deleted')
# except:
#     pass











#DELETE EXPIRED PROPERTIES
#####################################################################################################################
# for i in testichiro.each():
# p = db.child("Sale").get()
#     # print(i.val())

# tod = datetime.today()
# ok = date.strftime(tod, '%Y-%m-%d')



# new = tod + timedelta(days=93)

# for i in p.each():
#     check = datetime.strptime(i.val()['date'], '%Y-%m-%d')
#     new = check + timedelta(days=new)

#     if new < datetime.today():
#         email = i.val()['email']
#         print(email)
#         print(i.val()['date'])
#         print(i.key())
#         print("Removeing property")
#         db.child("Sale").child(i.key()).remove(dev['idToken'])
#         print("Removed property")
#         for user in users.users:
#             if user.email == email:
#                 curri["keys"].append(i.key())
#                 testichiro = db.child("People").child(str(user.uid)).child("ids").get(dev['idToken'])
#                 for u in testichiro.each():
                    
#                     if u.val()['prop_keys'] == i.key():
#                         db.child("People").child(str(user.uid)).child("ids").child(u.key()).remove(dev['idToken'])
#                         message = MIMEText(f"Your property {i.val()['housetype']}, {i.val()['bedrooms']} bedrooms, {i.val()['country']}, {i.val()['town']}, {i.val()['street']} has expired and has been deleted.")
#                         message['Subject'] = 'Your property has been deleted...'
#                         message["From"] = "hometernetmanager@gmail.com"
#                         message["To"] = email
#                         print('Starting server')
#                         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#                         server.login("hometernetmanager@gmail.com", "lhgajriuhglozfyd")
#                         server.sendmail("hometernetmanager@gmail.com", email, message.as_string())
#                         server.quit()
#                         print("Message sent")
#                         break
#                 print(testichiro)
#                 print(user.uid)

#         with open("New Test/evaluate.json", "w") as jsondude:
#             json.dump(curri, jsondude)
#         print('user id for property')

#         # db.child("Sale").child(i.key()).remove(user['idToken'])

#        
#         break
        


##################################################################################################################################################################################












from datetime import datetime, date, time
import cv2 as cv

print(time.hour)
# today = '2023-01-12'
# today = datetime.strptime(today, '%Y-%m-%d')
# print(tod<today)
# print(new)
# +44 7926690084
# 0244233534
















# from firebase_admin import credentials
# from firebase_admin import auth
# import firebase_admin


# cred = credentials.Certificate("first-db-77609-firebase-adminsdk-ykjt8-c7599cc9be.json")
# firebase_admin.initialize_app(cred, {"databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com"})


# firebase_admin.get_app()

