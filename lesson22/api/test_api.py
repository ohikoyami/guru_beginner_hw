from api.pages.cart import cart
from api.pages.favorites import add_in_favorite, update_favorite_product, get_favorite_products


def test_api():
    cart.add_to_cart().update_product_quantity().get_cart_data()
    add_in_favorite()
    update_favorite_product()
    get_favorite_products()
