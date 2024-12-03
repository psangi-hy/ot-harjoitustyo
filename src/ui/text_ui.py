from time import time

from game.game_state import GameState
from game.scores import save_score

def tile_str(state, x, y):
    if not state.is_open(x, y):
        return "."

    if state.is_mine(x, y):
        return "*"

    surr = state.num_surrounding_mines(x, y)
    if surr:
        return str(surr)

    return " "

def read_input():
    while True:
        i = input("Syötä koordinaatit: ")
        if i == "exit":
            return None

        s = i.split()
        if len(s) != 2 or not s[0].isdigit() or not s[1].isdigit():
            continue

        return (int(s[0]), int(s[1]))

def ask_difficulty():
    while True:
        i = input("Valitse vaikeustaso.\n1. Helppo\n2. Keskitaso\n3. Vaikea\n4. Mukautettu\n0. Poistu\n")

        if i.isdigit() and int(i) <= 4:
            return int(i)

def ask_parameter(prompt):
    while True:
        i = input(prompt)

        if i.isdigit() and int(i) >= 1:
            return int(i)

def run_text_ui():
    option = ask_difficulty()

    if not option:
        return
    elif option == 1:
        state = GameState(10, 10, 10)
    elif option == 2:
        state = GameState(16, 16, 40)
    elif option == 3:
        state = GameState(30, 16, 99)
    elif option == 4:
        width = ask_parameter("Pelikentän leveys: ")
        height = ask_parameter("Pelikentän korkeus: ")
        num_mines = ask_parameter("Miinojen lukumäärä: ")

        state = GameState(width, height, num_mines)
    else:
        assert False

    started = False

    while True:
        for y in range(state.height):
            print(" ".join(tile_str(state, x, y) for x in range(state.width)))

        if state.solved():
            solve_time = int(time() - start_time)
            print("Voitit! Aikasi oli " + str(solve_time) + " sekuntia.")
            name = input("Nimimerkki (jätä tyhjäksi ohittaaksesi): ")

            if name:
                save_score(solve_time, name, state.width, state.height, state.num_mines)

            return
        elif state.lost():
            print("Hävisit!")
            return

        print("")

        while True:
            user_input = read_input()

            if not user_input:
                return

            if not state.is_valid_tile(*user_input):
                continue

            break

        state.open(*user_input)

        if not started:
            started = True
            start_time = time()
