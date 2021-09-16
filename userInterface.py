from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        ### Criando margens para o conteúdo da janela
        self.window.size_hint = (0.6, 0.7)
        ### Centralizando os widgets na tela
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source="assets/logo.png"))

        ### Colocar texto na UI
        self.todo = Label(
                            text="Cadastrar pessoas",
                            font_size = 18,
                            color = '#00FFCE'
                        )
        self.window.add_widget(self.todo)

        ### Receber input do usuário
        self.nome = TextInput(
                                multiline=False,
                                padding_y = (20,20),
                                size_hint = (1, 0.5)
                            )
        self.window.add_widget(self.nome)

        ### Botão
        self.button = Button(
                                text='Cadastrar', 
                                size_hint = (1, 0.5),
                                bold = True,
                                background_color = '#00FFCE'
                            )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.todo.text = "Olá " + self.nome.text 

if __name__ == "__main__":
    SayHello().run()
