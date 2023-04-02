
import phonenumbers
import pycountry
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition, NoTransition, RiseInTransition, WipeTransition, SlideTransition, FallOutTransition, CardTransition
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivymd.uix.list import MDList, OneLineListItem, ImageLeftWidget, OneLineIconListItem, OneLineAvatarListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.behaviors import CommonElevationBehavior, FakeRectangularElevationBehavior
from kivymd.uix.snackbar import Snackbar
from kivy.uix.recycleview import RecycleView

from validate_email import validate_email
from kivymd.uix.label import MDLabel, MDIcon
import concurrent.futures

# from kivy.effects.scroll import ScrollEffect
# from kivy.effects.kinetic import KineticEffect
# from kivy.effects.dampedscroll import DampedScrollEffect


# from kivymd.effects.roulettescroll import RouletteScrollEffect

import pyrebase
import re
from kivy.clock import Clock, time
from kivy.animation import Animation
import json


from kivy.core.audio import SoundLoader
from kivy.base import EventLoop
from kivy.config import Config

from kivy.uix.textinput import TextInput











from plyer import filechooser

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
import smtplib
from email.mime.text import MIMEText



from kivy.uix.scrollview import ScrollView


from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDGridBottomSheet, MDListBottomSheet
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
from kivymd.uix.spinner import MDSpinner
import webbrowser


import requests
from kivy.clock import Clock, mainthread
from func_timeout import func_timeout, FunctionTimedOut, func_set_timeout
import random

import threading
from threading import Event
import certifi
import os
import ssl



ssl._create_default_https_context = ssl._create_unverified_context
os.environ['SSL_CERT_FILE'] = certifi.where()
Config.set('kivy', 'exit_on_escape', 0)



path = os.getcwd()
print(path)



firebaseconfig = {
    "apiKey": "AIzaSyDG9LX4CI6Rsef49D1VTMmA_9QHg5zHywo",
    "authDomain": "first-db-77609.firebaseapp.com",
    "databaseURL": "https://first-db-77609-default-rtdb.firebaseio.com",
    "projectId": "first-db-77609",
    "storageBucket": "first-db-77609.appspot.com",
    "messagingSenderId": "820407820543",
    "appId": "1:820407820543:web:62a2c15e88e30ef6346cca",
    "measurementId": "G-NGK0NGTGJX",
    "type": "service_account",
    "project_id": "first-db-77609",
    "private_key_id": "c7599cc9be6de93088877bd6b6db6ea6efd9e3a2",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC9Bycx+4BU4PGp\nDJ5XPpmswcegqk9dkdmB+8PmXdgjWdR9UFAPkE+VXytPMBUVvO1TNju1MwwvrJhT\nuOAjubXZj5euqtFHgaxBiD2CPZGSWMPUyTSLX1uVWwwexOuzhdBr/5aT44I30Go9\nZV3GUVKKlIysb/Fc1Gr7YtIE/6e9YsvN2dJvdCwfmxVaqSgga2xxqM0a6v0vlgDb\ndjDuFdhoPjCoB53cpYvsspMvRNSQ3Xa/lXOTCkOCY0wFad50rQtpito/0YXHIscN\nz5PcxaBpggFvGrV3pN28vxX1LEGBarknMfsgywQ0M9HVB3VoRXDO1LfoG4OkQBJt\n88dUFJTRAgMBAAECggEABeY3UB81j4iT6CsGdcn0izSCv7oS9yRML8sg/3N0MXG+\nMMFA92RhRHPTduGk9dBHLpSzpzV6MtJx0FKVra2//fPGF8eZV5BFpUeshkAYRwNF\nzNIw9WzO35XXZm4uPjR910IDM7c65xWmPCdpxly/PQeS7paBh4xyUIlCbVEifbW9\n64+zYUSFO8LamSGxQdcMcQl0858HXYFY793VWHPybZedZ8CM+xE0dBif1B2mp7kC\n0jwI25BeHfsj4l8V/FwlEtSFtG1Qx+C99a185ocqsmA0Am1BapCKZ7nX4IaJDp92\nbpHKsDKsP2T/o8Ex6dG+zsCCTmep9pG5zczecSq1QQKBgQDr322QPlc6idm9d+9x\ngKFkrRnWyUZzTCa0aiV73WKLN4G4k+DAL19qYwFkK5OutECDPBuweb8VSCYvyl5N\nMZcOMvuV+1DYuYhSuBabDfAE+zJMSmETvrSwJk0xEw0FdLgmm3/9O3WvthK5mX6+\nqbsN2Zks/tgG8re07HgsCAYmQQKBgQDNKGnfROTGrlTN7NfQS1/jGYC/6N33nTTm\nrEfdTw7jxBCWaplQrCHOrDhKz1g3UISR6tUY1PECJEV/W/mVylc/Q4yQPaW42WAt\n9KYJ8hVLoiRSPVdrwJAeSMXZypgiBONRKrRAaAGsIWoRpzguUEBB/j5wBPvA0PTg\nBH4WYEJqkQKBgAs6p8ymKyDuTx9mBlAw/337f69qBaCXj4AnTYGIGJjoG5Td9WUw\n3CoEbJyINo+qpSeaRPcx1Jb+yFKeH78tDTPv2WpafI7Uxlipyum20CZsjwhywgxe\nl9uK90HO1l/cHqg33u//VKr40Atl81LAYddW9KPfvgkWpQhH+bCe8SwBAoGAYapu\nlFJ40rilOI8awldPo449g565JKrbR0EWyR1cykNJXkILEKORSJEmDz8cEOEs60Yv\nAi5FOa7IwvOnIo777+sZXIVsgk5Bgj8oWC29w47B2cDIAEzgjvo37hGLUQ6gpMA+\npTaeLTKPCy5fCXU80e3WDX/h1Y3kNU0ONVrH43ECgYBWimuvPTmGwS5rBWC9Z7OD\nvfVT4uSuAiXrDdPo0N9HqCKunSuJIqihA/NJELmq9DrBWZI1AFDXaLBlz2RqBq3T\n4k/BaE9gsS0Tn+K9Plee/fWFkVO6fFTSiARn128VyF9hqXEm0vnIiyYhTQvIkQKZ\nmC+UyHUSL+EjIg1MXbE2vw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ykjt8@first-db-77609.iam.gserviceaccount.com",
    "client_id": "105639461294547029153",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ykjt8%40first-db-77609.iam.gserviceaccount.com"
}
# cred = credentials.Certificate("first-db-77609-firebase-adminsdk-ykjt8-c7599cc9be.json")
# admin = firebase_admin.initialize_app(cred, {'storageBucket': 'first-db-77609.appspot.com', 'databaseURL': 'https://first-db-77609-default-rtdb.firebaseio.com'})
# lala = firebase_admin.get_app()
# print(lala)
# lola = _get_iid_service(lala)


sound = SoundLoader.load('touch.wav')






firebasei = pyrebase.initialize_app(firebaseconfig)

db = firebasei.database()
authi = firebasei.auth()
storage = firebasei.storage()

# f = db.child("Sale").order_by_key().start_at('-NPoq8Avd25h5bvVSq21').limit_to_last(2).get()s

# DNS.defaults['server']=['8.8.8.8', '8.8.4.4']
print('Firebase initialized')

# label = MDLabel()



# client = auth._get_client()
# print(client)

# tgen = TokenGenerator()
# now = tgen.create_custom_token('firebase_token')



# ref = bd.reference('Sale')
# print(ref.order_by_key().start_at("-NOe4vmvTXsUOa6-g0_d").get())

        




        


Builder.load_file("HomeScreen.kv")
Builder.load_file("HomeCards.kv")
Builder.load_file("PropertyCards.kv")
Builder.load_file("PropertyRentCards.kv")
Builder.load_file("DetailScreen.kv")
Builder.load_file("SaleSubmit.kv")
Builder.load_file('RentSubmit.kv')
Builder.load_file('LoginPage.kv')
Builder.load_file("MyProducts.kv")
Builder.load_file("SignInScreen.kv")
Builder.load_file('SaleOrRent.kv')
Builder.load_file('bookmarks.kv')
Builder.load_file('EditDetails.kv')
Builder.load_file('EditRentDetails.kv')
Builder.load_file('search.kv')
Builder.load_file('LoadingScreen.kv')
Builder.load_file('DialogEntry.kv')
Builder.load_file('TheCreator.kv')
Builder.load_file('AppTutorial.kv')
Builder.load_file('Congrats.kv')
Builder.load_file('ForgotPasswordEntry.kv')
Builder.load_file('Warning.kv')
Builder.load_file('Countries.kv')
Builder.load_file('About.kv')
Builder.load_file('Contact.kv')
Builder.load_file('Starter.kv')
Builder.load_file('MyAccount.kv')
Builder.load_file('PasswordResetEntry.kv')
Builder.load_file('DeleteAccountEntry.kv')
Builder.load_file('AccountChoice.kv')
Builder.load_file('AccountItem.kv')
Builder.load_file('CodeVerifyer.kv')



class Input(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class WindowManager(ScreenManager):
    pass

class MainLayout(MDBoxLayout):
    pass

class AccountLoginPage(Screen):
    pass

class CreatorScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class StartingScreen(Screen):
    pass

class MyAccount(Screen):
    text = StringProperty()
    # with open(f'{path}/user.json', 'r') as jsonfile:
    #     curr = json.load(jsonfile)
    # text = curr['email']

    def read_user():
        with open(f'{path}/user.json', 'r') as jsonfile:
            curr = json.load(jsonfile)
        text = curr['email']


class ContactScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    
            
    @mainthread
    def show_dialog(self, notice, button1=None):
        self.dialog = MDDialog(title="Notice", text=notice, size_hint=(1, 1), buttons=[MDFlatButton(text="close", on_release=self.close_dialog), button1])
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()

    @mainthread
    def snackbar(self, text):
        snacky = Snackbar(text=text, snackbar_x="5dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y=None)
        snacky.open()

class HomeScreen(Screen):
    text = StringProperty()
    # with open(f'{path}/user.json', 'r') as jsonfile:
    #     curr = json.load(jsonfile)
    # text = curr['email']
    # print('texted')
    

    def __init__(self, **kw):
        super().__init__(**kw)

    
        
class Loading(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'loading...'
        self.font_size = '16dp'
        self.bold = True
        self.halign ='center'


class CodeVerifyer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        
        


class MainScroll(ScrollView):
    pass

    # def on_scroll_stop(self, touch, check_children=True):
    #     super().on_scoll_stop(touch, check_children=False)
        
class HomeSaleScroll(ScrollView):
    def on_scroll_move(self, touch):
        super().on_scroll_move(touch)
        touch.ud['sv.handled']['y'] = False


class HomeCards(MDCard, CommonElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    phonenumber = StringProperty()
    twitter = StringProperty()
    facebook = StringProperty()
    description = StringProperty()
    amenities = ListProperty()
    



class PropertyRentCards(MDCard, CommonElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    phonenumber = StringProperty()
    description = StringProperty()
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])
    facebook = StringProperty()
    twitter = StringProperty()
    views = NumericProperty()
    
        

       
            
        

    

class PropertySaleCards(MDCard, CommonElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    phonenumber = StringProperty()
    description = StringProperty()
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])
    facebook = StringProperty()
    twitter = StringProperty()
    views = NumericProperty()

    
   
           
    




    

    
class DetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    phonenumber = StringProperty()
    twitter = StringProperty()
    facebook = StringProperty()
    description = StringProperty()
    
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])

    # def __init__(self, *kw):
    #     super().__init__(**kw)

    # def on_pre_enter(self, *args):
        # print('pre-entering')
    #     return super().on_pre_enter(*args)
    
    # def on_enter(self, *args):
        # print('pre-entering')
    #     return super().on_enter(*args)


class EditDetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    description = StringProperty()
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])

class EditRentDetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    country = StringProperty()
    province = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    description = StringProperty()
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])

    def __init__(self, **kw):
        super().__init__(**kw)
        payment_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "/mth",
                
                "on_release": lambda x="/mth": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/yr",
                
                "on_release": lambda x="/yr": self.set_payment(x)
            }
        ]

        
        self.poi = MDDropdownMenu(
            caller=self.ids.pay_item,
            items=payment_items,
            position='center',
            ver_growth='up',
            width_mult=3
        )

        

        self.poi.bind()

    def set_payment(self, text_item):
        self.ids.pay_item.set_item(text_item)
        
        self.ids.pay_item.text = text_item
        print(self.ids.pay_item.text)
    
class SearchScreen(Screen):
    pass

class SpinnerWheel(MDSpinner):
    pass

class SearchLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    

    

    
        
            # print(u.val())

#-NGy3yrvpMXT0jYugGKH

class ErrorLabel(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Internet connection limited or unavailable"
        self.font_size = "30dp"
        self.halign = "center"
        self.size_hint_y = None
        self.adaptive_height = True

class ReturnButton(MDCard):
    positionx = int(Window.size[1]*0.45)
    positiony = int(Window.size[0]*0.8)

class SaleSubmit(Screen):
    bedrooms = StringProperty('0')
    bathrooms = StringProperty('0')
    


class RentSubmit(Screen):
    bedrooms = StringProperty('0')
    bathrooms = StringProperty('0')

    def __init__(self, **kw):
        super().__init__(**kw)
        payment_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "/mth",
                
                "on_release": lambda x="/mth": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/yr",
                
                "on_release": lambda x="/yr": self.set_payment(x)
            }
        ]

        
        self.poi = MDDropdownMenu(
            caller=self.ids.pay_item,
            items=payment_items,
            position='center',
            ver_growth='up',
            width_mult=3
        )

        

        self.poi.bind()

    def set_payment(self, text_item):
        self.ids.pay_item.set_item(text_item)
        
        self.ids.pay_item.text = text_item
        print(self.ids.pay_item.text)

class WordInput(MDTextField):
    pass

class MyProducts(Screen):
    pass

class SignInScreen(Screen):
    pass

class SaleOrRent(Screen):
    pass

class LoadingScreen(Screen):
    pass

class AppTutorial(Screen):
    pass

class Congrats(Screen):
    pass

class DeleteAccountEntry(MDBoxLayout):
    pass

class AccountChoice(ScrollView):
    pass

class PropertyCardsLayout(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.last_sold = 0
        self.loader = []
        self.counter = 0
        print("First initializing")
        self.done = False
        self.denied = 0
        self.deleted = False
        # self.account_choice = MDDropdownMenu(
        #     ver_growth='up',
            
        #     width_mult=5,
        #     position='center',
            
        # )
        
        # self.denied = 0
        
    
    
        
        
    
    

    
    

    @mainthread
    def snackbar(self, snack):
        snacky = Snackbar(text=snack, snackbar_x="5dp", snackbar_y="60dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = None)
        snacky.open()

    def sign_out_auth(self):
        text = 'Are you sure you want to sign out?'
        
        agree_button = MDFlatButton(text='Yes', on_release=self.sign_out)
        self.show_dialog(text,agree_button)

    def sign_out(self,obj=None):
        
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)

        data['email'] = ''
        data['password'] = ''
        data['idToken'] = ''
        data['house_images'] = []
        data['localid'] = ''
        
        
        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        self.loader.clear()
        self.last_sold = 0
        self.clear_widgets()
        p = 'Successfully signed out'
        self.snackbar(p)

    @mainthread
    def clear_all(self):
        self.clear_widgets()

    @mainthread
    def show_thread_dialog(self, notice, titler="Notice"):
        self.dialog = MDDialog(title=titler, text=notice, size_hint=(1, 1), on_open=lambda x:self.delete_user())
        
        self.dialog.open()

    @mainthread
    def toast(self, text):
        toast(text)


    @mainthread
    def show_dialog(self, notice, button=None, titler='Notice'):
        self.dialog = MDDialog(title=titler, text=notice, size_hint=(1, 1), buttons=[MDRaisedButton(text="close", on_press=lambda x:self.dialog.dismiss()), button])
        
        self.dialog.open()
        
    @mainthread
    def close_dialog(self):
        
        
        self.dialog.dismiss()


    # def join_thread(self, obj):
    #     self.delete_thread.join()

    def delete_user_auth(self):
        self.dialog_entry = DeleteAccountEntry()
        self.di = MDDialog(
            title='Please Enter your password to delete your account',
            type='custom',
            content_cls=self.dialog_entry,
            buttons=[
                MDFlatButton(
                    text='Cancel',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.di.dismiss()
                ),
                MDFlatButton(
                    text='Submit',
                    theme_text_color='Custom',
                    text_color='black',
                    on_release=lambda x:self.show_thread_dialog(titler='Deleting Account', notice="Please wait..."),
                    on_press=lambda x:self.di.dismiss()
                )
            ]
        )
        self.di.open()
        
    def thread_delete_user(self, obj):
        self.show_thread_dialog(titler='Deleting Account', notice="Please wait...")

        
        # self.delete_thread = threading.Thread(target=self.delete_user)
        # self.delete_thread.start()
        
        

    
    def delete_user(self):
        
        

        try:
            func_timeout(35, self.delete_account)
        except FunctionTimedOut:
            print("Failed to delete account timedout")
            self.toast("Failed to delete account timedout")
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            print(str(error) + "is the error")
            print(str(error) + "is the error") 
            if error == 'Permission denied':
                print("Permission denied")
                print("Resigning in")
                self.denied += 1
                if self.denied < 2:
                    try:
                        func_timeout(10, self.denied_signin)

                        self.delete_user_auth()
                    except FunctionTimedOut:
                        print("Failed to delete account timedout")
                        self.toast("Failed to delete account timedout")
                        self.denied = 0
                    except:
                        print("Failed to delete account")
                        self.toast("Failed to delete account")
                        self.denied = 0
                        
                else:
                    self.close_dialog()
                    self.show_dialog('All permissions have been denied for deleting your account right now. Please wait until slots are open. Else Contact us and make a request to delete your account in the Contact Page providing us with your account details.')
                    print("Permission finally denied")
                    self.denied = 0
            try:
                if error['message'] == 'Not found.':
                    self.toast("Not found")
                elif error['message'] == 'CREDENTIAL_TOO_OLD_LOGIN_AGAIN':
                    try:
                        func_timeout(10, self.denied_signin)

                        self.delete_user_auth()
                    except FunctionTimedOut:
                        print("Failed to delete account timedout")
                        self.toast("Failed to delete account timedout")
                    except:
                        print("Failed to delete account")
                        self.toast("Failed to delete account")
            except:
                pass
            
        except:
            print("An Unknown error occured")
            self.toast("Failed to delete account")
            self.deleted=True
        self.deleted = True
        self.close_dialog()
        
    

    def denied_signin(self):
        self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
        usero = authi.refresh(self.user['refreshToken'])
        self.curr['idToken'] = self.user['idToken']
        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)

    def delete_account(self):
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            dati = json.load(jsonfile)
            print(dati['password'])
        print(self.dialog_entry.ids.passy.text)
        if dati['email'] and dati['password'] != "":
            # try:
            print(self.dialog_entry.ids.passy.text)
            if self.dialog_entry.ids.passy.text == dati['password']:   
                message = MIMEText(dati['email'] + " " + "with localid" + " " + dati['localid'] + " " + "Just deleted their account")
                message['Subject'] = "Deleted account Notice"
                message["From"] = "anangjosh8@gmail.com"
                message["To"] = "anangjosh8@gmail.com"
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
                server.sendmail("anangjosh8@gmail.com", "anangjosh8@gmail.com", message.as_string())
                server.quit() 
                # user = authi.sign_in_with_email_and_password(dati['email'], dati['password'])
                # db.child("People").child(user['localId']).remove()
                testichiro = db.child("People").child(dati['localid']).child("ids").get(dati['idToken'])
                # testiroro = db.child("People").child(dati['localid']).child("ids").get(dati['idToken'])
                if testichiro.each():
                    for i in testichiro.each():

                        

                        dude = i.val()['prop_keys']
                        db.child("Sale").child(dude).remove(dati['idToken'])
                        db.child("Rent").child(dude).remove(dati['idToken'])
                        
                        
                        
                # local = r"{dati['localid']} + /"
                # storage.delete(local, dati['idToken'])
                
                db.child("People").child(dati['localid']).remove(dati['idToken'])
                            
                # except:
                #     print("DOesn't own property")
                

                        

                #         dudo = q.val()['prop_keys']
                #         db.child("Rent").child(dudo).remove(dati['idToken'])

                #         local = dati['localId'] + '/'                    
                #         storage.delete(local + i, dati['idToken'])
                
                # storage.delete(dati['localId'], dati['idToken'])
                    
                
                
                authi.delete_user_account(dati['idToken'])
                print("Removed account")
                
                for i in dati['accounts']:
                    if i['email'] == dati['email']:
                        dati['accounts'].remove(i)

                del dati['bookmarks'][dati['email']]
                del dati['viewed'][dati['email']]
                del dati['sold'][dati['email']]
                dati['email'] = ''
                dati['password'] = ''
                dati['idToken'] = ''
                dati['house_images'] = []
                
                dati['localid'] = ''

                
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(dati, jsonfile)
                
                self.snackbar('Successfully deleted account')
                print("successfully deleted account")
                self.clear_all()
                self.denied = 0
                # self.dialog.ids.passy = ''
            else:
                print('Invalid Password')
                text = "Invalid password"
                
                self.show_dialog(text)
                # self.dialog_entry.ids.passy = ''
    #    except:
            # print("Operation unsuccessful")
    #         p = 'Operation Unsuccessful'
    #         self.snackbar( p)
        else:
            p = 'No user signed in'
            self.snackbar(p)

    
        
    
        
            # Animation(opacity=0, duration = 0.5).start(self.loading)
        # except Exception as e:
        #     print("Network Error")
        #     toast("Network Error")
        
        
           
       
        # threading.Thread(target=self.added).start()
        
        
        # house = {
        #     'Housing': [{
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '1',
        #         'House_type': 'New House'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '2',
        #         'House_type': 'New House'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '3',
        #         'House_type': 'New House'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House'
        #     }
        #     ]
            
        # }
        # for i in house['Housing']:
        #     self.card = PropertySaleCards()
        #     self.card.tot= i["House_type"]
        #     self.card.image = i['Image']
        #     self.card.bedrooms = i['bedrooms']
            
        #     self.add_widget(self.card)
    
    # def added(self):
    #     print('mmhmm')
        
    #     with open(f'{path}/user.json', 'r') as jsonfile:
    #         self.curr = json.load(jsonfile)
        
        

    #     # print(a.val())
    #     # if a.key() == 'local_image':
    #         # print(a.val())
    #     #     curr['house_images'].append(a.val())

    #     #     with open(f'{path}/user.json', 'w') as jsonfile:
    #     #         json.dump(curr, jsonfile)
        
    #     print(self.curr['idToken'])
    #     print('OOh ma gaa')

    #     print(str(self.last_sold) + " " + "init last sold")
        
    #     if self.curr['email'] != '':
    #         if self.curr["sold"][self.curr['email']] > self.last_sold:
    #             print("Initializing")
    #             self.testichiro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
    #             # self.testiroro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
    #             self.last_sold = self.curr["sold"][self.curr['email']]
    #             print("After last sold")

    #             if self.testichiro.each():
            
    #                 for q in self.testichiro.each():
    #                     self.dude = q.val()['prop_keys']
    #                     print(self.loader)
    #                     if self.dude not in self.loader:
    #                         self.yours = db.child("Sale").order_by_key().equal_to(self.dude).get()
    #                         self.ours = db.child("Rent").order_by_key().equal_to(self.dude).get()
    #                         self.next_after(self.yours, self.ours)
    #                     else:
    #                         print("Already loaded booom in sale")
                            
    #             # if self.testiroro.each():
            
    #             #     for d in self.testiroro.each():    
    #             #         self.bruv = d.val()['prop_keys']
    #             #         if self.bruv not in self.loader:
    #             #             self.ours = db.child("Rent").order_by_key().equal_to(self.bruv).get()
    #             #             self.next_after(self.ours)
    #             #         else:
    #             #             print("Already loaded booom")
    #             #             print(self.loader)
    #     # Animation(opacity=0, duration = 0.5).start(self.loading)
        
        
    

    # @mainthread
    # def next_after(self, yours, ours):
    #     print("Hey")
        
    #     if yours:
    #         for u in yours:
    #                     # another = person.val()
                        
            
            
            
                
    #             print('Okay maybe it wokred')
    #             self.card = PropertySaleCards()
    #             self.card.image = u.val()['url']
    #             self.card.amenities = u.val()['amenities']
    #             self.card.tot = u.val()['housetype']
    #             self.card.country = u.val()['country']
    #             self.card.province = u.val()['state']
    #             self.card.town = u.val()['town']
    #             self.card.street = u.val()['street']
    #             self.card.bedrooms = u.val()['bedrooms']
    #             self.card.bathrooms = u.val()['bathrooms']
    #             self.card.landspace = u.val()['landspace']
    #             self.card.email = u.val()['email']
    #             self.card.price = u.val()['price']
    #             self.card.key = u.key()
    #             self.card.phonenumber = u.val()['phonenumber']
    #             self.card.twitter = u.val()['twitter']
    #             self.card.facebook = u.val()['facebook']
    #             self.card.description = u.val()['description']
    #             self.card.views = u.val()['views']
    #             self.card.local_image = u.val()['local_image']
                
    #             self.add_widget(self.card)
    #             print(self.loader)
    #             self.loader.append(u.key())
            
    #         # print("added")
    #         # print(self.loader)
            
    
                    
    #                     # print(self.loader)
                

    #     if ours:
    #         for u in ours:
                
    #             print(u.key())
                
                
                
                
    #             print(u.val()['url'])
                
                    
    #             print('Okay maybe it wokred')
    #             self.card = PropertyRentCards()
    #             self.card.image = u.val()['url']
    #             self.card.amenities = u.val()['amenities']
    #             self.card.tot = u.val()['housetype']
    #             self.card.country = u.val()['country']
    #             self.card.province = u.val()['state']
    #             self.card.town = u.val()['town']
    #             self.card.street = u.val()['street']
    #             self.card.bedrooms = u.val()['bedrooms']
    #             self.card.bathrooms = u.val()['bathrooms']
    #             self.card.landspace = u.val()['landspace']
    #             self.card.email = u.val()['email']
    #             self.card.price = u.val()['price']
    #             self.card.key = u.key()
    #             self.card.phonenumber = u.val()['phonenumber']
    #             self.card.twitter = u.val()['twitter']
    #             self.card.facebook = u.val()['facebook']
    #             self.card.description = u.val()['description']
    #             self.card.views = u.val()['views']
    #             self.card.local_image = u.val()['local_image']
                
    #             self.add_widget(self.card)
                
    #             self.loader.append(u.key())
    #             # print("added")
    #             print(self.loader)
    #             print(self.counter)
                    
        
                        

    # def reload(self):
    #     # self.loader.remove(key)
        
        
    #     print('pressde')
    #     print('disbaled')
        
    #     self.loader.clear()
    #     self.last_sold = 0
    #     print("Reloading")
    #     self.clear_widgets()
        # self.begin_loading()
        
       
    
        

                    
    

        
        
        
        # try:
        #     testichiro = db.child("People").child(dato['localid']).child("ids").get(dato['idToken'])
        #     for q in testichiro.each():
                
        #         dude = q.val()['prop_keys']
                
        #         them = db.child("Sale").child(dude).child("amenities").get(dato['idToken'])
        #         them1 = db.child("Sale").child(dude).child("bathrooms").get(dato['idToken'])
        #         them2 = db.child("Sale").child(dude).child("bedrooms").get(dato['idToken'])
        #         them3 = db.child("Sale").child(dude).child("country").get(dato['idToken'])
        #         them4 = db.child("Sale").child(dude).child("description").get(dato['idToken'])
                
        #         them7 = db.child("Sale").child(dude).child("housetype").get(dato['idToken'])
        #         them8 = db.child("Sale").child(dude).child("landspace").get(dato['idToken'])
        #         them9 = db.child("Sale").child(dude).child("local_image").get(dato['idToken'])
                
        #         them11 = db.child("Sale").child(dude).child("price").get(dato['idToken'])
        #         them12 = db.child("Sale").child(dude).child("street").get(dato['idToken'])
        #         them13 = db.child("Sale").child(dude).child("state").get(dato['idToken'])
                
        #         them14 = db.child("Sale").child(dude).child("town").get(dato['idToken'])
        #         them15 = db.child("Sale").child(dude).child("url").get(dato['idToken'])
                
        #         dato['house_images'].append(them9)

                
                
        #         self.card = PropertySaleCards()
        #         self.card.key = dude
        #         self.card.amenities = them.val()
        #         self.card.bathrooms = them1.val()
        #         self.card.bedrooms = them2.val()
        #         self.card.country = them3.val()
        #         self.card.description = them4.val()
                
        #         self.card.tot = them7.val()
        #         self.card.landspace = them8.val()
        #         self.card.local_image = them9.val()
                
        #         self.card.price = them11.val()
        #         self.card.street = them12.val()
        #         self.card.province = them13.val()
                
        #         self.card.town = them14.val()
        #         self.card.image = them15.val()
        #         self.add_widget(self.card)
        #     # with open(f'{path}/user.json', 'w') as jsonfile:
        #     #     json.dump(dato, jsonfile)
        # except:
        #     pass
        
                    
                    

            # againi = db.child("People").child("Sale").child(dato['localid']).child("house").get()

            # for u in againi.each():
                
            #     self.card.image = u.val()['url']
            #     self.card.tot = u.val()['housetype']
            #     self.card.country = u.val()['country']
            #     self.card.bedrooms = u.val()['bedrooms']
            #     self.card.bathrooms = u.val()['bathrooms']
            #     self.card.landspace = u.val()['landspace']
            #     self.card.email = u.val()['email']
            #     self.card.price = u.val()['price']
            #     self.card.key = u.key()
            #     self.card.town = u.val()['town']
            #     self.card.street = u.val()['street']
            #     self.card.local_image = u.val()['local_image']
            #     self.card.phonenumber = u.val()['phonenumber']
            #     self.card.description = u.val()['description']
            #     self.card.amenities = u.val()['amenities']
            #     self.add_widget(self.card)
            #     dato['house_images'].append(u.val()['local_image'])
            


            
            # again = db.child("People").child("Rent").child(dato['localid']).child("house").get()

            # for u in again.each():
            #     self.cardi = PropertyRentCards()
            #     self.cardi.image = u.val()['url']
            #     self.cardi.tot = u.val()['housetype']
            #     self.cardi.country = u.val()['country']
            #     self.cardi.bedrooms = u.val()['bedrooms']
            #     self.cardi.bathrooms = u.val()['bathrooms']
            #     self.cardi.landspace = u.val()['landspace']
            #     self.cardi.email = u.val()['email']
            #     self.cardi.price = u.val()['price']
            #     self.cardi.key = u.key()
            #     self.cardi.town = u.val()['town']
            #     self.cardi.street = u.val()['street']
            #     self.cardi.local_image = u.val()['local_image']
            #     self.cardi.phonenumber = u.val()['phonenumber']
            #     self.cardi.description = u.val()['description']
            #     self.add_widget(self.cardi)
            #     dato['house_images'].append(u.val()['local_image'])

           
                
        
        

                

# class call_control:

#     def __init__(self, max_call_interval):
#         self._max_call_interval = max_call_interval
#         self.last_call = time()

#     def __call__(self, function):

#         def wrapped(*args, **kwargs):
#             now = time()

#             if now > self._max_call_interval:
#                 self.last_call = now
#                 print("Is less than")
#                 function(*args, **kwargs)

#         return wrapped



# class Effect(DampedScrollEffect):

#     def on_overscroll(self, *args):
#         super().on_overscroll(*args)
#         # self.call_reload()
        
#         if self.overscroll <= -20:
#             self.call_reload()

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

        # self.min_overscroll = -20
        # self.overscroll = -20
        
        
        

    # @call_control(max_call_interval=1)
    # def call_reload(self):
    #     print('Reloading')
        
        # p = PropertyCardsLayout()
        # p.reload()
        # rd = Reload()
        # rd.setPos()
#         print("Overscrolled")
#         # self.root.ids.layout.reload()
#         self.overscroll = 0
#         if self.overscroll == 0:
#             self.homesser = HomeCardsLayout()
#             self.homesser.added()
#             self.do_something()
#         else:
#             pass

#     # @call_control(max_call_interval=1)
#     def do_something(self):
#         self.homesser = HomeCardsLayout()
#         self.homesser.added()
#         self.homesser.something = True


class Scroller(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_scroll_x = False
        self.do_scroll_y = True
        # self.effect = Effect
        # self.effect_cls = Effect
        
        
        


class HomeCardsLayout(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.j = 0
        self.last = ''
        self.something = ''
        self.counter = 0
        self.event=Event()
        self.thread_added()
        

    def thread_added(self):
        self.event=Event()
        self.thread_adding = threading.Thread(target=self.timing_added)
        self.thread_adding.start()
        

    def thread_other(self):
        self.event=Event()
        self.threa = threading.Thread(target=self.other).start()

    def timing_added(self):
        
        if not self.event.is_set():
            try:
                func_timeout(10, self.added)
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
            # except Exception as e:
            #     print("Network Error")
            #     self.toast("Network Error")
            #     self.event.set()

    @mainthread
    def toast(self, text):
        toast(text)

    def refresh(self):
        self.thread_added()
        
    def added(self):
        
        print("Okay now are you repeating the process or what tell me tell me tell me tell me")
        # house = {
        #     'Housing': [{
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House',
        #         'country': 'Netherlands',
        #         'town': 'Zwolle',
        #         'street': 'Zwolle Street ave.',
        #         'landspace': '345sq.ft',
        #         'description': "This is awesome i don't know what to say anymore zehahahahaha.....the dreams of pirates will never end.",
        #         'amenities': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
        #         'price': '$15,678'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House',
        #         'country': 'Canada',
        #         'town': 'Quebec',
        #         'street': 'Quebec Street ave.',
        #         'landspace': '345sq.ft',
        #         'description': "This is awesome i don't know what to say anymore zehahahahaha.....the dreams of pirates will never end.",
        #         'amenities': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
        #         'price': '$15,678'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House',
        #         'country': 'Mexico',
        #         'town': 'Mexico City',
        #         'street': 'Mexico Street ave.',
        #         'landspace': '345sq.ft',
        #         'description': "This is awesome i don't know what to say anymore zehahahahaha.....the dreams of pirates will never end.",
        #         'amenities': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
        #         'price': '$15,678'
        #     },
        #     {
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House',
        #         'country': 'Turkey',
        #         'town': 'Turkey City',
        #         'street': 'Turkey st.',
        #         'landspace': '345sq.ft',
        #         'description': "This is awesome i don't know what to say anymore zehahahahaha.....the dreams of pirates will never end.",
        #         'amenities': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'],
        #         'price': '$15,678'
        #     }
        #     ]
            
        # }
        # print(self.j)
        # if self.j >= len(house['Housing']):
        #     self.j == len(house)
            # print(self.j)
        # else:
        #     for i in house['Housing']:
                # print(i)
        #         self.card = HomeCards()
        #         self.card.tot= i["House_type"]
        #         self.card.image = i['Image']
        #         self.card.bedrooms = i['bedrooms']
        #         self.card.country = i['country']
        #         self.card.town = i['town']
        #         self.card.street = i['street']
        #         self.card.landspace = i['landspace']
        #         self.card.description = i['description']
        #         self.card.price = i['price']
        #         self.card.bedrooms = i['bedrooms']
        #         self.card.amenities = i['amenities']
        #         self.add_widget(self.card)
        #         self.j += 1
        #         if self.j % 3 == 0:
        #             break
        #         if self.j >= len(house['Housing']):
        #             break
                # print(self.j)

        bath_or_bed = ['bedrooms', 'bathrooms']
        first_choice = random.choice(bath_or_bed)
        print(first_choice)
        num = ['1', '2', '3', '4', '5', '6', '7', '7+']
        nume = random.choice(num)
        print(nume)
        if first_choice == 'bedrooms':
            self.people = db.child("Sale").order_by_child('bedrooms').equal_to(nume).limit_to_first(5).get()
        else:
            self.people = db.child("Sale").order_by_child('bathrooms').equal_to(nume).limit_to_first(5).get()
        if self.people.each():
            # if len(self.people.each()) < 1:
            #     self.thread_added()
                
            # else:
            print(len(self.people.each()))
            self.done()
            
        else:
            print(self.people.each())
            print("self.peop,e")
            self.thread_added()
            # self.done()
        

    @mainthread
    def done(self):
        self.j = 0
        # if self.people.each():
        for u in self.people.each():
            self.something = u.key()
            self.card = HomeCards()
            
                
            self.card.image = u.val()['url']
            
            self.card.tot = u.val()['housetype']
            self.card.country = u.val()['country']
            self.card.province = u.val()['state']
            self.card.town = u.val()['town']
            self.card.street = u.val()['street']
            self.card.bedrooms = u.val()['bedrooms']
            self.card.bathrooms = u.val()['bathrooms']
            self.card.landspace = u.val()['landspace']
            self.card.email = u.val()['email']
            self.card.price = u.val()['price']
            self.card.key = u.key()
            self.card.phonenumber = u.val()['phonenumber']
            self.card.twitter = u.val()['twitter']
            self.card.facebook = u.val()['facebook']
            self.card.description = u.val()['description']
            self.card.amenities = u.val()['amenities']
            
            self.add_widget(self.card)
            self.last = u.key()
            print('second iteration')
            self.j += 1
            print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            
            # another = person.val()
            print('First iteration')
            print(self.something)
                # break

        

        
            
                    
                    
        

        
    def other(self):
        if not self.event.is_set():
            try:
                func_timeout(10, self.omagaa)
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
            # except Exception as e:
            #     print("Network Error")
            #     self.toast("Network Error")
            #     self.event.set()
        
    @mainthread
    def clear(self):
        # toast("Self.j is full now dude")
        self.clear_widgets()

    def omagaa(self):
        # with open(f'{path}/user.json', 'r') as jsonfile:
        #     self.curr = json.load(jsonfile)
        #     print(self.curr['localid'])

        if self.something == '':
            # num = ['1', '2', '3', '4', '5', '6', '7', '7+']
            # nume = random.choice(num)
            # print(nume)
            
            # self.people = db.child("Sale").order_by_child('bedrooms').equal_to(nume).limit_to_first(5).get()
            # if self.people.each():
            #     # if len(self.people.each()) < 1:
            #     #     self.thread_added()
                    
            #     # else:
            #     print(len(self.people.each()))
            #     self.done()
                
            # else:
            #     print(self.people.each())
            #     print("self.peop,e")
            #     self.thread_added()
            self.added()

        else:
            
            
                
            # if self.j >= 5:
            print("Starting again")
            print(self.j)
            # bath_or_bed = ['order_by_key', 'order_by_val']
            # first_choice = random.choice(bath_or_bed)
            # print(first_choice)
            # num = ['1', '2', '3', '4', '5', '6', '7', '7+']
            # nume = random.choice(num)
            # print(nume)
            # if first_choice == 'order_by_val':
            #     print(str(self.j) + "This is self.jjjjjjj oh yeaaaahhhh")
            #     self.people = db.child("Sale").order_by_value().start_at(self.something).limit_to_first(5).get()
                
                
            # else:
            print(str(self.j) + "This is self.jjjjjjj oh yeaaaahhhh")
            self.people = db.child("Sale").order_by_key().start_at(self.something).limit_to_first(5).get()
                
                
            if self.j >= 5:
                if len(self.people.each()) >= 2:
                    self.clear()
            
            print(self.j)
            print("Checking if full")
            print(str(len(self.people.each())) + "This is the length of the new self.epple")
            self.j = 0
            self.another()
                    
            

    @mainthread
    def otheri(self):
        
        print('Is it working')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        
        if self.people.each():
            for u in self.people.each():
                self.something = u.key()
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                self.last = u.key()
                print('second iteration')
                self.j += 1
                print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                
                # another = person.val()
                print('First iteration')
                print(self.something)
                 
                break

    @mainthread
    def another(self):    
            
        
        
        if self.people.each():
            for u in self.people.each()[self.j:self.j+5]:
                # for i in u.val()['house']['-NL8x6ZNQQFpsXDfgm7c']['bathrooms']:
                
                    # print(i)
                if u.key() == self.something:
                    continue
                
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                
                self.add_widget(self.card)
                
                self.last = u.key()
                self.something = u.key()
                self.j += 1
                
                print(self.j)
            

        
        # print(again.val())
        # print(self.last)
    
        
    


        

class RentCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.last = ''
        self.j = 0
        self.something = ''
        self.event=Event()
        self.thread_added()

    @mainthread
    def toast(self, text):
        toast(text)

    def thread_added(self):
        self.event=Event()
        self.threa = threading.Thread(target=self.timing_added)
        self.threa.start()
    
    def timing_added(self):
        if not self.event.is_set():
            try:
                func_timeout(10, self.added)
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
            except:
                print("Network Error")
                self.toast("Network Error")
                self.event.set()

    def refresh(self):
        self.thread_added()
        # house = {
        #     'Housing': [{
        #         'Image': 'Brick House.jpg',
        #         'bedrooms': '1',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Brick House.jpg',
        #         'bedrooms': '2',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Brick House.jpg',
        #         'bedrooms': '3',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Brick House.jpg',
        #         'bedrooms': '4',
        #         'House_type': 'New House'
        #     }
        #     ]
            
        # }
        # for i in house['Housing']:
        #     self.card = HomeCards()
        #     # self.card.tot= i["House_type"]
        #     # self.card.image = i['Image']
        #     # self.card.bedrooms = i['bedrooms']
        #     self.add_widget(self.card)
    def added(self):
        bath_or_bed = ['bedrooms', 'bathrooms']
        first_choice = random.choice(bath_or_bed)
        print(first_choice)
        num = ['1', '2', '3', '4', '5', '6', '7', '7+']
        nume = random.choice(num)
        print(nume)
        if first_choice == 'bedrooms':
            self.people = db.child("Rent").order_by_child('bedrooms').equal_to(nume).limit_to_first(5).get()
        else:
            self.people = db.child("Rent").order_by_child('bathrooms').equal_to(nume).limit_to_first(5).get()
        if self.people.each():
            # if len(self.people.each()) < 1:
            #     self.thread_added()
                
            # else:
            print(len(self.people.each()))
            self.done()
            
        else:
            print(self.people.each())
            print("self.peop,e")
            self.thread_added()

    @mainthread
    def done(self):
        print('Renting')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        self.j = 0
            
        
        for u in self.people.each():
            self.something = u.key()
            self.card = HomeCards()
            self.card.image = u.val()['url']
            self.card.tot = u.val()['housetype']
            self.card.country = u.val()['country']
            self.card.town = u.val()['town']
            self.card.province = u.val()['state']
            self.card.street = u.val()['street']
            self.card.bedrooms = u.val()['bedrooms']
            self.card.bathrooms = u.val()['bathrooms']
            self.card.landspace = u.val()['landspace']
            self.card.email = u.val()['email']
            self.card.price = u.val()['price']
            self.card.key = u.key()
            self.card.phonenumber = u.val()['phonenumber']
            self.card.twitter = u.val()['twitter']
            self.card.facebook = u.val()['facebook']
            self.card.description = u.val()['description']
            self.card.amenities = u.val()['amenities']
            self.add_widget(self.card)
            self.last = u.key()
            print('second iteration')
            
            print('second iteration')
            # self.j += 1
            print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            
            # another = person.val()
            print('First iteration')
            print(self.something)
            # break

    @mainthread
    def clear(self):
        print("Self.j is full now dude!!!")
        # toast("Self.j is full now dude")
        self.clear_widgets()

    def thread_other(self):
        self.event=Event()
        self.threa = threading.Thread(target=self.other).start()
        
    def other(self):
        if not self.event.is_set():
            try:
                func_timeout(10, self.omagaa)
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.is_set()
            except:
                self.toast("Network Error")
                print("Network Error")
                self.event.is_set()
        else:
            print("Self. event has been set for rent cards layout")
        

    def omagaa(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])

        if self.something == '':
            self.added()

        else:
           
            print(str(self.j) + "This is self.jjjjjjj oh yeaaaahhhh")
            self.people = db.child("Rent").order_by_key().start_at(self.something).limit_to_first(5).get()
                
                
            if self.j >= 5:
                if len(self.people.each()) >= 2:
                    self.clear()
            
            print(self.j)
            print("Checking if full")
            print(str(len(self.people.each())) + "This is the length of the new self.epple")
            self.j = 0
            self.another()
            
                    
            
            
           

    @mainthread
    def otheri(self):
        print('Is it working')
        
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        
        
        
        if self.people.each():
            for u in self.people.each():
                self.something = u.key()
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                self.last = u.key()
                print('second iteration')
                self.j += 1
                print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                
                # another = person.val()
                print('First iteration')
                print(self.something)
                break

    @mainthread
    def another(self):
            
        print(self.people.val())
        if self.people.each():
            for u in self.people.each()[self.j:self.j+5]:
                # for i in u.val()['house']['-NL8x6ZNQQFpsXDfgm7c']['bathrooms']:
                    
                    # print(i)
                if u.key() == self.something:
                    continue
                
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                self.last = u.key()
                self.something = u.key()
                self.j += 1
            


class BookmarkScreen(Screen):
    pass
    


class BookmarkLayout(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    

    @mainthread
    def show_dialog(self, notice, button=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[MDRaisedButton(text="close", on_release=self.close_dialog), button])
        self.dialog.open()

    @mainthread
    def close_dialog(self,obj):
        self.dialog.dismiss()
        
    def clear_bookmarks_auth(self):
        
        text = 'Are you sure you want to clear all of your bookmarks?'
        
        agree_button = MDFlatButton(text='Yes', on_press=self.clear_bookmarks, on_release=self.close_dialog)
        self.show_dialog(text,agree_button)   

    def clear_bookmarks(self,obj):
        self.curr['bookmarks'][self.curr['email']] = []
        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)
        self.clear_widgets()
        print('Bookmarks cleared')
        


class DialogEntry(MDBoxLayout):
    pass


class ForgotPasswordEntry(MDBoxLayout):
    pass

class PasswordResetEntry(MDBoxLayout):
    pass

class Warning(MDBoxLayout):
    pass
            
class Countries(MDBoxLayout):
    pass

# list_item = OneLineAvatarListItem()

class List_item(OneLineListItem):
    method = StringProperty()

class Recycle(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': 'x'} for x in range(1)]

class Listings(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # def added(self):
        self.counter = 0
        Clock.schedule_interval(self.start, 0.3)
        
    def start(self, time):
        if self.counter < 50:
            countries = pycountry.countries
        
            for i in countries:
                
                list_item = List_item()
                list_item.text = i.name
                list_item.opacity = 0
                self.add_widget(list_item)
                Animation(opacity=1, duration=0.25).start(list_item)
                self.counter +=1
                
                

# princekofasiedu



class AccountItem(OneLineListItem):
    pass
                    



        

class MainApp(MDApp):
    def build(self):

        # self.screensers = [HomeScreen(name="Home"), DetailsScreen(name="detail"),  SaleSubmit(name="Sale"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SignInScreen(name="sign-in"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks'), EditDetailsScreen(name='edit'), EditRentDetailsScreen(name='edit-rent'), LoadingScreen(name="loading"), CreatorScreen(name='creator'), Congrats(name='congrats')]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        self.wm.transition = WipeTransition()
        self.wm.transition.duration = .2
        self.kill = False
        self.has_error = False
        self.splash()
        self.account = MyAccount(name='acc')
        self.signup = AccountLoginPage(name="sign-up")
        self.signin = SignInScreen(name="signin")
        self.starter = StartingScreen(name='starter')
        self.code_verifyer = CodeVerifyer(name="code")
        
        self.SaleOrRent = SaleOrRent(name="SaleOrRent")
        
        self.home = HomeScreen(name="Home")
        self.edit_rent = EditRentDetailsScreen(name="edit-rent")
        self.edit_sale = EditDetailsScreen(name="edit")
        self.bk = BookmarkScreen(name='bookmarks')
        self.products = MyProducts(name="products")
        self.about = AboutScreen(name="about")
        self.contact = ContactScreen(name="contact")
        self.detail = DetailsScreen(name="details")
        
        
        self.search = SearchScreen(name="search")
        self.loading = LoadingScreen(name="loading")
        self.creator_screen = CreatorScreen(name='creator')
        self.tutorial = AppTutorial(name='tutor')
        self.congrats = Congrats(name='congrats')
        self.warning = Warning()
        # self.pt = PropertyCardsLayout()

        

        self.screenos = []
        self.screeni = []
        self.denied = 0
        self.current_screen = ''
        self.sign_in_current = ''

        # self.wm.current = 'starter'
        # self.wm.switch_to(self.starter)
        

        choice_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Sale",
                
                "on_release": lambda x="Sale": self.set_item(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Rent",
                
                "on_release": lambda x="Rent": self.set_item(x)
            }
        ]

        self.choice = MDDropdownMenu(
            caller=self.search.ids.drop_item,
            
            position='center',
            width_mult=3
        )

        

        for i in choice_items:
            self.choice.items.append(i)
        
        
        
            
        self.close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)


        # size = Window.size[1]
        # real_size = str(size/3-60) + 'dp'
        # print(real_size)
        # print(Window.size[1])
        # print(Window.size[0])
        # self.home.ids.btn.user_font_size = real_size
        
  
        


        
        # self.account_choice = AccountChoice()
        
        
        

        # for i in self.screensers:
        #     self.wm.add_widget(i)
        
        # self.event = Event()
        
        # self.switch_loading()
        
        self.loader = []
        self.last_sold = 0
        self.numberiy = 'item 0'


        self.last_rec = 0
        self.loaded = []
        self.counter = 0

        

        self.sale_or_rent = ''
        
        self.mail = ''
        self.passwrd = ''
        self.confirmed = ''
        self.sign_in_mail = ''
        self.sign_in_pass = ''
        self.source = 'Images\Pirate King (2).jpg'

        self.tot = 'Nice House'
        self.country = 'Australia'
        self.state = 'New South Wales'
        self.town = 'Sydney'
        self.street = 'Sydney Street'
        self.bedrooms = '6'
        self.bathrooms = '3'
        self.landspace = '542'
        self.price = '120000'
        self.phonenumber = ''
        self.desc = 'Brief description will appear here..'
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        self.twitter = ''
        self.facebook = ''
        return self.wm
        return super().build()
    
    def switch_choice(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        self.account_choosing = AccountChoice()
        # accounts = [
        #     {
        #         "viewclass": "OneLineListItem",
        #         "text": acc['email'],
        #         "divider": None,
        #         "on_release": lambda x=acc['email'], y=acc['password']: self.switch(x, y)
        #     }
        #     for acc in self.curr['accounts']
        # ]

        self.account_choose = MDDialog(
            title='Accounts',
            type='custom',
            content_cls=self.account_choosing,

        )

        
        self.account_choose.open()
        
        # self.account_choice.caller=MyProducts().ids.account_choice
        for i in self.curr['accounts']:
            print(i)
            self.account_item = AccountItem()
            self.account_item.text = i['email']
            self.account_item.divider = None
            self.account_choosing.ids.account_listings.add_widget(self.account_item)
                
        
    def close_account_choose(self):
        sound.play()
        self.account_choose.dismiss()
        # self.account_choice.items.append(add_another)

        # self.account_choice.open()

    def switch(self, email):
        print(email)
        
        self.loading.ids.spin.active=True
        self.switch_loading()
        self.event = Event()
        self.thread_now = threading.Thread(target=self.switch_now, args=(email,))
        self.thread_now.start()

    def switch_now(self, email):
        # self.snackbar('Switching account....')s
        

        if not self.event.is_set():
            print('switching account')
            print(email)
            for i in self.curr['accounts']:
                if i['email'] == email:
                    password = i['password']
                    print(password)

            try:
                func_timeout(20, self.switch_account, args=(email, password,))
                
                self.switch_products()
                
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
                time.sleep(1)
                self.true_switch_products()
                self.spin_false()
            
        
            # except:
            #     print("Failed to switch account")
            #     self.toast("Failed to switch account")
                
            #     self.event.set()
            #     time.sleep(1)
            #     self.true_switch_products()
            #     self.spin_false()


    def switch_account(self, email, password):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        print(self.curr['email'])
        print(email)
        print(password)
        self.user = authi.sign_in_with_email_and_password(email, password)
        ino = authi.get_account_info(self.user['idToken'])
        if ino['users'][0]['emailVerified'] != True:
            authi.send_email_verification(self.user['idToken'])
            text = "An email verification link has been sent to your mail"
            
            self.show_dialog(text)
        
        self.curr['email'] = email
        self.curr['password'] = password
        self.curr['idToken'] = self.user['idToken']
        self.curr['localid'] = self.user['localId']

        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)
        self.snackbar('Successfully signed in loading properties')
        # self.account_choose.dismiss()
        self.loader.clear()
        self.last_sold = 0
        self.clear_products()
        


    def reload_products(self):
        self.loading.ids.spin.active = True
        self.switch_loading()
        print("Produts reloading")

        self.loader.clear()
        self.last_sold = 0
        self.products.ids.layout.clear_widgets()
        
        self.begin_loading()
        # time.sleep(5)
        # self.true_switch_products()

    def begin_loading(self):
        
       
        self.event = Event()
        self.th = threading.Thread(target=self.begin_now)
        self.th.start()
        

    def begin_now(self):
        # self.last_sold = 0
        # self.loading = Loading()
        
        # print(self.loader)
        print("Beginning now")
        print(self.event.is_set())
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            # print(self.curr)
            try:
                func_timeout(25, self.added)
            except FunctionTimedOut:
                print("Failed to load properties timed out")
                self.toast("Failed to load properties timed out")
                self.event.set()
                # self.true_switch_products()
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                print(str(error) + "is the error")
                print(str(error) + "is the error") 
                if error == 'Permission denied':
                    print("Permission denied")
                    print("Resigning in")
                    
                    # try:
                    try:
                        func_timeout(10, self.denied_signin)
                        self.begin_loading()
                    except FunctionTimedOut:
                        print("Failed to resign in timedout")
                        self.toast("Failed to resign in timedout")
                        self.event.set()
                        # self.true_switch_products()
                        
                    except:
                        print("Failed to resign")
                        self.toast("Failed to resign")
                        self.event.set()
                        # self.true_switch_products()
                        
                    
            except:
                self.toast("Failed to load properties")
                print("Failed to load properties")
                self.event.set()
                # self.true_switch_products()
            print(self.wm.current)
            time.sleep(1)
            self.true_switch_products()
        else:
            print("Event has been set")
            
        
        
        # self.spin_false()
        print("spin falllllsssssseeeeee")
        print(self.wm.current)
        

    @mainthread
    def true_switch_products(self):
        self.wm.transition=NoTransition()
        self.wm.switch_to(self.products)




    @mainthread
    def clear_products(self):
        self.products.ids.layout.clear_widgets()

    # @mainthread
    def switch_products(self):
        
        self.loading.ids.spin.active = True
        self.switch_loading()
        self.passwrd = ''
        self.mail = ''
        self.sign_in_current = 'products'
        
        self.begin_loading()
        
        # self.wm.switch_to(self.products)
        print(self.products.ids.layout.done)
        



    def added(self):
        print('mmhmm')
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        
        

        # print(a.val())
        # if a.key() == 'local_image':
            # print(a.val())
        #     curr['house_images'].append(a.val())

        #     with open(f'{path}/user.json', 'w') as jsonfile:
        #         json.dump(curr, jsonfile)
        
        print(self.curr['idToken'])
        print('OOh ma gaa')

        print(str(self.last_sold) + " " + "init last sold")
        
        if self.curr['email'] != '':
            if self.curr["sold"][self.curr['email']] > self.last_sold:
                print("Initializing")
                self.testichiro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                # self.testiroro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                self.last_sold = self.curr["sold"][self.curr['email']]
                print("After last sold")

                if self.testichiro.each():
                    print("Inside testichiro")
                    for q in self.testichiro.each():
                        self.dude = q.val()['prop_keys']
                        print(self.loader)
                        # if not self.event.is_set():
                        if self.dude not in self.loader:
                            self.yours = db.child("Sale").order_by_key().equal_to(self.dude).get()
                            self.ours = db.child("Rent").order_by_key().equal_to(self.dude).get()
                            self.next_after(self.yours, self.ours)
                        else:
                            print("Already loaded booom in sale")
                        
                else:
                    print("Not testichiro .each")
            else:
                print("self.curr is greater than last_sold")
        else:
            print("No one signed in")
        print("Self.switch true products")
        
                # if self.testiroro.each():
            
                #     for d in self.testiroro.each():    
                #         self.bruv = d.val()['prop_keys']
                #         if self.bruv not in self.loader:
                #             self.ours = db.child("Rent").order_by_key().equal_to(self.bruv).get()
                #             self.next_after(self.ours)
                #         else:
                #             print("Already loaded booom")
                #             print(self.loader)
        # Animation(opacity=0, duration = 0.5).start(self.loading)
        
        
    

    @mainthread
    def next_after(self, yours, ours):
        print("Hey")
        
        if yours:
            for u in yours:
                        # another = person.val()
                        
            
            
            
                
                print('Okay maybe it wokred')
                self.card = PropertySaleCards()
                self.card.image = u.val()['url']
                self.card.amenities = u.val()['amenities']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.views = u.val()['views']
                self.card.local_image = u.val()['local_image']
                
                self.products.ids.layout.add_widget(self.card)
                print(self.loader)
                self.loader.append(u.key())
            
            # print("added")
            # print(self.loader)
            
    
                    
                        # print(self.loader)
                

        if ours:
            for u in ours:
                
                print(u.key())
                
                
                
                
                print(u.val()['url'])
                
                    
                print('Okay maybe it wokred')
                self.card = PropertyRentCards()
                self.card.image = u.val()['url']
                self.card.amenities = u.val()['amenities']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.views = u.val()['views']
                self.card.local_image = u.val()['local_image']
                
                self.products.ids.layout.add_widget(self.card)
                
                self.loader.append(u.key())
                # print("added")
                print(self.loader)
                print(self.counter)

        
    @mainthread
    def true_switch_bookmarks(self):
        self.wm.transition=NoTransition()
        self.wm.switch_to(self.bk)


    def begin_thread_bookmarks(self):
        self.event = Event()
        self.thread_bookmarks = threading.Thread(target=self.begin_bookmarks)
        self.thread_bookmarks.start()


    def begin_bookmarks(self):
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            try:
                print("Starto")
                func_timeout(30, self.starto_bookmarks)
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
                
        
            except:
                self.toast("Network Error")
                print("Network Error")
                self.event.set()

            time.sleep(1)
            self.true_switch_bookmarks()

    def starto_bookmarks(self):
        # with open(f'{path}/user.json', 'r') as jsonfile:
        #     self.curr = json.load(jsonfile)
        # self.last_rec = len(self.curr['bookmarks'][self.curr['email']])
        # print(self.last_rec)
        # print('OOh ma gaa')
        if self.curr['email'] != '':
            if len(self.curr['bookmarks'][self.curr['email']]) > 0:

                # print(self.curr['bookmarks'][self.curr['email']])
                for i in self.curr['bookmarks'][self.curr['email']]:
                    if not self.event.is_set():
                        if i not in self.loaded:
                            print("checking")
                            
                            self.yours = db.child("Sale").order_by_key().equal_to(i).get()
                            self.mine = db.child("Rent").order_by_key().equal_to(i).get()
                            self.starti_bookmarks(self.yours, self.mine)  
                    else:
                        print("Event has been set")
                        break
                    

                print(self.loaded)

                

            
        
    @mainthread
    def starti_bookmarks(self, yours, mine):
        
            
        if yours:
            for u in yours:
                # something = u.key()
                # print(u.key())
                # another = person.val()
                
            
                # if u.key() not in self.loaded:
                #     if something not in self.loaded:
                # print('Okay maybe it wokred')
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.amenities = u.val()['amenities']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.bk.ids.bk.add_widget(self.card)
                self.loaded.append(u.key())
                print("added")
                print(self.loaded)
                            
                    
            print("DOne withe sale")
            
                
            
    
        if mine:   
            for u in mine:
                # something = u.key()
                # print(u.key())
                # another = person.val()
                
            
                # if u.key() not in self.loaded:
                #     if something not in self.loaded:
                # print('Okay maybe it wokred')
                self.card = HomeCards()
                self.card.image = u.val()['url']
                self.card.amenities = u.val()['amenities']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.province = u.val()['state']
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.phonenumber = u.val()['phonenumber']
                self.card.twitter = u.val()['twitter']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.bk.ids.bk.add_widget(self.card)
                self.loaded.append(u.key())
                print("added")
                print(self.loaded)

        self.counter += 1
        print(self.counter)
        print(self.loaded)
        if self.counter == len(self.curr['bookmarks'][self.curr['email']]):
            print("counted")
            for b in self.curr['bookmarks'][self.curr['email']]:
                if b not in self.loaded:
                    print(b)
                    print("Was not found")
                    self.curr['bookmarks'][self.curr['email']].remove(b)
                    self.toast("Some Properties may have been sold.")

            with open(f'{path}/user.json', 'w') as jsonfile:
                json.dump(self.curr, jsonfile)  
            self.counter = 0

        
    def reload_bookmarks(self):
        self.loading.ids.spin.active = True
        self.wm.switch_to(self.loading)
        # self.loader.remove(key)
        
        self.loaded.clear()
        # self.last_sold = 0
        
        self.bk.ids.bk.clear_widgets()
        self.begin_thread_bookmarks()
        



    def thread_initialize_contact_message(self):
        self.contact.ids.send.opacity = 0
        self.contact.ids.spin.active = True
        self.contact.ids.send_card.disabled = True
        
        self.event=Event()
        self.thread_message = threading.Thread(target=self.initialize_contact_message)
        self.thread_message.start()


    def initialize_contact_message(self):
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            if self.curr["email"] != '':
                
                if len(self.contact.ids.firstname.text) >= 2 and len(self.contact.ids.firstname.text) < 16:
                    if len(self.contact.ids.lastname.text) >= 2 and len(self.contact.ids.lastname.text) < 16:
                        if self.contact.ids.mail.text == self.curr["email"]:
                            if len(self.contact.ids.message.text) > 0:
                                try:
                                    func_timeout(16, self.send_contact_message)
                                except FunctionTimedOut:
                                    print("Network Error")
                                    self.toast("Failed to send message timedout")
                                    self.event.set()
                                except:
                                    print("Network Error")
                                    self.toast("Failed to send message")
                                    self.event.set()

                            else:
                                text = "Please input a message"
                                self.show_dialog(text)
                                self.event.set()
                                
                        else:
                            text = "Email mismatch"
                            self.show_dialog(text)
                            self.event.set()
                            
                    else:
                        text = "Lastname must be between 2 and 16 characters"
                        self.show_dialog(text)
                        self.event.set()
                        
                else:
                    text = "Firstname must be between 2 and 16 characters"
                    self.show_dialog(text)
                    self.event.set()
            else:
                self.show_dialog("You're not signed in")
                self.event.set()
        
        self.opacity_spin_false()
        
    @mainthread
    def opacity_spin_false(self):
        self.contact.ids.send_card.disabled = False
        self.contact.ids.spin.active = False
        self.contact.ids.send.opacity = 1
        
    
    def send_contact_message(self):
        
        message = MIMEText(self.contact.ids.mail.text + '\nSender:' + f'\n{self.contact.ids.firstname.text}' + " " + f'{self.contact.ids.lastname.text}')
        message['Subject'] = "Contact Us Hometernet Notice"
        message["From"] = self.contact.ids.mail.text
        message["To"] = "anangjosh8@gmail.com"
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
        server.sendmail(self.contact.ids.mail.text, "anangjosh8@gmail.com", message.as_string())
        server.quit()
        # self.doa.dismiss()
        print("server exited")
        
        text = "Message sent successfully"
        self.snackbar(text)
                        





    def search_thread(self, choice, country, state, city, bedrooms):
        self.new_country = ''
        self.new_choice = ''
        self.new_bedrooms = '1'
        self.search_j = 0
        self.last = ''
        self.search_something = ''
        self.old_country = ''
        self.new_state = ''
        self.new_city = ''
        self.search_counter = 0
        self.search_begin = None
        
        print(self.has_error)
        if self.has_error:
            self.search.ids.relative.remove_widget(self.err)
            self.search.ids.relative.remove_widget(self.ico_err)
            self.has_error = False
            print("Has removed error")
        self.search.ids.spin.active = True
        self.search.ids.more_card.disabled = True
        self.search.ids.more_card.opacity = 0
        
        print("Beginning the search..")
        self.event = Event()
        self.thread_search = threading.Thread(target=self.search_it, args=(choice, country, state, city, bedrooms,))
        self.thread_search.start()




    @mainthread
    def search_error(self, text, icon="cancel"):
        self.err = MDLabel()
        self.err.text=text
        self.err.font_size="16dp"
        self.err.halign="center"
        self.err.size_hint_y=None
        self.err.adaptive_height=True
        self.err.pos_hint = {'center_y':0.5}
        self.err.color="gray"
        self.search.ids.relative.add_widget(self.err)
           
        self.ico_err = MDIcon()
        self.ico_err.icon=icon
        self.ico_err.font_size="60dp"
        self.ico_err.size_hint=[None, None]
        self.ico_err.adaptive_size=True
        self.ico_err.pos_hint = {'center_y':0.6, 'center_x': 0.5}
        self.ico_err.color="gray"
        self.search.ids.relative.add_widget(self.ico_err)
        self.has_error = True
        print(self.has_error)

    def search_it(self, choice, country, state, city, bedrooms):
        if not self.event.is_set():
            try:
                func_timeout(70, self.search_now, args=(choice, country.title(), state.title(), city.title(), bedrooms,))
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                # self.toast("Internet connection limited or unavailable")
                self.event.set()
                self.search_error("Failed")
                
            except:
                print("Network Error")
                # self.toast("Network Error")
                self.search_error("Failed")
                self.event.set()
        self.search.ids.spin.active = False

    @mainthread
    def clear_search(self):
        self.search.ids.search.clear_widgets()

    def search_now(self, choice, country, state, city, bedrooms):
        
        print(choice)
        # self.old_country = country
        self.old_country = country
        self.old_choice = choice
        self.old_bedrooms = bedrooms
        self.old_state = state
        self.old_city = city
        if country != self.new_country or choice != self.new_choice or bedrooms != self.new_bedrooms:
            print('is not equal')
            self.new_country = country
            self.new_choice = choice
            self.new_bedrooms = bedrooms
            self.old_country = self.new_country
            self.something = ''
            
            self.clear_search()
        else:
            print('is equal')

        self.search_j = 0

        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
        
        
        self.clear_search()
        print(state, city)
        print(country+"Is the freak'n freak'n freaking country mannn yeeeaaaaahhhh")
        if state == '' and city == '':
            self.search_counter = 0
            self.search_begin = db.child(choice).order_by_child('country').equal_to(country).get()
            time.sleep(1)
            if not self.event.is_set():

                self.search_added(country, state, city, bedrooms)
                print(self.search_begin.each()[0:])
            
                print("This one")
            else:
                print("Tried to continue search")
        elif state != '' and city != '':
            print(country+state+city)
            self.search_counter = 0
            self.search_begin = db.child(choice).order_by_child('location').equal_to(country+state+city).get()
            print(self.search_begin.each()[0:])
            time.sleep(1)
            if not self.event.is_set():
                self.search_added(country, state, city, bedrooms)
                print("That one")
            else:
                print("Tried to continue search")
            
        
            # self.added(country, state, city, bedrooms)
        elif state == '' and city != '':
            print('Must input state')
            self.snackbar('Please enter a state')

        elif city == '' and state != '':
            print('Must input city')
            self.snackbar('Please enter a city')
        
        
        

        # self.begin = db.child(choice).child(self.begin.key()).order_by_child('bedrooms').equal_to(bedrooms).get()
        
        # if state != '':
        #     self.begin = self.begin.order_by_child('state').equal_to(state).get()
        #     self.added(country, state, city, bedrooms)
        # else:
        #     self.added(country, state, city, bedrooms)

    
        

    @mainthread
    def search_added(self, country, state, city, bedrooms):
        
    
        if self.search_begin.each():
            for u in self.search_begin.each():
                print(u.key())
                self.search_counter += 1
                
                
                if self.search_something == u.key():
                    continue
                
                # if u.val()['state'] == state:
                #     if u.val()['town'] == city:
                if u.val()['bedrooms'] == bedrooms:
                
                    self.card = HomeCards()
                    self.card.image = u.val()['url']
                
                    self.card.tot = u.val()['housetype']
                    self.card.country = u.val()['country']
                    self.card.province = u.val()['state']
                    self.card.town = u.val()['town']
                    self.card.street = u.val()['street']
                    self.card.bedrooms = u.val()['bedrooms']
                    self.card.bathrooms = u.val()['bathrooms']
                    self.card.landspace = u.val()['landspace']
                    self.card.email = u.val()['email']
                    self.card.price = u.val()['price']
                    self.card.key = u.key()
                    self.card.phonenumber = u.val()['phonenumber']
                    self.card.twitter = u.val()['twitter']
                    self.card.facebook = u.val()['facebook']
                    self.card.description = u.val()['description']
                    self.card.amenities = u.val()['amenities']
                    self.search.ids.search.add_widget(self.card)
                    self.last = u.key()
                    self.search_something = u.key()
                    self.search_j += 1 
                    
                    break

            if self.search_j == 0:
                print("No found for number of bedrooms")
                self.snackbar("Not found for number of bedrooms")
                self.search.ids.spin.active = False
            else:
                self.search.ids.more_card.disabled = False
                self.search.ids.more_card.opacity = 1
                self.search.ids.spin.active = False
        else:
            # self.snackbar("Not found")
            print("none")
            self.search.ids.spin.active = False
            self.search_error("Nothing found", icon="cloud")
        

    def next_thread(self, bedrooms):
        self.search.ids.spin.active = True
        self.search.ids.more_card.disabled = False
        self.event = Event()
        self.thread_next = threading.Thread(target=self.next, args=(bedrooms,))
        self.thread_next.start()

    def next(self, bedrooms):
        print("This is self.counter" +  " " + str(self.search_counter))
        if not self.event.is_set():
            try:
                func_timeout(30, self.next_next, args=(bedrooms,))
            except FunctionTimedOut:
                print("Internet connection limited or unavailable")
                self.toast("Internet connection limited or unavailable")
                self.event.set()
                # snack = "No internet conection"
                # snacky = Snackbar(text=snack, snackbar_x="15dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y=None)
                # snacky.open()
            except:
                print("Network Error")
                self.toast("Network Error")
                self.event.set()
        self.search.ids.more_card.disabled = False
        self.search.ids.spin.active = False

    def next_next(self, bedrooms):
        
        # print("This is self.j" + " " + str(self.j))
        # print(str(len(self.begin.each())) + "is the length of the availabel countries")
        print(self.search_counter)
        if self.search_begin:
            if self.search_counter < len(self.search_begin.each()):
                if self.search_j / 10 == 1:
                    self.clear_search()
        else:
            print('self.begin is empty')
            
        if self.search_something != '':
            # self.again = db.child(self.old_choice).order_by_child('country').start_at(self.old_country).order_by_key().start_at(self.something).get()
            self.real_next(bedrooms)
            self.search.ids.spin.active = False
            
        

    @mainthread
    def real_next(self, bedrooms):
        
        
        if self.search_begin.each():
            for u in self.search_begin.each()[self.search_counter:]:
                # print('lala')
                if u.key() == self.search_something:
                    continue
                
                # if u.val()['country'] == self.old_country:
                #     if u.val()['state'] == self.old_state:
                #         if u.val()['town'] == self.old_city:
                self.search_counter += 1
                print(u.key())
                if u.val()['bedrooms'] == self.old_bedrooms:
                    self.card = HomeCards()
                    self.card.image = u.val()['url']
                    self.card.tot = u.val()['housetype']
                    self.card.country = u.val()['country']
                    self.card.province = u.val()['state']
                    self.card.town = u.val()['town']
                    self.card.street = u.val()['street']
                    self.card.bedrooms = u.val()['bedrooms']
                    self.card.bathrooms = u.val()['bathrooms']
                    self.card.landspace = u.val()['landspace']
                    self.card.email = u.val()['email']
                    self.card.price = u.val()['price']
                    self.card.key = u.key()
                    self.card.phonenumber = u.val()['phonenumber']
                    self.card.twitter = u.val()['twitter']
                    self.card.facebook = u.val()['facebook']
                    self.card.description = u.val()['description']
                    self.card.amenities = u.val()['amenities']
                    self.search.ids.search.add_widget(self.card)
                    self.last = u.key()
                    self.something = u.key()
                    self.search_j += 1
                    print(self.search_j)
                    if self.search_j / 5 == 1:
                        
                        break

            














    def on_start(self):
        

        print("Starting")

        return super().on_start()

    def say_hey(self):
        print("Say hey")

    def splash(self):
        try:
            func_timeout(10, self.start_up)
        except FunctionTimedOut:
            print("Failed to sign in timedout")
            toast("Failed to sign in timedout")
        except:
            print("Failed to sign in")
            print("Pass")
            self.toast("Failed to sign in")
        print("Starting")

    def start_up(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
            
        if self.curr['first_time'] == "false":
            # self.switch_loading()
            self.switch_home()
            if self.curr['email'] == "":
                print("Fase")
                
            else:
                # try:
                print("bruuhhh")
                self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                usero = authi.refresh(self.user['refreshToken'])
                print(self.user)
                self.curr['idToken'] = self.user['idToken']

                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                # except:
                #     print("Pass")
                #     self.toast("Failed to sign in")
        else:
            self.switch_signin()

    def hook_keyboard(self, window, key, *largs):
           
        if key == 27:
            print(self.wm.current)
            if self.wm.current == "products":
                self.switch_home()

            elif self.wm.current == "details":
                if self.current_screen == "bookmarks":
                    self.switch_bookmarks()
                if self.current_screen == "search":
                    self.switch_search()
                if self.current_screen == "home":
                    self.switch_home()
                    
            elif self.wm.current == "bookmarks":
                self.switch_home() 
            elif self.wm.current == "sale" or self.wm.current == "rent":
                self.discard_auth()
            elif self.wm.current == "edit" or self.wm.current == 'edit-rent':
                print("oh dude")
                self.switch_products()
            elif self.wm.current == "signin":
                self.switch_from_signin()
                
                
                
                    
            elif self.wm.current == "sign-up":
                self.discard_mail()
                self.switch_signin()

            elif self.wm.current == "SaleOrRent":
                self.switch_products()
                
                
            elif self.wm.current == "search":
                print('What is wrong withn oyu')
                self.switch_home()
            elif self.wm.current == 'acc':
                self.switch_home()
            elif self.wm.current == "creator":
                self.switch_home()
            elif self.wm.current == "tutor":
                self.switch_home()
            elif self.wm.current == "about":
                self.switch_home()
            elif self.wm.current == "contact":
                self.switch_home()
            elif self.wm.current == "congrats":
                self.switch_products()
            elif self.wm.current == "code":
                self.switch_signup()
            # elif self.wm.current == "loading":
                # Event.set()
                # self.switch_home()
                # func_set_timeout(0, allowOverride=True)
                
                
               
            
    def bedrooms_choice(self):
        bedrooms_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "1",
                
                "on_release": lambda x='1': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "2",
                
                "on_release": lambda x='2': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "3",
                
                "on_release": lambda x='3': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "4",
                
                "on_release": lambda x='4': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "5",
                
                "on_release": lambda x='5': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "6",
                
                "on_release": lambda x='6': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "7",
                
                "on_release": lambda x='7': self.set_bed(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "7+",
                
                "on_release": lambda x='7+': self.set_bed(x)
            },
        ]

        self.bed_choice = MDDropdownMenu(
            caller=self.search.ids.bed_item,
            ver_growth='down',
            
            width_mult=3
        )

        for i in bedrooms_items:
            self.bed_choice.items.append(i)

        self.bed_choice.open()

    def discard_auth(self):
        self.dia = MDDialog(
            
            text='Are you sure you want to discard changes made?',
            buttons=[
                MDFlatButton(
                    text='Cancel',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.dia.dismiss()
                ),
                MDFlatButton(
                    text='Discard',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.discard(),
                    on_release=lambda y:self.switch_products(),
                     
                )
            ]
        )
        self.dia.open()

    def discard(self):
        self.tot = ''
        self.country = ''
        self.state = ''
        self.town = ''
        self.street = ''
        self.bedrooms = ''
        self.bathrooms = ''
        self.landspace = ''
        self.price = ''
        self.phonenumber = ''
        self.desc = ''
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        self.twitter = ''
        self.facebook = ''
        # self.dia.dismiss()
    
    def discard_mail(self):
        self.passwrd = ''
        self.mail = ''

    def set_item(self, text_item):
        self.search.ids.drop_item.set_item(text_item)
        
        self.search.ids.drop_item.text = text_item
    
    def set_bed(self, text_item):
        self.search.ids.bed_item.set_item(text_item)

        self.search.ids.bed_item.text = text_item
        
        # self.choice.dismiss()
    @mainthread
    def toast(self, info):
        toast(info)
    
    def callback_for_menu_items(self, *args):
        self.toast(args[0])

    def call_back(self, text_of_option):
        print(text_of_option)
    
    def on_checkbox_active(self, checkbox, value, num):
        # self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        if value:
            print(checkbox.ids)
            print(num)
            self.amenities[num] = 'Yes'
            print(self.amenities)
        else:
            self.amenities[num] = 'No'
            print(checkbox.state)
            print(self.amenities)


    def call(self, obg, icon):
        if icon == 'whatsapp':
            webbrowser.open('https://wa.me/' + obg)
        elif icon == 'email':
            print(obg + " " + 'is an email address')
            webbrowser.open('https://mail.google.com/mail/?view=cm&fs=1&to=' + obg + '&su=SUBJECT&body=BODY')

        elif icon == 'twitter':
            print(obg + " " + 'is a twitter handle')
            
            
            webbrowser.open('https://twitter.com/' + obg)
        elif icon == 'facebook':
            print(obg + " " + 'is a facebook handle')
           
            webbrowser.open('https://m.me/' + obg)

    

    @mainthread
    def show_bottom(self, email, phonenumber, twitter, facebook):
        bottom_sheet_menu = MDListBottomSheet()

        
        datop = {
            email: "email",
            phonenumber: "whatsapp",
            
        }
        if facebook != "":
            datop[facebook] = "facebook"

        if twitter != "":
            datop[twitter] = "twitter"

        print(len(datop))
        for item in datop.items():
            print(len(datop.items()))
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0], z=item[1]: self.call(y, z),
                icon = item[1],
                
            )
        
        
        bottom_sheet_menu.open()

    
    
    

    @mainthread
    def switch_home(self, direction='left'):
        self.wm.transition=SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.home, direction=direction)
        self.current_screen = 'home'
        self.sign_in_current = 'home'
        self.home.text = self.curr['email']
        

    @mainthread
    def switch_loading(self):
        # self.loading.ids.spin.active=True
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .2
        self.wm.switch_to(self.loading, direction='right')
        
    def switch_acc(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.account, direction='right')
        
        self.passwrd = ''
        self.mail = ''
        self.sign_in_current = 'acc'
        self.account.text = self.curr['email']
        

    def switch_creator(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.creator_screen, direction='right')

    def switch_contact(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.contact.ids.mail.text = ''
        
        self.contact.ids.firstname.text = ''
        self.contact.ids.lastname.text = ''
        self.contact.ids.message.text = ''

        self.wm.switch_to(self.contact, direction='right')

    def switch_tutorial(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.tutorial, direction='right')

    def switch_about(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.about, direction='right')

            
        

    
    def switch_from_details(self):
        if self.current_screen == "bookmarks":
            self.switch_bookmarks()
        if self.current_screen == "search":
            self.switch_search()
        if self.current_screen == "home":
            self.switch_home()            
        

    @mainthread
    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, phonenumber=None, twitter=None, facebook=None, description=None, key=None, amenities=None):
        self.wm.transition = CardTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.detail, direction='up')
        # self.switch_loading()
        self.sign_in_current = 'details'
        print(image)
        
        self.detail.image = image
        self.detail.type = House_type
        self.detail.price = pricing
        self.detail.country = locate
        self.detail.province = state
        self.detail.town = town
        self.detail.street = street
        self.detail.bedrooms = bedrooms
        self.detail.bathrooms = bathrooms
        self.detail.landspace = landspace
        self.detail.email = email
        self.detail.phonenumber = phonenumber
        self.detail.twitter = twitter
        self.detail.facebook = facebook
        self.detail.description = description
        self.detail.key = key
        self.detail.amenities = amenities
        print(self.detail.amenities)
        
        
        

    def switch_search(self, direction='down'):
        self.wm.transition = CardTransition()
        self.wm.transition.duration = .1
        
        self.wm.switch_to(self.search, direction=direction)
        self.current_screen = 'search'
        

    def switch_sale(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
        print(self.amenities)
        self.denied = 0
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        self.sale = SaleSubmit(name="sale")
        self.wm.switch_to(self.sale)

    def switch_rent(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
        print(self.amenities)
        self.denied = 0
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        self.rent = RentSubmit(name="rent")
        self.wm.switch_to(self.rent)

    @mainthread
    def switch_signup(self):
        self.passwrd = ''
        self.mail = ''
        self.signup.ids.email.text = ''
        self.signup.ids.password.text = ''
        self.signup.ids.confirm.text = ''
        self.wm.switch_to(self.signup)

    
        
        
        #     if self.products.ids.layout.done:
        #         self.products.ids.spinner.active=False
        #     if self.products.ids.layout.done is False:
        
            
        # self.products.ids.spinner.active=False
        # self.beg = PropertyCardsLayout()
        # self.beg.begin_loading()

        

    def switch_bookmarks(self):
        self.current_screen = 'bookmarks'    
        self.loading.ids.spin.active = True
        self.switch_loading()
        self.passwrd = ''
        self.mail = ''
        
        
        self.begin_thread_bookmarks()    
        

    @mainthread
    def switch_signin(self):
        print(self.wm.current)
        self.passwrd = ''
        self.mail = ''
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        if self.curr['email'] != "":
            # p="You're already signed in"
            # self.snackbar(p)
            pass
        else:
            
            # self.signin = SignInScreen(name="signin")
            self.signin.ids.email.text = ''
            self.signin.ids.password.text = ''
            self.wm.switch_to(self.signin)
            print(self.wm.current)

    @mainthread
    def switch_from_signin(self):
        self.passwrd = ''
        self.mail = ''
        if self.sign_in_current == "acc":
            self.switch_acc()
        if self.sign_in_current == "products":
            self.switch_products()
        if self.sign_in_current == "home":
            self.switch_home()
        if self.sign_in_current == "details":
            self.switch_home()

    @mainthread
    def switch_congrats(self):
        self.wm.switch_to(self.congrats)
    
    @mainthread
    def switch_code_verifyer(self):
        self.wm.switch_to(self.code_verifyer)
    
    def switch_saleorrent(self):
        
        
        
        self.mail = ''
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        
        if data['email'] == "":
            print(self.wm.current)
            self.switch_signin()
        else:
            self.wm.transition = SlideTransition()
            self.wm.switch_to(self.SaleOrRent, direction="left")
        
    def call_guy(self, lockwood, price):
        # self.loading.ids.spin.active=True
        # self.switch_loading()
        self.event = Event()
        self.thread_guy = threading.Thread(target=self.call_other_guy, args=(lockwood, price,))
        self.thread_guy.start()


    def call_other_guy(self, lockwood, price):
        print('WHy nigga why')
        print(lockwood)
        
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            try:
                func_timeout(15, self.boooiiii, args=(lockwood, price,))
            except FunctionTimedOut:
                print('No internet connection timedout')
                self.toast('No internet connection timedout')
                self.event.set()
            except:
                self.toast('Failed to update views')
                self.event.set()
        # self.loading.ids.spin.active=False
        
        

    def play(self):
        sound.play()
        

    def boooiiii(self, figaro,price):
        print(price)
        if self.curr['email'] != '':
            if figaro in self.curr["viewed"][self.curr["email"]]:
                print("Viewed")
            else:
                x = re.search(r"/mth$", price)
                y = re.search(r"/yr$", price)
                if x or y:
                    
                    try:
                        print('Trying rent')
                        them14 = db.child("Rent").child(figaro).child("views").get()
                        new_val = them14.val()
                        new_val += 1
                        print(new_val)
                        db.child("Rent").child(figaro).update({'views': new_val}, self.curr['idToken'])
                        self.curr["viewed"][self.curr["email"]].append(figaro)
                    except requests.exceptions.HTTPError as e:
                        error_json = e.args[1]
                        error = json.loads(error_json)['error']
                        print(str(error) + "is the error")
                        if error == 'Permission denied':
                            print("Permission denied")
                            print("Resigning in rent")
                            
                            try:
                                func_timeout(10, self.denied_signin)
                                self.call_guy(figaro,price)
                            except FunctionTimedOut:
                                self.toast("Internet conneciton limit or unavailable")
                            except:
                                self.toast("Network Error")
                                print("Network Error")
                        try:
                            if error['message'] == 'Permission denied.':
                                pass
                        except:
                            pass

                    
                else:
                    try:
                        them14 = db.child("Sale").child(figaro).child("views").get()
                        new_val = them14.val()
                        new_val += 1
                        print(new_val)
                        db.child("Sale").child(figaro).update({'views': new_val}, self.curr['idToken'])
                        self.curr["viewed"][self.curr["email"]].append(figaro)
                        print('updated views')

                    except requests.exceptions.HTTPError as e:
                        error_json = e.args[1]
                        error = json.loads(error_json)['error']
                        print(str(error) + "is the error")
                        if error == 'Permission denied':
                            print("Permission denied")
                            print("Resigning in")
                            
                            try:
                                self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                                usero = authi.refresh(self.user['refreshToken'])
                                self.curr['idToken'] = self.user['idToken']
                                with open(f'{path}/user.json', 'w') as jsonfile:
                                    json.dump(self.curr, jsonfile)
                                print('dumped')
                                self.call_guy(figaro,price)
                            except:
                                self.toast("Network Error")
                                print("Network Error")
                    
                    #
                    # try:
                
                    
                        # except:
                        #     print('Update views failed')
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
        else:
            print("No user in")

    def email(self, texta):
        self.mail = texta
        print(texta)
        

    def phone(self, texta):
        self.phonenumber = texta

    def tg(self, texta):
        self.twitter = texta

    def fb(self, texta):
        self.facebook = texta

    def password(self, texta):
        print(texta)
        self.passwrd = texta
       
    def confirmed_password(self, texta):
        self.confirmed = texta

    def signin_mail(self, texta):
        self.sign_in_mail = texta

    def signin_pass(self, texta):
        self.sign_in_pass = texta

    def word(self, texta):
        self.tot = texta
        

    def locate(self, texta):
        flag = pycountry.countries.get(name='Netherlands')
        print(flag.flag)
        self.sale.ids.flag.source = flag.flag
        self.country = texta
        print(self.country)

    def display(self, texta):
        print(texta)
        print(self.screeni[0])
        if self.screeni[0] == "Sale":
            self.sale.ids.country_text.text = texta
            self.country = texta
            print(self.country)
        elif self.screeni[0] == "Rent":
            self.rent.ids.country_text.text = texta
            self.country = texta
            print(self.country)
        elif self.screeni[0] == "EditSale":
            self.edit.ids.country_text.text = texta
            self.country = texta
        elif self.screeni[0] == "EditRent":
            self.edit_rent.ids.country_text.text = texta
            self.country = texta

    def statify(self, texta):
        self.state = texta

    

    def towni(self, texta):
        self.town = texta

    def streeti(self, texta):
        self.street = texta

    def land_space(self, texta):
        self.landspace = texta

    def pricing(self, texta):
        self.price = texta

    def rooms(self, texta):
        self.bedrooms = texta
        print(texta)

    def baths(self, texta):
        self.bathrooms = texta 

    def description(self, texta):
        self.desc = texta

    
    
    @mainthread
    def show_dialog(self, notice, button=None, titler="Notice"):
        self.dialog = MDDialog(title=titler, text=notice, size_hint=(1, 1), buttons=[MDFlatButton(text="close", on_release=self.close_dialog), button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    @mainthread
    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="5dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y=None)
        self.snack.open()

    def open_maps(self, location):
        webbrowser.open('https://www.google.com/maps/place/' + location)


    # def change_screen(self, screen, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None):
    #     self.detail = DetailsScreen()
    #     try:
    #         if screen == "detail":
    #             self.wm.switch_to(self.detail)
    #             self.detail.image = image
    #             self.detail.type = House_type
    #             self.detail.price = pricing
    #             self.detail.country = locate
    #             self.detail.town = town
    #             self.detail.street = street
    #             self.detail.bedrooms = bedrooms
    #             self.detail.bathrooms = bathrooms
    #             self.detail.landspace = landspace
    #             self.detail.email = email

    #         elif screen == "Home":
    #             self.wm.switch_to(self.home)
    #         elif screen == "Login":
    #             self.wm.switch_to(self.login)
    #         elif screen == "rent":
    #             self.wm.switch_to(self.rent)
    #         elif screen == "sign-up":
    #             self.wm.switch_to(self.signup)
    #         elif screen == "products":
    #             self.wm.switch_to(self.products)
    #         elif screen == "bookmarks":
    #             self.wm.switch_to(self.bk)
            
    #         elif screen == "sign-in":
                
                

    #             self.wm.switch_to(self.signin)

    #             # else:
    #             #     self.user = authi.sign_in_with_email_and_password(data['email'], data['password'])
    #             #     self.wm.switch_to(self.login)
    #                 # self.wm.switch_to(self.SaleOrRent)

            
    #         elif screen == "SaleOrRent":
    #             if dati['email'] == "":
                    
    #                 self.wm.switch_to(self.signin)
    #             else:
    #                 self.user = authi.sign_in_with_email_and_password(data['email'], data['password'])
    #                 self.wm.switch_to(self.SaleOrRent)
            
    #     except:
    #         pass
    
    def show_terms(self):
        self.dia = MDDialog(
            # title='Warning!',
            type='custom',
            content_cls=Warning(),
            size_hint=[None, None],
            width= Window.size[0] / 1.5,
            # height=Window.size[1]
            
            height='500dp',
            buttons=[
                
                MDRaisedButton(
                    text='Agree',
                    theme_text_color='Custom',
                    on_release= lambda x:self.dia.dismiss()
                )
            ]
        )
        self.dia.open()

    def send_thread_email(self, email, phonenumber, twitter, facebook):
        self.detail.ids.buy.opacity = 0
        self.detail.ids.spin.active=True
        self.detail.ids.biye.disabled = True
        self.event = Event()
        self.thread_email = threading.Thread(target=self.send_email, args=(email, phonenumber, twitter, facebook,))
        self.thread_email.start()

    @mainthread
    def detail_spin_false(self):
        self.detail.ids.spin.active=False
        self.detail.ids.buy.opacity = 1
        self.detail.ids.biye.disabled = False

    def send_email(self, email, phonenumber, twitter, facebook):
        if not self.event.is_set():
            try:
                func_timeout(10, self.send_email_now, args=(email, phonenumber, twitter, facebook,))
            except FunctionTimedOut:
                self.toast("Network Error")
                self.event.set()
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                print(str(error) + "is the error")
                try:
                    if error['message'] == 'INVALID_ID_TOKEN':
                        try:
                            func_timeout(10, self.denied_signin)
                            self.send_thread_email(email, phonenumber, twitter, facebook)
                        except FunctionTimedOut:
                            self.toast("Network error")
                            self.event.set()
                        except:
                            self.toast("Network error")
                            self.event.set()
                    else:
                        self.toast("An unknown error occured")
                        self.event.set()
                except:
                    self.toast("An unknown error occured")
                    self.event.set()
            except:
                self.toast("An unknown error occured")
                self.event.set()
        self.detail_spin_false()    
            
    def send_email_now(self, email, phonenumber, twitter, facebook):
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        if data['email'] == "":
            self.switch_signin()
        else:
            
            ino = authi.get_account_info(data['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                # authi.send_email_verification(data['idToken'])
                self.show_dialog(titler='Your email has not been verified!', notice='Please re-sign in to get the verification link.')
                
                    
                      
            else:
                
                print('horray hooray')
                
                message = MIMEText("Someone just viewed your contact information")
                message['Subject'] = "Hometernet Offer Notice"
                message["From"] = "anangjosh8@gmail.com"
                message["To"] = email
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
                server.sendmail(data['email'], email, message.as_string())
                message = MIMEText("An offer has been made to buy property belonging to" + " " + email + " " + phonenumber)
                server.sendmail("anangjosh8@gmail.com", "anangjosh8@gmail.com", message.as_string())
                server.quit()
                
                self.show_bottom(email, phonenumber, twitter, facebook)

    
                
    def show_pre_listings(self):
        print("Did it work")
        self.doa = MDDialog(
            title='Loading',
            text="Please wait..."
            
        )
        self.doa.open()

    def show_listings(self, scr):
        print(self.screeni)
       

        self.screeni.clear()
        self.screeni.append(scr)
        self.dia = MDDialog(
            type='custom',
            content_cls=Countries(),
            size_hint=[None, None],
            width= Window.size[0] / 1.2,
            # height=Window.size[1]
            
            height='600dp',
            # buttons=[
            #     MDFlatButton(
            #         text='Cancel',
            #         theme_text_color='Custom',
            #         text_color='black',
            #         on_press=lambda x:self.dia.dismiss()
            #     ),
            #     MDFlatButton(
            #         text='Agree',
            #         theme_text_color='Custom',
            #         text_color='black',
            #         on_press= lambda x:self.dia.dismiss()
            #     )
            # ]
        )
        self.dia.open()
    
    # @mainthread
    def show_terms_create(self, email):
        mail = email
        password = self.signup.ids.password.text
        
        print(self.signup.ids.confirm.text)
        if len(mail) > 0:
            if len(password) >= 6:
                if self.signup.ids.confirm.text == password:
                    self.dia = MDDialog(
                        type='custom',
                        content_cls=Warning(),
                        title='Warning!',
                        size_hint=[None, None],
                        width= Window.size[0] / 1.5,
                        # height=Window.size[1]
                        
                        height='500dp',
                        buttons=[
                            MDFlatButton(
                                text='Cancel',
                                theme_text_color='Custom',
                                text_color='black',
                                on_press=lambda x:self.dia.dismiss()
                            ),
                            MDRaisedButton(
                                text='Agree',
                                theme_text_color='Custom',
                                # on_press=lambda x: self.switch_code_verifyer(),
                                on_press= lambda x:self.validate_behind(email),
                                on_release= lambda x:self.dia.dismiss()
                            )
                        ],
                        
                    )
                    self.dia.open()
                else:
                    text = "Password does not match"
                    
                    self.show_dialog(text)
            else:
                text = "Password should be at least 6 characters"
                
                self.show_dialog(text)
        else:
            text='Please enter an email in the space'
            self.show_dialog(text)
            

    def onTimeOut(self):
        self.kill = True

    def validate_mail(self, email):
        print(email)
        # self.switch_loading()
        # self.loading.ids.spin.active=True
        
        try:
            func_timeout(10, self.validator, args=(email,))
        except FunctionTimedOut:
            self.toast("Authentication failed timedout")
            print("Authentication failed timdeout")
            self.switch_signup()
            
        except:
            self.toast("Authentication failed")
            self.switch_signup() 
             


    # def stopit(self):
    #     self.event.set()
    #     print('set')
    #     self.kill = True
        

    def validate_behind(self, email):
        self.loading.ids.spin.active=True
        self.switch_loading()
        
        
        # executor = concurrent.futures.ThreadPoolExecutor()
        # f2 = executor.submit(self.validator(email))
        
        threading.Thread(target=self.validate_mail, args=(email,)).start()
        
        # self.validator(email)

    def validator(self, email):
        # print(self.counting)
        print("validating behind")
        
        # while self.kill is False:
            # if self.event.is_set():
            #     print("Broken")
                
            #     self.switch_signup()
            #     break
        print("Okay is false now what??")
        self.evaluating_email = email
        # 
        # try:
        self.validator_status = validate_email(email)
        # print('verifying')
        print(self.validator_status)
        if self.validator_status:
            
            self.resend_now()
        elif self.validator_status == False:
            text = "Invalid email"
                
            self.show_dialog(text)
            self.switch_signup()
            self.spin_false()
        else:
            self.switch_signup()
            self.toast('Authentication failed')
            self.spin_false()
        # except:
        #     self.toast("Authentication failed")
        #     self.switch_signup()
            
                 
                

            
        # self.kill = True
        # else:
        #     print('Timedout out')
        

    # def account_submit(self):
        
                # try:
                    
                
                # threading.Thread(target=self.validator, args=(email,)).start()
                

                
                    
        # self.resend_now()
                        
                
                
                # except:
                #     self.toast("Authentication failed")
            
            
    def resend_now(self):
        self.loading.ids.spin.active=True
        self.switch_loading()
        self.event = Event()
        self.thread_create = threading.Thread(target=self.resend_code)
        self.thread_create.start()

    def resend_code(self):
        print("Sending code")
        if not self.event.is_set():
            try:
                func_timeout(20, self.sending_code)
            except FunctionTimedOut:
                print('Authentication failed timedout')
                self.toast("Authentication failed timedout")
                self.switch_signup()
                self.event.set()
                self.spin_false()
            except:
                self.toast("Authentication failed")
                self.switch_signin()
                self.event.set()
                self.spin_false()

    def sending_code(self):
        self.secret_num = random.randint(100000,999999)
        print(self.secret_num)
        message = MIMEText(f"Your email login code is {self.secret_num}. \n Warning do not share this code with anyone.")
        message['Subject'] = "Your Hometernet login code is..."
        message["From"] = "anangjosh8@gmail.com"
        message["To"] = self.evaluating_email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
        server.sendmail("anangjosh8@gmail.com", self.evaluating_email, message.as_string())
        server.quit()
        self.switch_code_verifyer()
        self.spin_false()



    def create_account_init(self, typed_in):
        # self.loading.ids.spin.active = True
        # self.switch_loading()
        print(self.secret_num)
        print(self.code_verifyer.ids.verify_code.text)
        print(typed_in + "is the code i typed")
        num = self.secret_num
        ot = self.secret_num
        
        print(ot == num)
        if typed_in == "":
            print("Invalid code")
            self.snackbar("Invalid code")
        else:
            if int(self.secret_num) == int(typed_in):
                print("was equal")
                self.loading.ids.spin.active=True
                self.switch_loading()
                self.event = Event()
                self.thread_create = threading.Thread(target=self.create_account_now)
                self.thread_create.start()
            else:
                print("Invalid code")
                self.snackbar("Invalid code")
    
    @mainthread
    def spin_false(self):
        self.loading.ids.spin.active = False

    def create_account_now(self):
        # self.loading.ids.labe.opacity = 0
        # self.loading.ids.spinner.active= True
        if not self.event.is_set():
            try:
                func_timeout(15, self.create_account)
            except FunctionTimedOut:
                print('Authentication failed timedout')
                self.toast("Authentication failed timedout")
                self.switch_signup()
                self.event.set()
                self.spin_false()
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                print(str(error) + "is the error")
                # self.toast(str(error) + "is the error")
                # self.toast("An unknown error occured")
                self.event.set()
                try:
                    if error['message'] == 'EMAIL_EXISTS':
                        self.show_dialog('Email Exists')
                        
                except:
                    self.toast("An unknown error occured")
                self.switch_signup()
                self.spin_false()
            # except:
            #     print("Authentication failed")
            #     self.toast("Authentication failed")
            #     self.event.set()
            #     self.switch_signup()
                
            
            
        
        

    def create_account(self):
        email = self.signup.ids.email.text
        password = self.signup.ids.password.text
        count = 0
        user = authi.create_user_with_email_and_password(email, password)
        useri = authi.send_email_verification(user['idToken'])
        # self.sign_in()
        text = "An email verification link has been sent to your mail. If not found in your inbox, check in spam."
       
        self.show_dialog(text)
        
        
        if self.curr['first_time'] == "true":
            self.switch_tutorial()
            self.curr['first_time'] = "false"
        else:
            self.switch_home()

        self.curr['sold'][email] = count
        self.curr['bookmarks'][email] = []
        self.curr['viewed'][email] = []
        self.curr['accounts'].append({'email': email, 'password': password})

        self.curr['email'] = email
        self.curr['password'] = password
        self.curr['idToken'] = user['idToken']
        self.curr['localid'] = user['localId']

        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)
        self.spin_false()
        
        
        
    def delete_property_auth(self, key, local_image, sale_or_rent):
        print(key,local_image,sale_or_rent)
        self.passwrd = ''
        self.dia = MDDialog(
            title='Please Enter your password',
            type='custom',
            content_cls=DialogEntry(),
            buttons=[
                MDFlatButton(
                    text='Cancel',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.dia.dismiss()
                ),
                MDFlatButton(
                    text='Submit',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x=key, a=key, y=local_image, z=sale_or_rent: self.delete_dialog(a,y,z),
                    on_release=lambda x:self.dia.dismiss()
                )
            ]
        )
        self.dia.open()


    def delete_dialog(self, name, local_image, sale_or_rent):
        self.dialog_delete = MDDialog(text="Please wait...", title="Deleting Property", size_hint=(1,1), on_open=lambda x:self.delete_property_init(name, local_image, sale_or_rent))
        self.dialog_delete.open()

    @mainthread
    def close_delete_dialog(self):
        self.dialog_delete.dismiss()

    def delete_property_init(self, name, local_image, sale_or_rent):
        
        try:
            func_timeout(20, self.delete_property, args=(name, local_image, sale_or_rent,))
        except FunctionTimedOut:
            print('Internet connection limited or unavailable')
            self.toast('Internet connection limited or unavailable')
        except:
            print('An unknown error occured')
            self.toast('AN unknown error occured')
        
        self.close_delete_dialog()

    def delete_property(self, name, local_image, sale_or_rent):

        print(name,local_image,sale_or_rent)
        
        # self.entry = DialogEntry()
        print(self.passwrd + " " + 'ooooohhhhh ma gaaaaa')
        
        if self.curr['email'] and self.curr['password'] == "":
            p = 'No user signed in'
            self.snackbar(p)
        else:
            
            if self.passwrd == self.curr['password']:
                
                print(str(name) + " " + "This is the name of the porperty")
                # user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                try:
                    
                    
                    if sale_or_rent == 'Sale':
                        print("Is equal to sale")
                        print(name)
                        db.child("Sale").child(name).remove(self.curr['idToken'])
                        remove_people = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                        if remove_people.each():
                            for u in remove_people.each():
                                print(u.val()['prop_keys'])
                                
                                if str(u.val()['prop_keys']) == name:
                                    print(u.key())
                                    print("Is equal")
                                    db.child("People").child(self.curr['localid']).child("ids").child(u.key()).remove(self.curr['idToken'])
                                    
                                    break
                        else:
                            print("Not found")
                            self.toast("Not found")

                    else:
                        print("Is equal to rent")
                        db.child("Rent").child(name).remove(self.curr['idToken'])
                        remove_people = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                        if remove_people.each():
                            for u in remove_people.each():
                                
                                if u.val()['prop_keys'] == name:
                                    db.child("People").child(self.curr['localid']).child("ids").child(u.key()).remove(self.curr['idToken'])
                                    print("Found it" + " " + name)
                        else:
                            print("Not found")
                            self.toast("Not found")

                    deletion = self.curr['localid'] + '/' + local_image
                    storage.delete(deletion, self.curr['idToken'])
                    self.curr['sold'][self.curr['email']] -= 1

                    with open(f'{path}/user.json', 'w') as jsonfile:
                        json.dump(self.curr, jsonfile)

                    p = 'Property Successfully deleted'
                    self.snackbar(p)
                        
                    self.passwrd = ''
                    self.denied = 0
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']
                    print(str(error) + "is the error")
                    # self.toast(str(error))
                    # print(error['message'])
                    if error == 'Permission denied':
                        print("Permission denied")
                        print("Resigning in")
                        self.denied += 1
                        if self.denied < 2:
                            try:
                                func_timeout(20, self.denied_signin)
                                self.delete_property_init(name, local_image, sale_or_rent)
                                self.denied = 0
                                print("This is self.denied" + " " + str(self.denied))
                            except FunctionTimedOut:
                                self.toast("Internet connection limited or unavailable")
                                print("Internet connection limited or unavailable")
                                self.denied = 0
                            except:
                                self.toast("Failed to delete property")
                                print("Failed to delete property")
                                self.denied = 0

                        else:
                            
                            self.show_dialog("All permissions are denied for deleting properties right now. Please wait until the slots are open. Or you could request to delete your property on our contact page providing us with full details of the property.", titler="Permission denied")
                            self.denied = 0
                            print("Permission finally denied")
                    # if error['message']:
                    try:
                        if error['message'] == 'Not Found.':
                            self.toast("Not found")
                            print("Not found")
                    except:
                        pass
                        
                    #     if error['message'] == 'Permission denied.':
                    #         self.show_dialog("All permissions are denied for deleting properties right now. Please wait until the slots are open.")
                    #         # self.denied = 0
                    #         print("Permission finally denied")

                
                
            else:
                text = "Invalid password"
                self.show_dialog(text)
                self.passwrd = ''
        

    

    def forgot_password_auth(self):
        self.mail = ''
        # self.text_error()
        self.di = MDDialog(
            title='Please Enter your email',
            type='custom',
            content_cls=ForgotPasswordEntry(),
            buttons=[
                MDFlatButton(
                    text='Cancel',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.di.dismiss()
                ),
                MDRaisedButton(
                    text='Submit',
                    theme_text_color='Custom',
                    on_press=self.thread_forgot_password,
                    on_release=lambda x:self.di.dismiss()
                )
            ]
        )
        self.di.open()

    def thread_forgot_password(self, obj):
        self.event = Event()
        self.thread_forgot = threading.Thread(target=self.forgot_password)
        self.thread_forgot.start()

    def forgot_password(self):
        print(self.mail)
        
        if self.mail == '':
            text = "Please type in your email in the space"
            
            self.show_dialog(text)
        else:
            if not self.event.is_set():
                try:
                    func_timeout(10, self.actual_forgot_password)
                except FunctionTimedOut:
                    self.toast('Failed to send link Internet connection limited or unavailable')
                    self.event.set()
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']['message']
                    print(str(error) + "is the error")
                    if error == 'EMAIL_NOT_FOUND':
                        text = "Email not found"
                        
                        self.show_dialog(text)
                        print('Email not found')
                        # self.mail = ''
                    self.event.set()
                except:
                    self.toast("Failed to send link network error")
                    self.event.set()

    def actual_forgot_password(self):
        self.snackbar("Sending password reset link to your email")
        authi.send_password_reset_email(self.mail)

        text = "A password reset email has been sent to your mail"
        
        self.show_dialog(text)
        self.mail = ''

    

        
    
    def password_reset_auth(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        self.passwrd = ''
        if self.curr['email'] == '':
            self.show_dialog('No user signed in')
        else:
            self.di = MDDialog(
                title='Please Enter your current password',
                type='custom',
                content_cls=PasswordResetEntry(),
                buttons=[
                    MDFlatButton(
                        text='Cancel',
                        theme_text_color='Custom',
                        text_color='black',
                        on_press=lambda x:self.di.dismiss()
                    ),
                    MDRaisedButton(
                        text='Submit',
                        theme_text_color='Custom',
                        on_press=self.thread_password_reset,
                        on_release=lambda x:self.di.dismiss()
                    )
                ]
            )
            self.di.open()

    def thread_password_reset(self, obj):
        print('threading password reset')
        self.password_thread = threading.Thread(target = self.password_reset)
        self.password_thread.start()

    def password_reset(self):
        
        try:
            func_timeout(15, self.actual_password_reset)
        except FunctionTimedOut:
            self.toast('Network Error')
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            print(str(error) + "is the error")
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                
                self.show_dialog(text)
                print('Email not found')
                self.passwrd = ''
        except:
            self.toast("Network Error")
    
    def actual_password_reset(self):
        print(self.passwrd)
        self.snackbar("Sending password reset link to your email")
        if self.passwrd == self.curr['password']:
            authi.send_password_reset_email(self.curr['email'])
            text = "A password reset email has been sent to your mail"
            
            
            self.show_dialog(text)
            self.passwrd = ''
        else:
            self.show_dialog('Invalid password')
            print("Invalid password")
            self.passwrd = ''

# "MKHRXCSZPZWXKIIF"
# "GeoWorl38751759"

    def stopit(self):
        self.threader.join()
        print('Joined')

    def sign_in(self):
        self.loading.ids.spin.active = True
        self.switch_loading()
        self.event = Event()
        self.threader = threading.Thread(target=self.sign_in_boi)
        self.threader.start()
        print(self.threader.is_alive())
        print('has started')
        
        # 
        # self.close_dialog()

    def sign_in_boi(self):
        # self.switch_loading()
        if not self.event.is_set():
            print('during thread')
            try:
                func_timeout(25, self.sign_in_now)
            except FunctionTimedOut:
                self.toast('Authentication failed timed out')
                print("Authentication failed timedout")
                self.switch_signin()
                self.event.set()
                
                # self.switch_from_signin()
            except:
                self.toast('Authentication failed')
                print("Sign in failed")
                self.switch_signin()
                self.event.set()
            
            # self.switch_from_signin()
            self.spin_false()
            
            
        
    
    def sign_in_now(self):
        email = self.signin.ids.email.text
        
        password = self.signin.ids.password.text
        
        count = 0
        
        try:
            self.user = authi.sign_in_with_email_and_password(email, password)
            ino = authi.get_account_info(self.user['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                authi.send_email_verification(self.user['idToken'])
                text = "An email verification link has been sent to your mail"
                
                self.show_dialog(text)
            
            
            
            
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
                

            if self.curr['first_time'] == "true":
                
                
                

                self.testichiro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                # self.testiroro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                
                if self.testichiro.each():
                    for i in self.testichiro.each():
                        count += 1

                # if self.testiroro.each():
                #     for u in self.testiroro.each():
                #         count += 1

                self.curr['sold'][email] = count
                self.curr['bookmarks'][email] = []
                self.curr['viewed'][email] = []
                self.curr['accounts'].append({'email': email, 'password': password})
                
            else:
                if email not in self.curr['bookmarks']:
                    
                    self.testichiro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                    # self.testiroro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                    
                    if self.testichiro.each():
                        for i in self.testichiro.each():
                            count += 1

                    # if self.testiroro.each():
                    #     for u in self.testiroro.each():
                    #         count += 1

                    self.curr['sold'][email] = count
                    self.curr['bookmarks'][email] = []
                    self.curr['viewed'][email] = []
                    self.curr['accounts'].append({'email': email, 'password': password})

                if self.curr['sold'][email] == 0:
                    self.testichiro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                    # self.testiroro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
                    
                    if self.testichiro.each():
                        for i in self.testichiro.each():
                            count += 1

                    self.curr['sold'][email] = count

            self.curr['email'] = email
            self.curr['password'] = password
            self.curr['idToken'] = self.user['idToken']
            self.curr['localid'] = self.user['localId']
            
            print(self.user['localId'] + " " + "aaaaaaaaaaaaahahahahaaaaaaaahahahahaa")
            
            
            
            print(self.curr['localid'])
            print(self.curr['idToken'])



# testro = db.child("People").get(curr['idToken'])
# for i in testro.each():
    # print(i.val()['prop_keys'])
#     # dude = i.val()['prop_keys']
    # print(i.key())
#     # them = db.child("Sale").child(dude).get(self.user['idToken'])
#     # for u in them.each():
    # print(u.val())
    # print(i.val())

# againi = db.child("People").child("Sale").child(curr['localid']).child("house").get()
# if againi.each():
#     for i in againi.each():
        # print(i.val()['local_image'])
#         curr['house_images'].append(i.val()['local_image'])
# else:
#     pass

            if self.curr['first_time'] == "true":
                self.switch_home()
                self.curr['first_time'] = "false"
            else:
                self.switch_from_signin()

            with open(f'{path}/user.json', 'w') as jsonfile:
                json.dump(self.curr, jsonfile)
            # self.reinit()
            

        
            p = 'Successfully signed in'
            self.snackbar(p)
            

            self.home.text = self.curr['email']
            self.kill = True
            self.spin_false()
        
        # self.mail = ''
        # self.passwrd = ''

        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            print(str(error) + "is the error")
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                
                self.switch_signin()
                print('Email not found')
                self.show_dialog(text)
                
                # self.text_error()
                
            if error == 'INVALID_PASSWORD':
                text = "Invalid password"
                self.switch_signin()
                self.show_dialog(text)
                print('Invalid password')
                
                # self.text_error()
            
            if error == 'INVALID_EMAIL':
                text = "Invalid email"
                self.switch_signin()
                self.show_dialog(text)
                print('Invalid email')
                
                # self.text_error()

            if error == "MISSING_PASSWORD":
                text = "Missing password"
                self.switch_signin()
                self.show_dialog(text)
                print('Missing password')
            self.spin_false()
                # self.text_error()
                
        # except:
        #     p = 'Network Error'
        #     self.snackbar(p)
        
        
        # except:
        #     p = 'No internet connection'
        #     self.snackbar(p)

        
            
        # except:
        #     text = "Invalid email or password"
        #     
    # @mainthread
    # def text_error(self):
    #     self.signin.ids.email.text = ''
    #     self.signin.ids.password.text = ''
        # self.signin.ids.password.error = True
        
    
    
    def editscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        print("this is self.amenities")
        self.passwrd = ''
        self.mail = ''
        print(self.amenities)
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        print("Another self.amenities")
        print(self.amenities)
        self.edit = EditDetailsScreen(name="edit")
        self.wm.switch_to(self.edit)
        self.edit.type = House_type
        self.edit.image = image
        self.edit.price = pricing
        self.edit.country = locate
        self.edit.province = state
        self.edit.town = town
        self.edit.street = street
        self.edit.bedrooms = bedrooms
        self.edit.bathrooms = bathrooms
        self.edit.landspace = landspace.replace('sq.ft', '') if landspace.endswith('sq.ft') else landspace
        self.edit.email = email
        self.edit.key = key
        self.edit.local_image = local_image
        self.edit.description = description
        self.edit.amenities = amenities
        print(key, town, street, local_image, amenities, House_type)
        print("This is the new self.amenities")
        print(self.amenities)
        self.denied = 0
        

    def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        self.edit_rent = EditRentDetailsScreen(name="edit-rent")
        print(self.amenities)
        self.passwrd = ''
        self.mail = ''
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        print("Another self.amenities")
        print(self.amenities)
        self.wm.switch_to(self.edit_rent)
        self.edit_rent.type = House_type
        self.edit_rent.image = image
        self.edit_rent.price = pricing.replace('/mth', '') if pricing.endswith('/mth') else pricing.replace('/yr', '')
        self.edit_rent.country = locate
        self.edit_rent.province = state
        self.edit_rent.town = town
        self.edit_rent.street = street
        self.edit_rent.bedrooms = bedrooms
        self.edit_rent.bathrooms = bathrooms
        self.edit_rent.landspace = landspace.replace('sq.ft', '') if landspace.endswith('sq.ft') else landspace 
        self.edit_rent.email = email
        self.edit_rent.key = key
        self.edit_rent.local_image = local_image
        self.edit_rent.description = description
        self.edit_rent.amenities = amenities
        print(key)
        self.denied = 0
        
        # refreshed = authi.refresh(self.user['refreshToken'])
        # self.curr['idToken'] = self.user['idToken']
        # with open(f'{path}/user.json', 'w') as jsonfile:
        #     json.dump(self.curr, jsonfile)

    def thread_dialog(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description, titler="Updating Property"):
        self.thread_dialogbox = MDDialog(text='Please wait...', title=titler, size_hint=(1,1), on_open=lambda x:self.thread_update_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description))
        self.thread_dialogbox.open()

    
    def close_thread_dialog(self):
        self.thread_dialogbox.dismiss()
    
    

    def update_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        print(locate)

        house_type = House_type.title()
        new_state = state.title()
        new_town = town.title()
        new_street = street.title()
        new_desc = description.capitalize()
        
        if '$' in pricing:
            self.amt = pricing
        else:
            self.amt = "$" + pricing
        
        
        if landspace.endswith('sq.ft'):
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'

        self.key = key
        self.local_image = local_image
        amenities = self.amenities
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        # pp = int(pricing)
        # print(pp)
        
        
        
        # self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
        # usero = authi.refresh(self.user['refreshToken'])
        # self.curr['idToken'] = self.user['idToken']
        # with open(f'{path}/user.json', 'w') as jsonfile:
        #     json.dump(self.curr, jsonfile)
        
        # try:

        if len(house_type) > 5 and len(house_type) < 21:
            
            
            if len(new_state) >= 3 and len(new_state) < 25:
                if len(new_town) >= 3 and len(new_town) < 25:

                    if len(new_street) >= 3 and len(new_street) < 25:
                        if len(pricing) > 1:
                            if len(new_desc) > 20 and len(new_desc) < 255:
                                self.thread_dialog(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description, titler="Updating Property")

                            else:
                                text = 'description must be between 20 and 255 characters long'
                                self.show_dialog(text)
                                self.edit.ids.description.error = True
                        else:
                            text = "Invalid Input for price"
                            self.show_dialog(text)
                            self.edit.ids.street.error = True
                    else:
                        text = "street must be between 3 and 25 characeters"
                        self.show_dialog(text)
                        self.edit.ids.street.error = True
                else:
                    text = "town must be between 2 and 25 characters"
                    self.show_dialog(text)
                    self.edit.ids.town.error = True
            else:
                text = "State must be between 2 and 25 characters"
                self.show_dialog(text)
                self.edit.ids.state.error = True
            
        else:
            text = "House type must be between 5 and 21 characters characeters"
            self.show_dialog(text)
            self.edit.ids.housetype.error = True

        # except
    # @mainthread
    # def reloading(self, key):
        
    #     PropertyCardsLayout().reload(key)

    def thread_update_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            func_timeout(20, self.actual_sale_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
        except FunctionTimedOut:
            self.toast("Internet connection limited or unavailable")
        except:
            self.toast("Failed to update Property")

        self.close_thread_dialog()

    def actual_sale_update(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            location = locate+state.title()+town.title()
            print(locate)
            print(location)
            amenities = self.amenities
            print(amenities)
            getting = db.child("Sale").child(key).get()
            if getting.val() == None:
                self.toast("Not found")
                print("Not found")
            else:
                db.child("Sale").child(key).update({'housetype': House_type.title()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'country': locate}, self.curr['idToken'])
                db.child("Sale").child(key).update({'state': state.title()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'town': town.title()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'street': street.title()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'bedrooms': bedrooms}, self.curr['idToken'])
                db.child("Sale").child(key).update({'bathrooms': bathrooms}, self.curr['idToken'])
                db.child("Sale").child(key).update({'landspace': self.landspace}, self.curr['idToken'])
                db.child("Sale").child(key).update({'price': self.amt}, self.curr['idToken'])
                db.child("Sale").child(key).update({'description': description.capitalize()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'amenities': amenities}, self.curr['idToken'])
                db.child("Sale").child(key).update({'location': location}, self.curr['idToken'])
                print(key)
                # print(loaded)
                print(self.amenities)
                self.amenities = amenities
                # self.reloading(key)
                # loaded.remove(key)
                self.sale_or_rent = "Sale"
                # self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
                print("Changes made successfully")
                self.denied = 0
                self.change_image_auth()
                p = 'Changes made successfully'
                self.snackbar(p)

        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            print(str(error) + "is the error")
            if error == 'Permission denied':
                print("Permission denied")
                print("Resigning in")
                self.denied += 1
                print(self.denied)
                if self.denied < 2:
                    # try:
                    try:
                        func_timeout(10, self.denied_signin)
                        self.update_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description)
                        self.denied = 0
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        print("Internet connection limited or unavailable")
                        self.denied = 0
                    except:
                        self.toast("Network Error")
                        print("Network Error")
                        self.denied = 0
                        # try:
                        #     func_timeout(40, self.actual_sale_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
                        # except FunctionTimedOut:
                        #     p = 'Failed to update Property'
                        #     self.snackbar(p)
                        #     print('Timed out')

                        
                    # except:
                    #     self.toast("Network Error")
                    #     print("Network Error")
                else:
                    self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.", titler="Permission denied")
                    self.denied = 0
                    print("Permission finally denied")
                # except Exception as e:
                #     p = 'Failed to update Property'
                #     self.snackbar(p)
                #     print('Failed to update property')
            # if error['message']:
            #     if error['message'] == 'Permission denied.':
            #         self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.")
            #         # self.denied = 0
            #         print("Permission finally denied")
    def thread_rent_dialog(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        self.thread_dialogbox = MDDialog(text='Please wait...', title="Updating Property", size_hint=(1,1), on_open=lambda x:self.thread_update_rent_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description))
        self.thread_dialogbox.open()    

    def close_thread_rent(self):
        self.thread_dialogbox.dismiss()

    def thread_update_rent_property(self,  local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            func_timeout(40, self.actual_rent_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
        except FunctionTimedOut:
            self.toast("Internet connection limited or unavailable")
        except:
            self.toast("Failed to update Property")

        self.close_thread_rent()
    def update_rent_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        self.key = key
        self.local_image = local_image
        print(pricing)
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        
        
        
        
        amenities = self.amenities

        
        if pricing[0] == '$':
            self.amt = pricing + self.edit_rent.ids.pay_item.text if not pricing.endswith('/mth') or pricing.endswith('/yr') else pricing
        else:
            self.amt = '$' + pricing + self.edit_rent.ids.pay_item.text if not pricing.endswith('/mth') or pricing.endswith('/yr') else '$' + pricing

        if landspace[-1] == 't':
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'
        # pp = int(pricing)
        # print(pp)
        
        

        if len(House_type) > 5 and len(House_type) < 21:
            
            if len(state) >= 3 and len(state) < 25:

                
                
                if len(town) >= 3 and len(town) < 25:

                    if len(street) >= 3 and len(street) < 25:
                        if len(pricing) > 2:
                            if len(description) > 20 and len(description) < 255:

                                self.thread_rent_dialog(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description)
                                

                                
                            else:
                                text = 'Description must be between 20 and 255 characters'
                                self.show_dialog(text)
                        else:
                            text = "Invalid Input for price"
                            self.show_dialog(text)
                    else:
                        text = "street must be between 3 and 25 characeters"
                        self.show_dialog(text)
                        self.edit_rent.ids.street.error = True
                else:
                    text = "town must be between 2 and 25 characters"
                    self.show_dialog(text)
                    self.edit_rent.ids.town.error = True
            else:
                text = "State must be between 2 and 25 characters"
                self.show_dialog(text)
                self.edit_rent.ids.state.error = True
        else:
            text = "House type must be between 5 and 21 characters"
            self.show_dialog(text)
            self.edit_rent.ids.housetype.error = True

    def actual_rent_update(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            location = locate+state.title()+town.title()
            amenities = self.amenities
            getting = db.child("Rent").child(key).get()
            if getting.val() == None:
                self.toast("Not found")
                print("Not found")
            else:
                db.child("Rent").child(key).update({'housetype': House_type.title()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'country': locate}, self.curr['idToken'])
                db.child("Rent").child(key).update({'state': state.title()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'town': town.title()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'street': street.title()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'bedrooms': bedrooms}, self.curr['idToken'])
                db.child("Rent").child(key).update({'bathrooms': bathrooms}, self.curr['idToken'])
                db.child("Rent").child(key).update({'landspace': self.landspace}, self.curr['idToken'])
                db.child("Rent").child(key).update({'price': self.amt}, self.curr['idToken'])
                db.child("Rent").child(key).update({'description': description.capitalize()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'amenities': amenities}, self.curr['idToken'])
                db.child("Rent").child(key).update({'location': location}, self.curr['idToken'])
                self.sale_or_rent = "Rent"
                self.amenities = amenities
                self.change_image_auth()
                p = 'Changes made successfully'
                self.snackbar(p)
                self.denied = 0
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            print(str(error) + "is the error")
            if error == 'Permission denied':
                print("Permission denied")
                print("Resigning in")
                self.denied += 1
                print(self.denied)
                if self.denied < 2:
                    # try:
                    try:
                        func_timeout(20, self.denied_signin)
                        self.update_rent_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description)
                        self.denied = 0
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        print("Internet connection limited or unavailable")
                        self.denied = 0
                    except:
                        self.toast("Network Error")
                        print("Network Error")
                        self.denied = 0
                        # try:
                        #     func_timeout(40, self.actual_rent_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
                        # except FunctionTimedOut:
                        #     p = 'Failed to update Property timedout'
                        #     self.toast(p)
                        #     print('Timed out')
                    # except:
                    #     self.toast("Network Error")
                    #     print("Network Error")
                else:
                    self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.")
                    self.denied = 0
                    print("Permission finally denied")
                # except Exception as e:
                #     p = 'Failed to update Property'
                #     self.snackbar(p)
                #     print('Failed to update property')
            # if error['message']:
            #     if error['message'] == 'Permission denied.':
            #         self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.")
            #         # self.denied = 0
            #         print("Permission finally denied")
        # except Exception as e:
             
        #     self.snackbar('Failed to update Property')
        #     print('Failed to update property')

    
    @mainthread
    def change_image_auth(self):
        agree_button = MDRaisedButton(text="yes", on_press=self.close_dialog, on_release=self.separate_function)
       
        info = "Do you want to change your property image?"
        self.show_dialog(info,button=agree_button)
        print("DOne being called")

    # def call_separate_function(self,obj):
    #     try:
    #         func_timeout(40, self.separate_function)
    #     except FunctionTimedOut:
    #         p = 'Failed to update Image'
    #         self.snackbar(p)
        
    def separate_function(self,obj):
        # boy = []
        
        filechooser.open_file(on_selection=self.change_image_dialog,)
        
        
        # print(boy)

    
    def change_image_dialog(self, selection):
        self.dialog_image = MDDialog(text="Please wait..", title="Updating image", size_hint=(1,1), on_open=lambda x:self.change_image(selection))
        self.dialog_image.open()

    def close_image_dialog(self):
        self.dialog_image.dismiss()
        
    def change_image(self, selection):
        print(selection)
        if len(selection) > 0:
            self.new_file = str(selection[0])
            # self.switch_loading()
            try:
                func_timeout(30, self.change_image_process, args=(self.new_file,))
            except FunctionTimedOut:
                self.toast("Internet conneciton limit or unavailable") 
                print("Internet conneciton limit or unavailable")
                self.switch_products()
            except:
                self.toast("Network Error")
                self.switch_products()
            
        self.close_image_dialog()
        
    def change_image_process(self, selection):
        print(selection)
        if len(selection) > 0:
            self.new_file = selection
            print(self.local_image)
            x = re.search(r".jpg$", self.new_file)
            y = re.search(r".png$", self.new_file)
            if x or y:
                # urli = storage.child(data['localid']).child(self.local_image).get_url(data['idToken'])
                # tokenop = "https://firebasestorage.googleapis.com/v0/b/first-db-77609.appspot.com/o/2C8VZdiEBCMhnFS0fnvzpa4jW2F2%2FC%3A%5CUsers%5CYvonne%5CDownloads%5Cbeautiful-house-15.jpg?alt=media"
                # storage.
                
                # user = authi.sign_in_with_email_and_password(dati['email'], dati['password'])
                try:
                    

                    # bucket = admin_storage.bucket()
                    # blob = bucket.blob(self.local_image)
                    # print(blob)
                    # blob.delete()
                   
                    print(self.curr['localid'])
                    print(self.new_file)
                    print(self.key)
                    if self.new_file[0] == "/":
                        storage.child(self.curr['localid'] + '/' + self.new_file.replace('/', ',,')).put(str(self.new_file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.new_file.replace('/', ',,')).get_url(None)
                        print("updated")
                    else:
                        storage.child(self.curr['localid'] + '/' + self.new_file).put(str(self.new_file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.new_file).get_url(None)
                        print("updated")
                    if self.sale_or_rent == 'Sale':
                        db.child("Sale").child(self.key).update({'local_image': self.new_file}, self.curr['idToken'])
                        db.child("Sale").child(self.key).update({'url': url}, self.curr['idToken'])
                    else:
                        db.child("Rent").child(self.key).update({'local_image': self.new_file}, self.curr['idToken'])
                        db.child("Rent").child(self.key).update({'url': url}, self.curr['idToken'])
                    storage.delete(self.curr['localid'] + '/' + self.local_image, self.curr['idToken'])
                    print('Successfully deleted')
                    p = 'Changes made successfully'
                    self.snackbar(p)
                    self.switch_products()
                
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']
                    print(str(error) + "is the error")
                    
                    if error == 'Permission denied':
                        print("Permission denied")
                        print("Resigning in")
                        
                        
                        try:
                            self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                            usero = authi.refresh(self.user['refreshToken'])
                            self.curr['idToken'] = self.user['idToken']
                            with open(f'{path}/user.json', 'w') as jsonfile:
                                json.dump(self.curr, jsonfile)

                            try:
                                func_timeout(35, self.change_image_process, args=(self.selection,))
                            except FunctionTimedOut:
                                self.toast('Failed to update image') 
                                print("Internet conneciton limit or unavailable")
                            except:
                                self.toast("Failed to update image")
                                self.switch_products()

                        except:
                            self.toast('Failed to update image')
                            print("Network Error")

                    try:
                        if error['message'] == 'Permission denied.':
                            self.show_dialog("All permissions are denied for updating property images right now. Please wait until the slots are open.", titler="Permission denied")
                            # self.denied = 0
                            print("Permission finally denied")
                    except:
                        pass
                # except Exception as e:
                #     print('Failed to update image')
                #     self.snackbar('Failed to update image')
            else:
                
                info = 'Please select an image file'
                print("please select an image file")
                self.show_dialog(info)

        
            

    
        

    
                # text = "yes"
                # self.close_dialog(text)
                
                # notice = "No user signed in"
            # self.show_dialog(notice)
    
    

    


    
    
        

    def bookmark(self, lola):
        
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            mail = data['email']
        if mail != '':
            if lola not in data['bookmarks'][mail]:
                if len(data['bookmarks'][mail]) < 24:
                    data['bookmarks'][mail].append(lola)
                    with open(f'{path}/user.json', 'w') as jsonfile:
                        json.dump(data, jsonfile)
                    notice = 'Successfully added to bookmarks'
                    self.snackbar(notice)
                else:
                    
                    info = "Bookmarks full. You can only add up to 24 bookmarks"
                    self.show_dialog(info)
            else:
                data['bookmarks'][mail].remove(lola)
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)
                notice = 'Successfully removed from bookmarks'
                self.snackbar(notice)

            
        

    def selected(self):
        
        
        print(self.mail)
        if self.mail == self.curr['email']:
            if self.phonenumber != '':
                phone_number  = phonenumbers.parse(self.phonenumber)
                valid = phonenumbers.is_valid_number(phone_number)
                print(valid)
                if valid == True:
                    if len(self.tot) > 5 and len(self.tot) < 21:
                        
                        if len(self.country) >= 2 and len(self.country) < 16:
                            # phone = '+2332222222222'
                            
                            if len(self.state) >= 3 and len(self.state) < 25:
                                if len(self.town) >= 3 and len(self.town) < 25:

                                    if len(self.street) >= 3 and len(self.street) < 25:
                                        if len(self.landspace) > 1:
                                            if len(self.price) > 1:
                                                if len(self.desc) > 20 and len(self.desc) < 255:
                                                    filechooser.open_file(on_selection=self.real_house_sale)
                                                else:
                                                    info = "description must be between 20 and 255 characters"
                                                    self.show_dialog(info)
                                            else:
                                                info = "Invalid input for price"
                                                self.show_dialog(info)
                                        else:
                                            info = "Invalid input for landspace"
                                            self.show_dialog(info)
                                    else:
                                        info = "Street must be between 3 and 25 characters"
                                        self.show_dialog(info)

                                else:
                                    info = "Town must be between 2 and 25 characters"
                                    self.show_dialog(info)
                            else:
                                info = "State must be between 2 and 25 characters"
                                self.show_dialog(info)
                        else:
                            info = "Please select your country"
                            self.show_dialog(info)
                    else:
                        info = "Property type must be between 5 and 21 characters"
                        self.show_dialog(info)
                else:
                    info = "Invalid phonenumber"
                    self.show_dialog(info)
            
            else:
                info = "Please enter a phonenumber"
                self.show_dialog(info)
        else:
            text = "Invalid email"
            self.show_dialog(text)

    def real_house_sale(self, selection):
        self.loading.ids.spin.active=True
        self.switch_loading()

        self.event = Event()
        
        self.sale_thread = threading.Thread(target=self.real_sale, args=(selection,))
        self.sale_thread.start()
        
        
        
    @mainthread
    def true_switch_sale(self):
        self.wm.switch_to(self.sale)

    def real_sale(self, selection):
        print('Real sale')
        self.sale_tot = self.tot.title()
        self.sale_country=self.country
        self.sale_state = self.state.title()
        self.sale_town=self.town.title()
        self.sale_street=self.street.title()
        self.sale_bedrooms = self.bedrooms
        self.sale_bathrooms = self.bathrooms
        self.sale_price = '$' + self.price
        self.sale_desc = self.desc.capitalize()
        self.sale_land = self.landspace + 'sq.ft'
        self.sale_amenities = self.amenities
        self.sale_mail = self.mail
        self.sale_phone = self.phonenumber
        self.sale_twitter = self.twitter
        self.sale_facebook = self.facebook



        selected_image = selection
        # self.denied = 0
        print(selected_image)
        if len(selected_image) > 0:
            # self.switch_loading()
            if not self.event.is_set():
                
                try:
                    func_timeout(30, self.house_sale, args=(selected_image,))
                except FunctionTimedOut:
                    self.toast("Internet connection limited or unavailable") 
                    print("Internet connection limit or unavailable")
                    self.true_switch_sale()
                    self.event.set()
                # except:
                #     print("Failed to submit property")
                #     self.toast("Failed to submit property")
                #     self.event.set()
                #     self.true_switch_sale()
                
            else:
                print("Event is set before anything")
            #     p="No intenet connection"
            #     self.snackbar(p)
        else:
            info = "You need to select an image to continue"
            self.show_dialog(info)
            self.true_switch_sale()
        
        # except FunctionTimedOut:
            # print("Failed to submit property")
        #     p="Failed to submit property"
        #     self.snackbar(p)
        # except Exception as e:
            # print("An error occured")
        #     p="An error occured"

    
    
    def house_sale(self, selection):
        
        
        # self.yet = False
        
        print(selection)
        # print("Number of times denied" + " " + str(self.denied))
        self.file = selection[0]

        print(self.file)
        print(self.file[-1:-4])
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png$", self.file)
        if x or y:
            print('yes there is a match')
            try:
                
                
                if self.file[0] == "/":
                    
                    if not self.event.is_set():
                        storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).get_url(None)
                    else:
                        print("Self.event set inside storage")
                else:
                    
                    if not self.event.is_set():
                        storage.child(self.curr['localid'] + '/' + self.file).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file).get_url(None)
                    else:
                        print("Self.event set inside storage")
                
                
                print(self.file)
                # with open(f'{path}/user.json', 'r') as jsonfile:
                #     dato = json.load(jsonfile)
                print(self.phonenumber)
            
                
                
                data = {
                    "housetype": "",
                    "country": "",
                    "state": "",
                    "town": "",
                    "street": "",
                    "bedrooms": "",
                    "bathrooms": "",
                    "landspace": "",
                    "url": "",
                    "email": "",
                    "phonenumber": "",
                    "twitter": "",
                    "facebook": "",
                    "price": "",
                    "local_image": "",
                    "description": "",
                    "amenities": [],
                    "views": 0,
                    "location": ""
                }

                
                
                data['housetype'] = self.sale_tot.strip()
                data['country'] = self.sale_country
                data['state'] = self.sale_state.strip()
                data['town'] = self.sale_town.strip()
                data['street'] = self.sale_street.strip()
                data['bedrooms'] = self.sale_bedrooms
                data['bathrooms'] = self.sale_bathrooms
                data['landspace'] = self.sale_land.strip()
                data['url'] = url
                data['email'] = self.sale_mail.strip()
                data['phonenumber'] = self.sale_phone.strip()
                data['price'] = self.sale_price.strip()
                data['local_image'] = self.file.replace('/', ',,')
                data['description'] = self.sale_desc.strip()
                data['amenities'] = self.sale_amenities
                data['twitter'] = self.sale_twitter.strip()
                data['facebook'] = self.sale_facebook.strip()
                data['location'] = self.sale_country.strip()+self.sale_state.strip()+self.sale_town.strip()
                
                print("pushing data")
                results = db.child("Sale").push(data, self.curr['idToken'])
                self.tot = ''
                self.country = ''
                self.state = ''
                self.town = ''
                self.street = ''
                self.bedrooms = ''
                self.bathrooms = ''
                self.landspace = ''
                self.price = ''
                self.phonenumber = ''
                self.desc = ''
                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
                self.twitter = ''
                self.facebook = ''
                self.mail = ''
                

                
                
                key_data = {
                    "prop_keys": "",
                }
                key_data['prop_keys'] = results['name']
                db.child("People").child(self.curr['localid']).child("ids").push(key_data, self.curr['idToken'])
                print(key_data)
                print(results)
                print("updating sold")
                self.curr["sold"][self.curr['email']] += 1
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                print("updated sold")
                self.switch_congrats()
            
                
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                print(str(error) + "is the error")
                if error == 'Permission denied':
                    print("Permission denied")
                    print("Resigning in")
                    print(self.curr['idToken'])
                    # self.denied += 1
                    # if self.denied < 2:
                    try:
                        func_timeout(1, self.denied_signin)
                        time.sleep(1)
                        if not self.event.is_set():
                            self.real_house_sale(selection)
                        else:
                            print("Tried to start after denial")
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        
                        self.event.set()
                        print("Internet connection limited or unavailable")
                        self.true_switch_sale()
                    except:
                        self.toast("Failed to submit property")
                        print("Failed to submit property")
                        self.event.set()
                        self.true_switch_sale()
                    
                       

                try:
                    if error['message'] == 'Permission denied.':
                        self.show_dialog("All permissions are denied for selling properties right now. Please wait until the slots are open.", titler="Permission denied")
                        # self.denied = 0
                        print("Permission finally denied")
                        self.true_switch_sale()
                except:
                    pass
                
        else:
            self.show_notice()
            self.true_switch_sale()
            print('no match at all')
            
    
        
        

    
        

    def rent_property(self):
        
        if self.mail == self.curr['email']:
            if self.phonenumber != '':
                phone_number  = phonenumbers.parse(self.phonenumber)
                valid = phonenumbers.is_valid_number(phone_number)
                print(valid)
                if valid == True:
                    if len(self.tot) > 5 and len(self.tot) < 21:
                        
                        if len(self.country) >= 2 and len(self.country) < 16:
                            # phone = '+2332222222222'
                            
                            if len(self.state) >= 3 and len(self.state) < 25:
                                if len(self.town) >= 3 and len(self.town) < 25:

                                    if len(self.street) >= 6 and len(self.street) < 25:
                                        if len(self.landspace) > 1:
                                            if len(self.price) > 1:
                                                if len(self.desc) > 20 and len(self.desc) < 255:
                                                    filechooser.open_file(on_selection=self.real_house_rent)
                                                else:
                                                    info = "description must be between 20 and 255 characters"
                                                    self.show_dialog(info)
                                            else:
                                                info = "Invalid input for price"
                                                self.show_dialog(info)
                                        else:
                                            info = "Invalid input for landspace"
                                            self.show_dialog(info)
                                    else:
                                        info = "Street must be between 3 and 25 characters"
                                        self.show_dialog(info)

                                else:
                                    info = "Town must be between 2 and 25 characters"
                                    self.show_dialog(info)
                            else:
                                info = "State must be between 2 and 25 characters"
                                self.show_dialog(info)
                        else:
                            info = "Please select your country"
                            self.show_dialog(info)
                    else:
                        info = "Property type must be between 5 and 21 characters"
                        self.show_dialog(info)
                else:
                    info = "Invalid phonenumber"
                    self.show_dialog(info)
            
            else:
                info = "Please enter a phonenumber"
                self.show_dialog(info)
        else:
            text = "Invalid email"
            self.show_dialog(text)

    @mainthread
    def true_switch_rent(self):
        self.wm.switch_to(self.rent)


    def real_house_rent(self, selection):
        self.loading.ids.spin.active = True
        self.switch_loading()
        self.event = Event()
        self.thread_rent = threading.Thread(target=self.real_rent, args=(selection,))
        self.thread_rent.start()



    def real_rent(self, selection):
        print('real rent')
        

        self.rent_tot = self.tot.title()
        self.rent_country=self.country
        self.rent_state = self.state.title()
        self.rent_town=self.town.title()
        self.rent_street=self.street.title()
        self.rent_bedrooms = self.bedrooms
        self.rent_bathrooms = self.bathrooms
        self.rent_price = self.price
        self.rent_desc = self.desc.capitalize()
        self.rent_land = self.landspace + 'sq.ft'
        self.rent_amenities = self.amenities
        self.rent_mail = self.mail
        self.rent_phone = self.phonenumber
        self.rent_twitter = self.twitter
        self.rent_facebook = self.facebook




        print('done')
        selected_image = selection
        if len(selected_image) > 0:
            print(selected_image)
            # self.switch_loading()
            
            try:
                func_timeout(30, self.house_rent, args=(selected_image,))
            except FunctionTimedOut:
                self.toast("Internet connection limited or unavailable")
                print("Internet connection limited or unavailable")
                self.event.set()
                self.true_switch_rent()
            # except:
            #     print("Failed to submit property")
            #     self.event.set()
            #     self.toast('Failed to submit property')
            #     self.true_switch_rent()
            #     self.snackbar(p)
            #     print("Failed to submit property")
            
        else:
            info = "You need to select an image to continue"
            self.show_dialog(info)
            self.true_switch_rent()

    
    def house_rent(self, selection):
        
        # self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
        print(selection)
        
        self.file = selection[0]
        
        print(self.file)
        print(self.file[-1:-4])
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png$", self.file)
        if x or y:
            try:
                if not self.event.is_set():
                    if self.file[0] == "/":
                        storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).get_url(None)
                    else:
                        storage.child(self.curr['localid'] + '/' + self.file).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file).get_url(None)
                else:
                    print("tried to upload to storage behnid my back")

            
                
                
                data = {
                    "housetype": "",
                    "country": "",
                    "state": "",
                    "town": "",
                    "street": "",
                    "bedrooms": "",
                    "bathrooms": "",
                    "landspace": "",
                    "url": "",
                    "email": "",
                    "price": "",
                    "local_image": "",
                    "phonenumber": "",
                    "twitter": "",
                    "facebook": "",
                    "description": "",
                    "amenities": "",
                    "views": 0,
                    "location": ""
                }
                
                
                data['housetype'] = self.rent_tot.strip()
                data['country'] = self.rent_country
                data['state'] = self.rent_state.strip()
                data['town'] = self.rent_town.strip()
                data['street'] = self.rent_street.strip()
                data['bedrooms'] = self.rent_bedrooms
                data['bathrooms'] = self.rent_bathrooms
                data['landspace'] = self.rent_land.strip()
                data['url'] = url
                data['email'] = self.rent_mail.strip()
                data['phonenumber'] = self.rent_phone.strip()
                data['price'] = "$" + self.rent_price.strip() + self.rent.ids.pay_item.text
                data['local_image'] = self.file.replace('/', ',,')
                data['description'] = self.rent_desc.strip()
                data['amenities'] = self.rent_amenities
                data['twitter'] = self.rent_twitter.strip()
                data['facebook'] = self.rent_facebook.strip()
                data['location'] = self.rent_country.strip()+self.rent_state.strip()+self.rent_town.strip()
                # db.child("People").child(key).child("house").push(data)
                # results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
                results = db.child("Rent").push(data, self.curr['idToken'])
                self.tot = ''
                self.country = ''
                self.state = ''
                self.town = ''
                self.street = ''
                self.bedrooms = ''
                self.bathrooms = ''
                self.landspace = ''
                self.price = ''
                self.phonenumber = ''
                self.desc = ''
                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
                self.twitter = ''
                self.facebook = ''
                self.mail = ''


                
                
                key_data = {
                    "prop_keys": "",
                }
                key_data['prop_keys'] = results['name']
                db.child("People").child(self.curr['localid']).child("ids").push(key_data, self.curr['idToken'])
                print(key_data)
                print(results)
                self.curr["sold"][self.curr['email']] += 1
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                self.switch_congrats()
                
            # for i in results.each():
                # print(i.key())

            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                print(str(error) + "is the error")
                if error == 'Permission denied':
                    print("Permission denied")
                    print("Resigning in")
                    
                    try:
                        func_timeout(1, self.denied_signin)
                        time.sleep(1)
                        if not self.event.is_set():
                            self.real_house_rent(selection)
                        else:
                            print("Tried to work after denial")
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        print("Internet connection limited or unavailable")
                        self.event.set()
                        self.switch_true_rent()
                        
                    except:
                        self.toast("Failed to submit property")
                        print("Failed to submit property")
                        self.event.set()
                        self.switch_true_rent()
                

                try:
                    if error['message'] == 'Permission denied.':
                        self.show_dialog("All permissions are denied for renting properties right now. Please wait until the slots are open.", titler="Permission denied")
                        # self.denied = 0
                        print("Permission finally denied")
                        self.switch_true_rent()
                except:
                    pass
                
        else:
            self.show_notice()
            self.switch_true_rent()
    
    @mainthread
    def show_notice(self):
        
        info = 'Please select an image file'
        self.show_dialog(info)

    def denied_signin(self):
        self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
        usero = authi.refresh(self.user['refreshToken'])
        self.curr['idToken'] = self.user['idToken']
        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)

MainApp().run()
