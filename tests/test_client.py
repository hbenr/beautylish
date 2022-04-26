import vcr
from pytest import fixture
from beautylish import Beautylish


@fixture
def product_keys():
    """
    Contains and returns test data associated with Beautylish products.

    :return: list of product properties/keys
    """

    return ['deleted', 'price', 'brand_name', 'id', 'hidden',
            'product_name']


@vcr.use_cassette('vcr_cassettes/beautylish_products.yml')
def test_beautylish_get_products(product_keys):
    """
    Tests API call to get a list of Beautylish products.

    """

    products_instance = Beautylish()
    response = products_instance.get_products()

    assert isinstance(response, list), "A list of products is returned"
    assert len(response) > 0, "Product list should contain at least 1 item"
    assert set(product_keys).issubset(response[0].keys()), "All keys should be in the response"
