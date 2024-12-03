from ui.graphical_ui import run_graphical_ui, NO_GRAPHICS_ENVIRONMENT
from ui.text_ui import run_text_ui

rc = run_graphical_ui()

if rc == NO_GRAPHICS_ENVIRONMENT:
    run_text_ui()
