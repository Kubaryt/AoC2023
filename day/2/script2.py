from script1 import get_games
from game_class import Game


def sum_powers(game_list: list[Game]) -> int:
    power_sum = 0
    for game in game_list:
        power_sum += game.get_power_of_game()
    return power_sum


if __name__ == "__main__":
    _game_list = get_games("input")
    print(sum_powers(_game_list))
