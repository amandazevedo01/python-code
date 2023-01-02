from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, SlideTransition
from kivy.uix.dropdown import DropDown

from kivy.core.window import Window

Window.size = (1080, 1920)

from ProjetoFinal_kivy.site import cralwer
from tinydb import TinyDB

db = TinyDB('db.json')
site = TinyDB('site.json')


class CustomDropDown(DropDown):
    pass


class CustomPopup(Popup):
    submit_form = ObjectProperty(None)

    def dismiss_popup(self):
        '''
        MODIFY: chiusura del popup
        '''
        self.dismiss()


class MainWindow(Screen):
    submit_button = ObjectProperty(None)
    nome = ObjectProperty(None)


    def confirm_submit_form(self):
        '''
        MODIFY: crea una finestra popup per una conferma di invio del form compilato
        '''
        custom_popup = CustomPopup(title="Confirm sending form", size_hint=(0.9, 0.9), submit_form=self.submit_form)
        custom_popup.open()



    def submit_form(self):


        db.insert({'nome': self.nome.text})
        print(db.all())
        sm.switch_to(screens[1], direction="left")


from kivy.uix.label import Label


class SecondWindow(Screen):
    summary_date = ObjectProperty(None)

    def get_data(self):
        for user in db:
            for key, value in user.items():
                try:
                    x = cralwer(value)
                except:
                    site.insert({'Status': 'Site not found'})
        for id in site:
            for key, value in id.items():
                try:

                    text = f'{key} | {value}.' "\n"
                except:
                    text = 'Site not found'  "\n"

            self.summary_date.add_widget(Label(text="\n" + text, color=(0, 0, 0, 1)))
        self.summary_date.add_widget(Label(text="-----------------------", color=(0, 0, 0, 1)))

    def go_back(self):
        '''
        MODIFY: cambia la finestra visualizzata passando alla MainWindow
        '''
        self.summary_date.clear_widgets()
        sm.switch_to(screens[0], direction="right")


class WindowManager(ScreenManager):
    pass


# caricamento del file kivy
kv = Builder.load_file("style.kv")

# creazione dello screen manager che viene usato per gestire gli Screen (schermate)
sm = WindowManager(transition=SlideTransition())

# lista degli screen (schermate)
screens = [MainWindow(name="mainwindow"), SecondWindow(name="secondwindow")]

for screen in screens:
    sm.add_widget(screen)

# definizione della schermata da visualizzare all'apertura dell'applicazione
sm.current = "mainwindow"


class MainApp(App):
    def build(self):
        return sm


sample_app = MainApp()
sample_app.run()