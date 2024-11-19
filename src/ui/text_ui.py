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

class TextUi:
    def __init__(self):
        pass

    def run(self, state):
        while True:
            for y in range(state.height):
                print(" ".join(tile_str(state, x, y) for x in range(state.width)))

            print("")

            while True:
                user_input = read_input()

                if not user_input:
                    return

                if not state.is_valid_tile(*user_input):
                    continue

                break

            state.open(*user_input)
