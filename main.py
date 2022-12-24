
import phonenumbers
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SwapTransition, NoTransition
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivymd.uix.list import MDList, OneLineListItem, ImageLeftWidget, OneLineIconListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.snackbar import Snackbar
import mysql.connector
import pyrebase
from kivy.clock import time

from kivy.uix.textinput import TextInput

import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore

from firebase_admin.messaging import Message, Notification

from firebase_admin import auth

from pyfcm import FCMNotification

from plyer import filechooser
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import smtplib
from email.message import EmailMessage
import ezgmail
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.uix.scrollview import ScrollView


from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
import webbrowser
import numpy as np
import threading
import requests



button = MDIconButton



Window.size = (400,768)
        



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
    "measurementId": "G-NGK0NGTGJX"
}
cred = credentials.Certificate("first-db-77609-firebase-adminsdk-ykjt8-c7599cc9be.json")
admin = firebase_admin.initialize_app(cred, {'storageBucket': 'first-db-77609.appspot.com'})





api = 'BBIDtbVGhPcTldT3YOq5_aW9Dm0QvUKHZCGbzb1NkMSoV8VRD9881TYICUeilDBpsdD9WBPWaN72lwY7VM0nUOM'



firebasei = pyrebase.initialize_app(firebaseconfig)

db = firebasei.database()
authi = firebasei.auth()
storage = firebasei.storage()

print('Firebase initialized')
signed_in = False

push_service = FCMNotification(api_key=api)







with open('user.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data['localid'])
    
    if data['email'] == "":
        print("Fase")
        
    else:
        try:
            print("bruuhhh")
            user = authi.sign_in_with_email_and_password(data['email'], data['password'])
            user = authi.refresh(user['refreshToken'])
            ino = authi.get_account_info(user['idToken'])
            print(ino)
            data['idToken'] = user
        except:
            pass

# registration_id = data['idToken']
# message_title = "Property Update"
# message_body = 'Hi Mr, an offer has been made to buy your property'
# result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
# print(result)
        


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

with open('user.json', 'r') as jsonfile:
    curr = json.load(jsonfile)


class Input(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class WindowManager(ScreenManager):
    pass

class MainLayout(MDBoxLayout):
    pass

class AccountLoginPage(Screen):
    pass

class HomeScreen(Screen):
    text = StringProperty()
    text = curr['email']

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        print('pre-entering')
        size = Window.size[1]
        real_size = str(size/3-60) + 'dp'
        print(real_size)
        print(Window.size[1])
        print(Window.size[0])
        self.ids.btn.user_font_size = real_size
        return super().on_pre_enter(*args)
        

    def on_enter(self, *args):
        print('entered')
        return super().on_enter(*args)
        

class SearchButton(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        
       


class HomeCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    phonenumber = StringProperty()
    description = StringProperty()

class PropertyRentCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
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
   
        

       
            
        

    # def house_type(self, texta):
    #     self.poop = texta
    #     again = db.child("People").child("Rent").child(self.user['localId']).child("house").get()
    #     self.new()
    #     for u in again.each():
    #         db.child("People").child("Rent").child(self.user['localId']).child("house").child(u.key()).update({'housetype': self.poop})

    # def new(self):
    #     print(self.poop)

class PropertySaleCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
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
   
           
    # def submit(self, tot, country, town, street, bedrooms, bathrooms, landspace, price):
    #     self.poop = tot
    #     again = db.child("People").child("Sale").child(self.user['localId']).child("house").get()
    #     self.new()
    #     for u in again.each():
    #         db.child("People").child("Sale").child(self.user['localId']).child("house").child(u.key()).update({'housetype': self.poop})




    def okay(self):
        print('Okay')

    
class DetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    country = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    phonenumber = StringProperty()
    description = StringProperty()

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
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    description = StringProperty()

class EditRentDetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    country = StringProperty()
    town = StringProperty()
    street = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    key = StringProperty()
    local_image = StringProperty()
    description = StringProperty()
    
class SearchScreen(Screen):
    pass

class SearchLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new_country = ''
        self.new_choice = ''
    def search(self, choice, country, town, street):
        
        print(choice)
            
        if country != self.new_country or choice != self.new_choice:
            print('is not equal')
            self.new_country = country
            self.new_choice = choice
            self.clear_widgets()
        else:
            print('is equal')
        try:
            people = db.child("People").child(choice).get()
            
            for person in people.each():
                something = person.key()
                print(something)
                
                again = db.child("People").child(choice).child(something).child("house").get()

                for u in again.each():
                    if u.val()['country'] == country:
                        self.card = HomeCards()
                        self.card.image = u.val()['url']
                        self.card.tot = u.val()['housetype']
                        self.card.country = u.val()['country']
                        self.card.town = u.val()['town']
                        self.card.street = u.val()['street']
                        self.card.bedrooms = u.val()['bedrooms']
                        self.card.bathrooms = u.val()['bathrooms']
                        self.card.landspace = u.val()['landspace']
                        self.card.email = u.val()['email']
                        self.card.price = u.val()['price']
                        self.card.key = u.key()
                        self.card.phonenumber = u.val()['phonenumber']
                        self.card.description = u.val()['description']
                        self.add_widget(self.card)
                        print(u.val()['country'])

        except:
            pass
        
        
        #     print(u.val())

#-NGy3yrvpMXT0jYugGKH

class ReturnButton(MDCard):
    positionx = int(Window.size[1]*0.45)
    positiony = int(Window.size[0]*0.8)

class LoginScreen(Screen):
    bedrooms = StringProperty('0')
    bathrooms = StringProperty('0')
    


class RentSubmit(Screen):
    bedrooms = StringProperty('0')
    bathrooms = StringProperty('0')

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

class PropertyCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # threading.Thread(target=self.added).start()
        
        self.added()
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
    # @mainthread
    def added(self):
        
        with open('user.json', 'r') as jsonfile:
            dato = json.load(jsonfile)
        try:
            againi = db.child("People").child("Sale").child(dato['localid']).child("house").get()

            for u in againi.each():
                self.card = PropertySaleCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                self.card.country = u.val()['country']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.local_image = u.val()['local_image']
                self.card.phonenumber = u.val()['phonenumber']
                self.card.description = u.val()['description']
                self.add_widget(self.card)
            


            
            again = db.child("People").child("Rent").child(dato['localid']).child("house").get()

            for u in again.each():
                self.cardi = PropertyRentCards()
                self.cardi.image = u.val()['url']
                self.cardi.tot = u.val()['housetype']
                self.cardi.country = u.val()['country']
                self.cardi.bedrooms = u.val()['bedrooms']
                self.cardi.bathrooms = u.val()['bathrooms']
                self.cardi.landspace = u.val()['landspace']
                self.cardi.email = u.val()['email']
                self.cardi.price = u.val()['price']
                self.cardi.key = u.key()
                self.card.town = u.val()['town']
                self.card.street = u.val()['street']
                self.card.local_image = u.val()['local_image']
                self.card.phonenumber = u.val()['phonenumber']
                self.card.description = u.val()['description']
                self.add_widget(self.cardi)
        except:
            pass
        

                

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
    
        
        self.added()
    def added(self):
        try:
            people = db.child("People").child("Sale").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                
                    
                    
                    again = db.child("People").child("Sale").child(something).child("house").get()
                
                    for u in again.each():
                        self.card = HomeCards()
                        self.card.image = u.val()['url']
                        self.card.tot = u.val()['housetype']
                        self.card.country = u.val()['country']
                        self.card.town = u.val()['town']
                        self.card.street = u.val()['street']
                        self.card.bedrooms = u.val()['bedrooms']
                        self.card.bathrooms = u.val()['bathrooms']
                        self.card.landspace = u.val()['landspace']
                        self.card.email = u.val()['email']
                        self.card.price = u.val()['price']
                        self.card.key = u.key()
                        self.card.phonenumber = u.val()['phonenumber']
                        self.card.description = u.val()['description']
                        self.add_widget(self.card)

        except:
            pass
        

        
        
           
        


        

class RentCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.added()
    def added(self):
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
        try:
            people = db.child("People").child("Rent").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                
                    next = db.child("People").child("Rent").child(something).get()
                    for i in next.each():
                        if "house" not in i.key():
                            pass
                        else:
                            again = db.child("People").child("Rent").child(something).child("house").get()
                        
                            for u in again.each():
                                self.card = HomeCards()
                                self.card.image = u.val()['url']
                                self.card.tot = u.val()['housetype']
                                self.card.country = u.val()['country']
                                self.card.town = u.val()['town']
                                self.card.street = u.val()['street']
                                self.card.bedrooms = u.val()['bedrooms']
                                self.card.bathrooms = u.val()['bathrooms']
                                self.card.landspace = u.val()['landspace']
                                self.card.email = u.val()['email']
                                self.card.price = u.val()['price']
                                self.card.key = u.key()
                                self.card.phonenumber = u.val()['phonenumber']
                                self.card.description = u.val()['description']
                                self.add_widget(self.card)
        except:
            pass

        
        


class BookmarkScreen(Screen):
    pass
    

class BookmarkLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            people = db.child("People").child("Sale").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                    # next = db.child("People").child("Sale").child(something).get()
                    # for i in next.each():
                    #     if "house" not in i.key():
                    #         pass
                    #     else:
                    again = db.child("People").child("Sale").child(something).child("house").get()
                    for u in again.each():
                        
                        if u.key() in curr['bookmarks']:
                        
                            self.card = HomeCards()
                            self.card.image = u.val()['url']
                            self.card.tot = u.val()['housetype']
                            self.card.country = u.val()['country']
                            self.card.town = u.val()['town']
                            self.card.street = u.val()['street']
                            self.card.bedrooms = u.val()['bedrooms']
                            self.card.bathrooms = u.val()['bathrooms']
                            self.card.landspace = u.val()['landspace']
                            self.card.email = u.val()['email']
                            self.card.price = u.val()['price']
                            self.card.key = u.key()
                            self.card.phonenumber = u.val()['phonenumber']
                            self.card.description = u.val()['description']
                            self.add_widget(self.card)

            people = db.child("People").child("Rent").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                    next = db.child("People").child("Rent").child(something).get()
                    for i in next.each():
                        if "house" not in i.key():
                            pass
                        else:
                            again = db.child("People").child("Rent").child(something).child("house").get()
                            for u in again.each():
                                
                                if u.key() in curr['bookmarks']:
                                    
                                    
                                    self.card = HomeCards()
                                    self.card.image = u.val()['url']
                                    self.card.tot = u.val()['housetype']
                                    self.card.country = u.val()['country']
                                    self.card.town = u.val()['town']
                                    self.card.street = u.val()['street']
                                    self.card.bedrooms = u.val()['bedrooms']
                                    self.card.bathrooms = u.val()['bathrooms']
                                    self.card.landspace = u.val()['landspace']
                                    self.card.email = u.val()['email']
                                    self.card.price = u.val()['price']
                                    self.card.key = u.key()
                                    self.card.phonenumber = u.val()['phonenumber']
                                    self.card.description = u.val()['description']
                                    self.add_widget(self.card)
        except:
            pass
            
# princekofasiedu



                    
                    



        

class MainApp(MDApp):
    def build(self):

        screens = [HomeScreen(name="Home"), DetailsScreen(name="detail"), LoginScreen(name="Login"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SignInScreen(name="sign-in"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks'), EditDetailsScreen(name='edit'), LoadingScreen(name="loading")]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        
        
        
        self.login = LoginScreen()
        self.signup = AccountLoginPage()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.SaleOrRent = SaleOrRent()
        self.rent = RentSubmit()
        self.home = HomeScreen()
        self.search = SearchScreen()
        self.loading = LoadingScreen(name="loading")

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
            width_mult=4
        )

        for i in choice_items:
            self.choice.items.append(i)
        self.choice.bind()

        size = Window.size[1]
        real_size = str(size/3-60) + 'dp'
        print(real_size)
        print(Window.size[1])
        print(Window.size[0])
        self.home.ids.btn.user_font_size = real_size
        
  
        Window.bind(on_keyboard=self.switchback)


        self.something = False
        if self.something == True:
            print(self.something)
            threading.Thread(target=self.added, daemon=True)
        
        with open('user.json', 'r') as jsonfile:
            self.data = json.load(jsonfile)
            print(data['email'])

        for i in screens:
            self.wm.add_widget(i)
        
        self.wm.current = "Home"
        self.wm.transition = SwapTransition()
        self.numberiy = 'item 0'
        
        self.mail = ''
        self.passwrd = ''
        self.confirmed = ''
        self.sign_in_mail = ''
        self.sign_in_pass = ''

        self.tot = ''
        self.country = ''
        self.town = ''
        self.street = ''
        self.bedrooms = ''
        self.bathrooms = ''
        self.landspace = ''
        self.price = ''
        self.phonenumber = ''
        self.desc = ''
        return self.wm
        return super().build()

    def set_item(self, text_item):
        self.search.ids.drop_item.set_item(text_item)
        
        self.search.ids.drop_item.text = text_item
        
        # self.choice.dismiss()
    
    def callback_for_menu_items(self, *args):
        toast(args[0])

    def call_back(self, text_of_option):
        print(text_of_option)
    
        
    def call(self, obg, icon):
        if icon == 'phone':
            print(obg + " " + 'is a phone number')
        elif icon == 'mail':
            print(obg + " " + 'is an email address')


    def show_bottom(self, email, phone_number):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            email: "mail",
            phone_number: "phone"
        }
        for item in data.items():
            print(item[0][0])
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0], z=item[1]: self.call(y, z),
                icon_src = item[1]
            )
        bottom_sheet_menu.open()

    
        

    def switch_home(self):
        
        self.wm.switch_to(self.home)

    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, phonenumber=None, description=None, key=None):
        self.wm.switch_to(self.loading)
        self.detail = DetailsScreen()
        self.detail.image = image
        self.detail.type = House_type
        self.detail.price = pricing
        self.detail.country = locate
        self.detail.town = town
        self.detail.street = street
        self.detail.bedrooms = bedrooms
        self.detail.bathrooms = bathrooms
        self.detail.landspace = landspace
        self.detail.email = email
        self.detail.phonenumber = phonenumber
        self.detail.description = description
        self.detail.key = key
        self.wm.switch_to(self.detail)

    def switch_search(self):
        self.wm.switch_to(self.search)
        

    def switch_login(self):
        self.wm.switch_to(self.login)

    def switch_rent(self):
        self.wm.switch_to(self.rent)

    def switch_signup(self):
        self.wm.switch_to(self.signup)

    def switch_products(self):
        
        
        self.products = MyProducts()
       
        self.wm.switch_to(self.products)

    def switch_bookmarks(self):
        self.wm.switch_to(self.loading)
        self.bk = BookmarkScreen()
        
        self.wm.switch_to(self.bk)
    
    def switch_signin(self):
        self.wm.switch_to(self.signin)

    

    def switchback(self,window,key,*largs):
        if self.wm.current != "Home":
            if key == 27:
                self.wm.switch_to(self.home) 
                
                return True
    
    def switch_saleorrent(self):
        try:
            
            with open('user.json', 'r') as jsonfile:
                data = json.load(jsonfile)
            
            if data['email'] == "":
                        
                self.wm.switch_to(self.signin)
            else:
                self.wm.switch_to(self.loading)
                self.wm.transition = NoTransition()
                self.user = authi.sign_in_with_email_and_password(data['email'], data['password'])
                self.wm.switch_to(self.SaleOrRent)
        except:
            self.snackbar("No internet connection")
        

    def email(self, texta):
        self.mail = texta
        

    def phone(self, texta):
        self.phonenumber = texta


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
        self.country = texta

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
            
    def send_email(self, email, phonenumber):
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        if data['email'] == "":
            self.wm.switch_to(self.signin)
        else:
            # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            # server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
            # server.sendmail("anangjosh8@gmail.com", email, "An offer has been made to buy your house.")
            # server.quit()
            self.show_bottom(email, phonenumber)


    def account_submit(self):
        email = self.mail
        password = self.passwrd
        print(self.signup.ids.confirm.text)
        
        
        
        try:
            response = requests.get('https://isitarealemail.com/api/email/validate', params= {'email':email})

            status = response.json()['status']
            if status == "valid":

                if self.signup.ids.confirm.text == password:
                    user = authi.create_user_with_email_and_password(email, password)
                    useri = authi.send_email_verification(user['idToken'])
                    self.switch_products()

                else:
                    text = "Password does not match"
                    close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                    self.show_dialog(text, close_button)
            else:
                text = "Invalid email"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
        except:
            text = "Password must be at least 6 characters"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)

        
            

        
    def delete_property(self, name):
        print(name + "Delete Delete Delete Delete Delete Delete Delete")
        db.child("People").child("Sale").child(curr['localid']).child("house").child(name).remove()
        db.child('People').child("Rent").child(curr['localid']).child("house").child(name).remove()

    def password_reset(self, email):
        try:
            if email != "":
                authi.send_password_reset_email(email)
                text = "A password reset email has been sent to your mail"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
            else:
                text = "Please type in yout email in the space"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)
        except:
            pass

# "MKHRXCSZPZWXKIIF"


    def sign_in(self):
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
                curr = json.load(jsonfile)
                print(curr['email'])
            
            curr['email'] = self.mail
            curr['password'] = self.passwrd
            curr['idToken'] = self.user['idToken']
            curr['localid'] = self.user['localId']

            with open('user.json', 'w') as jsonfile:
                json.dump(curr, jsonfile)
            self.switch_products()
            self.home.text = curr['email']
            
        except:
            text = "Invalid email or password"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)

        

    
    def editscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None):
        self.edit = EditDetailsScreen()
        self.wm.switch_to(self.edit)
        self.edit.type = House_type
        self.edit.image = image
        self.edit.price = pricing
        self.edit.country = locate
        self.edit.town = town
        self.edit.street = street
        self.edit.bedrooms = bedrooms
        self.edit.bathrooms = bathrooms
        self.edit.landspace = landspace
        self.edit.email = email
        self.edit.key = key
        self.edit.local_image = local_image
        self.edit.description = description

    def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None):
        self.edit_rent = EditRentDetailsScreen()
        self.wm.switch_to(self.edit_rent)
        self.edit_rent.type = House_type
        self.edit_rent.image = image
        self.edit_rent.price = pricing
        self.edit_rent.country = locate
        self.edit_rent.town = town
        self.edit_rent.street = street
        self.edit_rent.bedrooms = bedrooms
        self.edit_rent.bathrooms = bathrooms
        self.edit_rent.landspace = landspace
        self.edit_rent.email = email
        self.edit_rent.key = key
        self.edit_rent.local_image = local_image
        self.edit_rent.description = description
    

    def update_property(self, local_image, House_type, pricing, locate, town, street, bedrooms, bathrooms, landspace, key, description):
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
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        with open('user.json', 'r') as jsonfile:
            self.datp = json.load(jsonfile)
        # pp = int(pricing)
        # print(pp)
        

        if len(House_type) > 5 and len(House_type) < 21:
            
            if len(locate) >= 3 and len(locate) < 16:
                
                if len(town) >= 3 and len(town) < 16:

                    if len(street) >= 3 and len(street) < 25:
                        if len(pricing) > 1:
                            if len(description) > 20 and len(description) < 255:
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'housetype': House_type})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'country': locate})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'town': town})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'street': street})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'bedrooms': bedrooms})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'bathrooms': bathrooms})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'landspace': self.landspace})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'price': self.amt})
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'description': description})
                                agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function)
                                exit = MDFlatButton(text="close", on_release=self.close_dialog)
                                info = "Do you want to change your image?"
                                self.show_dialog(info,exit,agree_button)
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
                text = "country must be between 2 and 16 characters"
                self.show_dialog(text,close_button)
                self.edit.ids.location.error = True
        else:
            text = "House type must be between 5 and 21 characters characeters"
            self.show_dialog(text,close_button)
            self.edit.ids.housetype.error = True

    

    def update_rent_property(self, local_image, House_type, pricing, locate, town, street, bedrooms, bathrooms, landspace, key, description):
        self.rent_key = key
        self.rent_local_image = local_image
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        with open('user.json', 'r') as jsonfile:
            self.datp = json.load(jsonfile)

        if pricing[0] == '$' and pricing[-1:-4] == '/mth':
            self.amt = pricing
        else:
            self.amt = "$" + pricing + '/mth'

        if landspace[-1] == 't':
            self.landspace = landspace
        else:
            self.landspace = landspace + 'sq.ft'
        # pp = int(pricing)
        # print(pp)
        

        if len(House_type) > 5 and len(House_type) < 21:
            
            if len(locate) >= 3 and len(locate) < 16:
                
                if len(town) >= 3 and len(town) < 16:

                    if len(street) >= 3 and len(street) < 25:
                        if len(pricing) > 1:
                            if len(description) > 20 and len(description) < 255:
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'housetype': House_type})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'country': locate})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'town': town})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'street': street})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'bedrooms': bedrooms})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'bathrooms': bathrooms})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'landspace': self.landspace})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'price': self.amt})
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'description': description})
                                agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function)
                                exit = MDFlatButton(text="close", on_release=self.close_dialog)
                                info = "Do you want to change your image?"
                                self.show_dialog(info,exit,agree_button)
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
                text = "country must be between 2 and 16 characters"
                self.show_dialog(text,close_button)
                self.edit_rent.ids.location.error = True
        else:
            text = "House type must be between 5 and 21 characters characeters"
            self.show_dialog(text,close_button)
            self.edit_rent.ids.housetype.error = True

    def separate_function(self, obj):
        filechooser.open_file(on_selection=self.change_image, multiselect=True)
        
    def change_image(self, selection):
    
        if len(selection) > 0:
            self.new_file = str(selection[0])
            print(self.local_image)
            # urli = storage.child(data['localid']).child(self.local_image).get_url(data['idToken'])
            # tokenop = "https://firebasestorage.googleapis.com/v0/b/first-db-77609.appspot.com/o/2C8VZdiEBCMhnFS0fnvzpa4jW2F2%2FC%3A%5CUsers%5CYvonne%5CDownloads%5Cbeautiful-house-15.jpg?alt=media"
            # storage.child(self.data['localid']).delete(self.local_image, urli)
            # print('SUccessfully deleted')
            
            # img = storage.child(self.data['localid']).child(self.local_image).get_url(None)
            
            user = authi.sign_in_with_email_and_password(data['email'], data['password'])
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
            db.child("People").child("Sale").child(self.datp['localid']).child("house").child(self.key).update({'local_image': self.new_file})
            db.child("People").child("Sale").child(self.datp['localid']).child("house").child(self.key).update({'url': url})
            # db.child("People").child("Sale").child(self.data['localid']).child("house").child(self.rent_key).update({'url': url})
        else:
            pass

    def sign_out(self):
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)

        data['email'] = ''
        data['password'] = ''
        data['idToken'] = ''
        data['house_images'] = []
        data['localid'] = ''
        data['bookmarks'] = []
        with open('user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)


    def delete_user(self, obj):
        
        try:
            user = authi.sign_in_with_email_and_password(data['email'], data['password'])
            db.child("People").child(user['localId']).remove()
            with open('user.json', 'r') as jsonfile:
                dati = json.load(jsonfile)
                
            for i in dati['house_images']:
                storage.delete(i, user['idToken'])
                
            with open('user.json', 'w') as jsonfile:
                json.dump(dati, jsonfile)
            
            authi.delete_user_account(user['idToken'])

            with open('user.json', 'r') as jsonfile:
                dato = json.load(jsonfile)
                print(dato['email'])
            dato['email'] = ''
            dato['password'] = ''
            dato['idToken'] = ''
            dato['house_images'] = []
            with open('user.json', 'w') as jsonfile:
                json.dump(dato, jsonfile)
            
            
            print("successfully deleted account")
        except:
            print("No user signed in")
            p = 'No user signed in'
            self.snackbar(p)
            # text = "yes"
            # self.close_dialog(text)
            # close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            # notice = "No user signed in"
            # self.show_dialog(notice, close_button)
    
    def delete_user_notice(self):
        agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.delete_user)
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        info = "Are you sure"
        self.show_dialog(info,close_button, agree_button)

    def switch_account(self):
        self.sign_out()
        email = self.mail
        password = self.passwrd
        user = authi.sign_in_with_email_and_password(email, password)
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        
        data['email'] = self.mail
        data['password'] = self.passwrd
        
        with open('user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
            
        self.change_screen("products")

    def bookmark(self, lola):
        print(lola + "HOOOOOOOOOLLLLLAAAAA GAAAAANNNNNGGGGG!!!!!!")
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
                text = "Already added to bookmarks"
                close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                self.show_dialog(text, close_button)

            
        except:
            print("Unsuccessfully added to bookmarks")

    def selected(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])
        if len(self.tot) > 5:
            
            if len(self.country) >= 3 and len(self.country) < 16:
                
                if self.mail == self.info['email']:
                    # phone = '+2332222222222'
                    if self.phonenumber != '':
                        phone_number  = phonenumbers.parse(self.phonenumber)
                        valid = phonenumbers.is_valid_number(phone_number)
                        print(valid)
                        if valid == True:
                            if len(self.town) >= 3 and len(self.town) < 16:

                                if len(self.street) >= 6 and len(self.street) < 25:
                                    if len(self.price) > 1:
                                        if len(self.desc) > 20 and len(self.desc) < 100:
                                            filechooser.open_file(on_selection=self.house_sale, multiselect=True)
                                        else:
                                            info = "description must be between 20 and 100 characters"
                                            self.show_dialog(info,close_button)
                                    else:
                                        info = "Invalid input for price"
                                        self.show_dialog(info,close_button)
                                else:
                                    info = "street must be between 6 and 25 characters"
                                    self.show_dialog(info,close_button)

                            else:
                                info = "town must be between 2 and 16 characters"
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

    
    def house_sale(self, selection):
        
        
            
        if len(selection) > 0:
            self.file = str(selection[0])
            storage.child(self.info['localid']).child(str(self.file)).put(str(self.file))
            url = storage.child(self.info['localid']).child(self.file).get_url(None)
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
                "town": "",
                "street": "",
                "bedrooms": "",
                "bathrooms": "",
                "landspace": "",
                "url": "",
                "email": "",
                "phonenumber": "",
                "price": "",
                "local_image": "",
                "description": ""
            }

            
            data['housetype'] = self.tot
            data['country'] = self.country
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
            # db.child("People").child(key).child("house").push(data)
            results = db.child("People").child("Sale").child(self.user['localId']).child("house").push(data)
            print(results)
        # except:
        #     close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        #     info = 'Oops something went wrong'
        #     self.show_dialog(info, close_button)
        
        
        
            # for person in people.each():
            #     if person.val()['email'] == self.sign_in_mail:
            #         print(person.key())
            #         key = person.key()
                    # housetype = "housetype"
                    # location = "location"
                    # bedrooms = "bedrooms"
                    # bathrooms = "bathrooms"
                    # landspace = "landspace"
                    # link = "link"
                    # print(url)
                    # db.child("People").child(key).child(housetype).set(self.tot)
                    # db.child("People").child(key).child(location).set(self.location)
                    # db.child("People").child(key).child(bedrooms).set(self.bedrooms)
                    # db.child("People").child(key).child(bathrooms).set(self.bathrooms)
                    # db.child("People").child(key).child(landspace).set(self.landspace)
                    # db.child("People").child(key).child(link).set(url)

                
        

    def rent_property(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        if len(self.tot) > 5:
            
            if len(self.country) > 3 and len(self.country) < 16:
                if self.mail == curr['email']:
                    # phone = '+2332222222222'
                    if self.phonenumber != '':
                        phone_number  = phonenumbers.parse(self.phonenumber)
                        valid = phonenumbers.is_valid_number(phone_number)
                        print(valid)
                        if valid == True:
                            if len(self.town) >= 3 and len(self.town) < 16:

                                if len(self.street) >= 6 and len(self.street) < 25:
                                    if len(self.price) > 1:
                                        if len(self.desc) > 20 and len(self.desc) < 100:
                
                                            filechooser.open_file(on_selection=self.house_rent, multiselect=True)
                                        else:
                                            info = "description must be between 20 and 100 characters"
                                            self.show_dialog(info,close_button)
                                    else:
                                        info = "Invalid input for price"
                                        self.show_dialog(info,close_button)
                                else:
                                    info = "street must be between 6 and 25 characters"
                                    self.show_dialog(info,close_button)

                            else:
                                info = "town must be between 2 and 16 characters"
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

    def house_rent(self, selection):
        

        try:
            if len(selection) > 0:
                self.file = str(selection[0])
                storage.child(curr['localid']).child(str(self.file)).put(str(self.file))
                url = storage.child(curr['localid']).child(self.file).get_url(None)

            
                curr['house_images'].append(self.file)
                with open('user.json', 'w') as jsonfile:
                    json.dump(curr, jsonfile)
                
                data = {
                    "housetype": "",
                    "country": "",
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
                    "description": ""
                }

                
                data['housetype'] = self.tot
                data['country'] = self.country
                data['street'] = self.street
                data['town'] = self.town
                data['bedrooms'] = self.bedrooms
                data['bathrooms'] = self.bathrooms
                data['landspace'] = self.landspace + 'sq.ft'
                data['url'] = url
                data['email'] = curr['email']
                data['price'] = "$" + self.price + '/mth'
                data['local_image'] = self.file
                data['phonenumber'] = self.phonenumber
                data['description'] = self.desc
                # db.child("People").child(key).child("house").push(data)
                results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
                print(results)
        except:
            pass

MainApp().run()

firemail = 'first-db-77609.firebaseapp.com'