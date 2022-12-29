from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton

Builder.load_file('HomeScreen.kv')
Builder.load_file('Creator.kv')

class WindowManager(ScreenManager):
    pass

class SearchButton(MDIconButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        print(self.ids.btn.user_font_size)
        return super().on_pre_enter(*args)

class MainApp(MDApp):
    def build(self):
        self.wm = WindowManager()
        screens = [HomeScreen(name='Home'), CreatorScreen(name="creator")]
        self.home = HomeScreen()
        self.creator = CreatorScreen()
        self.wm.transition = SwapTransition()
        for i in screens:
            self.wm.add_widget(i)
        return self.wm

    def switch_home(self):
        self.wm.switch_to(self.home)

    def switch_creator(self):
        self.wm.switch_to(self.creator)

MainApp().run()