from time import time
from tkinter import Tk, Button, Label, Toplevel, Menu, Entry, IntVar, StringVar

from game.game_state import GameState
from game.scores import save_score

NO_GRAPHICS_ENVIRONMENT = -999

CR_EXIT = 0
CR_NEWGAME = 1

class UiState:
    def __init__(self, root, grid, game_state):
        self.root = root
        self.grid = grid
        self.game_state = game_state
        self.start_time = None
        self.close_reason = CR_EXIT

def run_graphical_ui():
    try:
        root = Tk()
    except:
        return NO_GRAPHICS_ENVIRONMENT

    width = 10
    height = 10
    num_mines = 10

    while True:
        game_state = GameState(width, height, num_mines)
        grid = [[None] * width for _ in range(height)]

        ui_state = UiState(root, grid, game_state)

        menu = Menu(root)
        root.config(menu=menu)

        new_game_menu = Menu(menu)
        menu.add_cascade(label="Uusi peli", menu=new_game_menu)
        new_game_menu.add_command(label="Helppo", command=lambda: new_game(ui_state, 10, 10, 10))
        new_game_menu.add_command(label="Keskitaso", command=lambda: new_game(ui_state, 16, 16, 40))
        new_game_menu.add_command(label="Vaikea", command=lambda: new_game(ui_state, 30, 16, 99))
        new_game_menu.add_command(label="Mukautettu", command=lambda: custom_new_game(ui_state))

        for y in range(height):
            for x in range(width):
                button = Button(
                        root,
                        width=2,
                        height=2,
                        command=button_command(ui_state, x, y))
                button.grid(column=x, row=y)
                grid[y][x] = button

        root.mainloop()

        cr = ui_state.close_reason

        if cr == CR_EXIT:
            return
        elif cr == CR_NEWGAME:
            (width, height, num_mines) = ui_state.new_game_params
            root = Tk()
            continue

# Funktion määritteleminen suoraan silmukassa ei toimi Python-syistä,
# joita en halua yrittää tämän enempää selvitellä.
def button_command(state, x, y):
    return lambda: open(state, x, y)

def custom_new_game(state):
    prompt = Toplevel(state.root)
    prompt.transient(state.root)

    width_label = Label(prompt, text="Leveys")
    width_var = IntVar()
    width_input = Entry(prompt, textvariable=width_var)
    height_label = Label(prompt, text="Korkeus")
    height_var = IntVar()
    height_input = Entry(prompt, textvariable=height_var)
    num_mines_label = Label(prompt, text="Miinojen lukumäärä")
    num_mines_var = IntVar()
    num_mines_input = Entry(prompt, textvariable=num_mines_var)
    ok_command = lambda: ask_params_ok(state, prompt, width_var, height_var, num_mines_var)
    ok_button = Button(prompt, text="Hyväksy", command=ok_command)
    cancel_button = Button(prompt, text="Peruuta", command=prompt.destroy)

    width_label.pack()
    width_input.pack()
    height_label.pack()
    height_input.pack()
    num_mines_label.pack()
    num_mines_input.pack()
    ok_button.pack()
    cancel_button.pack()

    prompt.mainloop()

def ask_params_ok(state, prompt, width_var, height_var, num_mines_var):
    try:
        width = int(width_var.get())
        height = int(height_var.get())
        num_mines = int(num_mines_var.get())
    except:
        return

    if width <= 0 or height <= 0 or num_mines <= 0:
        return

    new_game(state, width, height, num_mines)

def new_game(state, width, height, num_mines):
    state.close_reason = CR_NEWGAME
    state.new_game_params = (width, height, num_mines)
    state.root.destroy()

def open(state, x, y):
    state.game_state.open(x, y)

    for v in range(state.game_state.height):
        for u in range(state.game_state.width):
            if state.game_state.is_open(u, v):
                button = state.grid[v][u]
                num_surrounding = state.game_state.num_surrounding_mines(u, v)

                button["state"] = "disabled"
                button["bg"] = "lightgray"
                button["bd"] = 0

                if state.game_state.is_mine(u, v):
                    button["text"] = "*"
                    button["bg"] = "red"
                    button["disabledforeground"] = "black"
                elif num_surrounding:
                    button["text"] = str(num_surrounding)
                    button["disabledforeground"] = [
                            "blue",
                            "green",
                            "red",
                            "darkblue",
                            "darkred",
                            "cadetblue",
                            "purple",
                            "darkgrey"
                    ][num_surrounding - 1]

    if state.game_state.lost():
        for row in state.grid:
            for button in row:
                button["state"] = "disabled"
    elif state.game_state.solved():
        for row in state.grid:
            for button in row:
                button["state"] = "disabled"

        ask_name_and_save_score(
                state.root, int(time() - state.start_time),
                state.game_state.width,
                state.game_state.height,
                state.game_state.num_mines)
    elif not state.start_time:
        state.start_time = time()

def ask_name_and_save_score(root, score, width, height, num_mines):
    prompt = Toplevel(root)
    prompt.transient(root)

    label = Label(prompt, text="Voitit! Aikasi oli " + str(score) + " sekuntia. Syötä nimimerkki.")
    name_var = StringVar()
    name_input = Entry(prompt, textvariable=name_var)
    ok_command = lambda: ask_name_and_save_score_ok(prompt, score, name_var, width, height, num_mines)
    ok_button = Button(prompt, text="Tallenna", command=ok_command)
    cancel_button = Button(prompt, text="Peruuta", command=prompt.destroy)

    label.pack()
    name_input.pack()
    ok_button.pack()
    cancel_button.pack()

    prompt.mainloop()

def ask_name_and_save_score_ok(prompt, score, name_var, width, height, num_mines):
    name = name_var.get()

    if not name:
        return

    save_score(score, name, width, height, num_mines)
    prompt.destroy()