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

print(' banana is good for you  '.strip())