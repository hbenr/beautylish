import requests
import json

class Beautylish:

    def __init__(self):
        """

        :param api_key:
        """

        self.base_url = 'https://www.beautylish.com/rest/interview-product/list'
        self.session = requests.Session()

    def get_products(self, save_to_file=False):
        """

        :return:
        """

        try:
            response = self.session.get(self.base_url, timeout=5)
            if response.status_code >= 400:
                response.raise_for_status()

        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

        if save_to_file:
            with open('products.json', 'w') as json_file:
                json.dump(response.json(), json_file)

        return response.json()['products']


if __name__ == '__main__':
    product_list = Beautylish().get_products()
    print(product_list)


