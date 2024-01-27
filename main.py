from simple_kit import HashMap, create_screen

from screen_models import ProductsListScreen


@HashMap()
def app_on_start(hash_map: HashMap):
    hash_map.toast('on_start')
    hash_map.beep()


@HashMap()
def products_on_start(hash_map):
    create_screen(hash_map, ProductsListScreen).on_start()


@HashMap()
def products_on_input(hash_map):
    create_screen(hash_map, ProductsListScreen).on_input()
