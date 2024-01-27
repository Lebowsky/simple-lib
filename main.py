from simple_kit import HashMap, create_screen

from screen_models import Product


@HashMap()
def products_on_start(hash_map):
    create_screen(hash_map, Product).on_start()


@HashMap()
def products_on_input(hash_map):
    create_screen(hash_map, Product).on_input()
