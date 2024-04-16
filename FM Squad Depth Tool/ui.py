import tkinter as tk
from formation import Formation
from player_widget import PlayerWidget
from player_manager import PlayerManager

class UI:
    def __init__(self):
        self.window = tk.Tk()    
        self.window.title("FM Squad Depth Tool")
        self.canvas = tk.Canvas(self.window, width=500, height=660)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.pitch_image = tk.PhotoImage(file=r"C:\Users\Owner\dev\FM Squad Depth Tool\pitch.png")
        self.canvas.create_image(0,0,image=self.pitch_image, anchor=tk.NW)
        self.formation = Formation(self.canvas, self.window)
        self.manager = PlayerManager
        self.widgets = PlayerWidget(self.canvas, self.manager)
        self.setup_positions()
        #self.save_button = tk.Button(self.canvas, command=self.formation.save_complete_state, text="Save")
        #self.save_button_window = self.canvas.create_window(25,20, window=self.save_button)


    def setup_positions(self):
        player_positions= {
            "gk": (1,600, "gk"),
            "def": (4, 500, "def"),
            "dm": (0, 400, "dm"),
            "cm": (4, 300, "cm"),
            "am": (0, 200, "am"),
            "st": (2, 100, "st"),
        }
        for pos_id, (num_players, y, pos_key) in player_positions.items():
            self.formation.load_positions(num_players, y, pos_key)

   




