import argparse
from random_test_data_generator import generate_test_data
from output_formatter import format_output


def main():
    parser = argparse.ArgumentParser(description='Random Test Data Generator')
    parser.add_argument('--type', choices=['numeric', 'string', 'datetime'], default='numeric', help='Type of data to '
                                                                                                     'generate')
    parser.add_argument('--quantity', type=int, default=10, help="Quantity of test data to generate")
    parser.add_argument('--format', choices=['csv', 'json', 'sql'], default='csv', help='Output format')
    args = parser.parse_args()

    generated_data = generate_test_data(args.type, args.quantity)
    formatted_data = format_output(generated_data, args.format)
    print(formatted_data)


if __name__ == '__main__':
    main()
