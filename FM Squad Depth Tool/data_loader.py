import pandas as pd
import glob
import os


class DataLoader:
    def __init__(self):
        self.role_list = []
        file = r"C:\Users\Owner\dev\FM Squad Depth Tool\data.html"
        self.squad_rawdata_list = pd.read_html(file, header=0, encoding="utf-8", keep_default_na=False)
        self.squad_rawdata = self.squad_rawdata_list[0]
        self.calculate_dna_score()
        self.calculate_gk_score()
        self.calculate_CD_score()
        self.calculate_CM_score()
        self.calculate_DM_score()
        self.calculate_FB_score()
        self.calculate_ST_score()
        self.calculate_W_score()
        self.player_data = self.create_player_list()


    def calculate_dna_score(self):
        self.squad_rawdata["DNA"] = ((
            self.squad_rawdata["Wor"] +
            self.squad_rawdata["Tec"] +
            self.squad_rawdata["Dec"] +
            self.squad_rawdata["Pas"] +
            self.squad_rawdata["OtB"]
        ) / 5).round(1)

    def calculate_gk_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ['Ref', 'Pas','Cmp'],
            'core': ['Dec','Fir','1v1', 'Aer', 'Han', 'Kic', 'Thr'],
            'secondary': ['Agi','Pos','Cmd','Acc','Vis','Cnt','Ant']
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"gk_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["GK"] = ((self.squad_rawdata["gk_essential"] + self.squad_rawdata["gk_core"]
                                     + self.squad_rawdata["gk_secondary"]) / total_weight).round(1)
        
        self.role_list.append("GK")

    def calculate_CD_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Pos", "Acc", "Cmp"],
            'core': ["Pas", "Hea", "Tck", "Agg", "Bra", "Jum", "Str"],
            'secondary': ["Fir", "Mar", "Tec", "Ant", "Cnt"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"cd_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["CD"] = ((self.squad_rawdata["cd_essential"] + self.squad_rawdata["cd_core"]
                                     + self.squad_rawdata["cd_secondary"]) / total_weight).round(1)
        
        self.role_list.append("CD")

    def calculate_DM_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Wor", "Pos", "Pas", "Dec"],
            'core': ["Sta", "Cnt", "Cmp", "Ant", "Fir", "Tck"],
            'secondary': ["Tec", "Vis", "Bal", "Str"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"dm_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["DM"] = ((self.squad_rawdata["dm_essential"] + self.squad_rawdata["dm_core"]
                                     + self.squad_rawdata["dm_secondary"]) / total_weight).round(1)
        
        self.role_list.append("DM")



    def calculate_FB_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Wor", "Sta", "Acc"],
            'core': ["Pac", "OtB", "Fir", "Pas", "Agi"],
            'secondary': ["Cnt", "Tck", "Tec", "Fir", "Dri", "Dec", "Ant", "Agg", "Jum"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"FB_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["FB"] = ((self.squad_rawdata["FB_essential"] + self.squad_rawdata["FB_core"]
                                     + self.squad_rawdata["FB_secondary"]) / total_weight).round(1)
        
        self.role_list.append("FB")


    def calculate_CM_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Fir", "Cmp", "Pas", "Vis", "Tec"],
            'core': ["Wor", "Dri", "Sta", "OtB", "Bal", "Dec"],
            'secondary': ["Ant", "Tck", "Agg"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"CM_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["CM"] = ((self.squad_rawdata["CM_essential"] + self.squad_rawdata["CM_core"]
                                     + self.squad_rawdata["CM_secondary"]) / total_weight).round(1)
        
        self.role_list.append("CM")

    def calculate_W_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Acc", "Pac", "Dri"],
            'core': ["Cro", "Tec", "Wor", "Sta", "Ant", "OtB"],
            'secondary': ["Bal", "Dec", "Fir", "Agg", "Cmp", "Pas"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"W_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["W"] = ((self.squad_rawdata["W_essential"] + self.squad_rawdata["W_core"]
                                     + self.squad_rawdata["W_secondary"]) / total_weight).round(1)
        
        self.role_list.append("W")


    def calculate_ST_score(self):
        category_weights = {"essential":5, "core":3, "secondary":1}
        attribute_groups = {
            'essential': ["Acc", "Fin", "Fir"],
            'core': ["Pac", "Hea", "Agi", "Str", "Sta", "OtB", "Cmp"],
            'secondary': ["Ant", "Dri", "Dec", "Jum", "Wor"]
        }

        total_weight = 0

        for category, attributes in attribute_groups.items():
            self.squad_rawdata[f"ST_{category}"] = self.squad_rawdata[attributes].sum(axis=1) * category_weights[category]
            total_weight += category_weights[category] * len(attributes)

        self.squad_rawdata["ST"] = ((self.squad_rawdata["ST_essential"] + self.squad_rawdata["ST_core"]
                                     + self.squad_rawdata["ST_secondary"]) / total_weight).round(1)
        
        self.role_list.append("ST")

             
        

    def create_player_list(self):
        player_list = []
        for index, row in self.squad_rawdata.iterrows():
            player_dict = {
                "ID": index,
                "name": row["Name"],
                "DNA": row["DNA"],
                "GK": row["GK"],
                "CD": row["CD"],
                "FB": row["FB"],
                "DM": row["DM"],
                "CM": row["CM"],
                "W": row["W"],
                "ST": row["ST"]
            }
            player_list.append(player_dict)
        return player_list
















players = [
    {"name": "Martin Odegaard",
     "age": 23,
     "score": 15.2},
     {"name": "Gabriel",
     "age": 24,
     "score": 14.7},
     {"name": "Benjamin White",
     "age": 25,
     "score": 14.8},

]