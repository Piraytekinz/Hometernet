from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, CardTransition, WipeTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.card import MDCard

Builder.load_file('HomeScreen.kv')
Builder.load_file('Creator.kv') 
Builder.load_file('MyProperties.kv')
Builder.load_file('SignIn.kv')
Builder.load_file('SignUp.kv')



# bookmark
# \U000F00C0

# bed
# \U000F02E3




class WindowManager(ScreenManager):
    pass


        # self.user_font_size = str(Window.size[1]/3-60) + 'dp'

class MyProducts(Screen):
    pass

class SignInScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class CreatorScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):
        print(self.ids.pic.width)
        return super().on_pre_enter(*args)

class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_pre_enter(self, *args):          
        print(Window.size[1])
        # print(str(self.ids.second_box.height) + " " + 'secondary box height')
        
        # self.ids.btn.user_font_size = str(Window.size[1]/3-60) + 'dp'
        return super().on_pre_enter(*args)

    def on_enter(self, *args):
        print(str(Window.size[0]) + " " + 'is the width')
        print(str(self.ids.hero_box.height) + " " + 'main box height')
        print(str(self.ids.grid_card.height) + 'Grid Card height')
        print(str(self.ids.gridi.height) + 'Gridi card height')
        print(str(self.ids.gridi.width) + 'Gridi card width')
        
        print(str(self.ids.menu_card.height) + " " + 'menu_card height')
        print(str(self.ids.menu.width) + " " + 'menu icon width')
        print(str(self.ids.menu.height) + " " + 'menu icon height')
        print(str(self.ids.home_card.width) + " " + 'HomeCard width')
        print(str(self.ids.home_card.height) + " " + 'HomeCard height')
        print(str(self.ids.magnificent.font_size) + " " + 'search button font_size')
        return super().on_enter(*args)

class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.primary_hue = '900'
        screens = [HomeScreen(name='Home'), CreatorScreen(name="creator")]
        self.home = HomeScreen()
        self.creator = CreatorScreen()
        self.products = MyProducts()
        self.signin = SignInScreen()
        self.signup = SignUpScreen()
        self.wm.transition = WipeTransition()
        
        for i in screens:
            self.wm.add_widget(i)
        return self.wm

    def switch_home(self):
        self.wm.switch_to(self.home, direction='left')

    def switch_creator(self):
        self.wm.switch_to(self.creator, direction='right')

    def switch_products(self):
        self.wm.switch_to(self.products, direction='right')

    def switch_signin(self):
        self.wm.switch_to(self.signin, direction='right')

    def switch_signup(self):
        self.wm.switch_to(self.signup, direction='right')

MainApp().run()