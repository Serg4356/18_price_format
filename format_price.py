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
        if price % 1 > 0:
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
    print(format_price(2345))
    print(format_price([1,2,3,4]))
    print(format_price('1000000'))
    print(format_price('1000000.123123123'))
    print(format_price('1000000.0000000'))
    print(format_price('sfesefes'))
    print(format_price(None))
    print(format_price(1000000.2132131))
    print(format_price(1000000.9999))
    print(format_price(1000000.000000))
    print(format_price(1000000.))
    print(format_price(format_price))
