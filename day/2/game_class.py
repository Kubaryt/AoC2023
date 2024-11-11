class Game:
    id = int
    games = list
    def validate_game(self) -> int:
        if self.games is None:
            return 0
        for game_table in self.games:
            for item in game_table:
                item = item.split(" ")
                match item[1]:
                    case "red":
                        if int(item[0]) > 12:
                            return 0
                    case "green":
                        if int(item[0]) > 13:
                            return 0
                    case "blue":
                        if int(item[0]) > 14:
                            return 0
        return self.id

    def get_power_of_game(self) -> int:
        if self.games is None:
            return 0
        games_list = self.games
        games_list[0] = games_list[0] + games_list[1] + games_list[2]
        games_list.pop(1)
        games_list.pop(1)
        power_multipliers = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for table in games_list:
            for item in table:
                item = item.split(" ")
                _ = int(item[0])
                match item[1]:
                    case "red":
                        if _ > power_multipliers["red"]:
                            power_multipliers["red"] = _
                    case "green":
                        if _ > power_multipliers["green"]:
                            power_multipliers["green"] = _
                    case "blue":
                        if _ > power_multipliers["blue"]:
                            power_multipliers["blue"] = _
        power = power_multipliers["red"] * power_multipliers["green"] * power_multipliers["blue"]
        return power
