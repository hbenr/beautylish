"""
Part 2
● Write a test case for your solution."""

from beautylish import Beautylish
import pandas as pd


def main():
    beautylish_client = Beautylish()
    products = beautylish_client.get_products(save_to_file=True)

    # Create a pandas DataFrame from the API response
    # df = pd.read_json('products.json')
    df = pd.DataFrame(products)

    # Filter out any products that are hidden or deleted.
    df = df[~df.deleted & ~df.hidden]

    # Sort by lowest to highest price. If two items have the same price, sort by name.
    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    df.sort_values(by=['price', 'product_name'], inplace=True)

    # If the same product is included twice, only display it once.
    df.drop_duplicates(inplace=True)

    print(df)

    # Display a summary that includes:
    # The total number of unique products
    # The total number of unique brands
    # The average price
    print(f'\nTotal number of unique products: {df.product_name.nunique()}')
    print(f'Total number of unique brands: {df.brand_name.nunique()}')
    print(f'Average price: {df.price.mean():.2f}')


if __name__ == '__main__':
    main()

