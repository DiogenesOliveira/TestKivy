import kivy
import time 
#import cv2
import ocr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.lang import Builder 
from kivy.uix.camera import Camera
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class Gerenciador(ScreenManager):
    pass

class Inicio(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close = self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout (orientation = 'vertical', padding = 10, spacing = 10)
        botoes = BoxLayout(padding = 10, spacing = 10)

        pop = Popup(title = 'Tem certeza que deseja sair do App?', content = box, size_hint = (None, None),
                    size = (300, 180))

        sim = Botao(text = 'Sim', on_release = App.get_running_app().stop)
        nao = Botao(text = 'Não', on_release = pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source = 'atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()
        return True

class BotaoAlternancia(ButtonBehavior, Label):
    cor = ListProperty([0.25, 0.25, 0.25, 1])
    cor2 = ListProperty([0.1, 0.1, 0.1, 1])
    def __init__(self, **kwargs):
        super(BotaoAlternancia,self).__init__(**kwargs)
        self.atualizar()
    
    def on_pos(self, *args):
        self.atualizar()
    
    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor
    
    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba = self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=(self.pos))
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                     pos=(self.x + self.height / 2.0, self.y))

class Botao(ButtonBehavior, Label):
    cor = ListProperty([0.25, 0.25, 0.25, 1])
    cor2 = ListProperty([0.1, 0.1, 0.1, 1])
    def __init__(self, **kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()
    
    def on_pos(self, *args):
        self.atualizar()
    
    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor
    
    def on_release(self, *args):
        self.cor, self.cor2 = self.cor2, self.cor

    def on_cor(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba = self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=(self.pos))
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                     pos=(self.x + self.height / 2.0, self.y))
    
class Malte(Screen):                        
    def captureMalte(self):
        camera = self.ids['cameraMalte']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}_Malte.png".format(timestr))
        imagem = "IMG_{}_Malte.png".format(timestr)
        #ocr.extraiNFMalte(imagem)
        ocr.extraiNFMalte("Teste_cortado.png")
    
    def captureMaltose(self):
        camera = self.ids['cameraMalte']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}_Maltose.png".format(timestr))
        print("Captured_Maltose")

    def on_pre_enter(self):
        Window.bind(on_request_close = self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout (orientation = 'vertical', padding = 10, spacing = 10)
        botoes = BoxLayout(padding = 10, spacing = 10)

        pop = Popup(title = 'Tem certeza que deseja sair do App?', content = box, size_hint = (None, None),
                    size = (300, 180))

        sim = Botao(text = 'Sim', on_release = App.get_running_app().stop)
        nao = Botao(text = 'Não', on_release = pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source = 'atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()
        return True
    
class check_box(GridLayout):

	def __init__(self, **kwargs):
		# super function can be used to gain access
		# to inherited methods from a parent or sibling class
		# that has been overwritten in a class object.
		super(check_box, self).__init__(**kwargs)

		# 2 columns in grid layout
		self.cols = 2

		# Add checkbox, Label and Widget
		self.add_widget(Label(text ='Male'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

		# Adding label to screen
		self.lbl_active = Label(text ='Checkbox is on')
		self.add_widget(self.lbl_active)
		

		# Attach a callback
		self.active.bind(active = self.on_checkbox_Active)


	# Callback for the checkbox
	def on_checkbox_Active(self, checkboxInstance, isActive):
		if isActive:
			self.lbl_active.text ="Checkbox is ON"
			print("Checkbox Checked")
		else:
			self.lbl_active.text ="Checkbox is OFF"
			print("Checkbox unchecked")

class CheckBoxApp(App):
	def build(self):
		# build is a method of Kivy's App class used
		# to place widgets onto the GUI.
		return check_box()
        
class Test(App):
    def build(self):
        return Gerenciador()


Test().run()