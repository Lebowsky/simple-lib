from simple_kit import HashMap, create_screen

from screen_models import SettingsScreen


@HashMap()
def app_on_start(hash_map: HashMap):
    hash_map.toast("it's work!")


@HashMap()
def settings_on_start(hash_map: HashMap):
    create_screen(hash_map, SettingsScreen).on_start()
