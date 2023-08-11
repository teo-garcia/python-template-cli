import questionary
import colorama


def run_cli():
    colorama.init()
    print(f"\n {colorama.Fore.BLUE} Python Template CLI {colorama.Style.RESET_ALL} \n")

    options = {"Option A": "optionA", "Option B": "optionB", "Exit": "exit"}

    while True:
        selected_option = questionary.select(
            "Select an option:", choices=list(options.keys())
        ).ask()

        option_name = options.get(selected_option)

        return option_name
