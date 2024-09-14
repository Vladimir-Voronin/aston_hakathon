"""Some useful function for all project"""
import json
import inspect
from pathlib import Path
from colorama import Fore, Style, init
init()


def show_file_hints(hint_level=1, show_all=False):
    """Showing hints for the task based on file name from which this func was called."""
    stack = inspect.stack()
    caller_frame = stack[1]
    module = inspect.getmodule(caller_frame[0])
    full_path = Path(module.__file__)
    key = full_path.name.removesuffix('.py')
    with open(r'data/hints.json', 'r', encoding='utf-8') as hint_file:
        hints_json = json.load(hint_file)
    hints = hints_json[key]["hints"]
    print("\nYour hint(s):")
    if show_all:
        hint_level = float('inf')
    for cur_level, hint in enumerate(hints):
        if cur_level == hint_level:
            break
        print(Fore.YELLOW + f'\tLevel {cur_level + 1}: {hint}', end='\n\n' + Style.RESET_ALL)

    else:
        print(Fore.RED + '\tЭто была последняя подсказка.' + Style.RESET_ALL)


if __name__ == '__main__':
    pass
