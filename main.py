
import phonenumbers
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
from kivymd.uix.list import MDList, OneLineListItem, ImageLeftWidget, OneLineIconListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.behaviors import CommonElevationBehavior, FakeRectangularElevationBehavior
from kivymd.uix.snackbar import Snackbar

import pyrebase
import re

from kivy.clock import time

from kivy.uix.textinput import TextInput

import firebase_admin
from firebase_admin import storage as admin_storage, credentials, firestore, exceptions
from firebase_admin.instance_id import _get_iid_service

from firebase_admin.messaging import Message, Notification

from firebase_admin import auth

from pyfcm import FCMNotification

from plyer import filechooser
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import smtplib

from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.uix.scrollview import ScrollView


from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton
import webbrowser

import threading
import requests



button = MDIconButton



        



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

push_service = FCMNotification(api_key=api)



# client = auth._get_client()
# print(client)

# tgen = TokenGenerator()
# now = tgen.create_custom_token('firebase_token')


with open('user.json', 'r') as jsonfile:
    curr = json.load(jsonfile)
    print(curr['localid'])
    
    if curr['email'] == "":
        print("Fase")
        
    else:
        try:
            print("bruuhhh")
            user = authi.sign_in_with_email_and_password(curr['email'], curr['password'])
            user = authi.refresh(user['refreshToken'])
            ino = authi.get_account_info(user['idToken'])
            print(ino)
            curr['idToken'] = user
           
        except:
            pass
txt = 'C:/Users/Yvonne/Downloads/beautiful-house-15.jpg'
x = re.search(r".jpg$", txt)
if x:
    print('yes there is a match')
else:
    print('no match at all')


# registration_id = "1"
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
Builder.load_file('DialogEntry.kv')
Builder.load_file('TheCreator.kv')
Builder.load_file('AppTutorial.kv')
Builder.load_file('Congrats.kv')
Builder.load_file('ForgotPasswordEntry.kv')




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

class HomeScreen(Screen):
    text = StringProperty()
    text = curr['email']

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        print('pre-entering')
        print(str(self.ids.grid_card.width) + " " + 'is the width of the grid card')
        # size = Window.size[1]
        # real_size = str(size/3-60) + 'dp'
        # print(real_size)
        # print(Window.size[1])
        # print(Window.size[0])
        # self.ids.btn.user_font_size = real_size
        # self.ids.btn.md_bg_color = [1,1,1,1]
        return super().on_pre_enter(*args)
        

    def on_enter(self, *args):
        print('entered')
        return super().on_enter(*args)
        



        
       


class HomeCards(MDCard, CommonElevationBehavior):
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
    telegram = StringProperty()
    facebook = StringProperty()
    description = StringProperty()
    amenities = ListProperty()
    



class PropertyRentCards(MDCard, CommonElevationBehavior):
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

class PropertySaleCards(MDCard, CommonElevationBehavior):
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
    amenities = ListProperty(['No', 'No', 'No', 'No', 'No', 'No'])
   
           
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
    telegram = StringProperty()
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
        self.last = '-NL7lsIZbmkxuhMeprct'
        self.something = '7ifomlRiqKZOnCqUibGjX9E1p1x1'
    def search(self, choice, country, town, street):
        
        print(choice)
            
        if country != self.new_country or choice != self.new_choice:
            print('is not equal')
            self.new_country = country
            self.new_choice = choice
            self.clear_widgets()
        else:
            print('is equal')
        
        # people = db.child("People").child(choice).get()
        
        # for person in people.each():
        #     something = person.key()
        #     print(something)
            
        again = db.child("People").child(choice).order_by_key().start_at(self.something).get()
        print(again.val())
        for u in again.each():
            print(u.key())
            house = u.val()['house']
            
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
                self.card.telegram = u.val()['telegram']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                self.last = u.key()
                self.j +=1 
                if self.j % 2 == 0:
                    break
                    
    def next(self, choice, country, town, street):
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
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                dato['house_images'].append(u.val()['local_image'])
            


            
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
                self.cardi.town = u.val()['town']
                self.cardi.street = u.val()['street']
                self.cardi.local_image = u.val()['local_image']
                self.cardi.phonenumber = u.val()['phonenumber']
                self.cardi.description = u.val()['description']
                self.add_widget(self.cardi)
                dato['house_images'].append(u.val()['local_image'])

            with open('user.json', 'w') as jsonfile:
                json.dump(dato, jsonfile)
                
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
    
        self.j = 0
        self.last = ''
        self.something = ''
    #     self.added()
    # def added(self):
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
            people = db.child("People").child("Sale").get()
            if people.each():
                for person in people.each():
                    self.something = person.key()
                    # another = person.val()
                    print('First iteration')
                    print(self.something)
                    if self.j == 1: 
                        break
                    
                    again = db.child("People").child("Sale").child(self.something).child("house").get()
                    print(again.val())
        
                    for u in again.each():
                        print(u.val()['amenities'])
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
                        self.card.telegram = u.val()['telegram']
                        self.card.facebook = u.val()['facebook']
                        self.card.description = u.val()['description']
                        self.card.amenities = u.val()['amenities']
                        self.add_widget(self.card)
                        self.last = u.key()
                        print('second iteration')
                        self.j += 1
                        print(str(self.j) + ' ' + 'this is jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                        if self.j == 1: 
                            break
                        print(self.something)
        except:
            pass

        
       

    def other(self):
        # if self.something == '':
        #     try:
        #         people = db.child("People").child("Sale").get()
        #         if people.each():
        #             for person in people.each():
        #                 self.something = person.key()
        #     except:
        #         pass
        # else:
        print('Is it working')
        print(self.last)
        print(self.something + " " + "This is self.something and its supposed to be working but it's not.")
        again = db.child("People").child("Sale").order_by_key().start_at(self.something).limit_to_first(2).get()
        print(again.val())
        for i in again.each():
            # for i in u.val()['house']['-NL8x6ZNQQFpsXDfgm7c']['bathrooms']:
                
            #     print(i)
            self.something = i.key()
            print(self.something)
            againi = db.child("People").child("Sale").child(self.something).child("house").get()
            for u in againi.each():
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
                self.card.telegram = u.val()['telegram']
                self.card.facebook = u.val()['facebook']
                self.card.description = u.val()['description']
                self.card.amenities = u.val()['amenities']
                self.add_widget(self.card)
                self.last = u.key()
        
        # print(again.val())
        # print(self.last)
    
        
    


        

class RentCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.added()
        self.last = ''
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
                    self.something = person.key()
                    # another = person.val()
                    
                
                    # next = db.child("People").child("Rent").child(something).get()
                    # for i in next.each():
                    #     if "house" not in i.key():
                    #         pass
                    #     else:
                    again = db.child("People").child("Rent").child(self.something).child("house").get()
                
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
                        self.card.telegram = u.val()['telegram']
                        self.card.facebook = u.val()['facebook']
                        self.card.description = u.val()['description']
                        self.card.amenities = u.val()['amenities']
                        self.add_widget(self.card)
        except:
            pass

    def other(self):
        again = db.child("People").child("Rent").child(self.something).child("house").order_by_key().start_at(self.last).get()
        for u in again.each():
            print(u.val()['amenities'])
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
            self.card.telegram = u.val()['telegram']
            self.card.facebook = u.val()['facebook']
            self.card.description = u.val()['description']
            self.card.amenities = u.val()['amenities']
            self.add_widget(self.card)
            self.last = u.key()
        


class BookmarkScreen(Screen):
    pass
    

class BookmarkLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('user.json', 'r') as jsonfile:
            curr = json.load(jsonfile)
            
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
                            self.card.telegram = u.val()['telegram']
                            self.card.facebook = u.val()['facebook']
                            self.card.description = u.val()['description']
                            self.add_widget(self.card)

            people = db.child("People").child("Rent").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                    # next = db.child("People").child("Rent").child(something).get()
                    # for i in next.each():
                    #     if "house" not in i.key():
                    #         pass
                    #     else:
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
                            self.card.telegram = u.val()['telegram']
                            self.card.facebook = u.val()['facebook']
                            self.card.description = u.val()['description']
                            self.add_widget(self.card)
        except:
            pass


class DialogEntry(MDBoxLayout):
    pass


class ForgotPasswordEntry(MDBoxLayout):
    pass
            
# princekofasiedu



                    
                    



        

class MainApp(MDApp):
    def build(self):

        screens = [HomeScreen(name="Home"), DetailsScreen(name="detail"), SaleSubmit(name="Sale"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SignInScreen(name="sign-in"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks'), EditDetailsScreen(name='edit'), EditRentDetailsScreen(name='edit-rent'), LoadingScreen(name="loading"), CreatorScreen(name='creator'), Congrats(name='congrats')]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        
        
        
        self.sale = SaleSubmit()
        self.signup = AccountLoginPage()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.SaleOrRent = SaleOrRent()
        self.rent = RentSubmit()
        self.home = HomeScreen()
        
        
        self.search = SearchScreen()
        self.loading = LoadingScreen(name="loading")
        self.creator_screen = CreatorScreen(name='creator')
        self.tutorial = AppTutorial(name='tutor')
        self.congrats = Congrats(name='congrats')
        

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
        
        

        
        
        


        # size = Window.size[1]
        # real_size = str(size/3-60) + 'dp'
        # print(real_size)
        # print(Window.size[1])
        # print(Window.size[0])
        # self.home.ids.btn.user_font_size = real_size
        
  
        Window.bind(on_keyboard=self.switchback)


        self.something = False
        if self.something == True:
            print(self.something)
            threading.Thread(target=self.added(), daemon=True)
        
        with open('user.json', 'r') as jsonfile:
            self.data = json.load(jsonfile)
            print(self.data['email'])

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
        self.amenities = ['No', 'No', 'No', 'No', 'No', 'No']
        self.telegram = ''
        self.facebook = ''
        return self.wm
        return super().build()

    def on_start(self):
        

        print("Starting")

        return super().on_start()

    def set_item(self, text_item):
        self.search.ids.drop_item.set_item(text_item)
        
        self.search.ids.drop_item.text = text_item
        
        # self.choice.dismiss()

    def home_init(self):
        while True:
            self.home = HomeScreen()
    
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
            
        elif icon == 'telegram':
            print(obg + " " + 'is a telgram handle')
            webbrowser.open('https://t.me/' + obg)
        elif icon == 'facebook':
            print(obg + " " + 'is a facebook handle')
            webbrowser.open('https://m.me/' + obg)

    


    def show_bottom(self, email, phone_number, telegram, facebook):
        bottom_sheet_menu = MDGridBottomSheet()
        data = {
            email: "mail",
            phone_number: "whatsapp",
            telegram: "telegram",
            facebook: "facebook"
        }
        for item in data.items():
            print(item[0][0])
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0], z=item[1]: self.call(y, z),
                icon_src = item[1]
            )
        bottom_sheet_menu.open()

    
    def update(self):
        self.home = HomeScreen()

    def switch_home(self):
        
        self.wm.switch_to(self.home)

    

    def switch_creator(self):
        self.wm.switch_to(self.creator_screen)

    def switch_tutorial(self):
        self.wm.switch_to(self.tutorial)

    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, phonenumber=None, telegram=None, facebook=None, description=None, key=None, amenities=None):
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
        self.detail.telegram = telegram
        self.detail.facebook = facebook
        self.detail.description = description
        self.detail.key = key
        self.detail.amenities = amenities
        print(self.detail.amenities)
        self.wm.switch_to(self.detail)

    def switch_search(self):
        self.wm.switch_to(self.search)
        

    def switch_sale(self):
        self.wm.switch_to(self.sale)

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

    def switch_congrats(self):
        self.wm.switch_to(self.congrats)
    

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
                
                
                self.wm.switch_to(self.SaleOrRent)
        except:
            self.snackbar("No internet connection")
        

    def email(self, texta):
        self.mail = texta
        

    def phone(self, texta):
        self.phonenumber = texta

    def tg(self, texta):
        self.telegram = texta

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
            
    def send_email(self, email, phonenumber, telegram, facebook):
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        if data['email'] == "":
            self.wm.switch_to(self.signin)
        else:
            self.user = authi.sign_in_with_email_and_password(data['email'], data['password'])
            ino = authi.get_account_info(self.user['idToken'])
            if ino['users'][0]['emailVerified'] != True:
                self.dia = MDDialog(
                    title='Your email has not been verified!',
                    text='An email verification link has been sent to your email..check in spam',
                    buttons=[
                        MDFlatButton(
                            text='Cancel',
                            theme_text_color='Custom',
                            text_color='black',
                            on_press=lambda x:self.dia.dismiss()
                        )
                    ]
                )
            # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            # server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
            # server.sendmail("anangjosh8@gmail.com", email, "An offer has been made to buy your house.")
            # server.quit()
            else:
                self.show_bottom(email, phonenumber, telegram, facebook)


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
                    text = "An email verification link has been sent to your mail"
                    close_button = MDFlatButton(text="close", on_press=self.close_dialog)
                    self.show_dialog(text, close_button)
                    self.switch_products()
                    self.mail = ''
                    self.passwrd = ''
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
                
                
                user = authi.sign_in_with_email_and_password(curr['email'], curr['password'])
                storage.delete(user['localId'] + '/' + local_image, user['idToken'])
                curr['house_images'].remove(local_image)
                if sale_or_rent == 'Sale':
                    db.child("People").child("Sale").child(user['localId']).child("house").child(name).remove()
                else:
                    db.child('People').child("Rent").child(user['localId']).child("house").child(name).remove()
                p = 'Property Successfully deleted'
                self.snackbar(p)
                    
                self.passwrd = ''
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


    def sign_in(self):
        email = self.mail
        password = self.passwrd
        
        
        
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
            

        

        curr['email'] = self.mail
        curr['password'] = self.passwrd
        curr['idToken'] = self.user['idToken']
        curr['localid'] = self.user['localId']

        againi = db.child("People").child("Sale").child(curr['localid']).child("house").get()
        if againi.each():
            for i in againi.each():
                print(i.val()['local_image'])
                curr['house_images'].append(i.val()['local_image'])
        else:
            pass

        with open('user.json', 'w') as jsonfile:
            json.dump(curr, jsonfile)
        self.switch_products()

        p = 'Successfully signed in'
        self.snackbar(p)

        self.home.text = curr['email']
        self.mail = ''
        self.passwrd = ''

        # except requests.exceptions.HTTPError as e:
        #     error_json = e.args[1]
        #     error = json.loads(error_json)['error']['message']
        #     if error == 'EMAIL_NOT_FOUND':
        #         text = "Email not found"
        #         close_button = MDFlatButton(text="close", on_press=self.close_dialog)
        #         self.show_dialog(text, close_button)
        #         print('Email not found')
        #         self.mail = ''
        #     if error == 'INVALID_PASSWORD':
        #         text = "Invalid password"
        #         close_button = MDFlatButton(text="close", on_press=self.close_dialog)
        #         self.show_dialog(text, close_button)
        #         print('Invalid password')
        #         self.mail = ''
        # except:
        #     p = 'Oops something went wrong'
        #     self.snackbar(p)
        
        
        # except:
        #     p = 'No internet connection'
        #     self.snackbar(p)

        
            
        # except:
        #     text = "Invalid email or password"
        #     close_button = MDFlatButton(text="close", on_press=self.close_dialog)
        #     self.show_dialog(text, close_button)

        

    
    def editscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
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
        self.edit.amenities = amenities
        print(key, town, street)

    def editrentscreen(self, image=None, local_image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None, key=None, description=None, amenities=None):
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
        self.edit_rent.amenities = amenities
        print(key)
    

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
        amenities = self.amenities
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
                                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(key).update({'amenities': amenities})
                                agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function('Sale'))
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
                                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(key).update({'amenities': amenities})
                                agree_button = MDFlatButton(text="yes", on_release=self.close_dialog, on_press=self.separate_function('Rent'))
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

    def separate_function(self, obj, sale_or_rent):
        filechooser.open_file(on_selection=self.change_image(sale_or_rent), multiselect=True)
        
    def change_image(self, selection, sale_or_rent):
    
        if len(selection) > 0:
            self.new_file = str(selection[0])
            print(self.local_image)
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
            if sale_or_rent == 'Sale':
                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(self.key).update({'local_image': self.new_file})
                db.child("People").child("Sale").child(self.datp['localid']).child("house").child(self.key).update({'url': url})
            else:
                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(self.key).update({'local_image': self.new_file})
                db.child("People").child("Rent").child(self.datp['localid']).child("house").child(self.key).update({'url': url})
            p = 'Changes made successfully'
            self.snackbar(p)
            # db.child("People").child("Sale").child(self.data['localid']).child("house").child(self.rent_key).update({'url': url})
        else:
            pass

    def sign_out_auth(self):
        text = 'Are you sure you want to sign out'
        close_button = MDFlatButton(text="No", on_release=self.close_dialog)
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
                db.child("People").child("Sale").child(dato['localid']).remove()
                local = user['localId'] + '/'
                
                for i in dati['house_images']:
                    storage.delete(local + i, user['idToken'])
                # storage.delete(user['localId'], user['idToken'])
                    
                
                
                authi.delete_user_account(user['idToken'])

                with open('user.json', 'r') as jsonfile:
                    dato = json.load(jsonfile)
                    print(dato['email'])
                dato['email'] = ''
                dato['password'] = ''
                dato['idToken'] = ''
                dato['house_images'] = []
                dato['bookmarks'] = []
                dato['localid'] = ''
                with open('user.json', 'w') as jsonfile:
                    json.dump(dato, jsonfile)
                
                
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
        with open('user.json', 'r') as jsonfile:
            self.info = json.load(jsonfile)
            print(self.info['localid'])
        
        if len(self.tot) > 5:
            
            if len(self.country) >= 2 and len(self.country) < 16:
                
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
                                        if len(self.desc) > 20 and len(self.desc) < 255:
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
                info = "Country must be between 2 and 16 characters"
                self.show_dialog(info,close_button)
        else:
            text = "House type must be more than 5 characeters"
            self.show_dialog(text,close_button)

    
    def house_sale(self, selection):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        
        
            
        if len(selection) > 0:
            self.file = str(selection[0])
            print(self.file)
            print(self.file[-1:-4])
            
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
                "telegram": "",
                "facebook": "",
                "price": "",
                "local_image": "",
                "description": "",
                "amenities": [],
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
            data['amenities'] = self.amenities
            data['telegram'] = self.telegram
            data['facebook'] = self.facebook
            # db.child("People").child(key).child("house").push(data)
            results = db.child("People").child("Sale").child(self.info['localid']).child("house").push(data)
            print(results)
            self.switch_congrats()
            
        else:
            info = "You need to select an image to continue"
            self.show_dialog(info, close_button)
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
                if self.file[-1:-4] == '.jpg' or self.file[-1:-4] == '.png':
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
                        "telegram": "",
                        "facebook": "",
                        "description": "",
                        "amenities": "",
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
                    data['price'] = "$" + self.price + self.rent.ids.pay_item.text
                    data['local_image'] = self.file
                    data['phonenumber'] = self.phonenumber
                    data['telegram'] = self.telegram
                    data['facebook'] = self.facebook
                    data['description'] = self.desc
                    data['amenities'] = self.amenities
                    # db.child("People").child(key).child("house").push(data)
                    results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
                    print(results)
                    self.switch_congrats()
                else:
                    close_button = MDFlatButton(text="close", on_release=self.close_dialog)
                    info = "Please select an image"
                    self.show_dialog(info,close_button)
            else: 
                close_button = MDFlatButton(text="close", on_release=self.close_dialog)
                info = "You need to select an image to continue"
                self.show_dialog(info,close_button)
        except:
            pass

MainApp().run()

firemail = 'first-db-77609.firebaseapp.com'