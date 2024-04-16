from player_manager import PlayerManager
from player_dropdown_ui import PlayerDropdownUI
from role_dropdown_utils import RoleDropdown


class PlayerDropdown:
    def __init__(self, parent_canvas):
        self.canvas = parent_canvas
        self.manager = PlayerManager()
        self.role_dropdown = RoleDropdown(self.canvas)
        self.ui = PlayerDropdownUI(parent_canvas, self.manager, self.role_dropdown)
        self.restore_players()

    def show(self,x,y):
        self.ui.show_dropdown(x,y)

    def restore_players(self):
        players = self.manager.load_state()
        for player in players:
            self.manager.add_player(player)