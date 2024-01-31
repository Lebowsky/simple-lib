from typing import Union, Callable, Any, NoReturn
import reprlib

from simple_kit import HashMap

current_screen: Union['BaseScreen', None] = None
next_screen: Union['BaseScreen', None] = None


class BaseScreen:
    screen_name: str
    process_name: str

    def __init__(self, hash_map: HashMap, **kwargs):
        self.kwargs = kwargs
        self.hash_map: HashMap = hash_map
        self.parent_screen = kwargs.get('parent')
        self.is_finish_process = False
        self.result_handler: Union[Callable[[Any], None], None] = None
        self.result_process = None
        self.screen_data = {}
        self.hash_map_keys = []

    @property
    def listener(self):
        if self.hash_map['event'] == 'onResult' and self.result_handler:
            self.result_handler(self.result_process)
            self.result_handler = None

        return self.hash_map.listener

    @listener.setter
    def listener(self, v):
        pass

    @property
    def event(self):
        return self.hash_map.event

    @event.setter
    def event(self, v):
        pass

    def on_start(self):
        pass

    def on_input(self):
        pass

    def init_screen(self) -> None:
        """implement this method"""
        pass

    def show(self) -> None:
        _set_next_screen(self)
        self.init_screen()
        self.hash_map.show_screen(self.screen_name)

    def _update_hash_map_keys(self):
        self.hash_map.put_data(
            {key: self.screen_data.get(key, '') for key in self.hash_map_keys}
        )

    def _show_parent_screen(self) -> None:
        if self.parent_screen:
            self.parent_screen.hash_map = self.hash_map
            self.parent_screen.show()
        else:
            raise ValueError(f'parent screen not set for {self}!')

    def _finish_process(self):
        self.is_finish_process = True
        self.hash_map.finish_process()

    def _finish_process_result(self, result=None):
        self.is_finish_process = True

        if self.parent_screen:
            self.parent_screen.hash_map = self.hash_map
            self.parent_screen.result_process = result
            _set_next_screen(self.parent_screen)
        self.hash_map.finish_process_result()

    def _get_selected_card_data(self, remove=True):
        selected_card_data = self.hash_map.get_json('selected_card_data')
        if remove:
            self.hash_map.remove('selected_card_data')

        return selected_card_data

    def _is_result_positive(self, _listener) -> bool:
        return self.listener == _listener and self.event == 'onResultPositive'

    def _is_result_negative(self, _listener) -> bool:
        return self.listener == _listener and self.event == 'onResultNegative'

    def _listener_not_implemented(self) -> NoReturn:
        raise NotImplementedError(f'listener {self.listener} not implemented')

    def __str__(self):
        return f'{self.process_name} / {self.screen_name}'

    def __repr__(self):
        kwargs = reprlib.repr([f'{k}={v}' for k, v in self.kwargs.items()])
        return f'{self.__class__.screen_name}(hash_map, {kwargs})'


def _set_next_screen(screen) -> None:
    global next_screen
    next_screen = screen
    return next_screen


def create_screen(hash_map, screen_class) -> BaseScreen:
    """
    Метод для получения модели экрана соответствующей текущему процессу и экрану.
    Реализован синглтон через глобальную переменную current_screen, для сохренения состояния текущего экрана
    """
    global current_screen, next_screen

    if type(current_screen) is not screen_class:
        if type(next_screen) is screen_class:
            current_screen = next_screen
            next_screen = None
            current_screen.hash_map = hash_map
        else:
            current_screen = screen_class(hash_map)
    else:
        current_screen.hash_map = hash_map
        current_screen.listener = hash_map['listener']
        current_screen.event = hash_map['event']

    if current_screen.is_finish_process:
        finish_screen = current_screen
        current_screen = None
        return finish_screen

    return current_screen
