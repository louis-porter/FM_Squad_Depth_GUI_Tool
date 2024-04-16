from ui import UI
from player_manager import PlayerManager
from player_widget import PlayerWidget

ui = UI()
playermanager = PlayerManager()
loaded_players = playermanager.load_state()
for player in loaded_players:
    new_widget = PlayerWidget(ui.canvas, playermanager)
    new_widget.update_info(player, player["x"], player["y"], player["role"])
ui.window.mainloop()