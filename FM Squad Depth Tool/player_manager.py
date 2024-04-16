import json
from data_loader import DataLoader


class PlayerManager:
    def __init__(self):
        self.dataloader = DataLoader()
        self.available_players = self.dataloader.player_data
        self.save_states = self.load_state()

    def add_player(self, player):
        if not any(p["name"] == player["name"] for p in self.available_players):
            self.available_players.append(player)
        
    def find_and_remove_player(self, name):
        player = next((p for p in self.available_players if p["name"] == name), None)
        if player:
            self.available_players.remove(player)
        return player

    def load_state(self, filename="save_player_state.json"):
        with open(filename, "r") as f:
            loaded_data = json.load(f)
            return loaded_data
            
        
    def save_state(self, players, filename="save_player_state.json"):
        with open(filename, "w") as f:
            json.dump(players, f)