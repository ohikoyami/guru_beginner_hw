import requests
from pydantic import BaseModel

from data.ponchik_info import Ponchik
from products.raspberry_pistachio_shell import raspberry_pistachio_shell
from classes.api.PageClasses_API import Cart, Favorite

cart = Cart()
favorite = Favorite()


def test_api(api_session):
    cart.add_product_to_cart(raspberry_pistachio_shell, api_session)
    cart.update_product_quantity(raspberry_pistachio_shell, api_session)
    cart.get_cart_data(api_session)

    favorite.add_in_favorite(raspberry_pistachio_shell, api_session)
    favorite.update_favorite_product(raspberry_pistachio_shell, api_session)
    favorite.get_favorite_products(api_session)
