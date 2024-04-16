import tkinter as tk
from tkinter import ttk
from role_dropdown_utils import RoleDropdown
from player_widget import PlayerWidget

class PlayerDropdownUI:
    def __init__(self, parent_canvas, manager, role_dropdown):
        self.canvas = parent_canvas
        self.manager = manager
        self.role_dropdown = role_dropdown

    def show_dropdown(self, x, y):
        self.abs_x = self.canvas.winfo_rootx() + x
        self.abs_y = self.canvas.winfo_rooty() + y

        dropdown_window = tk.Toplevel(self.canvas)
        dropdown_window.wm_overrideredirect(True)
        dropdown_window.geometry(f"+{self.abs_x}+{self.abs_y}")

        selected_option = tk.StringVar(dropdown_window)
        combobox = ttk.Combobox(dropdown_window, textvariable=selected_option, state="readonly")
        combobox["values"] = [player["name"] for player in self.manager.available_players]
        combobox.set("Select a player")
        combobox.pack(fill="both", expand=True)
        combobox.bind("<<ComboboxSelected>>", lambda event: self.on_option_select(selected_option.get(), x, y, dropdown_window))

    def on_option_select(self, player_name, x, y, window):
        player = self.manager.find_and_remove_player(player_name)
        if player:
            self.role_dropdown.show_dropdown(x=self.abs_x, y=self.abs_y,
                                              callback=lambda role: self.update_player_widget_with_role(player, role, x, y, window))

    def update_player_widget_with_role(self, player, role, x, y, window):
        for loaded_player in self.manager.save_states:
            if loaded_player["y"] == y and loaded_player["x"] == x+10:
                y += 22
        self.player = PlayerWidget(self.canvas, self.manager).update_info(player, x+10, y, role)
        player["role"] = role
        player["x"] = x+10
        player["y"] = y
        self.manager.save_states.append(player)
        self.manager.save_state(self.manager.save_states)
        window.destroy()