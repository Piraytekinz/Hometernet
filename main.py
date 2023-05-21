
import phonenumbers
import pycountry
from datetime import datetime, timedelta, date
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.loader import Loader

from kivy.uix.screenmanager import ScreenManager, Screen,NoTransition, WipeTransition, SlideTransition,CardTransition
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, ListProperty, ObjectProperty

from kivy.properties import NumericProperty
from kivymd.uix.list import MDList, OneLineListItem,OneLineIconListItem,IconLeftWidget
from kivymd.uix.textfield import MDTextField
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.snackbar import Snackbar
from kivy.uix.recycleview import RecycleView
from kivymd.uix.gridlayout import MDGridLayout
from functools import partial

from kivymd.uix.label import MDLabel, MDIcon



from kivymd.utils import asynckivy

from kivymd.effects.stiffscroll import StiffScrollEffect



# from kivy.effects.scroll import ScrollEffect
# from kivy.effects.kinetic import KineticEffect
from kivy.effects.dampedscroll import DampedScrollEffect


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
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.toast import toast

from kivymd.uix.spinner import MDSpinner
import webbrowser


import requests
from kivy.clock import Clock, mainthread
from func_timeout import func_timeout, FunctionTimedOut
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



sound = SoundLoader.load('touch.wav')






firebasei = pyrebase.initialize_app(firebaseconfig)

db = firebasei.database()
authi = firebasei.auth()
storage = firebasei.storage()



Loader.loading_image = 'load-33.gif'





        


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
Builder.load_file('UpdateScreen.kv')





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
    
    
        
class Loading(MDLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'loading...'
        self.font_size = '16dp'
        self.bold = True
        self.halign ='center'


class CodeVerifyer(Screen):
    text = StringProperty()
    



        


class MainScroll(ScrollView):
    pass

   
        
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
    link = StringProperty()
    me = ObjectProperty()
    



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
    link = StringProperty()
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No', 'No'])



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
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No', 'No'])

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
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No', 'No'])

    def __init__(self, **kw):
        super().__init__(**kw)
        payment_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "/yr",
                
                "on_release": lambda x="/yr": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/mth",
                
                "on_release": lambda x="/mth": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/wk",
                
                "on_release": lambda x="/wk": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/night",
                
                "on_release": lambda x="/night": self.set_payment(x)
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
        
    
class SearchScreen(Screen):
    pass

class SpinnerWheel(MDSpinner):
    pass

class SearchLayout(MDGridLayout):
    pass

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
                "text": "/yr",
                
                "on_release": lambda x="/yr": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/mth",
                
                "on_release": lambda x="/mth": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/wk",
                
                "on_release": lambda x="/wk": self.set_payment(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": "/night",
                
                "on_release": lambda x="/night": self.set_payment(x)
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
        
        self.done = False
        self.denied = 0
        self.deleted = False
        self.has_deleted = False
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
        self.dia = MDDialog(title=titler, text=notice, size_hint=(1, 1), buttons=[MDRaisedButton(text="close", on_press=lambda x:self.dia.dismiss()), button])
        
        self.dia.open()
        
    @mainthread
    def close_dialog(self):
        
        
        self.dialog.dismiss()

    @mainthread
    def close_normal(self):
        self.dia.dismiss()
    

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
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        
    def thread_delete_user(self, obj):
        self.show_thread_dialog(titler='Deleting Account', notice="Please wait...")

        
        # self.delete_thread = threading.Thread(target=self.delete_user)
        # self.delete_thread.start()
        
        

    
    def delete_user(self):
        
        

        try:
            func_timeout(120, self.delete_account)
            self.has_deleted = True
        except FunctionTimedOut:
            
            self.toast("Failed to delete account timedout")
            self.denied = 0
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            
            
            if error == 'Permission denied':
                
                
                self.denied += 1
                if self.denied < 2:
                    try:
                        func_timeout(10, self.denied_signin)

                        self.delete_user_auth()
                    except FunctionTimedOut:
                        
                        self.toast("Failed to delete account timedout")
                        self.denied = 0
                    except:
                        
                        self.toast("Failed to delete account")
                        self.denied = 0
                        
                else:
                    self.close_dialog()
                    self.show_dialog('All permissions have been denied for deleting your account right now. Please wait until slots are open. Else Contact us and make a request to delete your account in the Contact Page providing us with your account details.')
                    
                    self.denied = 0
            try:
                if error['message'] == 'Not found.':
                    self.toast("Not found")
                elif error['message'] == 'CREDENTIAL_TOO_OLD_LOGIN_AGAIN':
                    try:
                        func_timeout(10, self.denied_signin)

                        self.thread_delete_user(None)
                    except FunctionTimedOut:
                        self.close_dialog()
                        
                        self.toast("Failed to delete account timedout")
                        self.denied = 0
                    except:
                        self.close_dialog()
                        
                        self.toast("Failed to delete account")
                        self.denied = 0
            except:
                pass
            
        except:
            
            self.toast("Failed to delete account")
            self.denied = 0
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
            
        
        if dati['email'] and dati['password'] != "":
            # try:
            
            if self.dialog_entry.ids.passy.text == dati['password']:   
                message = MIMEText(dati['email'] + " " + "with localid" + " " + dati['localid'] + " " + "Just deleted their account")
                message['Subject'] = "Deleted account Notice"
                message["From"] = "hometernetmanager@gmail.com"
                message["To"] = "hometernetmanager@gmail.com"
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("hometernetmanager@gmail.com", "lhgajriuhglozfyd")
                server.sendmail("hometernetmanager@gmail.com", "hometernetmanager@gmail.com", message.as_string())
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
                        
                        
                        
                
                
                db.child("People").child(dati['localid']).remove(dati['idToken'])
                            
                
                

                        

                #         dudo = q.val()['prop_keys']
                #         db.child("Rent").child(dudo).remove(dati['idToken'])

                #         local = dati['localId'] + '/'                    
                #         storage.delete(local + i, dati['idToken'])
                
                # storage.delete(dati['localId'], dati['idToken'])
                    
                
                
                authi.delete_user_account(dati['idToken'])
                
                
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
                
                self.close_dialog()
                self.snackbar('Successfully deleted account')
                
                self.clear_all()
                self.denied = 0
                # self.dialog.ids.passy = ''
            else:
                
                self.close_dialog()
                text = "Invalid password"
                
                self.show_dialog(text)
    
        else:
            p = 'No user signed in'
            self.snackbar(p)

    
        
    
        
        
        
        
           
       
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
    
        
    #     with open(f'{path}/user.json', 'r') as jsonfile:
    #         self.curr = json.load(jsonfile)
        
        

    
    #     # if a.key() == 'local_image':
    
    #     #     curr['house_images'].append(a.val())

    #     #     with open(f'{path}/user.json', 'w') as jsonfile:
    #     #         json.dump(curr, jsonfile)
        
    
    

    
        
    #     if self.curr['email'] != '':
    #         if self.curr["sold"][self.curr['email']] > self.last_sold:
    
    #             self.testichiro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
    #             # self.testiroro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
    #             self.last_sold = self.curr["sold"][self.curr['email']]
    

    #             if self.testichiro.each():
            
    #                 for q in self.testichiro.each():
    #                     self.dude = q.val()['prop_keys']
    
    #                     if self.dude not in self.loader:
    #                         self.yours = db.child("Sale").order_by_key().equal_to(self.dude).get()
    #                         self.ours = db.child("Rent").order_by_key().equal_to(self.dude).get()
    #                         self.next_after(self.yours, self.ours)
    #                     else:
    
                            
    #             # if self.testiroro.each():
            
    #             #     for d in self.testiroro.each():    
    #             #         self.bruv = d.val()['prop_keys']
    #             #         if self.bruv not in self.loader:
    #             #             self.ours = db.child("Rent").order_by_key().equal_to(self.bruv).get()
    #             #             self.next_after(self.ours)
    #             #         else:
    
    
        
        
    

    # @mainthread
    # def next_after(self, yours, ours):
    
        
    #     if yours:
    #         for u in yours:
    #                     # another = person.val()
                        
            
            
            
                
    
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
    
    #             self.loader.append(u.key())
            
    
    
            
    
                    
    
                

    #     if ours:
    #         for u in ours:
                
    
                
                
                
                
    
                
                    
    
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
    
    
    
                    
        
                        

    # def reload(self):
    #     # self.loader.remove(key)
        
        
    
    
        
    #     self.loader.clear()
    #     self.last_sold = 0
    
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
    
        
        # p = PropertyCardsLayout()
        # p.reload()
        # rd = Reload()
        # rd.setPos()

#         # self.root.ids.layout.reload()
#         self.overscroll = 0
#        
#         self.homesser.added()
#         self.homesser.something = True


class Scroller(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_scroll_x = False
        self.do_scroll_y = True
        # self.effect = Effect
        # self.effect_cls = Effect
        
        
        


class HomeCardsLayout(MDGridLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.j = 0
        self.last = ''
        self.something = ''
        self.rent_something = ''
        self.counter = 0
        self.rent_found = False
        self.sale_found = False
        self.not_loaded = False
        self.not_rent_loaded = False
        self.full = False
        self.full_rent = False
        self.has_error = False

        self.spin = MDSpinner()
        self.spin.size_hint = [None, None]
        self.spin.height = '30dp'
        self.spin.width = '30dp'
        self.spin.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.spin.active = True
        self.add_widget(self.spin)

        self.event=Event()
        self.starter = True
        sale_or_rent = ["Sale", "Rent"]
        self.op_choice = random.choice(sale_or_rent)
        if self.op_choice == 'Sale':
            self.thread_added()
        else:
            self.thread_rent_added()
        self.loaded = False
        self.rent_loaded = False

    @mainthread
    def connection(self):
        self.bxopo = MDBoxLayout()
        self.bxopo.orientation = 'vertical'
        
        self.bxopo.size_hint_y=None
        self.bxopo.adaptive_height = True
        self.bxopo.spacing = "20dp"
        
        self.err = MDLabel()
        self.err.text='Network Error'
        self.err.font_size="16dp"
        self.err.halign="center"
        self.err.size_hint=[None, None]
        self.err.adaptive_size=True
        self.err.pos_hint = {'center_y':0.5, 'center_x':0.5}
        self.err.halign='center'
        self.err.color="gray"
        
           
        self.ico_err = MDIcon()
        self.ico_err.icon='cloud'
        self.ico_err.font_size="70dp"
        self.ico_err.size_hint=[None, None]
        self.ico_err.adaptive_size=True
        self.ico_err.pos_hint = {'center_y':0.6, 'center_x': 0.5}
        self.ico_err.color="gray"
        self.bxopo.add_widget(self.ico_err)
        self.bxopo.add_widget(self.err)

        self.add_widget(self.bxopo)
        self.has_error = True
    def thread_added(self):
        self.event=Event()
        self.thread_adding = threading.Thread(target=self.timing_added)
        self.thread_adding.start()
        

    def thread_other(self):
        self.event=Event()
        self.threa = threading.Thread(target=self.other).start()

    
    def timing_added(self):
        if self.has_error:
            self.remove_err()
            self.has_error = False
        # if not self.event.is_set():
        try:
            func_timeout(20, self.added)
        except FunctionTimedOut:
            self.connection()
            self.not_loaded = True
            # self.toast("Internet connection limited or unavailable")
            
        except:
            self.connection()
            self.not_loaded = True
            # self.toast("Network Error")

        self.starter = False
        
        self.remove()
            
    @mainthread
    def remove(self):
        
        self.remove_widget(self.spin)

    @mainthread
    def toast(self, text):
        toast(text)
    @mainthread
    def remove_err(self):
        self.remove_widget(self.bxopo)


    def thread_rent_added(self):
        self.event=Event()
        self.thread_adding = threading.Thread(target=self.rent_timing_added)
        self.thread_adding.start()

    def rent_timing_added(self):
        if self.has_error:
            self.remove_err()
            self.has_error = False
        try:
            func_timeout(20, self.rent_added)
        except FunctionTimedOut:
            self.not_rent_loaded = True
            self.connection()
            # self.toast("Internet connection limited or unavailable")
            
        except:
            self.connection()
            self.not_rent_loaded = True
            # self.toast("Network Error")
        self.starter = False
        
        self.remove()

    def rent_added(self):
        bath_or_bed = ['bedrooms', 'bathrooms', 'price', 'country', 'views', 'state', 'town', 'street', 'housetype']
        self.first_choice = random.choice(bath_or_bed)
        
        
       
        
        if self.first_choice == 'bedrooms':
            
            self.peopler = db.child("Rent").order_by_child('bedrooms').limit_to_first(8).get()

        elif self.first_choice == 'bathrooms':
            
            self.peopler = db.child("Rent").order_by_child('bathrooms').limit_to_first(8).get()

        elif self.first_choice == 'price':
            
            self.peopler = db.child("Rent").order_by_child('price').limit_to_first(8).get()

        elif self.first_choice == 'country':
            
            self.peopler = db.child("Rent").order_by_child('country').limit_to_first(8).get()

        elif self.first_choice == 'views':
            
            self.peopler = db.child("Rent").order_by_child('views').limit_to_first(8).get()

        elif self.first_choice == 'state':
            
            self.peopler = db.child("Rent").order_by_child('state').limit_to_first(8).get()

        elif self.first_choice == 'town':
            
            self.peopler = db.child("Rent").order_by_child('town').limit_to_first(8).get()

        elif self.first_choice == 'street':
            
            self.peopler = db.child("Rent").order_by_child('street').limit_to_first(8).get()

        elif self.first_choice == 'housetype':
            
            self.peopler = db.child("Rent").order_by_child('housetype').limit_to_first(8).get()

        # self.peopler = db.child("Rent").order_by_key().limit_to_last(6).get()
        if self.peopler.each():
            # if len(self.people.each()) < 1:
            #     self.thread_added()
            self.rent_found = True
            # else:
            Clock.schedule_once(partial(self.rent_done), 0.3)
            
            
        else:
            
            self.thread_rent_added()
        
    def added(self):
        
       
        
                
        
        bath_or_bed = ['bedrooms', 'bathrooms', 'price', 'country', 'views', 'state', 'town', 'street', 'housetype']
        self.first_choice = random.choice(bath_or_bed)
        
        

        if self.first_choice == 'bedrooms':
            
            self.people = db.child("Sale").order_by_child('bedrooms').limit_to_first(8).get()

        elif self.first_choice == 'bathrooms':
            
            self.people = db.child("Sale").order_by_child('bathrooms').limit_to_first(8).get()

        elif self.first_choice == 'price':
            
            self.people = db.child("Sale").order_by_child('price').limit_to_first(8).get()

        elif self.first_choice == 'country':
            
            self.people = db.child("Sale").order_by_child('country').limit_to_first(8).get()

        elif self.first_choice == 'views':
            
            self.people = db.child("Sale").order_by_child('views').limit_to_first(8).get()

        elif self.first_choice == 'state':
            
            self.people = db.child("Sale").order_by_child('state').limit_to_first(8).get()

        elif self.first_choice == 'town':
            
            self.people = db.child("Sale").order_by_child('town').limit_to_first(8).get()

        elif self.first_choice == 'street':
            
            self.people = db.child("Sale").order_by_child('street').limit_to_first(8).get()

        elif self.first_choice == 'housetype':
            
            self.people = db.child("Sale").order_by_child('housetype').limit_to_first(8).get()
        
        # self.people = db.child("Sale").order_by_child('price').limit_lo_last(1).get()
        if self.people.each():
            self.sale_found = True
            Clock.schedule_once(partial(self.done), 0.3)
           
            
        else:
            
            self.thread_added()
        

            
        
    @mainthread
    def done(self, time):
        self.j = 0
       
        if self.has_error:
            self.remove_err()
        if self.sale_found:
            for u in self.people.each()[self.j:self.j+4]:
                if u.key() == self.something:
                    
                    continue
                self.something = u.key()
                self.card = HomeCards()
                
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.card.opacity = 0
                Animation(opacity=1, duration=0.5).start(self.card)
                self.add_widget(self.card)
                
                self.last = u.key()
                
                self.j += 1
            self.full = True
                    
            self.loaded = True
        
        
        

        
    @mainthread
    def rent_done(self, time):
        self.j = 0
        
        if self.has_error:
            self.remove_err()
        if self.rent_found:
            for u in self.peopler.each()[self.j:self.j+4]:
                if u.key() == self.rent_something:
                    
                    continue
                self.rent_something = u.key()
                self.card = HomeCards()
                
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.card.opacity = 0
                Animation(opacity=1, duration=0.5).start(self.card)
                self.add_widget(self.card)
                
                self.last = u.key()
                
                self.j += 1
                
                    
            self.full_rent = True
            self.rent_loaded = True
        
            
                    
        

    def rent_other(self):
        if self.has_error:
            self.remove_err()
            self.has_error = False
        try:
            func_timeout(20, self.rent_omagaa)
        except FunctionTimedOut:
            self.connection()
            
            
        except:
            self.connection()
            

    def other(self):
        if self.has_error:
            self.remove_err()
            self.has_error = False
        try:
            func_timeout(20, self.omagaa)
        except FunctionTimedOut:
            self.connection()
            
            
        except:
            self.connection()
            
            
        
    @mainthread
    def clear(self):
        
        self.clear_widgets()

    def rent_omagaa(self):
        
        
        len(self.peopler.each())
        if self.rent_something == '':
            
            self.rent_added()

        else:
            
            self.temp = self.peopler
            
            if self.j >= len(self.peopler.each()):
                if self.full_rent == True:
                    self.peopler = db.child("Rent").order_by_key().limit_to_first(8).get()
                    num = len(self.peopler.each())-1
                    
                    
                    self.rent_something = self.peopler.each()[num].key()
                    self.full_rent = False
                self.peopler = db.child("Rent").order_by_key().start_at(self.rent_something).limit_to_first(8).get()
                
                    
                
                    
                if len(self.peopler.each()) >= 2:
                    self.clear()
                    self.j = 0
                else:
                    self.peopler = self.temp

            
            
           
            time.sleep(1)
            Clock.schedule_once(partial(self.rent_another), 0.5)

    def omagaa(self):
        
        
        
        if self.something == '':
            
            self.added()

        else:
            
            self.n_temp = self.people
            
            if self.j >= len(self.people.each()):
                if self.full == True:
                    self.people = db.child("Sale").order_by_key().limit_to_first(8).get()
                    num = len(self.people.each())-1
                    self.something = self.people.each()[num].key()
                    
                    self.full = False
                self.people = db.child("Sale").order_by_key().start_at(self.something).limit_to_first(8).get()
                
                    
                
                    
                if len(self.people.each()) >= 2:
                    self.clear()
                    self.j = 0
                else:
                    self.people = self.n_temp
            
           
            time.sleep(1)
            Clock.schedule_once(partial(self.another), 0.5)
                    
            

    @mainthread
    def rent_another(self, time):
        if self.peopler.each():
            for u in self.peopler.each()[self.j:self.j+4]:
                
                
                    
                if u.key() == self.rent_something:
                    
                    continue
                
                self.card = HomeCards()
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.card.opacity = 0
                Animation(opacity=1, duration=1).start(self.card)
                self.add_widget(self.card)
                
                self.last = u.key()
                self.rent_something = u.key()
                self.j += 1
                if self.j == 8:
                    self.full_rent = True
                    break
                 
                
    @mainthread
    def another(self, time):    
            
        
        if self.people.each():
            for u in self.people.each()[self.j:self.j+4]:
                
                
                    
                if u.key() == self.something:
                    continue
                
                self.card = HomeCards()
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.card.opacity = 0
                Animation(opacity=1, duration=1).start(self.card)
                self.add_widget(self.card)
                
                self.last = u.key()
                self.something = u.key()
                self.j += 1
                if self.j == 8:
                    self.full = True
                    break
                
            
        
        
        
        
    
        
    


        


            


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
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        if self.curr['email'] != '':
            self.curr['bookmarks'][self.curr['email']].clear()


            with open(f'{path}/user.json', 'w') as jsonfile:
                json.dump(self.curr, jsonfile)
            
            self.clear_widgets()
            self.snackbar("Bookmarks cleared successfully")
        else:
            self.snackbar("You're not signed in")
        
        
    
    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="5dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y=None)
        self.snack.open()

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


class List_item(OneLineListItem):
    method = StringProperty()



class Recycle(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'text': 'x'} for x in range(1)]

class Listings(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.counter = 0
        Clock.schedule_interval(self.start, 0.3)
        
        
    def start(self, time):
        
        if self.counter < 50:
            countries = pycountry.countries
        
            for i in countries:
                list_item = List_item()
                
                list_item.text = i.name
                list_item.opacity = 0
                Animation(opacity=1, duration=0.1).start(list_item)
                self.add_widget(list_item)
                self.counter +=1
                
                

# princekofasiedu



class AccountItem(OneLineListItem):
    pass

class UpdateScreen(Screen):
    pass
                    



        

class MainApp(MDApp):
    def build(self):

        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        self.wm.transition = NoTransition()

        self.kill = False
        self.has_error = False
        self.loader = []
        self.last_sold = 0
        self.has_pressed = False
        self.has_entered = False

        self.last_rec = 0
        self.loaded = []
        self.counter = 0
        self.prod_err = False
        self.bk_err = False
        # self.has_home = False
        self.has_account = False
        
        
        self.has_tut = False
        self.has_create = False
        self.has_code = False
        self.has_contact = False
        self.has_congrats = False
        self.has_creator = False

        self.signup = AccountLoginPage(name="sign-up")
        self.signin = SignInScreen(name="signin")
        self.home = HomeScreen(name="Home")
        self.update = UpdateScreen(name="update")
        self.loading = LoadingScreen(name="loading")
      
        self.splash()
        
        
       
        
        
        
        
        
        self.products = MyProducts(name="products")
        self.bk = BookmarkScreen(name='bookmarks')
        
        self.SaleOrRent = SaleOrRent(name="SaleOrRent")
        
        
        
        
        
        
        self.about = AboutScreen(name="about")
        
        self.detail = DetailsScreen(name="details")
        
        
        self.search = SearchScreen(name="search")
        
        
        
        
        
   
        self.denied_image = 0
        self.prev_code = ''

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
            
            ver_growth='down',
            width_mult=3
        )

        

        for i in choice_items:
            self.choice.items.append(i)
        
        
        
            
        self.close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)


        
        
        
        


        

        

        self.sale_or_rent = ''
        
        self.mail = ''
        self.passwrd = ''
        self.confirmed = ''
        self.sign_in_mail = ''
        self.sign_in_pass = ''
        

        self.link = ''
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
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        self.twitter = ''
        self.facebook = ''
        return self.wm
        
    
    
    
    def switch_choice(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        self.account_choosing = AccountChoice()
        

        self.account_choose = MDDialog(
            title='Accounts',
            type='custom',
            content_cls=self.account_choosing,

        )

        
        self.account_choose.open()
        
        
        for i in self.curr['accounts']:
            
            if self.curr['email'] == i['email']:
                continue
            self.account_item = AccountItem()
            self.account_item.text = i['email']
            self.account_item.divider = None
            self.account_choosing.ids.account_listings.add_widget(self.account_item)

        self.add_account = OneLineIconListItem(on_press=lambda x:self.close_account_choose(), on_release=lambda x:self.first_time_signin())
        self.add_account.text = '[size=16dp]Add another account[/size]'

        self.add_account.divider = None
        self.ico_left = IconLeftWidget()
        self.ico_left.icon = 'plus'
        self.ico_left.icon_size = '20dp'
        self.add_account.add_widget(self.ico_left)
        self.account_choosing.ids.account_listings.add_widget(self.add_account)
        
    def close_account_choose(self):
        sound.play()
        self.account_choose.dismiss()
        

    def switch(self, email):
        
        
        self.loading.ids.spin.active=True
        self.switch_loading()
        self.event = Event()
        self.thread_now = threading.Thread(target=self.switch_now, args=(email,))
        self.thread_now.start()

    def switch_now(self, email):
        
        

        if not self.event.is_set():
            
            
            for i in self.curr['accounts']:
                if i['email'] == email:
                    password = i['password']
                    

            try:
                func_timeout(100, self.switch_account, args=(email, password,))
                time.sleep(1)
                if not self.event.is_set():
                    
                    self.switch_products()
                
                
                
            except FunctionTimedOut:
                
                self.toast("Internet connection limited or unavailable")
                self.event.set()
                time.sleep(1)
                self.true_switch_products()
                self.spin_false()
            
        
            except:
                
                self.toast("Failed to switch account")
                
                self.event.set()
                time.sleep(1)
                self.true_switch_products()
                self.spin_false()


    def switch_account(self, email, password):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        
        
        
        count = 0
        self.user = authi.sign_in_with_email_and_password(email, password)

        if self.curr['sold'][email] == 0:
            self.testichiro = db.child("People").child(self.user['localId']).child("ids").get(self.user['idToken'])
            
            
            if self.testichiro.each():
                for i in self.testichiro.each():
                    count += 1

            self.curr['sold'][email] = count

        time.sleep(1)
        if not self.event.is_set():
            ino = authi.get_account_info(self.user['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                authi.send_email_verification(self.user['idToken'])
                time.sleep(1)
                if not self.event.is_set():
                    text = "An email verification link has been sent to your mail"
                    
                    self.show_dialog(text)
            
            time.sleep(1)
            if not self.event.is_set():
                self.curr['email'] = email
                self.curr['password'] = password
                self.curr['idToken'] = self.user['idToken']
                self.curr['localid'] = self.user['localId']

                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                self.snackbar('Successfully signed in loading properties')
                
                self.loader.clear()
                self.last_sold = 0
                self.clear_products()
        


    def reload_products(self):
        self.loading.ids.spin.active = True
        self.switch_loading()
        

        self.loader.clear()
        self.last_sold = 0
        self.products.ids.layout.clear_widgets()
        if self.prod_err == True:
            self.remove_prod_err()
            self.prod_err = False
        self.begin_loading()
        # time.sleep(5)
        # self.true_switch_products()

    def begin_loading(self):
        
       
        self.event = Event()
        self.th = threading.Thread(target=self.begin_now)
        self.th.start()
        

    def begin_now(self):
        
        
        
        
        
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            
            try:
                func_timeout(100, self.added)
                time.sleep(1)
                self.true_switch_products()
            except FunctionTimedOut:
                
                
                self.last_sold = self.curr["sold"][self.curr['email']]
                self.event.set()
                time.sleep(1)
                self.empty_prod('Failed to load properties', icon='cloud')
                self.true_switch_products()
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                
                
                if error == 'Permission denied':
                    
                    
                    
                    # try:
                    try:
                        func_timeout(10, self.denied_signin)
                        time.sleep(1)
                        self.switch_products()
                    except FunctionTimedOut:
                        
                        self.empty_prod('Failed to load properties', icon='cloud')
                        self.event.set()
                        self.last_sold = self.curr["sold"][self.curr['email']]
                        time.sleep(1)
                        self.true_switch_products()
                        
                    except:
                        
                        self.empty_prod('Failed to load properties', icon='cloud')
                        self.event.set()
                        self.last_sold = self.curr["sold"][self.curr['email']]
                        time.sleep(1)
                        self.true_switch_products()
                        
                    
            except:
                
                self.empty_prod('Failed to load properties', icon='cloud')
                self.last_sold = self.curr["sold"][self.curr['email']]
                self.event.set()
                time.sleep(1)
                self.true_switch_products()
            
            
    @mainthread
    def empty_prod(self, text, color='black', icon='cloud-outline'):
        self.bxopi = MDBoxLayout()
        self.bxopi.orientation = 'vertical'
        self.bxopi.pos_hint = {'center_x': 0.5, 'center_y':0.5}
        self.bxopi.size_hint_y=None
        self.bxopi.adaptive_height = True
        self.bxopi.spacing = "20dp"
        
        self.err_prod = MDLabel()
        self.err_prod.text=text
        self.err_prod.font_size="16dp"
        self.err_prod.halign="center"
        self.err_prod.size_hint=[None, None]
        self.err_prod.adaptive_size=True
        self.err_prod.pos_hint = {'center_y':0.5, 'center_x':0.5}
        self.err_prod.halign='center'
        self.err_prod.color = color
        
        self.ico_err_prod = MDIcon()
        self.ico_err_prod.icon=icon
        self.ico_err_prod.font_size="70dp"
        self.ico_err_prod.size_hint=[None, None]
        self.ico_err_prod.adaptive_size=True
        self.ico_err_prod.pos_hint = {'center_y':0.6, 'center_x': 0.5}
        self.ico_err_prod.color=color
        self.bxopi.add_widget(self.ico_err_prod)
        self.bxopi.add_widget(self.err_prod)
        
        self.products.ids.relay.add_widget(self.bxopi)
        self.prod_err = True
        

    @mainthread
    def true_switch_products(self):
        self.sign_in_current = 'products'
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
        if self.prod_err == True:
            
            self.remove_prod_err()
            self.prod_err = False
        self.begin_loading()
        
       
    @mainthread
    def remove_prod_err(self):
        self.products.ids.relay.remove_widget(self.bxopi)  



    def added(self):
        
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        
        

        
        
        
        
        

        
        
        if self.curr['email'] != '':
            if self.curr["sold"][self.curr['email']] > self.last_sold:
                
                self.testichiro = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                self.last_sold = self.curr["sold"][self.curr['email']]
                

                if self.testichiro.each():
                    
                    for q in self.testichiro.each():
                        self.dude = q.val()['prop_keys']
                        
                        if self.dude not in self.loader:
                            self.yours = db.child("Sale").order_by_key().equal_to(self.dude).get()
                            
                                
                            self.ours = db.child("Rent").order_by_key().equal_to(self.dude).get()
                            
                            self.next_after(self.yours, self.ours)
                else:
                    self.curr["sold"][self.curr['email']] = 0
                    with open(f'{path}/user.json', 'r') as jsonfile:
                        json.dump(self.curr, jsonfile)

            if self.curr["sold"][self.curr['email']] == 0:
                self.empty_prod("You have no properties yet")
                      
        else:
            self.empty_prod("You're not signed in")
               
        
        
                
                
                
        
        
    

    @mainthread
    def next_after(self, yours, ours):
        
        if self.prod_err == True:
            self.remove_prod_err()
            self.prod_err = False
        if yours:
            for u in yours:

                        
            
            
            
                
                
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
                
                self.loader.append(u.key())
            
            
            
        
                    
                        
                

        if ours:
            for u in ours:
                
               
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
                
                
    @mainthread
    def empty_bk(self, text, icon='bookmark-outline'):
        
        self.bxopu = MDBoxLayout()
        self.bxopu.orientation = 'vertical'
        self.bxopu.pos_hint = {'center_x': 0.5, 'center_y':0.5}
        self.bxopu.size_hint_y=None
        self.bxopu.adaptive_height = True
        self.bxopu.spacing = "20dp"
        
        self.err_bk = MDLabel()
        self.err_bk.text=text
        self.err_bk.font_size="16dp"
        self.err_bk.halign="center"
        self.err_bk.size_hint=[None, None]
        self.err_bk.adaptive_size=True
        self.err_bk.pos_hint = {'center_y':0.5, 'center_x':0.5}
        self.err_bk.halign='center'
      
        
        self.ico_err_bk = MDIcon()
        self.ico_err_bk.icon=icon
        self.ico_err_bk.font_size="70dp"
        self.ico_err_bk.size_hint=[None, None]
        self.ico_err_bk.adaptive_size=True
        self.ico_err_bk.pos_hint = {'center_y':0.6, 'center_x': 0.5}
 
        self.bxopu.add_widget(self.ico_err_bk)
        self.bxopu.add_widget(self.err_bk)
        
        self.bk.ids.relayer.add_widget(self.bxopu)
        self.bk_err = True
        
    @mainthread
    def true_switch_bookmarks(self):
        self.wm.transition=NoTransition()
        if self.products.ids.layout.has_deleted == True:
            self.clear_bk()
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
                
                func_timeout(100, self.starto_bookmarks)
            except FunctionTimedOut:
                
                
                self.event.set()
                self.empty_bk('Internet connection limited or unavailable', icon='cloud')
        
            except:
       
                self.empty_bk('Internet connection limited or unavailable', icon='cloud')
                self.event.set()

            time.sleep(1)
            self.true_switch_bookmarks()

    def starto_bookmarks(self):
        
        
        
        if self.curr['email'] != '':
            if len(self.curr['bookmarks'][self.curr['email']]) > 0:

                
                for i in self.curr['bookmarks'][self.curr['email']]:
                    if not self.event.is_set():
                        
                        if i not in self.loaded:
                            
                            
                            self.yours = db.child("Sale").order_by_key().equal_to(i).get()
                            self.mine = db.child("Rent").order_by_key().equal_to(i).get()
                            self.starti_bookmarks(self.yours, self.mine)  
                    else:
                        
                        break
            

            time.sleep(1)
            if not self.event.is_set():
                for b in self.curr['bookmarks'][self.curr['email']]:
                    if b not in self.loaded:
                        
                        
                        self.curr['bookmarks'][self.curr['email']].remove(b)
                        self.toast("Some Properties may have been sold.")
                        
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile) 

                    
        else:
            self.empty_bk("You're not signed in")
                

                

            
        
    @mainthread
    def starti_bookmarks(self, yours, mine):
        if self.bk_err == True:
            self.bk.ids.relayer.remove_widget(self.bxopu)
            self.bk_err = False
            
        if yours:
            for u in yours:
                
                
                self.card = HomeCards()
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.bk.ids.bk.add_widget(self.card)
                self.loaded.append(u.key())
                
                
                            
                    
            
            
                
            
    
        if mine:   
            for u in mine:
                
                
                self.card = HomeCards()
                self.card.me = self.card
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
                self.card.link = u.val()['link']
                self.bk.ids.bk.add_widget(self.card)
                self.loaded.append(u.key())
                
        

        
    def reload_bookmarks(self):
        self.loading.ids.spin.active = True
        self.wm.switch_to(self.loading)
       
        
        self.loaded.clear()
        if self.bk_err == True:
            self.bk.ids.relayer.remove_widget(self.bxopu)
            self.bk_err = False
        
        self.bk.ids.bk.clear_widgets()
        self.begin_thread_bookmarks()

    def clear_bk(self):
        self.bk.ids.bk.clear_widgets()
        
        self.products.ids.layout.has_deleted = False
        

    def thread_reload_sale(self, which, one=None):
        self.spin = MDSpinner()
        self.spin.size_hint = [None, None]
        self.spin.height = '30dp'
        self.spin.width = '30dp'
        self.spin.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.spin.active = True
        
        
        self.home.ids.sale_arrow.disabled = True
        self.home.ids.refresh_sale.disabled = True
        self.has_pressed = True
        if which == 'reload':
            
            
            self.home.ids.grid.clear_widgets()
            
            
            
            
            self.home.ids.grid.add_widget(self.spin)
            
            if one == "change":
                
                self.event = Event()
                self.thread_reload = threading.Thread(target=self.reload_sale)
                self.thread_reload.start()
                
            else:
                
                # preload sale here
                if self.home.ids.grid.op_choice == "Sale":
                    self.home.ids.grid.loaded = False
                    self.event = Event()
                    self.thread_reload = threading.Thread(target=self.reload_sale)
                    self.thread_reload.start()
                else:
                    
                    self.home.ids.grid.rent_loaded = False
                    self.event = Event()
                    self.thread_reload = threading.Thread(target=self.new_rent)
                    self.thread_reload.start()

        elif which == 'more':   
            if self.home.ids.grid.has_error == True:
                self.home.ids.grid.remove_err()
                self.home.ids.grid.has_error = False

            
            self.home.ids.grid.add_widget(self.spin)
            
           
            
            if self.home.ids.grid.op_choice == "Sale":
                self.event = Event()
                self.thread_reload = threading.Thread(target=self.more_sale)
                self.thread_reload.start()
            else:
                self.event = Event()
                self.thread_reload = threading.Thread(target=self.more_rent)
                self.thread_reload.start()
            
    
    



    def thread_reload_rent(self, which, one=None):
        self.spin = MDSpinner()
        self.spin.size_hint = [None, None]
        self.spin.height = '30dp'
        self.spin.width = '30dp'
        self.spin.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.spin.active = True
        
        
        self.home.ids.sale_arrow.disabled = True
        self.home.ids.refresh_sale.disabled = True
        self.has_pressed = True
        if which == 'reload':
            
            
            self.home.ids.grid.clear_widgets()
            # self.home.ids.scroller.do_scroll_y = True
            
            if self.home.ids.grid.has_error == True:
                self.home.ids.grid.remove_err()
                self.home.ids.grid.has_error = False
            
            
            self.home.ids.grid.add_widget(self.spin)
            
            if one == "change":
                
                
                self.event = Event()
                self.thread_reload = threading.Thread(target=self.new_rent)
                self.thread_reload.start()
                
            else:
                
                # preload sale here
                
                self.event = Event()
                self.thread_reload = threading.Thread(target=self.new_rent)
                self.thread_reload.start()




    def reload_sale(self):
        time.sleep(1)
        if self.home.ids.grid.loaded == True:
            
            Clock.schedule_once(partial(self.home.ids.grid.done), 0.1)
            self.remove_reload_spin()
        else:
            self.home.ids.grid.timing_added()
            while True:
                if self.home.ids.grid.loaded == True or self.home.ids.grid.not_loaded == True:
                    
                    self.remove_reload_spin()
                    
                    break

    def new_rent(self):
        time.sleep(1)
        if self.home.ids.grid.rent_loaded == True:
            
            Clock.schedule_once(partial(self.home.ids.grid.rent_done), 0.1)
            self.remove_reload_spin()
        else:
            
            self.home.ids.grid.rent_timing_added()
            while True:
                if self.home.ids.grid.rent_loaded == True or self.home.ids.grid.not_rent_loaded == True:
                    
                    self.remove_reload_spin()
                    # self.home.ids.grid.rent_loaded = False
                    break

    def more_sale(self):
        
        time.sleep(1)
        self.home.ids.grid.other()
        
        self.remove_reload_spin()

    
        
        
    def more_rent(self):
        
        time.sleep(1)
        self.home.ids.grid.rent_other()
        
        self.remove_reload_spin()
        
    @mainthread
    def remove_reload_spin(self):
        self.home.ids.grid.remove_widget(self.spin)
        
        self.home.ids.sale_arrow.disabled = False
        self.home.ids.refresh_sale.disabled = False
        self.has_pressed = False

    
        

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
                                    func_timeout(30, self.send_contact_message)
                                except FunctionTimedOut:
                                    
                                    self.toast("Failed to send message timedout")
                                    self.event.set()
                                except:
                                    
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
        server.login("hometernetmanager@gmail.com", "lhgajriuhglozfyd")
        server.sendmail(self.contact.ids.mail.text, "anangjosh8@gmail.com", message.as_string())
        server.quit()
        
        
        
        text = "Message sent successfully"
        self.snackbar(text)
                        





    def search_thread(self, choice, country, state, city, bedrooms, property_type):
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
        self.new_search_property = ''
        
        
        if self.has_error:
            self.search.ids.search.remove_widget(self.bxopo)
            
            self.has_error = False
            
        self.search.ids.spin.active = True
        self.search.ids.spin.opacity = 1
        
        self.search.ids.more_card.disabled = True
        self.search.ids.more_card.opacity = 0
        
        self.search.ids.refresh_card.disabled = True
        self.search.ids.refresh_card.opacity = 0
        
        
        self.event = Event()
        self.thread_search = threading.Thread(target=self.search_it, args=(choice, country, state, city, bedrooms, property_type,))
        self.thread_search.start()




    @mainthread
    def search_error(self, text, icon="cloud"):
        self.bxopo = MDBoxLayout()
        self.bxopo.orientation = 'vertical'
        
        self.bxopo.size_hint_y=None
        self.bxopo.adaptive_height = True
        self.bxopo.spacing = "20dp"
        
        self.err = MDLabel()
        self.err.text=text
        self.err.font_size="16dp"
        self.err.halign="center"
        self.err.size_hint=[None, None]
        self.err.adaptive_size=True
        self.err.pos_hint = {'center_y':0.5, 'center_x':0.5}
        self.err.halign='center'
        self.err.color="gray"
        
           
        self.ico_err = MDIcon()
        self.ico_err.icon=icon
        self.ico_err.font_size="70dp"
        self.ico_err.size_hint=[None, None]
        self.ico_err.adaptive_size=True
        self.ico_err.pos_hint = {'center_y':0.6, 'center_x': 0.5}
        self.ico_err.color="gray"
        self.bxopo.add_widget(self.ico_err)
        self.bxopo.add_widget(self.err)

        self.search.ids.search.add_widget(self.bxopo)
        
        

    def search_it(self, choice, country, state, city, bedrooms, property_type):
        
        try:
            func_timeout(140, self.search_now, args=(choice, country.title(), state.title(), city.title(), bedrooms, property_type.title(),))
            
        except FunctionTimedOut:
            
            self.search_failed()
            self.event.set()
            self.has_error = True
            
            
        except:
            
            self.search_failed()
            self.has_error = True
            
            self.event.set()
        if self.has_error:
            self.search_error("Failed")
        
        self.spin_opacity()
        self.search.ids.spin.active = False
       

    @mainthread
    def search_failed(self):
        self.search.ids.check.text = 'Search Failed'
        self.search.ids.check.opacity = 1
         
    @mainthread
    def spin_opacity(self):
        self.search.ids.spin.opacity = 0

    @mainthread
    def clear_search(self):
        self.search.ids.search.clear_widgets()

    @mainthread
    def search_spin_unseen(self):
        pass

    def search_now(self, choice, country, state, city, bedrooms, property_type):
        
        
        self.old_country = country
        self.old_choice = choice
        self.old_bedrooms = bedrooms
        self.old_state = state
        self.old_city = city
        self.old_prop = property_type
        if country != self.new_country or choice != self.new_choice or bedrooms != self.new_bedrooms or property_type != self.new_search_property:
            
            self.new_country = country
            self.new_choice = choice
            self.new_bedrooms = bedrooms
            self.old_country = self.new_country
            self.something = ''
            self.new_search_property = property_type
             
            
            self.clear_search()
        
            

        self.search_j = 0

        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            
        
        
        self.clear_search()
        
        
        if property_type == '':
            self.snackbar('Please enter a property type')
        elif country == '' and state == '' and city == '':
            self.snackbar("Please enter location details")
        elif state == '' and city == '':
            self.search_counter = 0
            self.search_begin = db.child(choice).order_by_child('country').equal_to(country.strip()).get()
            time.sleep(1)
            if not self.event.is_set():
                Clock.schedule_once(partial(self.search_added, country.strip(), state.strip(), city.strip(), bedrooms, property_type.strip()), 0.3)
                
            
                
            
                
        elif state != '' and city != '' and country == '':
            self.snackbar('Please enter a country')

        elif state != '' and city != '':
            
            self.search_counter = 0
            self.search_begin = db.child(choice).order_by_child('location').equal_to(country.strip()+state.strip()+city.strip()).get()
            
            time.sleep(1)
            if not self.event.is_set():
                Clock.schedule_once(partial(self.search_added, country.strip(), state.strip(), city.strip(), bedrooms, property_type.strip()), 0.3)
                
           
                
            
        
            
        elif state == '' and city != '':
            
            self.snackbar('Please enter a state')

        elif city == '' and state != '':
            
            self.snackbar('Please enter a city')

        
       

        

    
        

    @mainthread
    def search_added(self, country, state, city, bedrooms, property_type, time=None):
        
    
        if self.search_begin.each():
            for u in self.search_begin.each():
                
                self.search_counter += 1
                
                
                # if self.search_something == u.key():
                #     continue
                
                
                if u.val()['housetype'] == property_type:
                    if u.val()['bedrooms'] == bedrooms:
                    
                        self.card = HomeCards()
                        self.card.me = self.card
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
                        self.card.link = u.val()['link']
                        self.card.opacity = 0
                        Animation(opacity=1,duration=0.5).start(self.card)
                        self.search.ids.search.add_widget(self.card)
                        self.last = u.key()
                        self.search_something = u.key()
                        self.search_j += 1 
                        break
                   
            if self.search_j == 0:
                self.search.ids.check.text = 'Search results'
                self.search.ids.check.opacity = 1
                
                self.snackbar("Not found please check provided number of bedrooms or property type")
                self.search.ids.spin.active = False
                
                self.search_error("Nothing found", icon="cloud-outline")
                self.spin_opacity()
            else:
                self.search.ids.check.opacity = 1
                self.search.ids.check.text = 'Search results'
                self.search.ids.more_card.disabled = False
                
                anim = Animation(opacity=1, duration=1)
                anim.start(self.search.ids.more_card)

                self.search.ids.refresh_card.disabled = False
                anim = Animation(opacity=1, duration=1)
                anim.start(self.search.ids.refresh_card)
                self.search.ids.spin.active = False
                self.spin_opacity()

                
                
        else:
            
            
            self.search.ids.spin.active = False
            self.search.ids.check.opacity = 1
            self.search.ids.check.text = 'Search results'
            self.search_error("Nothing found", icon="cloud-outline")
            self.spin_opacity()
        

    def next_thread(self, bedrooms):
        self.search.ids.spin.active = True
        
        self.search.ids.refresh_card.disabled = True
        self.search.ids.more_card.disabled = True
        
        self.event = Event()
        self.thread_next = threading.Thread(target=self.next, args=(bedrooms,))
        self.thread_next.start()

    def next(self, bedrooms):
        
        
        try:
            func_timeout(30, self.next_next, args=(bedrooms,))
        except FunctionTimedOut:
            
            self.toast("Internet connection limited or unavailable")
            self.event.set()
            
        except:
            
            self.toast("Network Error")
            self.event.set()
        self.search.ids.refresh_card.disabled = False
        self.search.ids.more_card.disabled = False
        

        self.search.ids.spin.active = False
        self.spin_opacity()

    def next_next(self, bedrooms):
        
        
        
        
        if self.search_begin:
            
            if self.search_counter < len(self.search_begin.each()):
                
                if self.search_j / 10 == 1:
                    self.clear_search()
        
            
            
        if self.search_something != '':
            Clock.schedule_once(partial(self.real_next, bedrooms), 0.3)
            
            self.search.ids.spin.active = False
            
        

    @mainthread
    def real_next(self, bedrooms, time):
        
        
        if self.search_begin.each():
            for u in self.search_begin.each()[self.search_counter:self.search_counter+5]:
                
                if u.key() == self.search_something:
                    continue
                
                
                self.search_counter += 1
                
                if u.val()['housetype'] == self.old_prop.strip():
                    if u.val()['bedrooms'] == self.old_bedrooms:
                        self.card = HomeCards()
                        self.card.me = self.card
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
                        self.card.link = u.val()['link']
                        self.card.opacity = 0
                        Animation(opacity=1, duration=0.5).start(self.card)
                        self.search.ids.search.add_widget(self.card)
                        self.last = u.key()
                        self.something = u.key()
                        self.search_j += 1
                        
                        if self.search_j / 5 == 1:
                            
                            break

            
    
    def reverser_next(self):
        self.search.ids.search.clear_widgets()
        
        self.search_counter = 0
        self.search_j = 0
        if self.search_begin.each():
            for u in self.search_begin.each():
                
                
                self.search_counter += 1
                
                
                if u.val()['housetype'] == self.old_prop.strip():
                    if u.val()['bedrooms'] == self.old_bedrooms:
                        self.card = HomeCards()
                        self.card.me = self.card
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
                        self.card.link = u.val()['link']
                        self.search.ids.search.add_widget(self.card)
                        self.last = u.key()
                        self.something = u.key()
                        self.search_j += 1
                        
                        if self.search_j == 5:
                            
                            break





    @mainthread
    def switch_update(self):
        self.wm.switch_to(self.update)





    def on_start(self):
        

        

        return super().on_start()

    @mainthread
    def ent(self):
        self.has_entered = True
        

    def splash(self):
        self.switch_loading()
        first = threading.Thread(target=self.splashi)
        first.start()
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        if self.curr['up_date'] != "":
            if datetime.strptime(self.curr['up_date'], '%Y-%m-%d') <= datetime.today():
                self.curr['updated'] = "No"
                self.curr['up_date'] = ""

            with open(f'{path}/user.json', 'w') as jsonfile:
                json.dump(self.curr, jsonfile)
        
            

    def splashi(self):
        
        try:
            func_timeout(20, self.start_up)
            
        except FunctionTimedOut:
            
            self.toast("Network Error")
            if self.curr['first_time'] == "false":
                
                
                self.switch_home()
                if self.curr['email'] == "":
                    pass
                    
                else:
                    
                    try:
                        self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                        usero = authi.refresh(self.user['refreshToken'])
                        
                        self.curr['idToken'] = self.user['idToken']

                        with open(f'{path}/user.json', 'w') as jsonfile:
                            json.dump(self.curr, jsonfile)
                    except:
                        pass
            else:
                
                self.first_time_signin()
            
        except:
            if self.curr['first_time'] == "false":
                
                
                self.switch_home()
                if self.curr['email'] == "":
                    pass
                    
                else:
                    
                    try:
                        self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                        usero = authi.refresh(self.user['refreshToken'])
                        
                        self.curr['idToken'] = self.user['idToken']

                        with open(f'{path}/user.json', 'w') as jsonfile:
                            json.dump(self.curr, jsonfile)
                    except:
                        pass
                    
            else:
                
                self.first_time_signin()
            
            self.toast("Network Error")
        

    def start_up(self):
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        
        
        
        check = db.child("Update").get()
        ia=''
        for i in check.each():
            ia = i.val()['update']
        if ia == "Yes":
            if self.curr['updated'] == "Yes":
                if self.curr['first_time'] == "false":
                
                
                    self.switch_home()
                    if self.curr['email'] == "":
                        pass
                        
                    else:
                        
                        
                        self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                        usero = authi.refresh(self.user['refreshToken'])
                        
                        self.curr['idToken'] = self.user['idToken']

                        with open(f'{path}/user.json', 'w') as jsonfile:
                            json.dump(self.curr, jsonfile)
                        
                else:
                    
                    self.first_time_signin()
            else:
                self.switch_update()

        else:
            if self.curr['first_time'] == "false":
                
                
                self.switch_home()
                if self.curr['email'] == "":
                    pass
                    
                else:
                    
                    
                    self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                    usero = authi.refresh(self.user['refreshToken'])
                    
                    self.curr['idToken'] = self.user['idToken']

                    with open(f'{path}/user.json', 'w') as jsonfile:
                        json.dump(self.curr, jsonfile)
                    
            else:
                
                self.first_time_signin()
           
        

        


   


    def update_app(self):
        webbrowser.open('https://play.google.com./store')       
        self.curr['updated'] = "Yes"
        tod = datetime.today()
        new = tod + timedelta(days=30)
        string_of_time = date.strftime(new, '%Y-%m-%d')
        
        self.curr['up_date'] = string_of_time
        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)

    @mainthread
    def first_time_signin(self, direction='left'):
        self.prev_code = 'sign-in'
        self.passwrd = ''
        self.mail = ''
        self.signin.ids.email.text = ''
        self.signin.ids.password.text = ''
        self.wm.switch_to(self.signin, direction=direction)

    def hook_keyboard(self, window, key, *largs):
           
        if key == 27:
            
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
                
                self.switch_products()
            elif self.wm.current == "signin":
                self.switch_from_signin()
                
                
                
                    
            elif self.wm.current == "sign-up":
                self.discard_mail()
                self.first_time_signin()

            elif self.wm.current == "SaleOrRent":
                self.switch_products()
                
                
            elif self.wm.current == "search":
                
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
                if self.prev_code == 'sign-in':
                    self.first_time_signin()
                else:
                    self.switch_signup()
            
                
                
               
            
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
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        self.twitter = ''
        self.facebook = ''
        self.link = ''
        
    
    def discard_mail(self):
        self.passwrd = ''
        self.mail = ''

    def set_item(self, text_item):
        self.search.ids.drop_item.set_item(text_item)
        
        self.search.ids.drop_item.text = text_item
    
    def set_bed(self, text_item):
        self.search.ids.bed_item.set_item(text_item)

        self.search.ids.bed_item.text = text_item
        
        
    @mainthread
    def toast(self, info):
        toast(info)
    
    def callback_for_menu_items(self, *args):
        self.toast(args[0])

    
        
    
    def on_checkbox_active(self, checkbox, value, num):
        
        if value:
            
            
            self.amenities[num] = 'Yes'
            
        else:
            self.amenities[num] = 'No'
            
            


    def call(self, obg, icon):
        if icon == 'whatsapp':
            webbrowser.open('https://wa.me/' + obg)
        elif icon == 'email':
            
            webbrowser.open('https://mail.google.com/mail/?view=cm&fs=1&to=' + obg + '&su=SUBJECT&body=BODY')

        elif icon == 'twitter':
            
            
            
            webbrowser.open('https://twitter.com/' + obg)
        elif icon == 'facebook':
            
           
            webbrowser.open('https://m.me/' + obg)

        elif icon == 'link':
            
            webbrowser.open(obg)
    

    @mainthread
    def show_bottom(self, email, phonenumber, twitter, facebook, link):
        bottom_sheet_menu = MDListBottomSheet()

        
        datop = {
            email: "email",
            phonenumber: "whatsapp",
            
        }
        if facebook != "":
            datop[facebook] = "facebook"

        if twitter != "":
            datop[twitter] = "twitter"
        
        if link != "":
            datop[link] = "link"

        
        for item in datop.items():
            
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
        if self.has_account == False:
            self.account = MyAccount(name='acc')
            self.has_account = True
        self.wm.switch_to(self.account, direction='right')
        
        self.passwrd = ''
        self.mail = ''
        self.sign_in_current = 'acc'
        self.account.text = self.curr['email']
        

    def switch_creator(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        if not self.has_creator:

            self.creator_screen = CreatorScreen(name='creator')
            self.has_creator = True
        self.wm.switch_to(self.creator_screen, direction='right')

    def switch_contact(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        if self.has_contact == False:
            self.contact = ContactScreen(name="contact")
            self.has_contact = True
        self.contact.ids.mail.text = ''
        
        self.contact.ids.firstname.text = ''
        self.contact.ids.lastname.text = ''
        self.contact.ids.message.text = ''

        self.wm.switch_to(self.contact, direction='right')

    def switch_tutorial(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        if self.has_tut == False:
            self.tutorial = AppTutorial(name='tutor')
            self.has_tut = True
        self.wm.switch_to(self.tutorial, direction='right')

    def switch_about(self):
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.about, direction='right')

            
        

    
    def switch_from_details(self):
        if self.current_screen == "bookmarks":
            self.switch_bookmarks()
        elif self.current_screen == "search":
            self.switch_search()
        elif self.current_screen == "home":
            self.switch_home()            
        

    @mainthread
    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, phonenumber=None, twitter=None, facebook=None, description=None, key=None, amenities=None, link=None):
        self.wm.transition = CardTransition()
        self.wm.transition.duration = .1
        self.detail.ids.dude.pos_hint = {'center_y': -1}
        
        self.wm.switch_to(self.detail, direction='up')
        # self.switch_loading()
        self.sign_in_current = 'details'
        
        
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
        self.detail.link = link
        
        
    
        
        

    def switch_search(self, direction='down'):
        self.wm.transition = CardTransition()
        self.wm.transition.duration = .1
        
        self.wm.switch_to(self.search, direction=direction)
        self.current_screen = 'search'
        

    def switch_sale(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            
        
        self.denied = 0
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        self.sale = SaleSubmit(name="sale")
        self.wm.switch_to(self.sale)

    def switch_rent(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            
        
        self.denied = 0
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        self.rent = RentSubmit(name="rent")
        self.wm.switch_to(self.rent)

    @mainthread
    def switch_signup(self):
        self.passwrd = ''
        self.mail = ''
        self.signup.ids.email.text = ''
        self.signup.ids.password.text = ''
        self.signup.ids.confirm.text = ''
        self.prev_code = 'sign-up'
        self.wm.transition = SlideTransition()
        self.wm.transition.duration = .1
        self.wm.switch_to(self.signup, direction='left')

    
        
        
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
        
        if self.bk_err == True:
            self.bk.ids.relayer.remove_widget(self.bxopu)
            self.bk_err = False
        self.begin_thread_bookmarks()    
        

    @mainthread
    def switch_signin(self, direction='left'):
        
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
            self.prev_code = 'sign-in'
            self.signin.ids.email.text = ''
            self.signin.ids.password.text = ''
            self.wm.transition = SlideTransition()
            self.wm.transition.duration = .1
            self.wm.switch_to(self.signin, direction=direction)
            

    @mainthread
    def switch_from_signin(self):
        self.passwrd = ''
        self.mail = ''
        
        
        if self.sign_in_current == "products":
            self.true_switch_products()
        elif self.sign_in_current == 'acc':
            self.switch_acc()
        else:
            self.switch_home()

    @mainthread
    def switch_congrats(self):
        if not self.has_congrats:
            self.congrats = Congrats(name='congrats')
            self.has_congrats = True
        self.wm.switch_to(self.congrats)
    
    @mainthread
    def switch_code_verifyer(self, email):
        
        if self.has_code == False:
            self.code_verifyer = CodeVerifyer(name="code")
            
            self.has_code = True
        self.code_verifyer.text = email
        self.code_verifyer.ids.verify_code.text = ''
        self.wm.switch_to(self.code_verifyer)
    
    def switch_saleorrent(self):
        
        
        
        self.mail = ''
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        
        if data['email'] == "":
            
            self.first_time_signin()
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
        
        
        
        if not self.event.is_set():
            with open(f'{path}/user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
            try:
                func_timeout(30, self.boooiiii, args=(lockwood, price,))
            except FunctionTimedOut:
                
                self.toast('Internet connection limited or unavailable')
                self.event.set()
                self.denied = 0
            except:
                
                self.event.set()
                self.denied = 0
        # self.loading.ids.spin.active=False
        
        

    def play(self):
        sound.play()
        

    def boooiiii(self, figaro,price):
        
        if self.curr['email'] != '':
            if figaro in self.curr["viewed"][self.curr["email"]]:
                pass
            else:
                x = re.search(r"/mth$", price)
                y = re.search(r"/yr$", price)
                z = re.search(r"/wk", price)
                a = re.search(r"/night", price)
                if x or y or a or z:
                    
                    try:
                        
                        them14 = db.child("Rent").child(figaro).child("views").get()
                        new_val = them14.val()
                        new_val += 1
                        
                        db.child("Rent").child(figaro).update({'views': new_val}, self.curr['idToken'])
                        self.curr["viewed"][self.curr["email"]].append(figaro)
                        self.denied = 0
                    except requests.exceptions.HTTPError as e:
                        error_json = e.args[1]
                        error = json.loads(error_json)['error']
                        
                        if error == 'Permission denied':
                            
                            
                            self.denied += 1
                            if self.denied < 2:
                                try:
                                    func_timeout(10, self.denied_signin)
                                    self.call_guy(figaro,price)
                                except FunctionTimedOut:
                                    self.toast("Internet connection limited or unavailable")
                                    self.denied = 0
                                except:
                                    # self.toast("Network Error")
                                    self.denied = 0
                                    
                        
                            else:
                                
                                self.denied = 0
                                
                    
                else:
                    try:
                        them14 = db.child("Sale").child(figaro).child("views").get()
                        new_val = them14.val()
                        new_val += 1
                        
                        db.child("Sale").child(figaro).update({'views': new_val}, self.curr['idToken'])
                        self.curr["viewed"][self.curr["email"]].append(figaro)
                        
                        self.denied = 0
                    except requests.exceptions.HTTPError as e:
                        error_json = e.args[1]
                        error = json.loads(error_json)['error']
                        
                        if error == 'Permission denied':
                            
                            
                            
                            self.denied += 1
                            if self.denied < 2:
                                try:
                                    func_timeout(10, self.denied_signin)
                                    self.call_guy(figaro,price)
                                except FunctionTimedOut:
                                    self.toast("Internet connection limited or unavailable")
                                    self.denied = 0
                                except:
                                    # self.toast("Network Error")
                                    self.denied = 0
                                    
                        
                            else:
                                
                                self.deneid = 0
                    
                    #
                    # try:
                
                    
                        # except:
                        
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
       
            

    def email(self, texta):
        self.mail = texta
        
        

    def phone(self, texta):
        self.phonenumber = texta

    def linki(self, texta):
        self.link = texta

    def tg(self, texta):
        self.twitter = texta

    def fb(self, texta):
        self.facebook = texta

    def password(self, texta):
        
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
        
        self.sale.ids.flag.source = flag.flag
        self.country = texta
        

    def display(self, texta):
        
        
        if self.screeni[0] == "Sale":
            self.sale.ids.country_text.text = texta
            self.country = texta
            
        elif self.screeni[0] == "Rent":
            self.rent.ids.country_text.text = texta
            self.country = texta
            
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
        

    def baths(self, texta):
        self.bathrooms = texta 

    def description(self, texta):
        self.desc = texta

    
    
    @mainthread
    def show_dialog(self, notice, button=None, titler="Notice"):
        self.dialog = MDDialog(title=titler, text=notice, size_hint=(1, 1), buttons=[MDRaisedButton(text="close", on_release=self.close_dialog), button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    @mainthread
    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="5dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y=None)
        self.snack.open()

    def open_maps(self, location):
        webbrowser.open('https://www.google.com/maps/place/' + location)


    
    
    def show_terms(self):
        
        
        self.dia = MDDialog(
            # title='Warning!',
            type='custom',
            content_cls=Warning(),
            size_hint=[None, None],
            width= Window.size[0] / 1.5,
            
            
            buttons=[
                
                MDRaisedButton(
                    text='Agree',
                    theme_text_color='Custom',
                    on_release= lambda x:self.dia.dismiss()
                )
            ]
        )
        self.dia.open()

    def send_thread_email(self, email, phonenumber, twitter, facebook, link, type, price, country, bedrooms):
        self.detail.ids.buy.opacity = 0
        self.detail.ids.spin.active=True
        self.detail.ids.biye.disabled = True
        self.event = Event()
        self.thread_email = threading.Thread(target=self.send_email, args=(email, phonenumber, twitter, facebook, link, type, price, country, bedrooms,))
        self.thread_email.start()

    @mainthread
    def detail_spin_false(self):
        self.detail.ids.spin.active=False
        self.detail.ids.buy.opacity = 1
        self.detail.ids.biye.disabled = False

    def send_email(self, email, phonenumber, twitter, facebook, link, type, price, country, bedrooms):
        if not self.event.is_set():
            try:
                func_timeout(40, self.send_email_now, args=(email, phonenumber, twitter, facebook, link, type, price, country, bedrooms,))
            except FunctionTimedOut:
                self.toast("Network Error")
                self.event.set()
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                
                try:
                    if error['message'] == 'INVALID_ID_TOKEN':
                        try:
                            func_timeout(10, self.denied_signin)
                            self.send_thread_email(email, phonenumber, twitter, facebook, link, type, price, country, bedrooms,)
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
                self.toast("Network Error")
                self.event.set()
        self.detail_spin_false()    
            
    def send_email_now(self, email, phonenumber, twitter, facebook, link, type, price, country, bedrooms,):
        with open(f'{path}/user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            
        if data['email'] == "":
            self.first_time_signin()
        else:
            
            ino = authi.get_account_info(data['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                # authi.send_email_verification(data['idToken'])
                self.show_dialog(titler='Your email has not been verified!', notice='Please re-sign in to get the verification link.')
                
                    
                      
            else:
                
                
                
                message = MIMEText(f"Someone just viewed your contact information for \n {type} \n {country} \n{price} \n{bedrooms} bedrooms.")
                message['Subject'] = "Hometernet Offer Notice"
                message["From"] = "hometernetmanager@gmail.com"
                message["To"] = email
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("hometernetmanager@gmail.com", "lhgajriuhglozfyd")
                server.sendmail("hometernetmanager@gmail.com", email, message.as_string())
                
                message = MIMEText("An offer has been made to buy property belonging to" + " " + email + " " + phonenumber)
                server.sendmail("hometernetmanager@gmail.com", "anangjosh8@gmail.com", message.as_string())
                server.quit()
                
                self.show_bottom(email, phonenumber, twitter, facebook, link)

    
                
    def show_pre_listings(self):
        
        self.doa = MDDialog(
            title='Loading',
            text="Please wait..."
            
        )
        self.doa.open()

    def show_listings(self, scr):
        
       

        self.screeni.clear()
        self.screeni.append(scr)
        self.dia = MDDialog(
            type='custom',
            content_cls=Countries(),
            size_hint=[None, None],
            width= Window.size[0] / 1.2,
            
        )
        self.dia.open()
    
    # @mainthread
    def show_terms_create(self, email):
        mail = email
        password = self.signup.ids.password.text
        
        
        if len(mail) > 0:
            if len(password) >= 6:
                if self.signup.ids.confirm.text == password:
                    self.dia = MDDialog(
                        type='custom',
                        content_cls=Warning(),
                        
                        size_hint=[None, None],
                        width= Window.size[0] / 1.5,
                        # height=Window.size[1]
                        
                        
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
        
        # self.switch_loading()
        # self.loading.ids.spin.active=True
        
        try:
            func_timeout(10, self.validator, args=(email,))
        except FunctionTimedOut:
            self.toast("Authentication failed timedout")
            
            self.switch_signup()
            
        except:
            self.toast("Authentication failed")
            self.switch_signup() 
             


    

    def validate_behind(self, email):
        self.loading.ids.spin.active=True
        self.switch_loading()
        
        
        
        
        threading.Thread(target=self.validate_mail, args=(email,)).start()
        
        # self.validator(email)

    def validator(self, email):
        
        
        
        # while self.kill is False:
            # if self.event.is_set():
            
                
            #     self.switch_signup()
            #     break
        
        self.evaluating_email = email
        # 
        # try:
        self.validator_status = re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
        
        
        if self.validator_status:
            
            self.resend_now('sign-up')
        else:
            text = "Invalid email"
                
            self.show_dialog(text)
            time.sleep(1)
            self.switch_signup()
            self.spin_false()
        
            
                 
                

       
                
                
                
            
            
    def resend_now(self, func):
        self.loading.ids.spin.active=True
        self.switch_loading()
        self.event = Event()
        self.thread_create = threading.Thread(target=self.resend_code, args=(func,))
        self.thread_create.start()

    def resend_code(self, func):
        
        self.func = func
        if not self.event.is_set():
            try:
                func_timeout(40, self.sending_code)
            except FunctionTimedOut:
                
                self.toast("Authentication failed timedout")
                if func == 'sign-up':
                    time.sleep(1)
                    self.switch_signup()
                elif func == 'sign-in':
                    time.sleep(1)
                    self.first_time_signin()
                self.event.set()
                self.spin_false()
            except:
                self.toast("Authentication failed")
                if func == 'sign-up':
                    time.sleep(1)
                    self.switch_signup()
                elif func == 'sign-in':
                    time.sleep(1)
                    self.first_time_signin()
                
                self.event.set()
                self.spin_false()

# lhgajriuhglozfyd
# iujwzdutnqmbpkjm
    def sending_code(self):
        self.tried = 0
        self.secret_num = random.randint(100000,999999)
        
        message = MIMEText(f"Your email login code is {self.secret_num}. \n Warning do not share this code with anyone. \n You can ignore this email if you weren't authenticating an account.")
        message['Subject'] = "Your Hometernet login code is..."
        message["From"] = "hometernetmanager@gmail.com"
        message["To"] = self.evaluating_email
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("hometernetmanager@gmail.com", "lhgajriuhglozfyd")
        server.sendmail("hometernetmanager@gmail.com", self.evaluating_email, message.as_string())
        server.quit()
        time.sleep(1)
        if not self.event.is_set():
            self.switch_code_verifyer(self.evaluating_email)
            self.spin_false()
        
            


    def create_account_init(self, typed_in):
        # self.loading.ids.spin.active = True
        # self.switch_loading()
        if self.func == 'sign-up':
            self.tried += 1
            
            
            
            num = self.secret_num
            ot = self.secret_num
            
            
            if self.tried >= 6:
                
                
                self.show_dialog('Code has expired after so many attempts. Press resend now to receive a new verification code')
            else:
                if typed_in == "":
                    
                    self.snackbar("Invalid code")
                else:
                    if int(self.secret_num) == int(typed_in):
                        
                        self.loading.ids.spin.active=True
                        self.switch_loading()
                        self.event = Event()
                        self.thread_create = threading.Thread(target=self.create_account_now)
                        self.thread_create.start()
                        self.tried = 0
                    else:
                        
                        self.snackbar("Invalid code")

        elif self.func == 'sign-in':
            self.tried += 1
            
            
            
            num = self.secret_num
            ot = self.secret_num
            
            
            if self.tried >= 6:
                
                
                self.show_dialog('Code has expired after so many attempts. Press resend now to receive a new verification code')
            else:
                if typed_in == "":
                    
                    self.snackbar("Invalid code")
                else:
                    if int(self.secret_num) == int(typed_in):
                        
                        self.loading.ids.spin.active=True
                        self.switch_loading()
                        self.event = Event()
                        self.thread_create = threading.Thread(target=self.sign_in_boi)
                        self.thread_create.start()
                        self.tried = 0
                    else:
                        
                        self.snackbar("Invalid code")
    
    @mainthread
    def spin_false(self):
        self.loading.ids.spin.active = False

    def create_account_now(self):
        # self.loading.ids.labe.opacity = 0
        # self.loading.ids.spinner.active= True
       
    
        try:
            func_timeout(70, self.create_account)
        except FunctionTimedOut:
            
            self.toast("Authentication failed timedout")
            time.sleep(1)
            self.switch_signup()
            self.event.set()
            self.spin_false()
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            
            # self.toast(str(error) + "is the error")
            # self.toast("An unknown error occured")
            
            if not self.event.is_set():
                
                try:
                    
                    if error['message'] == 'EMAIL_EXISTS':
                        self.show_dialog('Email Exists')
                        
                except:
                    self.toast("An unknown error occured")
                time.sleep(1)
                self.switch_signup()
                self.spin_false()
        except:
            
            self.toast("Authentication failed")
            self.event.set()
            time.sleep(1)
            self.switch_signup()
        
            
            
        
        

    def create_account(self):
        email = self.signup.ids.email.text
        password = self.signup.ids.password.text
        count = 0
        user = authi.create_user_with_email_and_password(email, password)
        useri = authi.send_email_verification(user['idToken'])
        # self.sign_in()
        time.sleep(1)
        if not self.event.is_set():
            self.snackbar("Account created successfully.")
            text = "An email verification link has been sent to your mail. If not found in your inbox, check in spam."
        
            self.show_dialog(text)
        
        
            if self.curr['first_time'] == "true":
                self.switch_home()
                self.curr['first_time'] = "false"
            else:
                
                self.switch_home()
        else:
            if self.curr['first_time'] == "true":
                self.switch_home()
                self.curr['first_time'] = "false"
            else:
                text = "Your account was created successfully in the background. An email verification link has been sent to your mail. If not found in your inbox, check in spam."
        
                self.show_dialog(text)
                self.switch_home()

        self.clear_products()
        self.loader.clear()
        self.last_sold = 0
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

    @mainthread
    def delete_dialog(self, name, local_image, sale_or_rent):
        self.dialog_delete = MDDialog(text="Please wait...", title="Deleting Property", size_hint=(1,1), on_open=lambda x:self.delete_property_init(name, local_image, sale_or_rent))
        self.dialog_delete.open()

    @mainthread
    def close_delete_dialog(self):
        self.dialog_delete.dismiss()

    def delete_property_init(self, name, local_image, sale_or_rent):
        
        try:
            func_timeout(70, self.delete_property, args=(name, local_image, sale_or_rent,))
        except FunctionTimedOut:
            
            self.toast('Internet connection limited or unavailable')
            self.denied = 0
            self.denied_image = 0
        except:
            
            self.toast('An unknown error occured')
            self.denied = 0
            self.denied_image = 0
        
        self.close_delete_dialog()

    def delete_property(self, name, local_image, sale_or_rent):

        
        
        # self.entry = DialogEntry()
        
        
        if self.curr['email'] and self.curr['password'] == "":
            p = 'No user signed in'
            self.snackbar(p)
        else:
            
            if self.passwrd == self.curr['password']:
                
                
                # user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                try:
                    
                    
                    if sale_or_rent == 'Sale':
                        
                        
                        db.child("Sale").child(name).remove(self.curr['idToken'])
                        remove_people = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                        if remove_people.each():
                            for u in remove_people.each():
                                
                                
                                if str(u.val()['prop_keys']) == name:
                                    
                                    
                                    db.child("People").child(self.curr['localid']).child("ids").child(u.key()).remove(self.curr['idToken'])
                                    
                                    break
                        else:
                            
                            self.toast("Not found")

                    else:
                        
                        db.child("Rent").child(name).remove(self.curr['idToken'])
                        remove_people = db.child("People").child(self.curr['localid']).child("ids").get(self.curr['idToken'])
                        if remove_people.each():
                            for u in remove_people.each():
                                
                                if u.val()['prop_keys'] == name:
                                    db.child("People").child(self.curr['localid']).child("ids").child(u.key()).remove(self.curr['idToken'])
                                    
                        else:
                            
                            self.toast("Not found")

                    deletion = self.curr['localid'] + '/' + local_image
                    storage.delete(deletion, self.curr['idToken'])
                    self.curr['sold'][self.curr['email']] -= 1

                    with open(f'{path}/user.json', 'w') as jsonfile:
                        json.dump(self.curr, jsonfile)

                    p = 'Property Successfully deleted'
                    self.show_dialog(p)
                        
                    self.passwrd = ''
                    self.denied_image = 0
                    self.denied = 0
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']
                    
                    # self.toast(str(error))
                    
                    if error == 'Permission denied':
                        
                        
                        self.close_delete_dialog()
                        self.denied += 1
                        if self.denied < 2:
                            try:
                                func_timeout(10, self.denied_signin)
                                self.delete_dialog(name, local_image, sale_or_rent)
                                
                                
                            except FunctionTimedOut:
                                self.toast("Internet connection limited or unavailable")
                                
                                self.denied = 0
                                self.close_delete_dialog()
                            except:
                                self.toast("Failed to delete property")
                                
                                self.denied = 0
                                self.close_delete_dialog()

                        else:
                            
                            self.show_dialog("All permissions are denied for deleting properties right now. Please wait until the slots are open. Or you could request to delete your property on our contact page providing us with full details of the property.", titler="Permission denied")
                            self.denied = 0
                            
                            self.close_delete_dialog()
                    # if error['message']:
                    try:
                        if error['message'] == 'Not Found.':
                            self.toast("Not found")
                            
                            self.close_delete_dialog()
                        elif error['message'] == 'Permission denied.':
                            self.close_delete_dialog()
                            self.denied_image += 1
                            if self.denied_image < 2:
                                try:
                                    func_timeout(10, self.denied_signin)
                                    self.delete_dialog(name, local_image, sale_or_rent)
                                except FunctionTimedOut:
                                    self.toast("Failed to delete property image")
                                    self.denied_image = 0
                                    self.close_delete_dialog()
                                except:
                                    self.toast("Failed to delete property image")
                                    self.denied_image = 0
                                    self.close_delete_dialog()
                            else:
                                self.show_dialog("All permissions are denied for deleting property images right now. Please wait until the slots are open.")
                                # self.show_dialog("All permissions are denied for updating property images right now. Please wait until the slots are open.", titler="Permission denied")
                                self.denied_image = 0
                                self.close_delete_dialog()
                                
                            # self.denied = 0
                            
                    except:
                        pass
                        
                    #     

                
                
            else:
                text = "Invalid password"
                self.show_dialog(text)
                self.passwrd = ''
        

    def remove_user_auth(self):
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
        if self.curr['email'] != '':
            self.di = MDDialog(
                text='Are you sure you want to remove your account? This will mean signing out from this device completely.',
                
                buttons=[
                    MDRaisedButton(
                        text='Cancel',
                        
                        on_press=lambda x:self.di.dismiss()
                    ),
                    MDFlatButton(
                        text='Yes',
                        
                        on_press=self.removing_user,
                        on_release=lambda x:self.di.dismiss()
                    )
                ]
            )
            self.di.open()
        else:
            self.show_dialog("You're not signed in")

    def removing_user(self, obj):
        for i in self.curr['accounts']:
            if i['email'] == self.curr['email']:
                self.curr['accounts'].remove(i)

        del self.curr['bookmarks'][self.curr['email']]
        del self.curr['viewed'][self.curr['email']]
        del self.curr['sold'][self.curr['email']]
        self.curr['email'] = ''
        self.curr['password'] = ''
        self.curr['idToken'] = ''
        self.curr['house_images'] = []
        
        self.curr['localid'] = ''
        self.clear_products()
        self.loader.clear()
        self.last_sold = 0

        with open(f'{path}/user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)
        self.snackbar('Successfully removed account')

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
        
        
        if self.mail == '':
            text = "Please type in your email in the space"
            
            self.show_dialog(text)
        else:
            self.validator_check = re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.mail)
            if self.validator_check:
                try:
                    func_timeout(20, self.actual_forgot_password)
                except FunctionTimedOut:
                    self.toast('Internet connection limited or unavailable')
                    self.event.set()
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']['message']
                    
                    if error == 'EMAIL_NOT_FOUND':
                        text = "Email not found"
                        
                        self.show_dialog(text)
                        
                        # self.mail = ''
                    self.event.set()
                except:
                    self.toast("Failed to send link network error")
                    self.event.set()
            else:
                self.show_dialog('Invalid email')

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
        
        self.password_thread = threading.Thread(target = self.password_reset)
        self.password_thread.start()

    def password_reset(self):
        
        try:
            func_timeout(20, self.actual_password_reset)
        except FunctionTimedOut:
            self.toast('Network Error')
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                
                self.show_dialog(text)
                
                self.passwrd = ''
        except:
            self.toast("Network Error")
    
    def actual_password_reset(self):
        
        self.snackbar("Sending password reset link to your email")
        if self.passwrd == self.curr['password']:
            authi.send_password_reset_email(self.curr['email'])
            text = "A password reset email has been sent to your mail"
            
            
            self.show_dialog(text)
            self.passwrd = ''
        else:
            self.show_dialog('Invalid password')
            
            self.passwrd = ''

# "MKHRXCSZPZWXKIIF"
# "GeoWorl38751759"

    def stopit(self):
        self.threader.join()
        



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
        self.products.ids.layout.clear_widgets()
        self.bk.ids.bk.clear_widgets()
        p = 'Successfully signed out'
        self.snackbar(p)





    def sign_in(self):
        
        if self.signin.ids.email.text != '':
            if self.signin.ids.password.text != '':
                self.validator_check = re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.signin.ids.email.text)
                
                if self.validator_check:
                    self.evaluating_email = self.signin.ids.email.text
                    self.loading.ids.spin.active = True
                    self.switch_loading()
                    self.event = Event()
                    self.threader = threading.Thread(target=self.resend_now, args=('sign-in',))
                    self.threader.start()
                    
                    
                else:
                    self.show_dialog('Invalid email')
            else:
                self.show_dialog('Invalid password')
        else:
            self.show_dialog('Invalid email')
        
        # 
        # self.close_dialog()

    def sign_in_boi(self):
        # self.switch_loading()
        
        
        
        try:
            func_timeout(60, self.sign_in_now)
        except FunctionTimedOut:
            self.toast('Authentication failed timed out')
            
            time.sleep(1)
            self.first_time_signin()
            self.event.set()
            
            # self.switch_from_signin()
        except:
            self.toast('Authentication failed')
            
            time.sleep(1)
            self.first_time_signin()
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
            time.sleep(1)
            if not self.event.is_set():
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
                            if self.event.is_set():
                                break

                    # if self.testiroro.each():
                    #     for u in self.testiroro.each():
                    #         count += 1
                    time.sleep(1)
                    if not self.event.is_set():
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
                                if self.event.is_set():
                                    break
                        # if self.testiroro.each():
                        #     for u in self.testiroro.each():
                        #         count += 1
                        time.sleep(1)
                        if not self.event.is_set():
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
                                if self.event.is_set():
                                    break

                        self.curr['sold'][email] = count

            time.sleep(1)
            if not self.event.is_set():
                self.curr['email'] = email
                self.curr['password'] = password
                self.curr['idToken'] = self.user['idToken']
                self.curr['localid'] = self.user['localId']
                
                
                
                
                
                
                

                self.last_sold = 0
                self.loader.clear()
                self.clear_products()

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
            
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                
                self.first_time_signin()
                
                self.show_dialog(text)
                
                # self.text_error()
                
            if error == 'INVALID_PASSWORD':
                text = "Invalid password"
                self.first_time_signin()
                self.show_dialog(text)
                
                
                # self.text_error()
            
            if error == 'INVALID_EMAIL':
                text = "Invalid email"
                self.first_time_signin()
                self.show_dialog(text)
                
                
                # self.text_error()

            if error == "MISSING_PASSWORD":
                text = "Missing password"
                self.first_time_signin()
                self.show_dialog(text)
                
            self.spin_false()
                # self.text_error()
                
        
        #     
    # @mainthread
    # def text_error(self):
    #     self.signin.ids.email.text = ''
    #     self.signin.ids.password.text = ''
        # self.signin.ids.password.error = True
        
    
    
    def editscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        
        self.passwrd = ''
        self.mail = ''
        
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        
        
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
        self.amenities = amenities
        
        
        
        self.denied = 0
        

    # def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
    #     self.loading.ids.spin.active = True
    #     self.switch_loading()
    #     self.e = threading.Thread(target=self.editrentscreeni, args=(image, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, email, key, description, amenities,))
    #     self.e.start()

    def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        
        
        self.passwrd = ''
        self.mail = ''
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
        
        
        self.edit_rent = EditRentDetailsScreen(name="edit-rent")
        self.wm.switch_to(self.edit_rent)
        self.edit_rent.type = House_type
        self.edit_rent.image = image
        x = re.search(r"/mth$", pricing)
        y = re.search(r"/yr$", pricing)
        z = re.search(r"/wk", pricing)
        a = re.search(r"/night", pricing)
        if x or y:

            self.edit_rent.price = pricing.replace('/mth', '') if pricing.endswith('/mth') else pricing.replace('/yr', '')
        elif a or z:
            self.edit_rent.price = pricing.replace('/wk', '') if pricing.endswith('/wk') else pricing.replace('/night', '')

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
        
        self.amenities = amenities
        self.denied = 0
        
        
        self.spin_false()
        # refreshed = authi.refresh(self.user['refreshToken'])
        # self.curr['idToken'] = self.user['idToken']
    @mainthread
    def init_rent(self):
        self.edit_rent = EditRentDetailsScreen(name="edit-rent")
        # with open(f'{path}/user.json', 'w') as jsonfile:
        #     json.dump(self.curr, jsonfile)
    @mainthread
    def thread_dialog(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description, titler="Updating Property"):
        self.thread_dialogbox = MDDialog(text='Please wait...', title=titler, size_hint=(1,1), on_open=lambda x:self.thread_update_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description))
        self.thread_dialogbox.open()
        

    @mainthread
    def close_thread_dialog(self):
        self.thread_dialogbox.dismiss()
    
    

    def update_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        

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

       
    # @mainthread
    # def reloading(self, key):
        
    #     PropertyCardsLayout().reload(key)

    def thread_update_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            func_timeout(70, self.actual_sale_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
        except FunctionTimedOut:
            self.toast("Internet connection limited or unavailable")
            self.denied = 0
                        
        except:
            self.toast("Failed to update property")
            self.denied = 0

        self.close_thread_dialog()

    def actual_sale_update(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            location = locate+state.title()+town.title()
            
            
            amenities = self.amenities
            
            getting = db.child("Sale").child(key).get()
            if getting.val() == None:
                self.toast("Not found")
                
            else:
                db.child("Sale").child(key).update({'housetype': House_type.title().strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'country': locate.strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'state': state.title().strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'town': town.title().strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'street': street.title().strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'bedrooms': bedrooms}, self.curr['idToken'])
                db.child("Sale").child(key).update({'bathrooms': bathrooms}, self.curr['idToken'])
                db.child("Sale").child(key).update({'landspace': self.landspace.strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'price': self.amt.strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'description': description.capitalize().strip()}, self.curr['idToken'])
                db.child("Sale").child(key).update({'amenities': amenities}, self.curr['idToken'])
                db.child("Sale").child(key).update({'location': location.strip()}, self.curr['idToken'])
                
                
                
                self.amenities = amenities
                # self.reloading(key)
                # loaded.remove(key)
                self.sale_or_rent = "Sale"
                # self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
                
                self.denied = 0
                self.change_image_auth()
                p = 'Changes made successfully'
                self.snackbar(p)

        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            
            if error == 'Permission denied':
                
                
                self.denied += 1
                
                if self.denied < 2:
                    # try:
                    self.close_thread_dialog()
                    try:
                        func_timeout(10, self.denied_signin)
                        self.update_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description)
                        
                        # self.denied = 0
                        self.close_thread_dialog()
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        
                        self.denied = 0
                        self.close_thread_dialog()
                    except:
                        self.toast("Failed to update property")
                        
                        self.denied = 0
                        self.close_thread_dialog()
                        # try:
                        #     func_timeout(40, self.actual_sale_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
                        
                else:
                    self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.", titler="Permission denied")
                    self.denied = 0
                    
                    self.close_thread_dialog()
                
            # if error['message']:
            #     if error['message'] == 'Permission denied.':
            #         self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.")
            #         # self.denied = 0
            
    @mainthread
    def thread_rent_dialog(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        self.thread_dialogbox = MDDialog(text='Please wait...', title="Updating Property", size_hint=(1,1), on_open=lambda x:self.thread_update_rent_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description))
        self.thread_dialogbox.open()    

    @mainthread
    def close_thread_rent(self):
        self.thread_dialogbox.dismiss()

    def thread_update_rent_property(self,  local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        try:
            func_timeout(70, self.actual_rent_update, args=(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description,))
        except FunctionTimedOut:
            self.toast("Internet connection limited or unavailable")
            self.denied = 0
                        
        except:
            self.toast("Failed to update Property")
            self.denied = 0
                        

        self.close_thread_rent()
    def update_rent_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        self.key = key
        self.local_image = local_image
        
        
        with open(f'{path}/user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)

        
        
        
        
        amenities = self.amenities

        
        if pricing[0] == '$':
            self.amt = pricing + self.edit_rent.ids.pay_item.text if not pricing.endswith('/mth') or pricing.endswith('/yr') or pricing.endswith('/wk') or pricing.endswith('/night') else pricing
        else:
            self.amt = '$' + pricing + self.edit_rent.ids.pay_item.text if not pricing.endswith('/mth') or pricing.endswith('/yr') or pricing.endswith('/wk') or pricing.endswith('/night') else '$' + pricing

        if landspace[-1] == 't':
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'
        # pp = int(pricing)
        
        
        

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
                
            else:
                db.child("Rent").child(key).update({'housetype': House_type.title().strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'country': locate}, self.curr['idToken'])
                db.child("Rent").child(key).update({'state': state.title().strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'town': town.title().strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'street': street.title().strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'bedrooms': bedrooms}, self.curr['idToken'])
                db.child("Rent").child(key).update({'bathrooms': bathrooms}, self.curr['idToken'])
                db.child("Rent").child(key).update({'landspace': self.landspace.strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'price': self.amt.strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'description': description.capitalize().strip()}, self.curr['idToken'])
                db.child("Rent").child(key).update({'amenities': amenities}, self.curr['idToken'])
                db.child("Rent").child(key).update({'location': location.strip()}, self.curr['idToken'])
                self.sale_or_rent = "Rent"
                self.amenities = amenities
                self.change_image_auth()
                p = 'Changes made successfully'
                self.snackbar(p)
                self.denied = 0
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            
            if error == 'Permission denied':
                
                
                self.denied += 1
                
                if self.denied < 2:
                    # try:
                    self.close_thread_rent()
                    try:
                        func_timeout(20, self.denied_signin)
                        self.update_rent_property(local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description)
                        
                    except FunctionTimedOut:
                        self.toast("Internet connection limited or unavailable")
                        
                        self.denied = 0
                        self.close_thread_rent()
                    except:
                        self.toast("Failed to update property")
                        
                        self.denied = 0
                        self.close_thread_rent()
                        
                else:
                    self.show_dialog("All permissions are denied for updating properties right now. Please wait until the slots are open.")
                    self.denied = 0
                    
                    self.close_thread_rent()
                

    
    @mainthread
    def change_image_auth(self):
        agree_button = MDRaisedButton(text="yes", on_press=self.close_dialog, on_release=self.separate_function)
       
        info = "Do you want to change your property image?"
        self.show_dialog(info,button=agree_button)
        

    # def call_separate_function(self,obj):
    #     try:
    #         func_timeout(40, self.separate_function)
    #     except FunctionTimedOut:
    #         p = 'Failed to update Image'
    #         self.snackbar(p)
        
    def separate_function(self,obj):
        # boy = []
        
        filechooser.open_file(open = '/storage/emmc/DCIM', on_selection=self.change_image_dialog,)
        
        
        

    @mainthread
    def change_image_dialog(self, selection):
        self.dialog_image = MDDialog(text="Please wait..", title="Updating image", size_hint=(1,1), on_open=lambda x:self.change_image(selection))
        self.dialog_image.open()

    @mainthread
    def close_image_dialog(self):
        self.dialog_image.dismiss()
        
    def change_image(self, selection):
        
        if selection[0] != None:
            if len(selection) > 0:
                
                # self.switch_loading()
                try:
                    func_timeout(80, self.change_image_process, args=(selection,))
                except FunctionTimedOut:
                    self.toast("Internet connection limited or unavailable") 
                    
                    self.switch_products()
                    self.denied = 0
                    self.denied_image = 0
                except:
                    self.toast("Failed to update image")
                    self.switch_products()
                    self.denied = 0
                    self.denied_image = 0
        else:
            self.show_dialog("Please select an image from a folder or directly from your gallery.")
        self.close_image_dialog()
        
    def change_image_process(self, selection):
        
        if len(selection) > 0:
            self.new_file = str(selection[0])
            
            
            x = re.search(r".jpg$", self.new_file)
            y = re.search(r".png$", self.new_file)
            z = re.search(r".jpeg$", self.new_file)
            if x or y or z:
                # urli = storage.child(data['localid']).child(self.local_image).get_url(data['idToken'])
                # tokenop = "https://firebasestorage.googleapis.com/v0/b/first-db-77609.appspot.com/o/2C8VZdiEBCMhnFS0fnvzpa4jW2F2%2FC%3A%5CUsers%5CYvonne%5CDownloads%5Cbeautiful-house-15.jpg?alt=media"
                # storage.
                
                # user = authi.sign_in_with_email_and_password(dati['email'], dati['password'])
                try:
                    

                    # bucket = admin_storage.bucket()
                    # blob = bucket.blob(self.local_image)
                    
                    # blob.delete()
                   
                    
                    
                    
                    if self.new_file[0] == "/":
                        storage.child(self.curr['localid'] + '/' + self.new_file.replace('/', ',,')).put(str(self.new_file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.new_file.replace('/', ',,')).get_url(None)
                        
                    else:
                        storage.child(self.curr['localid'] + '/' + self.new_file).put(str(self.new_file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.new_file).get_url(None)
                        
                    self.denied_image = 0
                    if self.sale_or_rent == 'Sale':
                        self.get_local_image = db.child("Sale").child(self.edit.key).child('local_image').get()
                        
                        db.child("Sale").child(self.key).update({'local_image': self.new_file}, self.curr['idToken'])
                        db.child("Sale").child(self.key).update({'url': url}, self.curr['idToken'])
                    else:
                        db.child("Rent").child(self.key).update({'local_image': self.new_file}, self.curr['idToken'])
                        db.child("Rent").child(self.key).update({'url': url}, self.curr['idToken'])
                    storage.delete(self.curr['localid'] + '/' + self.local_image, self.curr['idToken'])
                    
                    p = 'Updated image successfully'
                    self.toast(p)
                    self.switch_products()
                
                except requests.exceptions.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']
                    
                    
                    if error == 'Permission denied':
                        
                        
                        
                        
                        try:
                            self.user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                            usero = authi.refresh(self.user['refreshToken'])
                            self.curr['idToken'] = self.user['idToken']
                            with open(f'{path}/user.json', 'w') as jsonfile:
                                json.dump(self.curr, jsonfile)

                            try:
                                func_timeout(80, self.change_image_process, args=(self.selection,))
                            except FunctionTimedOut:
                                self.toast('Failed to update image') 
                                
                            except:
                                self.toast("Failed to update image")
                                self.switch_products()

                        except:
                            self.toast('Failed to update image')
                            

                    try:
                        if error['message'] == 'Permission denied.':
                            self.close_image_dialog()
                            self.denied_image += 1
                            
                            if self.denied_image < 2:
                                try:
                                    func_timeout(10, self.denied_signin)
                                    self.change_image_dialog(selection)
                                except FunctionTimedOut:
                                    self.toast("Failed to resign in timedout")
                                    self.denied_image = 0
                                    self.close_image_dialog()
                                except:
                                    self.toast("Failed to update image")
                                    self.denied_image = 0
                                    self.close_image_dialog()
                            else:
                                self.show_dialog("All permissions are denied for updating property images right now. Please wait until the slots are open.", titler="Permission denied")
                                # self.denied = 0
                                
                                self.denied_image = 0
                                
                                self.close_image_dialog()
                    except:
                        pass
                
            else:
                
                info = 'Please select an image file'
                
                self.show_dialog(info)

        
            

    
        

    
                # text = "yes"
                # self.close_dialog(text)
                
                # notice = "No user signed in"
            # self.show_dialog(notice)
    
    

    


    
    
        

    def bookmark(self, lola, wid='p'):
        
        
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
                    
                    info = "Bookmarks full. You can only bookmark 24 properties."
                    self.show_dialog(info)
            else:
                
                self.bk.ids.bk.remove_widget(wid)
                data['bookmarks'][mail].remove(lola)
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)
                notice = 'Successfully removed from bookmarks'
                self.snackbar(notice)

            
        

    def selected(self):
        self.denied = 0
        
        
        if self.mail == self.curr['email']:
            if self.phonenumber != '':
                phone_number  = phonenumbers.parse(self.phonenumber)
                valid = phonenumbers.is_valid_number(phone_number)
                
                if valid == True:
                    if len(self.tot) > 5 and len(self.tot) < 21:
                        
                        if len(self.country) > 0:
                            
                            
                            if len(self.state) >= 3 and len(self.state) < 25:
                                if len(self.town) >= 3 and len(self.town) < 25:

                                    if len(self.street) >= 3 and len(self.street) < 25:
                                        if len(self.landspace) > 1:
                                            if len(self.price) > 1:
                                                if len(self.desc) > 20 and len(self.desc) < 255:
                                                    filechooser.open_file(open='/storage/emmc/DCIM', on_selection=self.real_house_sale)
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
        self.sale_link = self.link



        selected_image = selection
        # self.denied = 0
        
        if selected_image[0] != None:
            if len(selected_image) > 0:
                # self.switch_loading()
                
                    
                try:
                    func_timeout(120, self.house_sale, args=(selected_image,))
                except FunctionTimedOut:
                    self.toast("Internet connection limited or unavailable") 
                    
                    time.sleep(1)
                    self.true_switch_sale()
                    self.event.set()
                    self.denied = 0
                    self.denied_image = 0
                except:
                    
                    self.toast("Failed to submit property")
                    self.event.set()
                    time.sleep(1)
                    self.true_switch_sale()
                    self.denied = 0
                    self.denied_image = 0
                    
                
                #     p="No intenet connection"
                #     self.snackbar(p)
            else:
                info = "You need to select an image to continue"
                self.show_dialog(info)
                time.sleep(1)
                self.true_switch_sale()
        else:
            self.show_dialog("Please select an image directly from any folder or your gallery.")
            
            time.sleep(1)
            self.true_switch_sale()
        
        

    
    
    def house_sale(self, selection):
        
        
        # self.yet = False
        
        
        
        self.file = selection[0]

        
        
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png$", self.file)
        z = re.search(r".jpeg$", self.file)
        if x or y or z:
            
            try:
                
                
                if self.file[0] == "/":
                    
                    if not self.event.is_set():
                        storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).get_url(None)
                    
                        
                else:
                    
                    if not self.event.is_set():
                        storage.child(self.curr['localid'] + '/' + self.file).put(str(self.file), self.curr['idToken'])
                        url = storage.child(self.curr['localid'] + '/' + self.file).get_url(None)
                    
                        
                
                self.denied_image = 0
                
                # with open(f'{path}/user.json', 'r') as jsonfile:
                #     dato = json.load(jsonfile)
                
            
                
                
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
                    "location": "",
                    "link": "", 
                    "date": ""
                }

                today = datetime.today()
                string_of_time = date.strftime(today, '%Y-%m-%d')
                
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
                data['link'] = self.sale_link.strip()
                data['date'] = string_of_time
                
                
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
                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
                self.twitter = ''
                self.facebook = ''
                self.mail = ''
                self.link = ''

                
                
                key_data = {
                    "prop_keys": "",
                }
                key_data['prop_keys'] = results['name']
                db.child("People").child(self.curr['localid']).child("ids").push(key_data, self.curr['idToken'])
                
                
                
                self.curr["sold"][self.curr['email']] += 1
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                
                time.sleep(1)
                if not self.event.is_set():
                    self.switch_congrats()
                    self.show_dialog('Your property will expire in three months.')
                else:
                    self.show_dialog("Your Property was submitted in the background. Expires in three months.")
            
                self.denied = 0
            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                
                if error == 'Permission denied':
                    
                    
                    
                    self.denied += 1
                    if self.denied < 2:
                        try:
                            func_timeout(10, self.denied_signin)
                            time.sleep(1)
                            if not self.event.is_set():
                                self.real_house_sale(selection)
                            
                                
                        except FunctionTimedOut:
                            self.toast("Internet connection limited or unavailable")
                            self.denied = 0
                            self.event.set()
                            
                            time.sleep(1)
                            self.true_switch_sale()
                        except:
                            self.toast("Failed to submit property")
                            
                            self.denied = 0
                            self.event.set()
                            time.sleep(1)
                            self.true_switch_sale()
                    else:
                        self.show_dialog("All permissions are denied for selling properties right now. Please wait until the slots are open.", titler="Permission denied")
                        self.denied = 0
                        
                        time.sleep(1)
                        self.true_switch_sale()
                    
                       

                try:
                    if error['message'] == 'Permission denied.':
                        self.denied_image += 1
                        if self.denied_image < 2:
                            try:
                                func_timeout(10, self.denied_signin)
                                time.sleep(1)
                                if not self.event.is_set():
                                    self.real_house_sale(selection)
                                
                                    
                                
                            except FunctionTimedOut:
                                self.toast("Failed to update image")
                                self.denied_image = 0
                                self.event.set()
                                time.sleep(1)
                                self.true_switch_sale()
                            except:
                                self.toast("Failed to update image")
                                self.denied_image = 0
                                self.event.set()
                                time.sleep(1)
                                self.true_switch_sale()
                        else:
                            self.show_dialog("All permissions are denied for selling properties right now. Please wait until the slots are open.", titler="Permission denied")
                            # self.denied = 0
                            
                            self.denied_image = 0
                            
                            time.sleep(1)
                            self.true_switch_sale()
                except:
                    pass
                
        else:
            self.show_notice()
            time.sleep(1)
            self.true_switch_sale()
            
            
    
        
        

    
        

    def rent_property(self):
        self.denied = 0
        if self.mail == self.curr['email']:
            if self.phonenumber != '':
                phone_number  = phonenumbers.parse(self.phonenumber)
                valid = phonenumbers.is_valid_number(phone_number)
                
                if valid == True:
                    if len(self.tot) > 5 and len(self.tot) < 21:
                        
                        if len(self.country) > 0:
                            # phone = '+2332222222222'
                            
                            if len(self.state) >= 3 and len(self.state) < 25:
                                if len(self.town) >= 3 and len(self.town) < 25:

                                    if len(self.street) >= 6 and len(self.street) < 25:
                                        if len(self.landspace) > 1:
                                            if len(self.price) > 1:
                                                if len(self.desc) > 20 and len(self.desc) < 255:
                                                    filechooser.open_file(open='/storage/emmc/DCIM', on_selection=self.real_house_rent)
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
        self.rent_link = self.link

        


        
        selected_image = selection
        if selected_image[0] != None:
            if len(selected_image) > 0:
                
                # self.switch_loading()
                
                try:
                    func_timeout(120, self.house_rent, args=(selected_image,))
                except FunctionTimedOut:
                    self.toast("Internet connection limited or unavailable")
                    
                    self.event.set()
                    time.sleep(1)
                    self.true_switch_rent()
                    self.denied = 0
                    self.denied_image = 0
                except:
                    
                    self.event.set()
                    self.toast('Failed to submit property')
                    time.sleep(1)
                    self.true_switch_rent()
                    
                    
                    self.denied = 0
                    self.denied_image = 0
                
            else:
                info = "You need to select an image to continue"
                self.show_dialog(info)
                time.sleep(1)
                self.true_switch_rent()
        else:
            self.show_dialog("Please select an image from any folder or directly from your gallery")
            time.sleep(1)
            self.true_switch_rent()

    
    def house_rent(self, selection):
        
      
        
        
        self.file = selection[0]
        
        
        
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png$", self.file)
        z = re.search(r".jpeg$", self.file)
        if x or y or z:
            try:
                
                if self.file[0] == "/":
                    storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).put(str(self.file), self.curr['idToken'])
                    url = storage.child(self.curr['localid'] + '/' + self.file.replace('/', ',,')).get_url(None)
                else:
                    storage.child(self.curr['localid'] + '/' + self.file).put(str(self.file), self.curr['idToken'])
                    url = storage.child(self.curr['localid'] + '/' + self.file).get_url(None)
               
                    

            
                self.denied_image = 0
                
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
                    "location": "",
                    "link": "",
                    "date": ""
                }
                
                today = datetime.today()
                string_of_time = date.strftime(today, '%Y-%m-%d')

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
                data['link'] = self.rent_link.strip()
                data['date'] = string_of_time
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
                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No', 'No']
                self.twitter = ''
                self.facebook = ''
                self.mail = ''
                self.link = ''


                
                
                key_data = {
                    "prop_keys": "",
                }
                key_data['prop_keys'] = results['name']
                db.child("People").child(self.curr['localid']).child("ids").push(key_data, self.curr['idToken'])
                
                
                self.curr["sold"][self.curr['email']] += 1
                with open(f'{path}/user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                if not self.event.is_set():
                    self.switch_congrats()
                    self.show_dialog("Your property will expire in three months.")
                else:
                    self.show_dialog("Your Property was submitted in the background. Expires in three months.")
                self.denied = 0
            # for i in results.each():
                

            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']
                
                if error == 'Permission denied':
                    
                    
                    self.denied += 1
                    if self.denied < 2:
                        try:
                            func_timeout(10, self.denied_signin)
                            time.sleep(1)
                            if not self.event.is_set():
                                self.real_house_rent(selection)
                            
                                
                        except FunctionTimedOut:
                            self.toast("Internet connection limited or unavailable")
                            
                            self.event.set()
                            time.sleep(1)
                            self.switch_true_rent()
                            self.denied = 0
                            
                        except:
                            self.toast("Failed to submit property")
                            
                            self.event.set()
                            time.sleep(1)
                            self.switch_true_rent()
                            self.denied = 0
                    else:
                        self.show_dialog("All permissions are denied for renting properties right now. Please wait until the slots are open.", titler="Permission denied")
                        # self.denied = 0
                        
                        time.sleep(1)
                        self.switch_true_rent()
                        self.denied = 0
                

                try:
                    if error['message'] == 'Permission denied.':
                        self.denied_image += 1
                        if self.denied_image < 2:
                            try:
                                func_timeout(10, self.denied_signin)
                                time.sleep(1)
                                if not self.event.is_set():
                                    self.real_house_rent(selection)
                                
                                    
                                
                            except FunctionTimedOut:
                                self.toast("Failed to update image")
                                self.denied_image = 0
                                self.event.set()
                                time.sleep(1)
                                self.true_switch_sale()
                            except:
                                self.toast("Failed to update image")
                                self.denied_image = 0
                                self.event.set()
                                time.sleep(1)
                                self.true_switch_sale()
                        else:
                            self.show_dialog("All permissions are denied for renting properties right now. Please wait until the slots are open.", titler="Permission denied")
                            # self.denied = 0
                            
                            self.denied_image = 0
                            
                            time.sleep(1)
                            self.true_switch_rent()
                        
                except:
                    pass
                
        else:
            self.show_notice()
            time.sleep(1)
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



    

    def change_color(self):
        Animation(md_bg_color=[0,0,0,1], duration=0.3).start(self.home.ids.sale_btn)
        Animation(md_bg_color=self.theme_cls.primary_color, duration=0.3).start(self.home.ids.rent_btn)

    def change_rent_color(self):
        Animation(md_bg_color=[0,0,0,1], duration=0.3).start(self.home.ids.rent_btn)
        Animation(md_bg_color=self.theme_cls.primary_color, duration=0.3).start(self.home.ids.sale_btn)

    def regulate(self):
        self.change_color()
        self.play()
        self.home.ids.grid.op_choice="Sale"
        self.has_pressed=True
        self.home.ids.sale_arrow.disabled = True
        self.home.ids.refresh_sale.disabled = True
        self.thread_reload_sale('reload', 'change')

    def rent_regulate(self):
    
        self.change_rent_color()
        self.play()
        self.home.ids.grid.op_choice="Rent"
        self.has_pressed = True
        self.home.ids.sale_arrow.disabled = True
        self.home.ids.refresh_sale.disabled = True

        self.thread_reload_rent('reload', 'change')

    def do(self):
        pass

    def set_it_out(self):
        threading.Thread(target=self.set_it_in).start()

    def set_it_in(self):
      
        if self.detail.ids.refresh.scroll_y > 1.2:
            
            self.detail.ids.house_image.reload()
        
   
    def show_image(self):
        print(self.detail.house_image.image)

    def show_view(self):
        
        print('scroll_y: ' + str(self.home.ids.scroller.scroll_y))
    
MainApp().run()

