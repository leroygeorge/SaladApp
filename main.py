import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.base import EventLoop
from kivy.animation import Animation

# Get the screen size
screen_width, screen_height = Window.size

# Adjust image size based on screen size
image_width = screen_width * 0.75  # 75% of screen width
image_height = screen_height * 0.6  # 60% of screen height
# Adjust label height based on screen size
label_height = screen_height * 0.2  # 20% of screen height

# Define a list of salads with their definitions and image paths
salads = [
    {
        "name": "Insalata Caprese",
        "definition": "A classic Italian salad with fresh mozzarella, ripe tomatoes, basil, olive oil, balsamic vinegar, salt, and pepper.",
        "image": "insalata_caprese.jpg",
    },
    {
        "name": "Panzanella",
        "definition": "A Tuscan salad with stale bread, ripe tomatoes, cucumbers, red onions, basil, red wine vinegar, and olive oil.",
        "image": "panzanella.jpg",
    },
    {
        "name": "Insalata di Rucola e Parmigiano (Arugula and Parmesan Salad)",
        "definition": "A simple salad with arugula, shaved Parmesan cheese, lemon juice, olive oil, salt, and pepper.",
        "image": "arugula_parmesan.jpeg",
    },
    {
        "name": "Insalata di Mare (Seafood Salad)",
        "definition": "A seafood salad with mixed seafood (calamari, shrimp, mussels, and/or octopus), lemon juice, parsley, olive oil, garlic, and red pepper flakes.",
        "image": "seafood_salad.jpg",
    },
    {
        "name": "Insalata di Finocchio (Fennel Salad)",
        "definition": "A salad with thinly sliced fennel bulb, orange segments, red onion, lemon juice, and olive oil.",
        "image": "fennel_salad.jpg",
    },
    {
        "name": "Insalata Tricolore (Tricolor Salad)",
        "definition": "A salad with arugula, radicchio, endive, lemon juice, and olive oil.",
        "image": "tricolor_salad.jpg",
    },
    {
        "name": "Insalata di Ceci (Chickpea Salad)",
        "definition": "A salad with chickpeas, red onion, parsley, lemon juice, and olive oil.",
        "image": "chickpea_salad.jpg",
    },
    {
        "name": "Insalata di Pomodoro (Tomato Salad)",
        "definition": "A salad with tomatoes, red onion, basil, olive oil, red wine vinegar, salt, and pepper.",
        "image": "tomato_salad.jpeg",
    },
    {
        "name": "Insalata di Pollo (Chicken Salad)",
        "definition": "A salad with grilled or poached chicken, mixed greens, cherry tomatoes, olives, and Italian dressing (olive oil, vinegar, herbs).",
        "image": "chicken_salad.jpeg",
    },
    {
        "name": "Insalata di Orzo (Orzo Salad)",
        "definition": "A salad with cooked orzo pasta, cherry tomatoes, cucumbers, red onion, fresh herbs, and lemon vinaigrette.",
        "image": "orzo_salad.jpg",
    },
    {
        "name": "Insalata di Pasta (Pasta Salad)",
        "definition": "A pasta salad with fusilli or penne pasta, cherry tomatoes, olives, mozzarella cheese, and Italian dressing.",
        "image": "pasta_salad.jpg",
    },
    {
        "name": "Kartoffelsalat (German Potato Salad)",
        "definition": "A German potato salad with potatoes, bacon, onions, broth, vinegar, mustard, fresh herbs, and mayonnaise (optional).",
        "image": "Kartoffelsalat.jpg",
    },
    {
        "name": "Sauerkraut Salat (Sauerkraut Salad)",
        "definition": "A sauerkraut salad with sauerkraut, bacon, onions, broth, vinegar, sugar, and caraway seeds (optional).",
        "image": "sauerkraut_salad.jpg",
    },
    {
        "name": "Wurstsalat (Sausage Salad)",
        "definition": "A sausage salad with sliced German sausages, onions, pickles, vinegar and oil dressing, mustard, and radishes (optional).",
        "image": "sausage_salad.jpg",
    },
    {
        "name": "Gurkensalat (Cucumber Salad)",
        "definition": "A cucumber salad with sliced cucumbers, sour cream or yogurt, dill, onions, vinegar, sugar, salt, and pepper.",
        "image": "Gurkensalat.jpg",
    },
    {
        "name": "Heringssalat (Herring Salad)",
        "definition": "A herring salad with pickled herring fillets, apples, onions, mayonnaise or sour cream, pickles, and potatoes (optional).",
        "image": "herring_salad.jpg",
    },
    {
        "name": "Krautsalat (Coleslaw)",
        "definition": "A coleslaw with shredded white cabbage, carrots, onions, mayonnaise or vinegar-based dressing, and sugar (for a touch of sweetness).",
        "image": "Krautsalat.jpg",
    },
    {
        "name": "Rettichsalat (Radish Salad)",
        "definition": "A radish salad with sliced radishes, sour cream or yogurt, chives, salt, and pepper.",
        "image": "Rettichsalat.jpg",
    },
    {
        "name": "Bohnensalat (Green Bean Salad)",
        "definition": "A green bean salad with blanched green beans, onions, bacon, vinegar and oil dressing, and fresh herbs (such as parsley or tarragon).",
        "image": "Green_Bean_Salad.jpg",
    },
    {
        "name": "Spargelsalat (Asparagus Salad)",
        "definition": "An asparagus salad with cooked white asparagus (in spring), hard-boiled eggs, fresh herbs, mayonnaise-based dressing, and lemon juice.",
        "image": "Spargelsalat.jpg",
    },
    {
        "name": "Kohlrabi Salat (Kohlrabi Salad)",
        "definition": "A kohlrabi salad with peeled and sliced kohlrabi, apples, lemon juice, mayonnaise or yogurt, and dill.",
        "image": "kohlrabi_salad.jpg",
    },
    {
        "name": "Salade Niçoise",
        "definition": "A Salade Niçoise with tuna, boiled or steamed green beans, cherry tomatoes, hard-boiled eggs, black olives, anchovies, potatoes (optional), and Dijon vinaigrette.",
        "image": "salade_nicoise.jpeg",
    },
    {
        "name": "Salade Lyonnaise",
        "definition": "A Salade Lyonnaise with frisée lettuce, bacon (lardons), poached or fried egg, croutons, and Dijon vinaigrette.",
        "image": "salade_lyonnaise.jpg",
    },
    {
        "name": "Salade Parisienne",
        "definition": "A Salade Parisienne with mixed greens, ham, Emmental cheese, mushrooms, hard-boiled eggs, and Dijon vinaigrette.",
        "image": "salade_parisienne.jpg",
    },
    {
        "name": "Salade Verte (Green Salad)",
        "definition": "A simple green salad with mixed greens, herbs (e.g., tarragon, chervil, or parsley), and a simple vinaigrette (olive oil, red wine vinegar, Dijon mustard).",
        "image": "green_salad.jpg",
    },
    {
        "name": "Salade de Chèvre Chaud (Warm Goat Cheese Salad)",
        "definition": "A warm goat cheese salad with mixed greens, warm goat cheese rounds, honey or balsamic reduction, and nuts (e.g., walnuts or almonds).",
        "image": "warm_goat_cheese_salad.jpg",
    },
    {
        "name": "Salade aux Lardons",
        "definition": "A Salade aux Lardons with romaine lettuce, bacon (lardons), tomatoes, Gruyère cheese, and a simple vinaigrette.",
        "image": "salade_aux_lardons.jpg",
    },
    {
        "name": "Salade de Betteraves (Beet Salad)",
        "definition": "A beet salad with roasted or boiled beets, goat cheese or feta, walnuts or pecans, and a simple vinaigrette.",
        "image": "beet_salad.jpg",
    },
    {
        "name": "Salade d'Endives (Endive Salad)",
        "definition": "An endive salad with endive leaves, Roquefort cheese, walnuts, and Dijon vinaigrette.",
        "image": "endive_salad.jpg",
    },
    {
        "name": "Salade de Lentilles (Lentil Salad)",
        "definition": "A lentil salad with cooked green or Puy lentils, carrots, onions, celery, and red wine vinaigrette.",
        "image": "lentil_salad.jpg",
    },
    {
        "name": "Salade de Céleri Rémoise (Celery Root Salad)",
        "definition": "A celery root salad with celery root (celeriac), apples, walnuts, mayonnaise or Dijon dressing.",
        "image": "celery_root_salad.jpeg",
    },
    {
        "name": "Salade de Tomates (Tomato Salad)",
        "definition": "A tomato salad with sliced tomatoes, red onion, fresh herbs (e.g., basil, parsley), and a simple vinaigrette.",
        "image": "tomato_salad.jpg",
    },
    {
        "name": "Greek Salad (Horiatiki Salata)",
        "definition": "A Greek salad with tomatoes, cucumbers, red onions, Kalamata olives, feta cheese, Greek extra virgin olive oil, oregano, and red wine vinegar.",
        "image": "greek_salad.jpg",
    },
    {
        "name": "Cretan Dakos (Koukouvagia)",
        "definition": "A Cretan salad with dried barley rusk (paximadi), tomatoes, feta or mizithra cheese, capers, olives, and olive oil.",
        "image": "cretan_dakos.jpg",
    },
    {
        "name": "Horta Salata (Wild Greens Salad)",
        "definition": "A salad with steamed or boiled wild greens (e.g., dandelion, chicory), olive oil, lemon juice, salt, and pepper.",
        "image": "wild_greens_salad.jpg",
    },
    {
        "name": "Maroulosalata (Romaine Lettuce Salad)",
        "definition": "A romaine lettuce salad with fresh dill or mint, scallions, Greek extra virgin olive oil, and lemon juice.",
        "image": "maroulosalata.jpeg",
    },
    {
        "name": "Melitzanosalata (Eggplant Salad)",
        "definition": "An eggplant salad with roasted or grilled eggplant, garlic, Greek yogurt or tahini, lemon juice, olive oil, and parsley.",
        "image": "eggplant_salad.jpeg",
    },
    {
        "name": "Tzatziki",
        "definition": "A classic Tzatziki with Greek yogurt, cucumber, garlic, dill, olive oil, and lemon juice.",
        "image": "tzatziki.jpg",
    },
    {
        "name": "Xoriatiki Salata (Greek Village Salad)",
        "definition": "Similar to the classic Greek salad, but with additional green bell peppers and sometimes capers.",
        "image": "village_salad.jpg",
    },
    {
        "name": "Revithosoupa (Chickpea Salad)",
        "definition": "A salad with cooked chickpeas, red onion, parsley, olive oil, and lemon juice.",
        "image": "chickpea_salade.jpg",
    },
    {
        "name": "Fasolada (Greek Bean Salad)",
        "definition": "A bean salad with white beans (cannellini or Great Northern), red onion, parsley, olive oil, and lemon juice.",
        "image": "Greek_Bean_Salad.jpg",
    },
    {
        "name": "Melon and Feta Salad",
        "definition": "A salad with watermelon or cantaloupe, feta cheese, fresh mint, Greek extra virgin olive oil, and balsamic vinegar (optional).",
        "image": "melon_feta_salad.jpg",
    },
    {
        "name": "Lahanosalata (Cabbage Salad)",
        "definition": "A cabbage salad with shredded cabbage, carrots, olive oil, lemon juice, Greek yogurt or mayonnaise (optional).",
        "image": "cabbage_salad.jpg",
    },
]
# Specify the path to your audio file
background_music_path = "background_music.mp3"  # Change this to your audio file path

class SaladSelectorApp(App):
    def build(self):
        self.title = "Salad Selector"
        self.current_salad = None
        self.selected_salads = []

        # Adjust label height based on screen size
        label_height = Window.height * 0.2  # 20% of screen height

        # Create a top-level layout using a BoxLayout with a vertical orientation
        self.layout = BoxLayout(orientation='vertical')

        # Create a RelativeLayout to hold the image and label
        self.container_layout = RelativeLayout()
        self.layout.add_widget(self.container_layout)

        # Create an AnchorLayout to center the image and label within the RelativeLayout
        self.anchor_layout = AnchorLayout(anchor_x="center", anchor_y="center")
        self.container_layout.add_widget(self.anchor_layout)

        # Create a ScrollView for the salad description (vertical scrolling)
        self.description_scrollview = ScrollView(size_hint=(1, 0.4))
        self.description_label = Label(text="", markup=True, size_hint=(1, None), height=label_height, halign='center')
        self.description_scrollview.add_widget(self.description_label)
        self.layout.add_widget(self.description_scrollview)

        # Create the image
        self.salad_image = Image(source="", size=(image_width, image_height), allow_stretch=True)
        self.anchor_layout.add_widget(self.salad_image)

        # Create a GridLayout to hold the buttons
        self.button_layout = GridLayout(cols=3, size_hint_y=None, height=40)

        # Create the buttons
        self.select_button = Button(text="Select Salad", on_press=self.select_salad)
        self.reload_button = Button(text="Reload", on_press=self.reset)
        self.close_button = Button(text="Close", on_press=self.close)

        # Add buttons to the button layout
        self.button_layout.add_widget(self.select_button)
        self.button_layout.add_widget(self.reload_button)
        self.button_layout.add_widget(self.close_button)

        # Add the button layout to the main layout
        self.layout.add_widget(self.button_layout)

        # Load and play background music
        self.background_music = SoundLoader.load(background_music_path)
        if self.background_music:
            self.background_music.loop = True
            self.background_music.play()

        self.all_salads_selected = False  # Flag to track if all salads are selected

        return self.layout

    def select_salad(self, instance):
        if salads:
            self.current_salad = random.choice(salads)
            salad_name = self.current_salad["name"]
            salad_definition = self.current_salad["definition"]
            self.salad_image.source = self.current_salad["image"]

            # Create fade-out animations
            fade_out_label = Animation(opacity=0, duration=0.5)
            fade_out_image = Animation(opacity=0, duration=0.5)

            # Bind a callback to the label fade-out animation to start the fade-in animation
            fade_out_label.bind(on_complete=self.fade_in_label)
            fade_out_label.start(self.description_label)

            fade_out_image.bind(on_complete=self.fade_in_image)
            fade_out_image.start(self.salad_image)

            self.next_salad_data = {
                "salad_name": salad_name,
                "salad_definition": salad_definition,
            }

        if not salads:
            self.all_salads_selected = True  # All salads are selected
            self.select_button.disabled = True  # Disable the "Select" button when all salads are selected
            self.update_popup(0)  # Show the popup

    def fade_in_label(self, instance, value):
        next_salad_name = self.next_salad_data["salad_name"]
        next_salad_definition = self.next_salad_data["salad_definition"]

        # Set the label text and opacity simultaneously
        self.description_label.text = "[b][size=24]" + next_salad_name + "[/size][/b]\n" + next_salad_definition
        self.description_label.opacity = 1

        # Create fade-in animation for the label
        fade_in_label = Animation(opacity=1, duration=0.5)
        fade_in_label.start(self.description_label)

    def fade_in_image(self, instance, value):
        # Create fade-in animation for the image
        fade_in_image = Animation(opacity=1, duration=0.5)
        fade_in_image.start(self.salad_image)

    def reset(self, instance):
        self.current_salad = None
        self.description_label.text = ""
        self.salad_image.source = ""
        self.select_button.disabled = False  # Re-enable the "Select" button
        self.selected_salads = []
        salads.extend(self.selected_salads)
        self.all_salads_selected = False  # Reset the flag



    def update_popup(self, dt):
        if self.all_salads_selected:
            self.show_restart_popup()

    def show_restart_popup(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='All salads have been selected!'))
        restart_button = Button(text='Close App')
        restart_button.bind(on_release=self.restart_app)
        content.add_widget(restart_button)

        popup = Popup(title='No More Salads', content=content, size_hint=(0.4, 0.3), auto_dismiss=False)  # Set auto_dismiss to False
        popup.open()

    def restart_app(self, instance):
        if self.background_music:
            self.background_music.stop()

        # Create a new instance of the app
        app = SaladSelectorApp()
        self.stop()


        # Close the current instance
        EventLoop.window.close()


    def close(self, instance):
        if self.background_music:
            self.background_music.stop()
        self.stop()

if __name__ == "__main__":
    app = SaladSelectorApp()
    app.run()

