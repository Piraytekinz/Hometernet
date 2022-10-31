
from tokenize import String
from unittest import result
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




class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_scroll_stop
        self.on_effect_cls
        
        
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

with open('current_user.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data['email'])
        
    print(data['email'])
    print(data['password'])
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
Builder.load_file("DetailScreen.kv")
Builder.load_file("SaleSubmit.kv")
Builder.load_file('RentSubmit.kv')
Builder.load_file('LoginPage.kv')
Builder.load_file("MyProducts.kv")
Builder.load_file("SignInScreen.kv")
Builder.load_file('SaleOrRent.kv')

with open('current_user.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data['email'])


class WindowManager(ScreenManager):
    pass

class MainLayout(MDBoxLayout):
    pass

class AccountLoginPage(Screen):
    pass

class HomeScreen(Screen):
    text = StringProperty()
    with open('current_user.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        text = data['email']
        print(data['email'])

class HomeCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    location = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()

class PropertyCards(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    tot = StringProperty()
    location = StringProperty()
    bedrooms = StringProperty()
    bathrooms = StringProperty()
    landspace = StringProperty()
    email = StringProperty()
    price = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        print("Let's see")
        with open('current_user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        print(data['email'], data['password'])
        self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
        

    def house_type(self, texta):
        self.poop = texta
        again = db.child("People").child("Sale").child(self.user['localId']).child("house").get()
        self.new()
        for u in again.each():
            db.child("People").child("Sale").child(self.user['localId']).child("house").child(u.key()).update({'housetype': self.poop})

    def new(self):
        print(self.poop)

    
class DetailsScreen(Screen):
    image = StringProperty()
    type = StringProperty()
    price = StringProperty()
    location = StringProperty()
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

        with open('current_user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
                
            print(data['email'])
            print(data['password'])
            if data['email'] == "":
                print("Fase")
            else:
                try:
                    user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                except:
                    pass
                self.cols = int(Window.size[0]*0.5/100)
                
                if self.cols > 1 and self.cols < 3:
                    self.cols = 1
                if self.cols > 3:
                    self.ad = int(Window.size[0]*0.5/100)
                    result = self.ad-3
                    actual = self.cols-result
                    self.cols = actual

                # mydb = mysql.connector.connect(
                #     host = "localhost",
                #     user = "root",
                #     password = "GermaDouble6",
                #     database = 'first_db'
                # )

                # cursor = mydb.cursor()
                # cursor.execute("SELECT id, name FROM Users")
                # recs = cursor.fetchall()

                
                    
                
                # for i in house["Housing"]:
                #     self.card = HomeCards()
                #     self.card.house_type = i["House_type"]
                #     self.card.image = i['Image']
                #     self.card.rooms = i['bedrooms']
                #     self.add_widget(self.card)
                    
                try:
                    people = db.child("People").get()
                    if people.each():
                        for person in people.each():
                            something = person.key()
                            
                            next = db.child("People").child("Sale").child(user['localId']).get()
                            for i in next.each():
                                if "house" not in i.key():
                                    pass
                                else:
                                    again = db.child("People").child("Sale").child(user['localId']).child("house").get()
                                    for u in again.each():
                                        self.card = PropertyCards()
                                        self.card.image = u.val()['url']
                                        self.card.tot = u.val()['housetype']
                                        self.card.location = u.val()['location']
                                        self.card.bedrooms = u.val()['bedrooms']
                                        self.card.bathrooms = u.val()['bathrooms']
                                        self.card.landspace = u.val()['landspace']
                                        self.card.email = u.val()['email']
                                        self.card.price = u.val()['price']
                                        self.add_widget(self.card)
                            


                    people = db.child("People").child("Rent").get()
                    if people.each():
                        for person in people.each():
                            something = person.key()
                            # another = person.val()
                            print(something)
                            # print(another)
                            next = db.child("People").child("Rent").child(user['localId']).get()
                            for i in next.each():
                                if "house" not in i.key():
                                    pass
                                else:
                                    again = db.child("People").child("Rent").child(user['localId']).child("house").get()

                                    for u in again.each():
                                        self.cardi = PropertyCards()
                                        self.cardi.image = u.val()['url']
                                        self.cardi.tot = u.val()['housetype']
                                        self.cardi.location = u.val()['location']
                                        self.cardi.bedrooms = u.val()['bedrooms']
                                        self.cardi.bathrooms = u.val()['bathrooms']
                                        self.cardi.landspace = u.val()['landspace']
                                        self.cardi.email = u.val()['email']
                                        self.cardi.price = u.val()['price']
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

class Effect(DampedScrollEffect):
    def on_overscroll(self, *args):
        super().on_overscroll(*args)
        self.overscroll = 0
        if self.overscroll == 0:
            self.homesser = HomeCardsLayout()
            self.homesser.added()
            self.do_something()
        else:
            pass

    # @call_control(max_call_interval=1)
    def do_something(self):
        self.homesser = HomeCardsLayout()
        self.homesser.added()
        self.homesser.something = True
        print("It worked")

class Scroller(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_scroll_x = False
        self.do_scroll_y = True
        self.effect = Effect
        # self.effect_cls = Effect



    def scrolled(self):
        self.do_scroll_y = False
        
    def unscrolled(self):
        self.do_scroll_y = True
        




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
        self.card = HomeCards()
        self.add_widget(self.card)
        self.added()
       
    # @call_control(max_call_interval=1)
    def added(self):
        
        print("Okay")
        self.something = True
        house = {
            'Housing': [{
                'Image': 'Images/Brick House.jpg',
                'bedrooms': '1',
                'House_type': 'New House'
            },
            {
            'Image': 'Images/Brick House.jpg',
                'bedrooms': '2',
                'House_type': 'New House'
            },
            {
            'Image': 'Images/Brick House.jpg',
                'bedrooms': '3',
                'House_type': 'New House'
            },
            {
            'Image': 'Images/Brick House.jpg',
                'bedrooms': '4',
                'House_type': 'New House'
            }
            ]
            
        }
        for i in house['Housing']:
            self.card = HomeCards()
            # self.card.tot= i["House_type"]
            # self.card.image = i['Image']
            # self.card.bedrooms = i['bedrooms']
            self.add_widget(self.card)
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
            
                
            
        
        # people = db.child("People").child("Sale").get()
        # if people.each():
        #     for person in people.each():
        #         something = person.key()
        #         # another = person.val()
        #         print(something)
        #         # print(another)
        #         next = db.child("People").child("Sale").child(something).get()
        #         for i in next.each():
        #             if "house" not in i.key():
        #                 pass
        #             else:
        #                 again = db.child("People").child("Sale").child(something).child("house").get()

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
        house = {
            'Housing': [{
                'Image': 'Brick House.jpg',
                'bedrooms': '1',
                'House_type': 'New House'
            },
            {
            'Image': 'Brick House.jpg',
                'bedrooms': '2',
                'House_type': 'New House'
            },
            {
            'Image': 'Brick House.jpg',
                'bedrooms': '3',
                'House_type': 'New House'
            },
            {
            'Image': 'Brick House.jpg',
                'bedrooms': '4',
                'House_type': 'New House'
            }
            ]
            
        }
        for i in house['Housing']:
            self.card = HomeCards()
            # self.card.tot= i["House_type"]
            # self.card.image = i['Image']
            # self.card.bedrooms = i['bedrooms']
            self.add_widget(self.card)
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
    
# princekofasiedu



                    
                    
                    


class MainApp(MDApp):
    def build(self):

        screens = [HomeScreen(name="Home"), DetailsScreen(name="detail"), LoginScreen(name="Login"), AccountLoginPage(name="sign-up"), MyProducts(name="products"), SaleOrRent(name="SaleOrRent"), RentSubmit(name="rent")]
        self.wm = WindowManager()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "900"
        self.homes = HomeCardsLayout()
        self.haight = self.homes.height * 350
        self.effect = Effect()
        
        for i in screens:
            self.wm.add_widget(i)
        
        self.wm.current = "Home"
        self.home = HomeScreen()
        self.mail = ''
        self.passwrd = ''
        self.sign_in_mail = ''
        self.sign_in_pass = ''

        self.tot = ''
        self.location = ''
        self.bedrooms = ''
        self.bathrooms = ''
        self.landspace = ''
        self.price = ''
        return self.wm
        return super().build()

    def check_pull_refresh(self, view, grid):
        max_pixel = 200
        to_relative = max_pixel / (grid.height - view.height)
        print(to_relative)
        print(1.0 + to_relative)
        print(view.scroll_y)
        if view.scroll_y + 1.0 < 1.0 + to_relative:
            print("Okad")


    def email(self, texta):
        self.mail = texta
        print(texta)

    def password(self, texta):
        self.passwrd = texta
        print(texta)

    def signin_mail(self, texta):
        self.sign_in_mail = texta

    def signin_pass(self, texta):
        self.sign_in_pass = texta

    def word(self, texta):
        self.tot = texta
        print(texta)

    def locate(self, texta):
        self.location = texta
    
    def rooms(self, texta):
        self.bedrooms = texta
    
    def baths(self, texta):
        self.bathrooms = texta

    def land_space(self, texta):
        self.landspace = texta

    def pricing(self, texta):
        self.price = texta
        
    def on_start(self):
        self.home = HomeCardsLayout()
        self.home.column = 3
        return super().on_start()

    def show_dialog(self, notice, button, button1=None):
        self.dialog = MDDialog(text=notice, size_hint=(1, 1), buttons=[button, button1])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def snackbar(self, obj):
        self.snack = Snackbar(text="No user signed in!")
        self.snack.open()

    def change_screen(self, screen, image=None, House_type=None, pricing=None, locate=None, email=None):
        self.home = HomeScreen()
        self.detail = DetailsScreen()
        self.login = LoginScreen()
        self.signup = AccountLoginPage()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.SaleOrRent = SaleOrRent()
        self.rent = RentSubmit()
        try:
            if screen == "detail":
                self.wm.switch_to(self.detail, direction='left')
                self.detail.image = image
                self.detail.type = House_type
                self.detail.price = pricing
                self.detail.location = locate
                self.detail.email = email
                print(image, House_type, email)
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
            elif screen == "SaleOrRent":
                with open('current_user.json', 'r') as jsonfile:
                    data = json.load(jsonfile)
                    print(data['email'])
                    
                print(data['email'])
                print(data['password'])
                if data['email'] == "":
                    print("Fase")
                    self.wm.switch_to(self.signin)
                else:
                    self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                    self.wm.switch_to(self.SaleOrRent)
            elif screen == "sign-in":
                
                # with open('current_user.json', 'r') as jsonfile:
                #     data = json.load(jsonfile)
                #     print(data['email'])
                    
                # print(data['email'])
                # print(data['password'])
                # if data['email'] == "":
                #     print("Fase")

                self.wm.switch_to(self.signin)

                # else:
                #     self.user = auth.sign_in_with_email_and_password(data['email'], data['password'])
                #     self.wm.switch_to(self.login)
                    # self.wm.switch_to(self.SaleOrRent)
        except:
            pass
            
    def send_email(self, email):
        print(email + "is the mail")
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
            

        


# "MKHRXCSZPZWXKIIF"


    def sign_in(self):
        email = self.mail
        password = self.passwrd
        
        with open('current_user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        
        data['email'] = self.mail
        data['password'] = self.passwrd
        
            
        self.user = auth.sign_in_with_email_and_password(email, password)

        data['idToken'] = self.user['idToken']

        
            # auth.send_email_verification(self.user['idToken'])
            # gain = db.child("People").child("Sale").child(self.user['localId']).child("house").get()
            # if gain.each():
            #     for i in gain.each():
            #         data['house_images'].append(i.val()['local_image'])
            
            
        with open('current_user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
                
            # self.change_screen("products")
            
            # print("Success")
        
        
    
        

    def sign_out(self):
        with open('current_user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        data['email'] = ''
        data['password'] = ''
        data['idToken'] = ''
        data['house_images'] = []
        with open('current_user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)


    def delete_user(self, obj):
        
        try:
            user = auth.sign_in_with_email_and_password(data['email'], data['password'])
            db.child("People").child(user['localId']).remove()
            with open('current_user.json', 'r') as jsonfile:
                dati = json.load(jsonfile)
                print(dati['email'])
            for i in dati['house_images']:
                storage.delete(i, user['idToken'])
                
            with open('current_user.json', 'w') as jsonfile:
                json.dump(dati, jsonfile)
            
            auth.delete_user_account(user['idToken'])

            with open('current_user.json', 'r') as jsonfile:
                dato = json.load(jsonfile)
                print(dato['email'])
            dato['email'] = ''
            dato['password'] = ''
            dato['idToken'] = ''
            dato['house_images'] = []
            with open('current_user.json', 'w') as jsonfile:
                json.dump(dato, jsonfile)
            
            
            print("successfully deleted account")
        except:
            print("No user signed in")
            p = 'p'
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
        with open('current_user.json', 'r') as jsonfile:
            data = json.load(jsonfile)
            print(data['email'])
        
        data['email'] = self.mail
        data['password'] = self.passwrd
        
        with open('current_user.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
            
        self.change_screen("products")

    def selected(self):
        close_button = MDFlatButton(text="close", on_release=self.close_dialog)
        if len(self.tot) > 5:
            
            if len(self.location) > 6:
                
                filechooser.open_file(on_selection=self.house_sale, multiselect=True)
            
            else:
                info = "location must be more than 6 characters"
                self.show_dialog(info,close_button)
        else:
            text = "House type must be more than 5 characeters"
            self.show_dialog(text,close_button)

    def house_sale(self, selection):
        print(self.tot)


        
        print("Something")
        if len(selection) > 0:
            self.file = str(selection[0])
            storage.child(str(self.file)).put(str(self.file))
            url = storage.child(self.file).get_url(None)

            with open('current_user.json', 'r') as jsonfile:
                dato = json.load(jsonfile)
                print(dato['email'])
            dato['house_images'].append(self.file)
            with open('current_user.json', 'w') as jsonfile:
                json.dump(dato, jsonfile)
            
            data = {
                "housetype": "",
                "location": "",
                "bedrooms": "",
                "bathrooms": "",
                "landspace": "",
                "url": "",
                "email": "",
                "price": "",
                "local_image": ""
            }

            
            data['housetype'] = self.tot
            data['location'] = self.location
            data['bedrooms'] = self.bedrooms
            data['bathrooms'] = self.bathrooms
            data['landspace'] = self.landspace
            data['url'] = url
            data['email'] = self.mail
            data['price'] = "$" + self.price
            data['local_image'] = self.file
            # db.child("People").child(key).child("house").push(data)
            results = db.child("People").child("Sale").child(self.user['localId']).child("house").push(data)
            print(results)
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
            
            if len(self.location) > 6:
                
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
            storage.child(str(self.file)).put(str(self.file))
            url = storage.child(self.file).get_url(None)

            with open('current_user.json', 'r') as jsonfile:
                dato = json.load(jsonfile)
                print(dato['email'])
            dato['house_images'].append(self.file)
            with open('current_user.json', 'w') as jsonfile:
                json.dump(dato, jsonfile)
            
            data = {
                "housetype": "",
                "location": "",
                "bedrooms": "",
                "bathrooms": "",
                "landspace": "",
                "url": "",
                "email": "",
                "price": "",
                "local_image": ""
            }

            
            data['housetype'] = self.tot
            data['location'] = self.location
            data['bedrooms'] = self.bedrooms
            data['bathrooms'] = self.bathrooms
            data['landspace'] = self.landspace
            data['url'] = url
            data['email'] = self.mail
            data['price'] = "$" + self.price + '/mth'
            data['local_image'] = self.file
            # db.child("People").child(key).child("house").push(data)
            results = db.child("People").child("Rent").child(self.user['localId']).child("house").push(data)
            print(results)

    def Scroll(self):
        self.homeser = HomeCardsLayout()
        self.homeser.add()
        print("Scrolled")

    


MainApp().run()

firemail = 'first-db-77609.firebaseapp.com'