from typing import Callable, Union, List, Dict, Any
from functools import wraps
import json


class HashMap:
    def __init__(self):
        self.hash_map = None

    def __call__(self, func: Callable[..., None]):
        @wraps(func)
        def wrapper(hash_map, *args, **kwargs):
            self.hash_map = hash_map
            func(self)
            return hash_map

        return wrapper

    def __getitem__(self, item):
        return self.get(item, False)

    def __setitem__(self, key, value):
        self.put(key, value, False)

    @property
    def listener(self):
        return self['listener']

    @listener.setter
    def listener(self, v):
        pass

    @property
    def event(self):
        return self['event']

    @event.setter
    def event(self, v):
        pass

    def get(self, item, from_json=False):
        if from_json:
            return json.loads(self.hash_map.get(item)) if self.hash_map.get(item) else None
        else:
            return self.hash_map.get(item)

    def get_bool(self, item) -> bool:
        value = str(self.hash_map.get(item)).lower() not in ('0', 'false', 'none')
        return value

    def get_json(self, item):
        return json.loads(self.hash_map.get(item)) if self.hash_map.get(item) else None

    def put(self, key, value: Union[str, List, Dict, bool] = '', to_json=False):
        if to_json:
            self.hash_map.put(key, json.dumps(value))
        else:
            if isinstance(value, bool):
                value = str(value).lower()
            self.hash_map.put(key, str(value))

    def put_bool(self, key, value: Any):
        value = False if str(value).lower() in ('false', 'none', '0') else bool(value)
        self.put(key, value)

    def remove(self, key):
        self.hash_map.remove(key)

    def toast(self, text):
        self.hash_map.put('toast', str(text))

    def show_screen(self, screen_name):
        self.put('ShowScreen', screen_name)

    def finish_process(self):
        self.hash_map.put('FinishProcess', '')

    def finish_process_result(self):
        self.hash_map.put('FinishProcessResult', '')

    def no_refresh(self):
        self['NoRefresh'] = ''
