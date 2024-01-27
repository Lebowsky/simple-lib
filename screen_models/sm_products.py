from simple_kit import Screen, HashMap


class ProductsListScreen(Screen):
    def __init__(self, hash_map: HashMap, **kwargs):
        super().__init__(hash_map, **kwargs)

    def on_start(self):
        pass

    def on_input(self):
        if self.listener == 'set_en':
            self.hash_map['setLocale'] = 'en'
        elif self.listener == 'set_ru':
            self.hash_map['setLocale'] = 'ru'

        self.hash_map.update_configurations()


class ProductItemScreen(Screen):
    def __init__(self, hash_map: HashMap, **kwargs):
        super().__init__(hash_map, **kwargs)


