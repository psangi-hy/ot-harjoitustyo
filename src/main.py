from ui.text_ui import TextUi
from game.game_state import GameState

ui = TextUi()
state = GameState(10, 10, 10)

ui.run(state)
