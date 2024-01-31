from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class BaseElement(BaseModel):
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


class LinearLayout(BaseModel):
    type: str = 'LinearLayout'
    Variable: Optional[str]
    height: Literal['wrap_content', 'match_parent'] = 'wrap_content'
    width: Literal['wrap_content', 'match_parent'] = 'match_parent'
    weight: int = 0
    orientation: Literal['vertical', 'horizontal'] = 'horizontal',
    BackgroundColor: str = '',
    StrokeWidth: int = 0,
    padding: int = Field(default=0, alias='Padding')
    elements: List[BaseElement] = []


class TextView(TextElement):
    type: str = 'TextView'


class ModernEditText(TextElement):
    type: str = 'ModernEditText'


class Button(TextElement):
    variable: str = Field(alias='Variable')


class Operation(BaseModel):
    name: str = Field(alias='Name')
    hide_toolbar: bool = Field(default=False, alias="hideToolBarScreen")
    hide_bottom_bar: bool = Field(default=False, alias="hideBottomBarScreen")
    no_scroll: bool = Field(default=False, alias="noScroll")
    no_confirmation: bool = Field(default=False, alias="noConfirmation")
    elements: List[LinearLayout]
