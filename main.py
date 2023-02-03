
import phonenumbers
import pycountry
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition, NoTransition
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

import pyrebase
import re


from kivy.clock import time
from kivy.base import EventLoop
from kivy.config import Config

from kivy.uix.textinput import TextInput

import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore, exceptions
from firebase_admin.instance_id import _get_iid_service
import sys


from firebase_admin.messaging import Message, Notification

from firebase_admin import auth

from pyfcm import FCMNotification

from plyer import filechooser
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
import smtplib
from email.mime.text import MIMEText

from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.uix.scrollview import ScrollView


from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
import webbrowser

import threading
import requests
from kivy.clock import Clock, mainthread
from func_timeout import func_timeout, FunctionTimedOut



button = MDIconButton



Config.set('kivy', 'exit_on_escape', 0)



# firebaseconfig = {
#     "apiKey": "AIzaSyA4WwgZlTp-P42AYn8OuY8GZtNDA4TsGVs",
#     "authiDomain": "dreams-home-database.firebaseapp.com",
#     "projectId": "dreams-home-database",
#     "storageBucket": "dreams-home-database.appspot.com",
#     "messagingSenderId": "831110022658",
#     "appId": "1:831110022658:web:b05635cb2c88005b40c91b",
#     "measurementId": "G-8T6YR1TNNN"
# }

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
    "project_id": "new-db-c52f3",
    "private_key_id": "85e61a29ee210543d9f7d95c04d0ca9e25d2897a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCkCh0Idi6NUmfC\n00Mup8EhZXLIMm4boxZIb71kxVumLySabUNhlvb+lCleDraxB97+y89QyNxJQFTC\n0+dodstZbqq6iwK9yMDrsnjrulPMgRfq1pkV8j/ZPHPUn6z1jaiYWG+a1DYYa+fD\nuqZBoHxCtJgPgu5UojU0xEqAOBpGBFDFye80OnDDV8f18ROh/FjDtuv7+U9PaH02\naCD45mE8nqcNAU9bX4tK8C8Y0VXxMrXVEUx2fwpw3dfu/5jDRF5Ce5uT4YkW0HSv\nOeUYWD4Uk+pO60XRA6cxd27LwE/CafeQimwwcF0fB33oaEWatHWSUjvW1oCV0/cB\nIUpxnYUrAgMBAAECggEADZ+1Z5WBKkWUzo6DPuW52Y82aEAf+vWhjSSSo0Ls6LFz\npcu7U+iY3O3rPZ+VNsDDmX/N2RTFjuPj5kZ5KqjrHKNfVJzk/mQk+a5Z8qIIAa0b\nEmr+Td9PxDgMGrWkRMSeIwD9S+uiDocvuYbP9hVhHJ0pH+is6KSMLLS8x0dhjzz8\nczZXW1HtAMl1vYzPDAe7p+WFZaV2Mej2C5uWnK47lIwajwc/ON+qx1igTgk35Ib7\nqqMk/4zyVvYaZHoe5MUeufD7/P73gs8+WM5TAXaS7M2fboUFkjGD9ZRF6S79oxJx\n1iWzAXUO8+le7jAA0nuW+Qt+e2wU1EOo7p5vF9POeQKBgQDVWDw+Qjv0Eczk3v+8\nkMYISKc4r2zehcBC7Uji3cA2klFrv5KIPWvSaX9iP4uqZkOyvRAyb6rOD+OIiIR3\nrCeaiSKYARSFiZfSyKSA8Zq9oBjj1wtghouxDNk2NitOaEHaGXUgjsJAEPKDI8Wj\nue3Y0lLA0i0Z5LQTfcESy6LPnQKBgQDE1kItONv/LR+IgPnfPCndjLzEgVN9wFZY\ndDitU4B1IO75BuR9RQqkv/sv9oCC9x14sZ9ibLRyYHyTGbL8pRqf7dma7Rson8OD\nX8F4SplcvUL/gC2W+JSM4QVXUoSNXbo0G3Ab1rrvJv6BWZdwJDOc9I8MElJg4/27\nzeffrz/hZwKBgB2s9FREqko8359GVZRJHwKv+HKuFBqvyBqHHwhPiBkPKTwvnZZN\n1N2jxxBHfonpR6lpGwOo/L1FAIVRV/u9epTIVoOGQvCAPxoWxqsY8ElIJ64pj2+R\nx4SNIPmld0ikv+QyflRVBzgaI2GSbD9l8WujdddUZOmhIltDtsOCh9cRAoGAH6yi\nxYgqzqtCMcMfcm7KBd7J2Y0+FDRJML6zCCExwKdmDSiwx/++MLi8AQHXuDtvwKZE\nkaAQgX9JTJqMFN+0oxuxMp8JCcZ7vb5A8cx/VU8XYuoLbAngTbNAGscqkV0Nw6jO\np4wsVKOfvMzf86m/rHgmNLkWDIVjpT8DGxmmW+0CgYBsIAwKLZ0vuWrx9DXbas8F\nT4mVaY6bsI9UdrkN8WMlMRO1g1WL6LKzBGEe11mpCeF/SponrP3ijsQmBqoZ/y9a\n8iiJtKS23ESzwUbgBOyop70DLeHwlCq8CJHxJysYRMt4LqX0V9iaxXcXdITiX3V9\n4VTDqWp8S3fPfnrbFZRuSQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-xni47@new-db-c52f3.iam.gserviceaccount.com",
    "client_id": "104850809630481020404",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xni47%40new-db-c52f3.iam.gserviceaccount.com"
}
cred = credentials.Certificate("first-db-77609-firebase-adminsdk-ykjt8-c7599cc9be.json")
admin = firebase_admin.initialize_app(cred, {'storageBucket': 'first-db-77609.appspot.com'})
lala = firebase_admin.get_app()
print(lala)
lola = _get_iid_service(lala)




api = 'BBIDtbVGhPcTldT3YOq5_aW9Dm0QvUKHZCGbzb1NkMSoV8VRD9881TYICUeilDBpsdD9WBPWaN72lwY7VM0nUOM'



firebasei = pyrebase.initialize_app(firebaseconfig)

db = firebasei.database()
authi = firebasei.auth()
storage = firebasei.storage()



print('Firebase initialized')
signed_in = False





# client = auth._get_client()
# print(client)

# tgen = TokenGenerator()
# now = tgen.create_custom_token('firebase_token')





        




        


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

class ContactScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def initialize_contact_message(self):
        try:
            func_timeout(30, self.work_thistime)
        except FunctionTimedOut:
            print("No internet connection")
            snack = "No internet conection"
            snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
            snacky.open()
        except Exception as e:
            snack = "No internet conection"
            snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
            snacky.open()

    def work_thistime(self):
        self.send_contact_message()

    
    def send_contact_message(self):
        
        firstname = self.ids.firstname.text
        lastname = self.ids.lastname.text
        email = self.ids.mail.text
        messagi = self.ids.message.text
        if len(firstname) >= 2 and len(lastname) < 16:
            if len(lastname) >= 2 and len(lastname) < 16:
                if email == "anangjosh8@gmail.com":
                    if len(messagi) > 20 and len(messagi) < 225:
                        message = MIMEText(messagi)
                        message['Subject'] = "Contact Us Hometernet Notice"
                        message["From"] = email
                        message["To"] = "anangjosh8@gmail.com"
                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
                        server.sendmail(email, "anangjosh8@gmail.com", message.as_string())
                        server.quit()
                        # self.doa.dismiss()
                        print("server exited")
                    else:
                        text = "Message must be between 20 and 225 characters"
                        self.show_dialog(text)
                        
                else:
                    text = "Email mismatch"
                    self.show_dialog(text)
                    
            else:
                text = "Lastname must be between 2 and 16 characters"
                self.show_dialog(text)
                
        else:
            text = "Firstname must be between 2 and 16 characters"
            self.show_dialog(text)
            
    @mainthread
    def show_dialog(self, notice, button1=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[MDFlatButton(text="close", on_release=self.close_dialog), button1])
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()

class HomeScreen(Screen):
    text = StringProperty()
    with open('user.json', 'r') as jsonfile:
        curr = json.load(jsonfile)
    text = curr['email']

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        print('pre-entering')
        print(str(self.ids.grid_card.width) + " " + 'is the width of the grid card')
        
        
            
        # real_size = str(size/3-60) + 'dp'
        # print(real_size)
        # print(Window.size[1])
        # print(Window.size[0])
        # self.ids.btn.user_font_size = real_size
        # self.ids.btn.md_bg_color = [1,1,1,1]
        return super().on_pre_enter(*args)
        

    def on_enter(self, *args):
        print('entered')
        print(str(self.ids.menu.width) + " " + "is the width")
        print(str(self.ids.menu.height) + " " + "is the height")
        return super().on_enter(*args)
        



        
       


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
    #     print('pre-entering')
    #     return super().on_pre_enter(*args)
    
    # def on_enter(self, *args):
    #     print('pre-entering')
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

class SearchLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new_country = ''
        self.new_choice = ''
        self.j = 0
        self.last = ''
        self.something = ''
        self.old_country = ''

    def search(self, choice, country, town, street):
        try:
            func_timeout(30, self.search_now, args=(choice, country, town, street))
        except FunctionTimedOut:
            print("No internet connection")
            snack = "No internet conection"
            snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
            snacky.open()
        except Exception as e:
            snack = "No internet conection"
            snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
            snacky.open()

    def search(self, choice, country, town, street):
        
        print(choice)
        self.old_country = country
        if country != self.new_country or choice != self.new_choice:
            print('is not equal')
            self.new_country = country
            self.new_choice = choice
            self.old_country = self.new_country
            self.clear_widgets()
        else:
            print('is equal')

        with open('user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
        
        # people = db.child("People").child(choice).get(
        
        # for person in people.each():
        #     something = person.key()
        #     print(something)
        self.begin = db.child(choice).get()
        self.added(country, town, street)

    @mainthread
    def added(self, country, town, street):
        for u in self.begin.each():
            if u.key() == self.something:
                continue
            if u.val()['country'] == country or u.val()['town'] == town or u.val()['street'] == street:
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
                if self.j == 1:
                    break
            if u.val()['country'] != country or u.val()['town'] != town or u.val()['street'] != street:
                snack = "Not found"
                snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
                snacky.open()
        

    def next(self, choice, country, town, street):
        try:
            again = db.child(choice).order_by_key().start_at(self.something).limit_to_first(2).get()
            print(again.val())
            for u in again.each():
                
                if u.key() == self.something:
                    continue
                
                if u.val()['country'] == country or u.val()['town'] == town or u.val()['street'] == street:
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
        except:
            pass
        
        #     print(u.val())

#-NGy3yrvpMXT0jYugGKH

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

loader = []

class PropertyCardsLayout(MDBoxLayout):
    def starter(self):
        try:
            func_timeout(30, self.added)
        except FunctionTimedOut:
            print("No internet connection")
        except:
            print("An error occured")
        
           
       
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
    
    def added(self):
        print('mmhmm')
        

        # print(a.val())
        # if a.key() == 'local_image':
        #     print(a.val())
        #     curr['house_images'].append(a.val())

        #     with open('user.json', 'w') as jsonfile:
        #         json.dump(curr, jsonfile)
        with open('user.json', 'r') as jsonfile:
            curr = json.load(jsonfile)
        print('OOh ma gaa')
        
        self.testichiro = db.child("People").child(curr['localid']).child("Sale").get(curr['idToken'])
        self.testiroro = db.child("People").child(curr['localid']).child("Rent").get(curr['idToken'])

        self.people = db.child("Sale").get()
        self.peopler = db.child("Rent").get()
        self.next_after()

    @mainthread
    def next_after(self):
        if self.testichiro.each():
            for q in self.testichiro.each():
                
                dude = q.val()['prop_keys']
            
            
            
                if self.people.each():
                    for u in self.people.each():
                        something = u.key()
                        print(u.key())
                        # another = person.val()
                        
                        if u.key() == q.val()['prop_keys']:
                            print(u.val()['url'])
                            if u.key() not in loader:
                                if something not in loader:
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
                                    self.add_widget(self.card)
                                    loader.append(u.key())
                                    print("added")
                                    print(loader)
                                else:
                                    print("Something else")
                            else:
                                print("Already loaded booom")
                                print(loader)
                        else:
                            print('Nope')
            for d in self.testiroro.each():    
                if self.peopler.each():
                    for u in self.peopler.each():
                        something = u.key()
                        print(u.key())
                        # another = person.val()
                        
                        if u.key() == d.val()['prop_keys']:
                            print(u.val()['url'])
                            if u.key() not in loader:
                                if something not in loader:
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
                                    self.add_widget(self.card)
                                    loader.append(u.key())
                                    print("added")
                                    print(loader)
                                else:
                                    print("Something else")
                            else:
                                print("Already loaded booom")
                                print(loader)
                        else:
                            print('Nope')

        
        
        
        # try:
        #     testichiro = db.child("People").child(dato['localid']).child("Sale").get(dato['idToken'])
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
        #     # with open('user.json', 'w') as jsonfile:
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

#             if now - self.last_call > self._max_call_interval:
#                 self.last_call = now

#                 function(*args, **kwargs)

#         return wrapped

# class Effect(DampedScrollEffect):
#     def on_overscroll(self, *args):
#         super().on_overscroll(*args)
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
        try:
            func_timeout(30, self.added)
        except FunctionTimedOut:
            print("No internet connection")
        
        
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
        #     print(self.j)
        # else:
        #     for i in house['Housing']:
        #         print(i)
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
        #         print(self.j)
        try:
            self.people = db.child("Sale").get()
            self.done()
        except:
            pass

    @mainthread
    def done(self):
        
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
                if self.j == 1: 
                    break

        

        
            
                    
                    
        

        
    def other(self):
        try:
            func_timeout(30, self.omagaa)
        except FunctionTimedOut:
            print("No internet connection")
        except Exception as e:
            print("An error occured")

    def omagaa(self):
        with open('user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])

        if self.something == '':
            self.people = db.child("Sale").get()
            self.otheri()

        else:
            self.again = db.child("Sale").order_by_key().start_at(self.something).limit_to_first(3).get(token=self.curr['idToken'])
            self.another()

    @mainthread
    def otheri(self):
        
        print('Is it working')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        
            
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
            if self.j == 1: 
                break

    @mainthread
    def another(self):    
            
        
        print(self.again.val())
        for u in self.again.each():
            # for i in u.val()['house']['-NL8x6ZNQQFpsXDfgm7c']['bathrooms']:
            
            #     print(i)
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
            

        
        # print(again.val())
        # print(self.last)
    
        
    


        

class RentCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.last = ''
        self.j = 0
        self.something = ''
        try:
            func_timeout(30, self.added)
        except FunctionTimedOut:
            print("No internet connection")
        except Exception as e:
            print("An error occured")
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
        self.people = db.child("Rent").get()
        self.done()

    @mainthread
    def done(self):
        print('Renting')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        
            
        if self.people.each():
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
                self.j += 1
                print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                
                # another = person.val()
                print('First iteration')
                print(self.something)
                if self.j == 1: 
                    break

    
        
    def other(self):
        try:
            func_timeout(30, self.omagaa)
        except FunctionTimedOut:
            print("No internet connection")
        except Exception as e:
            print("An error occured")

    def omagaa(self):
        with open('user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])

        if self.something == '':
            self.peopli = db.child("Rent").get(token=self.curr['idToken'])
            self.otheri()

        else:
            self.again = db.child("Rent").order_by_key().start_at(self.something).limit_to_first(3).get(token=self.curr['idToken'])
            self.another()

    @mainthread
    def otheri(self):
        print('Is it working')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        
        
        
        if self.peopli.each():
            for u in self.peopli.each():
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
                if self.j == 1: 
                    break

    @mainthread
    def another(self):
            
        print(self.again.val())
        for u in self.again.each():
            # for i in u.val()['house']['-NL8x6ZNQQFpsXDfgm7c']['bathrooms']:
                
            #     print(i)
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
            


class BookmarkScreen(Screen):
    pass
    
loaded = []

class BookmarkLayout(MDBoxLayout):
    
    
    
    def start(self):
        
        try:
            func_timeout(30, self.starti)
        except FunctionTimedOut:
            print("No internet connection")
        
    @mainthread
    def starti(self):
        try:
            with open('user.json', 'r') as jsonfile:
                curr = json.load(jsonfile)
            print('OOh ma gaa')
            people = db.child("Sale").get()
            
            
            print(curr['bookmarks'][0])
            for u in people.each():
                something = u.key()
                print(u.key())
                # another = person.val()
                
                if u.key() in curr['bookmarks']:
                    print(u.val()['url'])
                    if u.key() not in loaded:
                        if something not in loaded:
                            print('Okay maybe it wokred')
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
                            self.add_widget(self.card)
                            loaded.append(u.key())
                            print("added")
                            print(loaded)
                        else:
                            print("Something else")
                    else:
                        print("Already loaded booom")
                        print(loaded)
                else:
                    print('Nope')
        
        
            people = db.child("Rent").get()
        
            print(curr['bookmarks'][0])
            for u in people.each():
                something = u.key()
                print(u.key())
                # another = person.val()
                
                if u.key() in curr['bookmarks']:
                    print(u.val()['url'])
                    if u.key() not in loaded:
                        if something not in loaded:
                # another = person.val()
                
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
                            self.add_widget(self.card)
        except:
            print("Somerhing happedn")
            snack = "No internet conection"
            snacky = Snackbar(text=snack, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
            snacky.open()
        
        


class DialogEntry(MDBoxLayout):
    pass


class ForgotPasswordEntry(MDBoxLayout):
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
        countries = pycountry.countries
        
        for i in countries:
            
            list_item = List_item()
            list_item.text = i.name
            
            self.add_widget(list_item)

# princekofasiedu



                    
                    



        

class MainApp(MDApp):
    def build(self):

        # self.screensers = [HomeScreen(name="Home"), DetailsScreen(name="detail"),  SaleSubmit(name="Sale"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SignInScreen(name="sign-in"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks'), EditDetailsScreen(name='edit'), EditRentDetailsScreen(name='edit-rent'), LoadingScreen(name="loading"), CreatorScreen(name='creator'), Congrats(name='congrats')]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        
        
        
        
        self.signup = AccountLoginPage(name="sign-up")
        
        
        self.SaleOrRent = SaleOrRent(name="SaleOrRent")
        
        self.home = HomeScreen(name="Home")
        self.edit_rent = EditRentDetailsScreen(name="edit-rent")
        self.edit_sale = EditDetailsScreen(name="edit")
        self.bk = BookmarkScreen(name='bookmarks')
        self.products = MyProducts(name="products")
        self.about = AboutScreen(name="about")
        self.contact = ContactScreen(name="contact")
        
        
        
        self.search = SearchScreen(name="search")
        self.loading = LoadingScreen(name="loading")
        self.creator_screen = CreatorScreen(name='creator')
        self.tutorial = AppTutorial(name='tutor')
        self.congrats = Congrats(name='congrats')
        
        self.screenos = []
        self.screeni = []

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
        
        
        with open('user.json', 'r') as jsonfile:
            self.curr = json.load(jsonfile)
            print(self.curr['localid'])
            
        if self.curr['email'] == "":
            print("Fase")
            
        else:
            try:
                print("bruuhhh")
                user = authi.sign_in_with_email_and_password(self.curr['email'], self.curr['password'])
                usero = authi.refresh(user['refreshToken'])
                print(user)
                ino = authi.get_account_info(user['idToken'])
                
                print(ino)
                self.curr['idToken'] = user['idToken']

                with open('user.json', 'w') as jsonfile:
                    json.dump(self.curr, jsonfile)
                
            except:
                pass
        
        
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)


        # size = Window.size[1]
        # real_size = str(size/3-60) + 'dp'
        # print(real_size)
        # print(Window.size[1])
        # print(Window.size[0])
        # self.home.ids.btn.user_font_size = real_size
        
  
        


        self.something = False
        
            
        
        
        

        # for i in self.screensers:
        #     self.wm.add_widget(i)
        
        
        self.wm.transition = SwapTransition()
        # self.wm.switch_to(self.loading)
        
        self.wm.switch_to(self.home)
        self.numberiy = 'item 0'

        self.sale_or_rent = ''
        
        self.mail = ''
        self.passwrd = ''
        self.confirmed = ''
        self.sign_in_mail = ''
        self.sign_in_pass = ''
        self.source = 'Images\Pirate King (2).jpg'

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
        return self.wm
        return super().build()

    def on_start(self):
        

        print("Starting")

        return super().on_start()

    def hook_keyboard(self, window, key, *largs):
        print(self.wm.current)
        if key == 27:
            
            if self.wm.current == "products":
                self.wm.switch_to(self.home)
            
            elif self.wm.current == "bookmarks":
                self.switch_home() 
            elif self.wm.current == "sale" or self.wm.current == "rent":
                self.discard_auth()
            elif self.wm.current == "edit" or self.wm.current == 'edit-rent':
                print("oh dude")
                self.discard_auth()
            elif self.wm.current == "sign_in":
                self.discard_mail()
                self.switch_products()
            elif self.wm.current == "sign-up":
                self.discard_mail()
                self.switch_signin()
            elif self.wm.current == "search":
                print('What is wrong withn oyu')
                self.switch_home()
            elif self.wm.current == "creator":
                self.switch_home()
            elif self.wm.current == "tutor":
                self.switch_home()
            elif self.wm.current == "about":
                self.switch_home()
            elif self.wm.current == "contact":
                self.switch_home()
            
            

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
                    on_release=lambda y:self.switch_products()
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
    
    def discard_mail(self):
        self.passwrd = ''
        self.mail = ''

    def set_item(self, text_item):
        self.search.ids.drop_item.set_item(text_item)
        
        self.search.ids.drop_item.text = text_item
        
        # self.choice.dismiss()

    
    
    def callback_for_menu_items(self, *args):
        toast(args[0])

    def call_back(self, text_of_option):
        print(text_of_option)
    
    def on_checkbox_active(self, checkbox, value, num):
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
        elif icon == 'mail':
            print(obg + " " + 'is an email address')
            
        elif icon == 'twitter':
            print(obg + " " + 'is a twitter handle')
            
            
            webbrowser.open('https://t.co/' + obg)
        elif icon == 'facebook':
            print(obg + " " + 'is a facebook handle')
           
            webbrowser.open('https://m.me/' + obg)

    


    def show_bottom(self, email, phonenumber, twitter, facebook):
        bottom_sheet_menu = MDGridBottomSheet()

        
        datop = {
            email: "mail",
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
                icon_src = item[1]
            )
        
        
        bottom_sheet_menu.open()

    
    
    def stopper(self):
        sys.exit()
    def switch_home(self):
        
        self.wm.switch_to(self.home)

    def switch_loading(self):
        self.wm.transition = NoTransition()
        self.wm.switch_to(self.loading)

    def switch_creator(self):
        self.wm.switch_to(self.creator_screen)

    def switch_contact(self):
        with open('user.json', 'r') as jsonfile:
            self.contact_info = json.load(jsonfile)
            
        self.wm.switch_to(self.contact)

    def switch_tutorial(self):
        self.wm.switch_to(self.tutorial)

    def switch_about(self):
        self.wm.switch_to(self.about)

    def call_guy(self, lockwood):
        print(lockwood)
        func_timeout(30, self.boooiiii, args=(lockwood,))
        

    
        

    def boooiiii(self, figaro):
        
            
        them14 = db.child("Sale").child(figaro).child("views").get()
        new_val = them14.val()
        new_val += 1
        print(new_val)
        db.child("Sale").child(figaro).update({'views': new_val}, self.curr['idToken'])
        self.curr["viewed"].append(figaro)
        with open('user.json', 'w') as jsonfile:
            json.dump(self.curr, jsonfile)
                
        

    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, phonenumber=None, twitter=None, facebook=None, description=None, key=None, amenities=None):
        self.wm.switch_to(self.loading)
        
        print(image)
        self.detail = DetailsScreen()
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
        self.wm.switch_to(self.detail)
        

    def switch_search(self):
        if len(self.screenos) == 2:
            self.screenos.pop()
        self.screenos.insert(0, "search")
        self.wm.switch_to(self.search)
        

    def switch_sale(self):
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])
        self.sale = SaleSubmit(name="sale")
        self.wm.switch_to(self.sale)

    def switch_rent(self):
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])
        self.rent = RentSubmit(name="rent")
        self.wm.switch_to(self.rent)

    def switch_signup(self):
        self.wm.switch_to(self.signup)

    def switch_products(self):
        
        self.wm.transition = SwapTransition()
        if len(self.screenos) == 2:
            self.screenos.pop()
        self.screenos.insert(0, "products")
        
        
        self.wm.switch_to(self.products)

    def switch_bookmarks(self):
        self.wm.transition = SwapTransition()
        
        if len(self.screenos) == 2:
            self.screenos.pop()
        self.screenos.insert(0, "bookmarks")
        

        self.wm.switch_to(self.bk)
    
    def switch_signin(self):
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
        if self.info['email'] != "":
            p="You're already signed in"
            self.snackbar(p)
        else:
            self.signin = SignInScreen(name="sign_in")
            self.wm.switch_to(self.signin)

    def switch_congrats(self):
        self.wm.switch_to(self.congrats)
    

    
    
    def switch_saleorrent(self):
        try:
            
            with open('user.json', 'r') as jsonfile:
                data = json.load(jsonfile)
            
            if data['email'] == "":
                        
                self.wm.switch_to(self.signin)
            else:
                
                
                self.wm.switch_to(self.SaleOrRent)
        except:
            self.snackbar("No internet connection")

    

    def email(self, texta):
        self.mail = texta
        

    def phone(self, texta):
        self.phonenumber = texta

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
            self.edit_sale.ids.country_text.text = texta
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

    
    

    def show_dialog(self, notice, button, button1=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[button, button1])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="10dp", snackbar_y="70dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.1)
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
            title='Warning!',
            type='custom',
            content_cls=Warning(),
            buttons=[
                
                MDRaisedButton(
                    text='Agree',
                    theme_text_color='Custom',
                    on_release= lambda x:self.dia.dismiss()
                )
            ]
        )
        self.dia.open()
            
    def send_email(self, email, phonenumber, twitter, facebook):
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        if data['email'] == "":
            self.wm.switch_to(self.signin)
        else:
            
            ino = authi.get_account_info(data['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                # authi.send_email_verification(data['idToken'])
                self.dia = MDDialog(
                    title='Your email has not been verified!',
                    text='Please re-sign in to get the verification link',
                    buttons=[
                        MDFlatButton(
                            text='Cancel',
                            theme_text_color='Custom',
                            text_color='black',
                            on_press=lambda x:self.dia.dismiss()
                        )
                    ]
                )
                self.dia.open()
                    
                      
            else:
                
                print('horray hooray')
                
                message = MIMEText("An offer has been made to buy your house")
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
            title='Select Country',
            type='custom',
            content_cls=Countries(),
            buttons=[
                MDFlatButton(
                    text='Cancel',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=lambda x:self.dia.dismiss()
                ),
                MDFlatButton(
                    text='Agree',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press= lambda x:self.dia.dismiss()
                )
            ]
        )
        self.dia.open()
        
        
    def account_submit(self):
        email = self.mail
        password = self.passwrd
        
        print(self.signup.ids.confirm.text)
        
        if len(password) >= 6:
        
            try:
                response = requests.get('https://isitarealemail.com/api/email/validate', params= {'email':email})

                status = response.json()['status']
                if status == "valid":

                    if self.signup.ids.confirm.text == password:
                        self.dia = MDDialog(
                            title='Warning!',
                            type='custom',
                            content_cls=Warning(),
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
                                    text_color='black',
                                    on_press= lambda x:self.create_account(),
                                    on_release= lambda x:self.dia.dismiss()
                                )
                            ]
                        )
                        self.dia.open()
                        
                    else:
                        text = "Password does not match"
                        close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                        self.show_dialog(text, close_button)
            # else:
            #     text = "Invalid email"
            #     close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            #     self.show_dialog(text, close_button)
            
            except:
                p="Oops something went wrong"
                self.snackbar(p)
        else:
            text = "Password should be at least 6 characters"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)

    def create_account(self):
        email = self.mail
        password = self.passwrd
        
        user = authi.create_user_with_email_and_password(email, password)
        useri = authi.send_email_verification(user['idToken'])
        self.sign_in()
        text = "An email verification link has been sent to your mail"
        close_button = MDFlatButton(text="close", on_press=self.close_dialog)
        self.show_dialog(text, close_button)
        self.switch_products()
        self.mail = ''
        self.passwrd = ''
        
    def delete_property_auth(self, key, local_image, sale_or_rent):
        print(key,local_image,sale_or_rent)
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
                    on_press=lambda x=key, a=key, y=local_image, z=sale_or_rent: self.delete_property(a,y,z)
                )
            ]
        )
        self.dia.open()
        
    def delete_property(self, name, local_image, sale_or_rent):

        print(name,local_image,sale_or_rent)
        next = False
        self.entry = DialogEntry()
        print(self.passwrd + " " + 'ooooohhhhh ma gaaaaa')
        with open('user.json', 'r') as jsonfile:
            curr = json.load(jsonfile)
            print(curr['email'])
            print(curr['password'])
        if curr['email'] and curr['password'] == "":
            p = 'No user signed in'
            self.snackbar(p)
        else:
            
            if self.passwrd == curr['password']:
                
                try:
                    user = authi.sign_in_with_email_and_password(curr['email'], curr['password'])
                    storage.delete(user['localId'] + '/' + local_image, user['idToken'])
                    
                    if sale_or_rent == 'Sale':
                        db.child("Sale").child(name).remove(user['idToken'])
                        remove_people = db.child("People").child(curr['localid']).child("Sale").get(user['idToken'])
                        for u in remove_people.each():
                            print(u.val()['prop_keys'])
                            if u.val()['prop_keys'] == name:
                                db.child("People").child(curr['localid']).child("Sale").child(u.key()).child(name).remove(user['idToken'])
                        

                    else:
                        db.child("Sale").child(name).remove(user['idToken'])
                        remove_people = db.child("People").child(curr['localid']).child("Rent").get(user['idToken'])
                        for u in remove_people.each():
                            print(u.val()['prop_keys'])
                            if u.val()['prop_keys'] == name:
                                db.child("People").child(curr['localid']).child("Rent").child(u.key()).child(name).remove(user['idToken'])
                    p = 'Property Successfully deleted'
                    self.snackbar(p)
                        
                    self.passwrd = ''
                except:
                    p="No internet connection"
                    self.snackbar(p)
            else:
                text = "Invalid password"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
        

    def password_reset(self):
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
                MDFlatButton(
                    text='Submit',
                    theme_text_color='Custom',
                    text_color='black',
                    on_press=self.forgot_auth
                )
            ]
        )
        self.di.open()
    def forgot_auth(self, obj):
        try:
            if self.mail == '':
                text = "Please type in your email in the space"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
            else:
                authi.send_password_reset_email(self.mail)
                text = "A password reset email has been sent to your mail"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
                self.mail = ''
        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
                print('Email not found')
                self.mail = ''
        except:
            p = 'No internet connection'
            self.snackbar(p)
        

# "MKHRXCSZPZWXKIIF"
# "GeoWorl38751759"

    def sign_in(self):
        try:
            func_timeout(30, self.sign_in_now)
        except FunctionTimedOut:
            p = 'Network Error'
            self.snackbar(p)

    @mainthread
    def sign_in_now(self):
        email = self.mail
        password = self.passwrd
        
        
        try:
            self.user = authi.sign_in_with_email_and_password(email, password)
            ino = authi.get_account_info(self.user['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                authi.send_email_verification(self.user['idToken'])
                text = "An email verification link has been sent to your mail"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
            else:
                pass
            
            
            
            with open('user.json', 'r') as jsonfile:
                self.curr = json.load(jsonfile)
                

            

            self.curr['email'] = self.mail
            self.curr['password'] = self.passwrd
            self.curr['idToken'] = self.user['idToken']
            self.curr['localid'] = self.user['localId']
            print(self.user['localId'] + " " + "aaaaaaaaaaaaahahahahaaaaaaaahahahahaa")
            
            
            print(self.curr['localid'])
            print(self.curr['idToken'])

        

        # testro = db.child("People").get(curr['idToken'])
        # for i in testro.each():
        #     # print(i.val()['prop_keys'])
        #     # dude = i.val()['prop_keys']
        #     # print(i.key())
        #     # them = db.child("Sale").child(dude).get(self.user['idToken'])
        #     # for u in them.each():
        #     #     print(u.val())
        #     print(i.val())
        
        # againi = db.child("People").child("Sale").child(curr['localid']).child("house").get()
        # if againi.each():
        #     for i in againi.each():
        #         print(i.val()['local_image'])
        #         curr['house_images'].append(i.val()['local_image'])
        # else:
        #     pass

            with open('user.json', 'w') as jsonfile:
                json.dump(self.curr, jsonfile)
            self.switch_products()

            p = 'Successfully signed in'
            self.snackbar(p)

            self.home.text = self.curr['email']
            self.mail = ''
            self.passwrd = ''

        except requests.exceptions.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == 'EMAIL_NOT_FOUND':
                text = "Email not found"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
                print('Email not found')
                self.mail = ''
            if error == 'INVALID_PASSWORD':
                text = "Invalid password"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
                print('Invalid password')
                self.mail = ''
        except:
            p = 'Network Error'
            self.snackbar(p)
        
        
        # except:
        #     p = 'No internet connection'
        #     self.snackbar(p)

        
            
        # except:
        #     text = "Invalid email or password"
        #     close_button = MDFlatButton(text="close", on_press=self.close_dialog)
        #     self.show_dialog(text, close_button)

        

    
    def editscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        self.edit = EditDetailsScreen()
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
        self.edit.landspace = landspace
        self.edit.email = email
        self.edit.key = key
        self.edit.local_image = local_image
        self.edit.description = description
        self.edit.amenities = amenities
        print(key, town, street)
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])

    def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, state=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
        self.edit_rent = EditRentDetailsScreen()
        self.wm.switch_to(self.edit_rent)
        self.edit_rent.type = House_type
        self.edit_rent.image = image
        self.edit_rent.price = pricing
        self.edit_rent.country = locate
        self.edit_rent.province = state
        self.edit_rent.town = town
        self.edit_rent.street = street
        self.edit_rent.bedrooms = bedrooms
        self.edit_rent.bathrooms = bathrooms
        self.edit_rent.landspace = landspace
        self.edit_rent.email = email
        self.edit_rent.key = key
        self.edit_rent.local_image = local_image
        self.edit_rent.description = description
        self.edit_rent.amenities = amenities
        print(key)
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])

    
    

    def update_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        print(bedrooms)
        print(street)
        print(landspace)
        print(key)
        print(House_type)
        print(len(House_type))
        
        if pricing[0] == '$':
            self.amt = pricing
        else:
            self.amt = "$" + pricing
        
        print(landspace[-1])
        if landspace[-1] == 't':
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'

        self.key = key
        self.local_image = local_image
        amenities = self.amenities
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        with open('user.json', 'r') as jsonfile:
            self.datp = json.load(jsonfile)
        # pp = int(pricing)
        # print(pp)
        

        if len(House_type) > 5 and len(House_type) < 21:
            
            
            if len(state) >= 3 and len(state) < 20:
                if len(town) >= 3 and len(town) < 16:

                    if len(street) >= 3 and len(street) < 25:
                        if len(pricing) > 1:
                            if len(description) > 20 and len(description) < 255:
                                db.child("Sale").child(key).update({'housetype': House_type}, self.info['idToken'])
                                db.child("Sale").child(key).update({'country': locate}, self.info['idToken'])
                                db.child("Sale").child(key).update({'state': state}, self.info['idToken'])
                                db.child("Sale").child(key).update({'town': town}, self.info['idToken'])
                                db.child("Sale").child(key).update({'street': street}, self.info['idToken'])
                                db.child("Sale").child(key).update({'bedrooms': bedrooms}, self.info['idToken'])
                                db.child("Sale").child(key).update({'bathrooms': bathrooms}, self.info['idToken'])
                                db.child("Sale").child(key).update({'landspace': self.landspace}, self.info['idToken'])
                                db.child("Sale").child(key).update({'price': self.amt}, self.info['idToken'])
                                db.child("Sale").child(key).update({'description': description}, self.info['idToken'])
                                db.child("Sale").child(key).update({'amenities': amenities}, self.info['idToken'])
                                self.sale_or_rent = "Sale"
                                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
                                agree_button = MDRaisedButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function)
                                exit = MDFlatButton(text="close", on_release=self.close_dialog)
                                info = "Do you want to change your image?"
                                self.show_dialog(info,exit,agree_button)
                                p = 'Changes made successfully'
                                self.snackbar(p)
                            else:
                                text = 'description must be between 20 and 255 characters long'
                                self.show_dialog(text, close_button)
                                self.edit.ids.description.error = True
                        else:
                            text = "Invalid Input for price"
                            self.show_dialog(text,close_button)
                            self.edit.ids.street.error = True
                    else:
                        text = "street must be between 2 and 25 characeters"
                        self.show_dialog(text,close_button)
                        self.edit.ids.street.error = True
                else:
                    text = "town must be between 2 and 16 characters"
                    self.show_dialog(text,close_button)
                    self.edit.ids.town.error = True
            else:
                text = "State must be between 2 and 16 characters"
                self.show_dialog(text,close_button)
                self.edit.ids.state.error = True
            
        else:
            text = "House type must be between 5 and 21 characters characeters"
            self.show_dialog(text,close_button)
            self.edit.ids.housetype.error = True

    

    def update_rent_property(self, local_image, House_type, pricing, locate, state, town, street, bedrooms, bathrooms, landspace, key, description):
        self.rent_key = key
        self.local_image = local_image
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        with open('user.json', 'r') as jsonfile:
            self.datp = json.load(jsonfile)
        
        amenities = self.amenities

        if self.edit_rent.price[0] == '$' and self.edit_rent.price[-1] == 'h' or self.edit_rent.price[-1] == 'r':
            self.amt = pricing
        elif pricing[0] == '$' and pricing[-1] == 'h' or pricing[-1] == 'r':
            self.amt = pricing
        elif pricing[0] != '$' and pricing[-1] != 'h' or pricing[-1] == 'r':
            self.amt = pricing + self.edit_rent.ids.pay_item.text

        if landspace[-1] == 't':
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'
        # pp = int(pricing)
        # print(pp)
        

        if len(House_type) > 5 and len(House_type) < 21:
            
            if len(state) >= 3 and len(state) < 20:

                
                
                if len(town) >= 3 and len(town) < 16:

                    if len(street) >= 3 and len(street) < 25:
                        if len(pricing) > 1:
                            if len(description) > 20 and len(description) < 255:
                                db.child("Rent").child(key).update({'housetype': House_type}, self.info['idToken'])
                                db.child("Rent").child(key).update({'country': locate}, self.info['idToken'])
                                db.child("Rent").child(key).update({'state': state}, self.info['idToken'])
                                db.child("Rent").child(key).update({'town': town}, self.info['idToken'])
                                db.child("Rent").child(key).update({'street': street}, self.info['idToken'])
                                db.child("Rent").child(key).update({'bedrooms': bedrooms}, self.info['idToken'])
                                db.child("Rent").child(key).update({'bathrooms': bathrooms}, self.info['idToken'])
                                db.child("Rent").child(key).update({'landspace': self.landspace}, self.info['idToken'])
                                db.child("Rent").child(key).update({'price': self.amt}, self.info['idToken'])
                                db.child("Rent").child(key).update({'description': description}, self.info['idToken'])
                                db.child("Rent").child(key).update({'amenities': amenities}, self.info['idToken'])
                                self.sale_or_rent = "Rent"
                                self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
                                agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function)
                                exit = MDFlatButton(text="close", on_release=self.close_dialog)
                                info = "Do you want to change your image?"
                                self.show_dialog(info,exit,agree_button)
                                p = 'Changes made successfully'
                                self.snackbar(p)
                            else:
                                text = 'Description must be between 20 and 255 characters'
                                self.show_dialog(text,close_button)
                        else:
                            text = "Invalid Input for price"
                            self.show_dialog(text,close_button)
                    else:
                        text = "street must be between 2 and 25 characeters"
                        self.show_dialog(text,close_button)
                        self.edit_rent.ids.street.error = True
                else:
                    text = "town must be between 2 and 16 characters"
                    self.show_dialog(text,close_button)
                    self.edit_rent.ids.town.error = True
            else:
                text = "State must be between 2 and 20 characters"
                self.show_dialog(text,close_button)
                self.edit_rent.ids.state.error = True
        else:
            text = "House type must be between 5 and 21 characters characeters"
            self.show_dialog(text,close_button)
            self.edit_rent.ids.housetype.error = True

    def separate_function(self):
        
        filechooser.open_file(on_selection=self.change_image, multiselect=True)
        
    def change_image(self, selection):
        print(selection)
        if len(selection) > 0:
            self.new_file = str(selection[0])
            print(self.local_image)
            x = re.search(r".jpg$", self.file)
            y = re.search(r".png$", self.file)
            if x or y:
                # urli = storage.child(data['localid']).child(self.local_image).get_url(data['idToken'])
                # tokenop = "https://firebasestorage.googleapis.com/v0/b/first-db-77609.appspot.com/o/2C8VZdiEBCMhnFS0fnvzpa4jW2F2%2FC%3A%5CUsers%5CYvonne%5CDownloads%5Cbeautiful-house-15.jpg?alt=media"
                # storage.child(self.data['localid']).delete(self.local_image, urli)
                # print('SUccessfully deleted')
                
                # img = storage.child(self.data['localid']).child(self.local_image).get_url(None)
                with open('user.json', 'r') as jsonfile:
                    dati = json.load(jsonfile)
                user = authi.sign_in_with_email_and_password(dati['email'], dati['password'])
                storage.delete(self.datp['localid'] + '/' + self.local_image, user['idToken'])

                # bucket = admin_storage.bucket()
                # blob = bucket.blob(self.local_image)
                # print(blob)
                # blob.delete()
                print('Successfully deleted')
                print(self.datp['localid'])
                print(self.new_file)
                print(self.key)
                storage.child(self.datp['localid']).child(str(self.new_file)).put(str(self.new_file))
                url = storage.child(self.datp['localid']).child(self.new_file).get_url(None)
                if self.sale_or_rent == 'Sale':
                    db.child("Sale").child(self.key).update({'local_image': self.new_file})
                    db.child("Sale").child(self.key).update({'url': url})
                else:
                    db.child("Rent").child(self.key).update({'local_image': self.new_file})
                    db.child("Rent").child(self.key).update({'url': url})
                p = 'Changes made successfully'
                self.snackbar(p)
            else:
                info = 'Please select an image file'
                close_button = MDFlatButton(text="No", on_release=self.close_dialog)
                self.show_dialog(info,close_button)

        else:
            info = "No image selected"
            close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
            self.show_dialog(info,close_button)
            self.switch_products()

    def sign_out_auth(self):
        text = 'Are you sure you want to sign out? You will loose all of your bookmarks.'
        close_button = MDRaisedButton(text="No", on_release=self.close_dialog)
        agree_button = MDFlatButton(text='Yes', on_release=self.sign_out)
        self.show_dialog(text,close_button, agree_button)

    def sign_out(self,obj=None):
        
        
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)

        data['email'] = ''
        data['password'] = ''
        data['idToken'] = ''
        data['house_images'] = []
        data['localid'] = ''
        data['bookmarks'] = []
        data["viewed"] = []
        with open('user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        p = 'Successfully signed out'
        self.snackbar(p)
        

    def delete_user_auth(self):
        self.di = MDDialog(
            title='Please Enter your password',
            type='custom',
            content_cls=DialogEntry(),
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
                    on_press=self.delete_user
                )
            ]
        )
        self.di.open()
    
    

    def delete_user(self, obj):
        
        with open('user.json', 'r') as jsonfile:
            dati = json.load(jsonfile)
            print(dati['password'])
        print(self.passwrd)
        if dati['email'] and dati['password'] != "":
            # try:
            
            if self.passwrd == dati['password']:    
                user = authi.sign_in_with_email_and_password(dati['email'], dati['password'])
                # db.child("People").child(user['localId']).remove()
                testichiro = db.child("People").child(dati['localid']).child("Sale").get(dati['idToken'])
                testiroro = db.child("People").child(dati['localid']).child("Rent").get(dati['idToken'])
                if testichiro.each():
                    for i in testichiro.each():

                        local = user['localId'] + '/'                    
                        storage.delete(local + i, user['idToken'])

                        dude = i.val()['prop_keys']
                        db.child("Sale").child(dude).remove(user['idToken'])
                if testiroro.each():
                    for q in testiroro.each():

                        local = user['localId'] + '/'                    
                        storage.delete(local + i, user['idToken'])

                        dudo = q.val()['prop_keys']
                        db.child("Rent").child(dudo).remove(user['idToken'])
                try:
                    db.child("People").child(dati['localid']).remove(user['idToken'])
                    
                except:
                    p="Doesn't own property"
                    self.snackbar(p)
                # storage.delete(user['localId'], user['idToken'])
                    
                
                
                authi.delete_user_account(user['idToken'])
                message = MIMEText(dati['email'] + " " + "with localid" + " " + dati['localid'] + " " + "Just deleted their account")
                message['Subject'] = "Deleted account Notice"
                message["From"] = "anangjosh8@gmail.com"
                message["To"] = "anangjosh8@gmail.com"
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
                server.sendmail("anangjosh8@gmail.com", "anangjosh8@gmail.com", message.as_string())
                server.quit()
                
                dati['email'] = ''
                dati['password'] = ''
                dati['idToken'] = ''
                dati['house_images'] = []
                dati['bookmarks'] = []
                dati['localid'] = ''
                with open('user.json', 'w') as jsonfile:
                    json.dump(dati, jsonfile)
                
                
                print("successfully deleted account")
                self.passwrd = ''
            else:
                print('Invalid Password')
                text = "Invalid password"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
                self.passwrd = ''
    #    except:
    #         print("Operation unsuccessful")
    #         p = 'Operation Unsuccessful'
    #         self.snackbar( p)
        else:
            p = 'No user signed in'
            self.snackbar(p)
                # text = "yes"
                # self.close_dialog(text)
                # close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                # notice = "No user signed in"
            # self.show_dialog(notice, close_button)
    
    def delete_user_notice(self):
        agree_button = MDFlatButton(text="Yes", on_release=self.close_dialog, on_press=self.delete_user_auth)
        close_button = MDFlatButton(text="No", on_release=self.close_dialog)
        info = "Are you sure you want to delete your account"
        self.show_dialog(info,close_button, agree_button)

    def switch_account_auth(self):
        agree_button = MDFlatButton(text="Yes", on_release=self.close_dialog, on_press=self.switch_account)
        close_button = MDFlatButton(text="No", on_release=self.close_dialog)
        info = "Are you sure you want to switch accounts? This will mean signing out."
        self.show_dialog(info,close_button, agree_button)


    def switch_account(self, obj):
        self.sign_out()
        self.switch_signin()
            
        

    def bookmark(self, lola):
        
        try:
            with open('user.json', 'r') as jsonfile:
                data = json.load(jsonfile)
            if lola not in data['bookmarks']:
                data['bookmarks'].append(lola)
                with open('user.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)
                notice = 'Successfully added to bookmarks'
                self.snackbar(notice)
            else:
                data['bookmarks'].remove(lola)
                with open('user.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)
                notice = 'Successfully removed from bookmarks'
                self.snackbar(notice)

            
        except:
            print("Unsuccessfully added to bookmarks")

    def selected(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        
        if len(self.tot) > 5:
            
            if len(self.country) >= 2 and len(self.country) < 16:
                
                if self.mail == self.info['email']:
                    # phone = '+2332222222222'
                    if self.phonenumber != '':
                        phone_number  = phonenumbers.parse(self.phonenumber)
                        valid = phonenumbers.is_valid_number(phone_number)
                        print(valid)
                        if valid == True:
                            if len(self.state) >= 3 and len(self.state) < 20:
                                if len(self.town) >= 3 and len(self.town) < 16:

                                    if len(self.street) >= 6 and len(self.street) < 25:
                                        if len(self.price) > 1:
                                            if len(self.desc) > 20 and len(self.desc) < 255:
                                                filechooser.open_file(on_selection=self.real_sale, multiselect=True)
                                            else:
                                                info = "description must be between 20 and 100 characters"
                                                self.show_dialog(info,close_button)
                                        else:
                                            info = "Invalid input for price"
                                            self.show_dialog(info,close_button)
                                    else:
                                        info = "Street must be between 6 and 25 characters"
                                        self.show_dialog(info,close_button)

                                else:
                                    info = "Town must be between 2 and 16 characters"
                                    self.show_dialog(info,close_button)
                            else:
                                info = "State must be between 2 and 20 characters"
                                self.show_dialog(info,close_button)
                        else:
                            info = "Invalid phonenumber"
                            self.show_dialog(info,close_button)
                    else:
                        info = "Please Enter a phone number"
                        self.show_dialog(info,close_button)
                else:
                    info = "Invalid email"
                    self.show_dialog(info,close_button)
            
            else:
                info = "Country must be between 2 and 16 characters"
                self.show_dialog(info,close_button)
        else:
            text = "House type must be more than 5 characeters"
            self.show_dialog(text,close_button)

    def real_sale(self, selection):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        selected_image = selection
        
        print(selected_image)
        if len(selected_image) > 0:
            try:
                func_timeout(40, self.house_sale, args=(selected_image,))
            except:
                print("No internet connection")
        else:
            info = "You need to select an image to continue"
            self.show_dialog(info, close_button)
        
        # except FunctionTimedOut:
        #     print("No internet connection")
        #     p="no internet connection"
        #     self.snackbar(p)
        # except Exception as e:
        #     print("An error occured")
        #     p="An error occured"
        #     self.snackbar(p)
    @mainthread
    def house_sale(self, selection):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        self.signing = authi.sign_in_with_email_and_password(self.info['email'], self.info['password'])
        print(selection)
        
        self.file = selection
        print(self.file)
        print(self.file[-1:-4])
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png", self.file)
        if x or y:
            print('yes there is a match')
            storage.child(self.signing['localId']).child(str(self.file)).put(str(self.file))
            url = storage.child(self.signing['localId']).child(self.file).get_url(None)
            print(self.file)
            # with open('user.json', 'r') as jsonfile:
            #     dato = json.load(jsonfile)
            print(self.phonenumber)
            self.info['house_images'].append(self.file)
            with open('user.json', 'w') as jsonfile:
                json.dump(self.info, jsonfile)
            
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
                "views": 0
            }

            
            data['housetype'] = self.tot
            data['country'] = self.country
            data['state'] = self.state
            data['town'] = self.town
            data['street'] = self.street
            data['bedrooms'] = self.bedrooms
            data['bathrooms'] = self.bathrooms
            data['landspace'] = self.landspace + 'sq.ft'
            data['url'] = url
            data['email'] = self.mail
            data['phonenumber'] = self.phonenumber
            data['price'] = "$" + self.price
            data['local_image'] = self.file
            data['description'] = self.desc
            data['amenities'] = self.amenities
            data['twitter'] = self.twitter
            data['facebook'] = self.facebook
            
            
            results = db.child("Sale").push(data, self.signing['idToken'])
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


            self.house_key = []
            self.house_key.append(results['name'])
            
            key_data = {
                "prop_keys": "",
            }
            key_data['prop_keys'] = results['name']
            db.child("People").child(self.signing['localId']).child("Sale").push(key_data, self.signing['idToken'])
            print(key_data)
            print(results)
            self.switch_congrats()
        else:
            print('no match at all')
            info = 'Please select an image file'
            self.show_dialog(info, close_button)
            
            
        
        
        

                
        

    def rent_property(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        if len(self.tot) > 5:
            
            if len(self.country) > 3 and len(self.country) < 16:
                if self.mail == self.info['email']:
                    # phone = '+2332222222222'
                    if self.phonenumber != '':
                        phone_number  = phonenumbers.parse(self.phonenumber)
                        valid = phonenumbers.is_valid_number(phone_number)
                        print(valid)
                        if valid == True:
                            if len(self.state) >= 3 and len(self.state) < 20:
                                if len(self.town) >= 3 and len(self.town) < 16:

                                    if len(self.street) >= 6 and len(self.street) < 25:
                                        if len(self.price) > 1:
                                            if len(self.desc) > 20 and len(self.desc) < 100:
                    
                                                filechooser.open_file(on_selection=self.real_rent)
                                            else:
                                                info = "description must be between 20 and 100 characters"
                                                self.show_dialog(info,close_button)
                                        else:
                                            info = "Invalid input for price"
                                            self.show_dialog(info,close_button)
                                    else:
                                        info = "Street must be between 6 and 25 characters"
                                        self.show_dialog(info,close_button)

                                else:
                                    info = "Town must be between 2 and 16 characters"
                                    self.show_dialog(info,close_button)
                            else:
                                info = "State must be between 2 and 20 characters"
                                self.show_dialog(info,close_button)
                        else:
                            info = "Invalid phonenumber"
                            self.show_dialog(info,close_button)
                    else:
                        info = "Please Enter a phone number"
                        self.show_dialog(info,close_button)
                else:
                    info = "Invalid email"
                    self.show_dialog(info,close_button)
            else:
                info = "location must be more than 6 characters"
                self.show_dialog(info,close_button)
        else:
            text = "House type must be more than 5 characeters"
            self.show_dialog(text,close_button)


    def real_rent(self, selection):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        selected_image = selection
        if len(selected_image) > 0:
            print(selected_image)
            try:
                func_timeout(40, self.house_rent, args=(selected_image))
            except:
                print("No internet connection")
        else:
            info = "You need to select an image to continue"
            self.show_dialog(info, close_button)

    @mainthread
    def house_rent(self, selection):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        self.signing = authi.sign_in_with_email_and_password(self.info['email'], self.info['password'])
        print(selection)
        
        self.file = selection
        print(self.file)
        print(self.file[-1:-4])
        x = re.search(r".jpg$", self.file)
        y = re.search(r".png$", self.file)
        if x or y:
            storage.child(self.info['localid']).child(str(self.file)).put(str(self.file))
            url = storage.child(self.info['localid']).child(self.file).get_url(None)

        
            self.info['house_images'].append(self.file)
            with open('user.json', 'w') as jsonfile:
                json.dump(self.info, jsonfile)
            
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
                "views": 0
            }

            
            data['housetype'] = self.tot
            data['country'] = self.country
            data['state'] = self.state
            data['street'] = self.street
            data['town'] = self.town
            data['bedrooms'] = self.bedrooms
            data['bathrooms'] = self.bathrooms
            data['landspace'] = self.landspace + 'sq.ft'
            data['url'] = url
            data['email'] = self.info['email']
            data['price'] = "$" + self.price + self.rent.ids.pay_item.text
            data['local_image'] = self.file
            data['phonenumber'] = self.phonenumber
            data['twitter'] = self.twitter
            data['facebook'] = self.facebook
            data['description'] = self.desc
            data['amenities'] = self.amenities
            # db.child("People").child(key).child("house").push(data)
            # results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
            results = db.child("Rent").push(data, self.info['idToken'])
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


            self.house_key = []
            self.house_key.append(results['name'])
            
            key_data = {
                "prop_keys": "",
            }
            key_data['prop_keys'] = results['name']
            db.child("People").child(self.info['localid']).child("Rent").push(key_data, self.info['idToken'])
            print(key_data)
            print(results)
            self.switch_congrats()
            # for i in results.each():
            #     print(i.key())
            
        else:
            close_button = MDFlatButton(text="close", on_release=self.close_dialog)
            info = "Please select an image"
            self.show_dialog(info,close_button)
    


MainApp().run()

