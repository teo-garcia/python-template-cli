from app import cli, core


def main():
  option_actions = {
      'optionA': core.do_optionA,
      'optionB': core.do_optionB,
      'exit': lambda: print("\n Thank you for using the Project CLI. Goodbye! \n")
  }

  selected_option = cli.run_cli()
  action = option_actions.get(selected_option)

  if action:
      action()

if __name__ == '__main__':
    main()
