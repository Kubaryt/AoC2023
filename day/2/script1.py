from game_class import Game


def get_games(file_name: str) -> list[Game]:
    i = 1
    games_list = []
    with open(file_name) as f:
        for line in f:
            new_game = Game()
            new_game.id = i
            new_game.games = []
            line = line.split(":")[1]
            line = line.strip().split(";")
            for row in line:
                row = row.split(",")
                new_game_table = []
                for item in row:
                    item = item.strip()
                    new_game_table.append(item)
                new_game.games.append(new_game_table)
            games_list.append(new_game)
            i+=1
    return games_list


def validate_games(games_list: list[Game]) -> list:
    valid_games_id = []
    for game in games_list:
        _id = game.validate_game()
        valid_games_id.append(_id)

    return valid_games_id

if __name__ == "__main__":
    _games_list = get_games("input")
    valid_ids = validate_games(_games_list)
    print(sum(valid_ids))
