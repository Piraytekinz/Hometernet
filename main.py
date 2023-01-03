from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior

Builder.load_file('HomeScreen.kv')
Builder.load_file('Creator.kv') 
Builder.load_file('MyProperties.kv')
Window.size = (400, 1200)


# bookmark
# \U000F00C0

# bed
# \U000F02E3
print(Window.size[1]*2)



class WindowManager(ScreenManager):
    pass

class SearchButton(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.user_font_size = str(Window.size[1]/3-60) + 'dp'

class MyProducts(Screen):
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
        print(str(self.ids.hero_box.height) + " " + 'main box height')
        print(str(self.ids.grid_card.height) + 'Grid Card height')
        print(str(self.ids.gridi.height) + 'Gridi card height')
        print(str(self.ids.gridi.height/2) + 'Gridi.height divide by 2')
        print(str(self.ids.grid_card.height/2)+ "Grid card divided by two")
        print(str(self.ids.menu_card.height) + " " + 'menu_card height')
        print(str(self.ids.menu.width) + " " + 'menu icon width')
        print(str(self.ids.menu.height) + " " + 'menu icon height')
        print(str(self.ids.home_card.height) + " " + 'HomeCard height')
        return super().on_enter(*args)

class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [HomeScreen(name='Home'), CreatorScreen(name="creator")]
        self.home = HomeScreen()
        self.creator = CreatorScreen()
        self.products = MyProducts()
        self.wm.transition = SwapTransition()
        for i in screens:
            self.wm.add_widget(i)
        return self.wm

    def switch_home(self):
        self.wm.switch_to(self.home)

    def switch_creator(self):
        self.wm.switch_to(self.creator)

    def switch_products(self):
        self.wm.switch_to(self.products)

MainApp().run()