import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='''
                    Program converts inputted string of digits into
                    given format, for example it converts 3425.00000 into
                    3 425
                    '''
    )
    parser.add_argument(
        '-n',
        '--number',
        help='Enter your number to format')
    return parser


def format_price(price):
    try:
        pattern = '{:,.0f}'
        price = float(price)
        if 0.005 < price % 1 <= 0.991:
            pattern = '{:,.2f}'
        return pattern.format(price).replace(',', ' ')
    except (ValueError, TypeError):
        pass


if __name__ == '__main__':
    parser = create_parser()
    input_price = parser.parse_args().number
    if input_price:
        output_price = format_price(input_price)
        if output_price:
            print(output_price)
        else:
            print('Incorrect input')
