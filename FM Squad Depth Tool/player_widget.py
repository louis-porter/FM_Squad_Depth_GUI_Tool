import tkinter as tk
from player_manager import PlayerManager

class PlayerWidget(tk.Frame):
    def __init__(self, parent, manager, **kwargs):
        super().__init__(parent, **kwargs)
        self.manager = manager
        self.score_label = tk.Label(self, text="", font=("Arial", 7), width = 3,
                                     relief=tk.RAISED, bg="white")
        self.score_label.pack(side=tk.LEFT)
        self.score_label.bind("<Button-1>", self.delete_widget)
        self.name_label = tk.Label(self, text="", font=("Arial", 8), width = 11, 
                                   relief=tk.RAISED, bg="white")
        self.name_label.pack(side=tk.LEFT)
        self.name_label.bind("<Button-1>", self.delete_widget)

    def update_info(self, player_info, x_pos, y_pos, role):
        self.player_info = player_info
        name_parts = player_info["name"].split()
        formatted_name = f"{name_parts[0][0]}. {name_parts[-1]}" if len(name_parts) > 1 else name_parts[0]
        self.player_name = formatted_name
        self.player_role_score = player_info.get(role, "")
        self.score_label.config(text=self.player_role_score)
        self.name_label.config(text=self.player_name)
        self.place(x=x_pos, y=y_pos)
        self.lift()

    def delete_widget(self, event):
        if hasattr(self, "player_info"):
            # Remove player from the in-memory list and update the save file.
            self.manager.find_and_remove_player(self.player_info["name"])
            updated_players = [player for player in self.manager.load_state() if player["ID"] 
                               != self.player_info["ID"]]
            self.manager.save_state(updated_players)
            self.destroy()    
