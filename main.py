
import phonenumbers
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
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
from plyer import filechooser
import json
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import smtplib
from email.message import EmailMessage
import ezgmail
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivy.uix.scrollview import ScrollView
from kivy.effects.dampedscroll import DampedScrollEffect
from time import sleep, time
from kivy.clock import time
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.toast import toast
import webbrowser
import numpy as np







        
Window.size = (300, 600)

# firebaseconfig = {
#     "apiKey": "AIzaSyA4WwgZlTp-P42AYn8OuY8GZtNDA4TsGVs",
#     "authDomain": "dreams-home-database.firebaseapp.com",
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

firebase = pyrebase.initialize_app(firebaseconfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

signed_in = False

with open('user.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    
    if data['email'] == "":
        print("Fase")
        
    else:
        try:
            user = auth.sign_in_with_email_and_password(data['email'], data['password'])
        except:
            pass
        


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

with open('user.json', 'r') as jsonfile:
    dati = json.load(jsonfile)



class WindowManager(ScreenManager):
    pass

class MainLayout(MDBoxLayout):
    pass

class AccountLoginPage(Screen):
    pass

class HomeScreen(Screen):
    text = StringProperty()
    with open('user.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        text = data['email']


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

class PropertyRentCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            
        self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])

    def house_type(self, texta):
        self.poop = texta
        again = db.child("People").child("Rent").child(self.user['localId']).child("house").get()
        self.new()
        for u in again.each():
            db.child("People").child("Rent").child(self.user['localId']).child("house").child(u.key()).update({'housetype': self.poop})

    def new(self):
        print(self.poop)

class PropertySaleCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    country = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    key = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
       
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
           
        self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
        

    

    
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

class PropertyCardsLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        try:
            again = db.child("People").child("Sale").child(dati['localid']).child("house").get()

            for u in again.each():
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
                self.add_widget(self.card)
            


            
            again = db.child("People").child("Rent").child(dati['localid']).child("house").get()

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
    
        self.j = 0
        self.added()

    def added(self):
            
        try:
            people = db.child("People").child("Sale").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    
                    next = db.child("People").child("Sale").child(something).get()
                    for i in next.each():
                        if "house" not in i.key():
                            pass
                        else:
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
                    
                    next = db.child("People").child("Sale").child(something).get()
                    for i in next.each():
                        if "house" not in i.key():
                            pass
                        else:
                            again = db.child("People").child("Sale").child(something).child("house").get()
                            for u in again.each():
                                
                                if u.key() in dati['bookmarks']:
                                
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
                                
                                if u.key() in dati['bookmarks']:
                                    
                                    
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
                                    self.add_widget(self.card)
        except:
            pass
            
# princekofasiedu

class IconListItem(OneLineIconListItem):
    icon = StringProperty()

                    
                    



        

class MainApp(MDApp):
    def build(self):

        screens = [HomeScreen(name="Home"), DetailsScreen(name="detail"), LoginScreen(name="Login"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks')]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        
        self.home = HomeScreen()
        
        self.login = LoginScreen()
        self.signup = AccountLoginPage()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.SaleOrRent = SaleOrRent()
        self.rent = RentSubmit()
        self.bk = BookmarkScreen()
  

        
        

        for i in screens:
            self.wm.add_widget(i)
        
        self.wm.current = "Home"
        self.wm.transition = FadeTransition()
        self.numberiy = 'item 0'
        
        self.mail = ''
        self.passwrd = ''
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
        return self.wm
        return super().build()

    def set_item(self, text_item):
        self.numberiy = text_item
    
    def callback_for_menu_items(self, *args):
        toast(args[0])


    def show_bottom(self):
        bottom_sheet_menu = MDListBottomSheet()
        arr = np.array([])
        for i in sum(range(192)):
            bottom_sheet_menu.add_item(f"item {i}", lambda x, y=i: self.callback_for_menu_items(f"Item{y}"))
        bottom_sheet_menu.open()

    def switch_home(self):
        self.home = HomeScreen()
        self.wm.switch_to(self.home)

    def switch_details(self, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None ):
        self.detail = DetailsScreen()
        self.wm.switch_to(self.detail)
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
        self.bk = BookmarkScreen()
        self.wm.switch_to(self.bk)
    
    def switch_signin(self):
        self.wm.switch_to(self.signin)
    
    def switch_saleorrent(self):
        try:
            if dati['email'] == "":
                        
                self.wm.switch_to(self.signin)
            else:
                self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                self.wm.switch_to(self.SaleOrRent)
        except:
            pass

    def email(self, texta):
        self.mail = texta
        

    def phone(self, texta):
        self.phonenumber = texta


    def password(self, texta):
        self.passwrd = texta
       

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

    
    

    def show_dialog(self, notice, button, button1=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[button, button1])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="10dp", snackbar_y="80dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width, size_hint_y = 0.7, bg_color = 'white')
        self.snack.open()

    def open_maps(self, location):
        webbrowser.open('https://www.google.com/maps/place/' + location)


    def change_screen(self, screen, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None):
        self.detail = DetailsScreen()
        try:
            if screen == "detail":
                self.wm.switch_to(self.detail)
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

            elif screen == "Home":
                self.wm.switch_to(self.home)
            elif screen == "Login":
                self.wm.switch_to(self.login)
            elif screen == "rent":
                self.wm.switch_to(self.rent)
            elif screen == "sign-up":
                self.wm.switch_to(self.signup)
            elif screen == "products":
                self.wm.switch_to(self.products)
            elif screen == "bookmarks":
                self.wm.switch_to(self.bk)
            
            elif screen == "sign-in":
                
                

                self.wm.switch_to(self.signin)

                # else:
                #     self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                #     self.wm.switch_to(self.login)
                    # self.wm.switch_to(self.SaleOrRent)

            
            elif screen == "SaleOrRent":
                if dati['email'] == "":
                    
                    self.wm.switch_to(self.signin)
                else:
                    self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                    self.wm.switch_to(self.SaleOrRent)
            
        except:
            pass
            
    def send_email(self, email):

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("anangjosh8@gmail.com", "iujwzdutnqmbpkjm")
        server.sendmail("anangjosh8@gmail.com", "pirateyonko5@gmail.com", "An offer has been made to buy your house.")
        server.quit()

    def account_submit(self):
        email = self.mail
        password = self.passwrd
        try:
            
            user = auth.create_user_with_email_and_password(email, password)
            useri = auth.send_email_verification(user['idToken'])
            self.change_screen("products")
        except:
            text = "Invalid email or password"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)
            

        
    def delete_property(self, name):
        print(name + "Delete Delete Delete Delete Delete Delete Delete")
        db.child("People").child("Sale").child(dati['localid']).child("house").child(name).remove()
        db.child('People').child("Rent").child(dati['localid']).child("house").child(name).remove()

# "MKHRXCSZPZWXKIIF"


    def sign_in(self):
        email = self.mail
        password = self.passwrd
        
        
        try:
            self.user = auth.sign_in_with_email_and_password(email, password)
            
            
            with open('user.json', 'r') as jsonfile:
                data = json.load(jsonfile)
                print(data['email'])
            
            data['email'] = self.mail
            data['password'] = self.passwrd
            data['idToken'] = self.user['idToken']
            data['localid'] = self.user['localId']

            with open('user.json', 'w') as jsonfile:
                json.dump(data, jsonfile)
            self.change_screen("products")
            
        except:
            text = "Invalid email or password"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)

        

    
            

        
        
    
        

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
            user = auth.sign_in_with_email_and_password(data['email'], data['password'])
            db.child("People").child(user['localId']).remove()
            with open('user.json', 'r') as jsonfile:
                dati = json.load(jsonfile)
                
            for i in dati['house_images']:
                storage.delete(i, user['idToken'])
                
            with open('user.json', 'w') as jsonfile:
                json.dump(dati, jsonfile)
            
            auth.delete_user_account(user['idToken'])

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
        user = auth.sign_in_with_email_and_password(email, password)
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
        if len(self.tot) > 5:
            
            if len(self.country) >= 3:
                
                if self.mail == dati['email']:
                    # phone = '+2332222222222'
                    if self.phonenumber != '':
                        phone_number  = phonenumbers.parse(self.phonenumber)
                        valid = phonenumbers.is_valid_number(phone_number)
                        if valid == True:
                            filechooser.open_file(on_selection=self.house_sale, multiselect=True)
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
        try:
            if len(selection) > 0:
                self.file = str(selection[0])
                storage.child(dati['localid']).child(str(self.file)).put(str(self.file))
                url = storage.child(dati['localid']).child(self.file).get_url(None)
                print(self.file)
                # with open('user.json', 'r') as jsonfile:
                #     dato = json.load(jsonfile)
                print(self.phonenumber)
                dati['house_images'].append(self.file)
                with open('user.json', 'w') as jsonfile:
                    json.dump(dati, jsonfile)
                
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
                    "local_image": ""
                }

                
                data['housetype'] = self.tot
                data['country'] = self.country
                data['town'] = self.town
                data['street'] = self.street
                data['bedrooms'] = self.bedrooms
                data['bathrooms'] = self.bathrooms
                data['landspace'] = self.landspace
                data['url'] = url
                data['email'] = dati['email']
                data['phonenumber'] = self.phonenumber
                data['price'] = "$" + self.price
                data['local_image'] = self.file
                # db.child("People").child(key).child("house").push(data)
                results = db.child("People").child("Sale").child(self.user['localId']).child("house").push(data)
                print(results)
        except:
            close_button = MDFlatButton(text="close", on_release=self.close_dialog)
            info = 'Oops something went wrong'
            self.show_dialog(info, close_button)
        
        
        
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

                
        else:
            pass

    def rent_property(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        if len(self.tot) > 5:
            
            if len(self.country) > 3:
                
                filechooser.open_file(on_selection=self.house_rent, multiselect=True)
            
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
                storage.child(dati['localid']).child(str(self.file)).put(str(self.file))
                url = storage.child(dati['localid']).child(self.file).get_url(None)

            
                dati['house_images'].append(self.file)
                with open('user.json', 'w') as jsonfile:
                    json.dump(dati, jsonfile)
                
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
                    "local_image": ""
                }

                
                data['housetype'] = self.tot
                data['country'] = self.country
                data['street'] = self.street
                data['town'] = self.town
                data['bedrooms'] = self.bedrooms
                data['bathrooms'] = self.bathrooms
                data['landspace'] = self.landspace
                data['url'] = url
                data['email'] = dati['email']
                data['price'] = "$" + self.price + '/mth'
                data['local_image'] = self.file
                # db.child("People").child(key).child("house").push(data)
                results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
                print(results)
        except:
            pass

MainApp().run()

firemail = 'first-db-77609.firebaseapp.com'