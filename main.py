import argparse

from app import core

def main():
    parser = argparse.ArgumentParser(description='Project CLI')
    parser.add_argument('--option', help='Specify an option', choices=['option1', 'option2'])
    # Add more CLI arguments as needed
    args = parser.parse_args()

    if args.option == 'option1':
        core.do_option1()
    elif args.option == 'option2':
        core.do_option2()
    else:
        print("Invalid option. Use --help for usage information.")

if __name__ == '__main__':
    main()
