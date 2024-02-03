import requests

LIB_URL = 'http://localhost'
# from simple_kit import HashMap, create_screen
#
# from screen_models import SettingsScreen


# @HashMap()
def app_on_start(hash_map, _, __):
    requests.get(LIB_URL)
    return hash_map


# @HashMap()
# def settings_on_start(hash_map: HashMap):
#     create_screen(hash_map, SettingsScreen).on_start()
#
#
# @HashMap()
# def settings_on_input(hash_map: HashMap):
#     create_screen(hash_map, SettingsScreen).on_input()
