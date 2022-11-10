
import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivymd.uix.list import MDList, OneLineListItem, ImageLeftWidget
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
import webbrowser




class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_scroll_stop
        self.on_effect_cls
        self.scroll_type
        
        
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
        
        

Builder.load_file("KV files/HomeScreen.kv")
Builder.load_file("KV files/HomeCards.kv")
Builder.load_file("KV files/PropertyCards.kv")
Builder.load_file("KV files/PropertyRentCards.kv")
Builder.load_file("KV files/DetailScreen.kv")
Builder.load_file("KV files/SaleSubmit.kv")
Builder.load_file('KV files/RentSubmit.kv')
Builder.load_file('KV files/LoginPage.kv')
Builder.load_file("KV files/MyProducts.kv")
Builder.load_file("KV files/SignInScreen.kv")
Builder.load_file('KV files/SaleOrRent.kv')
Builder.load_file('KV files/bookmarks.kv')

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
        
        print("Let's see")
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
    pass

class RentSubmit(Screen):
    pass

class WordInput(MDTextField):
    pass

class MyProducts(Screen):
    pass

class SignInScreen(Screen):
    pass

class SaleOrRent(Screen):
    pass

class PropertyCardsLayout(MDGridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # with open('user.json', 'r') as jsonfile:
        #     data = json.load(jsonfile)
        #     print(data['email'])
                
        #     print(data['email'])
        #     print(data['password'])
        #     if data['email'] == "":
        #         print("Fase")
        #     else:
        #         try:
        #             user = auth.sign_in_with_email_and_password(data['email'], data['password'])
        #         except:
        #             pass
        self.cols = int(Window.size[0]*0.5/100)
        
        if self.cols > 1 and self.cols < 3:
            self.cols = 1
        if self.cols > 3:
            self.ad = int(Window.size[0]*0.5/100)
            result = self.ad-3
            actual = self.cols-result
            self.cols = actual

        

        
            
        
        # for i in house["Housing"]:
        #     self.card = HomeCards()
        #     self.card.house_type = i["House_type"]
        #     self.card.image = i['Image']
        #     self.card.rooms = i['bedrooms']
        #     self.add_widget(self.card)
            
        
        try:
            again = db.child("People").child("Sale").child(dati['localid']).child("house").get()
            print(again.each(), "LEFMONBIENGoasjfniodvsvberhfieubcvihdsfv ougeSHFPw")
            for u in again.each():
                self.card = PropertySaleCards()
                self.card.image = u.val()['url']
                self.card.tot = u.val()['housetype']
                print(u.val()['housetype'])
                self.card.country = u.val()['country']
                self.card.bedrooms = u.val()['bedrooms']
                self.card.bathrooms = u.val()['bathrooms']
                self.card.landspace = u.val()['landspace']
                self.card.email = u.val()['email']
                self.card.price = u.val()['price']
                self.card.key = u.key()
                self.add_widget(self.card)
        except:
            pass


        try:
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
#         print("It worked")

class Scroller(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_scroll_x = False
        self.do_scroll_y = True
        # self.effect = Effect
        # self.effect_cls = Effect
        

    

    
        



    # def scrolled(self):
    #     self.do_scroll_y = False
        
    # def unscrolled(self):
    #     self.do_scroll_y = True
        




class HomeCardsLayout(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        
        # self.cols = int(Window.size[0]*0.5/100)
        
        # if self.cols > 1 and self.cols < 3:
        #     self.cols = 1
        # if self.cols > 3:
        #     self.ad = int(Window.size[0]*0.5/100)
        #     result = self.ad-3
        #     actual = self.cols-result
        #     self.cols = actual

        # mydb = mysql.connector.connect(
        #     host = "localhost",
        #     user = "root",
        #     password = "GermaDouble6",
        #     database = 'first_db'
        # )

        # cursor = mydb.cursor()
        # cursor.execute("SELECT id, name FROM Users")
        # recs = cursor.fetchall()
    
        self.j = 0
        
        self.added()
       
    # @call_control(max_call_interval=1)
    def added(self):
        
        # print("Okay")
        # self.something = True
        # house = {
        #     'Housing': [{
        #         'Image': 'Images/Brick House.jpg',
        #         'bedrooms': '1',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Images/Brick House.jpg',
        #         'bedrooms': '2',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Images/Brick House.jpg',
        #         'bedrooms': '3',
        #         'House_type': 'New House'
        #     },
        #     {
        #     'Image': 'Images/Brick House.jpg',
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
        # housinger = house["Housing"]
        # for i in house["Housing"]:
            
        #     self.card = HomeCards()
        #     
        #     # scrolli = Scroller()
        #     # scrolli.scrolled()
        #     self.add_widget(self.card)
        #     # scrolli.unscrolled()
            
            
        #     self.j += 1
            
        #     if self.j == 3:
        #         self.j += 1
        #         print(self.j)
        #         break
        #     print(i)

            
            
            #     
            
                
            
        try:
            people = db.child("People").child("Sale").get()
            if people.each():
                for person in people.each():
                    something = person.key()
                    # another = person.val()
                    
                    # print(another)
                    next = db.child("People").child("Sale").child(something).get()
                    for i in next.each():
                        if "house" not in i.key():
                            pass
                        else:
                            again = db.child("People").child("Sale").child(something).child("house").get()

                            for u in again.each():
                                print(u.key())
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


        # people = db.child("People").child("Rent").get()
        # if people.each():
        #     for person in people.each():
        #         something = person.key()
        #         # another = person.val()
        #         print(something)
        #         # print(another)
        #         next = db.child("People").child("Rent").child(something).get()
        #         for i in next.each():
        #             if "house" not in i.key():
        #                 pass
        #             else:
        #                 again = db.child("People").child("Rent").child(something).child("house").get()

        #                 for u in again.each():
        #                     self.card = HomeCards()
        #                     self.card.image = u.val()['url']
        #                     self.card.tot = u.val()['housetype']
        #                     self.card.location = u.val()['location']
        #                     self.card.bedrooms = u.val()['bedrooms']
        #                     self.card.bathrooms = u.val()['bathrooms']
        #                     self.card.landspace = u.val()['landspace']
        #                     self.card.email = u.val()['email']
        #                     self.card.price = u.val()['price']
        #                     self.add_widget(self.card)
        
        

        
       
        
            # if again is not None:
            #     for i in again.each():
            #         if i is not None:
                        
            # for person in people.each():
            #     guy = person.key()
            #     nigga = db.child("People").child(guy).get()
            #     for i in nigga.each():
            #         dude = i.key()
                    
            #         duda = db.child("People").child(guy).child(dude).child("house").get()
            #         for house in duda.each():
     
        #             print(house.key())

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
                                print(u.key())
                                
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
            
# princekofasiedu



                    
                    
                    


class MainApp(MDApp):
    def build(self):

        screens = [HomeScreen(name="Home"), DetailsScreen(name="detail"), LoginScreen(name="Login"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent"), BookmarkScreen(name='bookmarks')]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        self.homes = HomeCardsLayout()
        self.haight = self.homes.height * 350
        
        for i in screens:
            self.wm.add_widget(i)
        
        self.wm.current = "Home"
        self.home = HomeScreen()
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
        return self.wm
        return super().build()

    def check_pull_refresh(self, view, grid):
        max_pixel = 200
        to_relative = max_pixel / (grid.height - view.height)
        
        if view.scroll_y + 1.0 < 1.0 + to_relative:
            print("Okad")


    def email(self, texta):
        self.mail = texta
        

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
    
    def rooms(self, texta):
        self.bedrooms = texta
    
    def baths(self, texta):
        self.bathrooms = texta

    def land_space(self, texta):
        self.landspace = texta

    def pricing(self, texta):
        self.price = texta
        
    

    def show_dialog(self, notice, button, button1=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[button, button1])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def snackbar(self, obj):
        self.snack = Snackbar(text=obj, snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - ((10) * 2)) / Window.width)
        self.snack.open()

    def open_maps(self, location):
        webbrowser.open('https://www.google.com/maps/place/' + location)


    def change_screen(self, screen, image=None, House_type=None, pricing=None, locate=None, town=None, street=None, bedrooms=None, bathrooms=None, landspace=None, email=None):
        self.home = HomeScreen()
        self.detail = DetailsScreen()
        self.login = LoginScreen()
        self.signup = AccountLoginPage()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.SaleOrRent = SaleOrRent()
        self.rent = RentSubmit()
        self.bk = BookmarkScreen()
        try:
            if screen == "detail":
                self.wm.switch_to(self.detail, direction='left')
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
                self.wm.switch_to(self.home, direction='right')
            elif screen == "Login":
                self.wm.switch_to(self.login)
            elif screen == "rent":
                self.wm.switch_to(self.rent)
            elif screen == "sign-up":
                self.wm.switch_to(self.signup)
            elif screen == "products":
                self.wm.switch_to(self.products, direction='left')
            elif screen == "bookmarks":
                self.wm.switch_to(self.bk, direction='left')
            
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
        server.login("anangjosh8@gmail.com", "iidkyxnpbhywvcjw")
        server.sendmail("anangjosh8@gmail.com", "pirateyonko5@gmail.com", "An offer has been made to buy your house.")
        server.quit()

    def account_submit(self):
        email = self.mail
        password = self.passwrd
        try:
            user = auth.create_user_with_email_and_password(email, password)
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
        
        with open('user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        
        data['email'] = self.mail
        data['password'] = self.passwrd
        
        
        try:
            self.user = auth.sign_in_with_email_and_password(email, password)
            data['idToken'] = self.user['idToken']
            data['localid'] = self.user['localId']
            
        except:
            text = "Invalid email or password"
            close_button = MDFlatButton(text="close", on_press=self.close_dialog)
            self.show_dialog(text, close_button)

        with open('user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        self.change_screen("products")

        
            # auth.send_email_verification(self.user['idToken'])
            # gain = db.child("People").child("Sale").child(self.user['localId']).child("house").get()
            # if gain.each():
            #     for i in gain.each():
            #         data['house_images'].append(i.val()['local_image'])
            
            
        
                
            # self.change_screen("products")
            

        
        
    
        

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
                
                filechooser.open_file(on_selection=self.house_sale, multiselect=True)
            
            else:
                info = "location must be more than 6 characters"
                self.show_dialog(info,close_button)
        else:
            text = "House type must be more than 5 characeters"
            self.show_dialog(text,close_button)

    def house_sale(self, selection):
        print(self.tot)
        try:
            if len(selection) > 0:
                self.file = str(selection[0])
                storage.child(dati['localid']).child(str(self.file)).put(str(self.file))
                url = storage.child(dati['localid']).child(self.file).get_url(None)
                print(self.file)
                # with open('user.json', 'r') as jsonfile:
                #     dato = json.load(jsonfile)
                    
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
                data['town'] = self.town
                data['street'] = self.street
                data['bedrooms'] = self.bedrooms
                data['bathrooms'] = self.bathrooms
                data['landspace'] = self.landspace
                data['url'] = url
                data['email'] = dati['email']
                data['price'] = "$" + self.price
                data['local_image'] = self.file
                # db.child("People").child(key).child("house").push(data)
                results = db.child("People").child("Sale").child(self.user['localId']).child("house").push(data)
                print(results)
        except:
            pass
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
        print(self.tot)


        people = db.child("People").get()
        print("Something")
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

MainApp().run()

firemail = 'first-db-77609.firebaseapp.com'