from typing import List, Literal, Optional
import json

from pydantic import BaseModel, Field


class BaseSimpleModel(BaseModel):
    class Config:
        allow_population_by_field_name = True

    def to_json(self):
        return json.dumps(
            self,
            default=lambda x: {k: v for k, v in vars(x).items()},
            indent=4, ensure_ascii=False
        ).encode('utf8').decode()


class BaseElement(BaseSimpleModel):
    type: str
    Value: str = ''
    height: Literal['wrap_content', 'match_parent'] = 'wrap_content'
    width: Literal['wrap_content', 'match_parent'] = 'match_parent'
    weight: int = 0


class TextElement(BaseElement):
    TextSize: str = ''
    TextColor: str = ''
    TextBold: bool = False
    TextItalic: bool = False


class LinearLayout(BaseSimpleModel):
    type: str = 'LinearLayout'
    Variable: Optional[str]
    height: Literal['wrap_content', 'match_parent'] = 'wrap_content'
    width: Literal['wrap_content', 'match_parent'] = 'wrap_content'
    weight: int = 0
    orientation: Literal['vertical', 'horizontal'] = 'horizontal'
    backgrpund_color: str = Field(default='', alias='BackgroundColor')
    StrokeWidth: int = 0
    padding: int = Field(default=0, alias='Padding')
    elements: List[BaseElement] = []

    gravity_vertical: str = ''
    gravity_horizontal: str = ''


class TextView(TextElement):
    type: str = 'TextView'
    gravity_horizontal: str = ''


class ModernEditText(TextElement):
    type: str = 'ModernEditText'
    variable: str = Field(alias='Variable')


class Button(TextElement):
    variable: str = Field(alias='Variable')


class Handler(BaseSimpleModel):
    type: str = 'python'
    action: str = 'run'
    event: str = 'onStart'
    method: str
    postExecute: str = ''
    listener: str = ''


class Operation(BaseSimpleModel):
    name: str = Field(alias='Name')
    hide_toolbar: bool = Field(default=False, alias="hideToolBarScreen")
    hide_bottom_bar: bool = Field(default=False, alias="hideBottomBarScreen")
    no_scroll: bool = Field(default=False, alias="noScroll")
    no_confirmation: bool = Field(default=False, alias="noConfirmation")
    elements: List[LinearLayout] = []
    handlers: List[Handler] = []
