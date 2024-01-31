from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import json
from constants import *


class Widget(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        self.type: str
        self.Value: str
        self.width = WRAP_CONTENT
        self.height = WRAP_CONTENT
        self.weight = 0

        if kwargs:
            for key, value in kwargs.items():
                self.__dict__[key] = value

    def __repr__(self):
        return f'Widget(type={self.type}, Value={self.Value})'

    def to_json(self):
        return json.dumps(self, default=lambda x: vars(x), indent=4)


class Picture(Widget):
    def __init__(self, **kwargs):
        self.Value = '@pic'
        super().__init__(**kwargs)
        self.type = "Picture"


class TextView(Widget):
    def __init__(self, **kwargs):
        self.Value = '@value'
        super().__init__(**kwargs)
        self.type = "TextView"


class CheckBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = 'CheckBox'


class PopupMenuButton(Widget):
    def __init__(self, **kwargs):
        self.Value = '@value'
        super().__init__(**kwargs)
        self.type = "PopupMenuButton"
        self.show_by_condition = ''
        self.NoRefresh = False
        self.document_type = ''
        self.mask = ''


class LinearLayout(Widget):
    def __init__(self, *args, **kwargs):
        self.type = 'LinearLayout'
        self.orientation = "vertical"

        super().__init__(**kwargs)
        self.Elements = list(args) or []

    def append(self, *widgets):
        for widget in widgets:
            self.Elements.append(widget)


class Options:
    def __init__(self, search_enabled=True, save_position=True, override_search=False):
        self.options = {
            'search_enabled': search_enabled,
            'save_position': save_position,
            'override_search': override_search
        }


class CustomCards:
    def __init__(self, layout: LinearLayout, options: Options, cardsdata: List[dict] = []):
        self.customcards = {
            'options': options or Options(),
            'layout': layout,
            'cardsdata': cardsdata
        }

    def to_json(self):
        return json.dumps(self, default=lambda x: vars(x), indent=4, ensure_ascii=False).encode('utf8').decode()


class CustomTable:
    def __init__(self, layout: LinearLayout, options: Options, tabledata: List[dict]):
        self.customtable = {
            'options': options or Options(),
            'layout': layout,
            'tabledata': tabledata
        }

    def to_json(self):
        return json.dumps(self, default=lambda x: vars(x), indent=4, ensure_ascii=False).encode('utf8').decode()


@dataclass
class ModernField:
    hint: str = ''
    default_text: str = ''
    counter: bool = False
    counter_max: int = 0
    input_type: int = 0
    password: bool = False
    events: bool = False

    def to_json(self):
        return json.dumps(
            self,
            default=lambda x: {k: v for k, v in vars(x).items() if v},
            indent=4, ensure_ascii=False
        ).encode('utf8').decode()
