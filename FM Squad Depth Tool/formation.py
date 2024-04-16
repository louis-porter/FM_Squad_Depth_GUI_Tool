import tkinter as tk
from player_dropdown import PlayerDropdown
from role_dropdown_utils import RoleDropdown
import json


class Formation:
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        self.player_dropdown = PlayerDropdown(self.canvas)
        self.role_dropdown = RoleDropdown(self.canvas)
    
    def calculate_start_end_dots(self, num_players, pos_id):
        if pos_id == "am" and num_players == 1:
            return 250,250
        elif pos_id == "am":
            return 400,100
        else:
            return 250 - 50 * (num_players - 1), 260 + 50 * (num_players - 1)
        

    def load_positions(self, num_players, y, pos_id):
        radius = 15
        start_x, end_x = self.calculate_start_end_dots(num_players, pos_id)
        spacing = (end_x - start_x) / max(num_players -1, 1)
        y_adjustment = 50
        for i in range(num_players):
            x = start_x + i * spacing
            adjusted_y = y - y_adjustment if num_players == 5 and (i == 0 or i == num_players - 1) else y
            self.canvas.create_oval(x-radius, adjusted_y-radius, x+radius, adjusted_y+radius, fill="light blue", tags=(pos_id, "player_spot"))
        self.canvas.tag_bind("player_spot", "<Button-1>", self.on_player_left_click)

    def on_player_left_click(self, event):
        clicked_item = event.widget.find_withtag("current")[0]
        x1,y1,x2,y2 = event.widget.coords(clicked_item)
        pos_x = int(x1-42.5)
        pos_y = int(y2)
        self.player_dropdown.show(pos_x, pos_y)



        



 