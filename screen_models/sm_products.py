from simple_kit import Screen, HashMap


class Product(Screen):
    def __init__(self, hash_map: HashMap, **kwargs):
        super().__init__(hash_map, **kwargs)

    def on_start(self):
        pass

    def on_input(self):
        self.hash_map.toast(self.listener)


