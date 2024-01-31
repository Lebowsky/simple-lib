from simple_kit import HashMap, BaseScreen


class SettingsScreen(BaseScreen):
    def __init__(self, _hash_map: HashMap, **kwargs):
        super().__init__(_hash_map, **kwargs)
        self.is_init = True
        self.init_screen()

    def init_screen(self) -> None:
        pass
        # self._render_screen()

    def on_start(self):
        if self.is_init:
            super().on_start()
            self.hash_map.toast('screen is ready')
            self.is_init = False
            self._render_screen()

    def on_input(self):
        super().on_input()
        if self.listener == 'text':
            self.hash_map.toast('screen is input')
        elif self.listener == 'ON_BACK_PRESSED':
            self.hash_map.toast(self._finish_process())

    def _render_screen(self):
        screen = {
            "type": "Operation",
            "Name": "[SettingsScreen]",
            "hideToolBarScreen": False,
            "hideBottomBarScreen": True,
            "noScroll": False,
            "noConfirmation": True,
            "Elements": [{
                "type": "LinearLayout",
                "Variable": "",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "Value": "TEST",
                        "Variable": "text",
                        "height": "wrap_content",
                        "width": 'match_parent',
                        "weight": 1,
                        "TextSize": "",
                        "TextColor": "",
                        "TextBold": False,
                        "TextItalic": False,
                        "type": "ModernEditText"
                    },
                    {
                        "Value": "TEST",
                        "Variable": "text",
                        "height": "wrap_content",
                        "width": 'match_parent',
                        "weight": 1,
                        "TextSize": "",
                        "TextColor": "",
                        "TextBold": False,
                        "TextItalic": False,
                        "type": "Button"
                    },
                ],
                "BackgroundColor": "",
                "StrokeWidth": "",
                "Padding": ""
            }],
            "Handlers": [
                {
                    "type": "python",
                    "action": "run",
                    "event": "onStart",
                    "method": "settings_on_start",
                    "postExecute": "",
                    "listener": ""
                },
                {
                    "type": "python",
                    "action": "run",
                    "event": "onInput",
                    "method": "settings_on_input",
                    "postExecute": "",
                    "listener": ""
                }
            ]
        }
        self.hash_map.set_json_screen(screen=screen)
