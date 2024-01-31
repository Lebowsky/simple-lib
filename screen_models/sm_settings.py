from simple_kit import HashMap, BaseScreen


class SettingsScreen(BaseScreen):
    def __init__(self, _hash_map: HashMap, **kwargs):
        super().__init__(_hash_map, **kwargs)

    def on_start(self):
        # super().on_start()
        self.hash_map.toast('screen is ready')

        # screen_elements = [
        #     sm_types.VerticalLayout(
        #
        #     )
        # ]
        # sdm = ScreenDataModel(title='TITLE', is_true=True, table_data=[{1: 1, 2: 2}])
        # factory = screens.ScreenFactory('settings', sdm)
        # screen = factory.create()
        # self.hash_map.put('setJSONConfiguration', screen, to_json=True)

    def on_input(self):
        super().on_input()
