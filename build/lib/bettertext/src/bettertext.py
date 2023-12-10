import time
import sys
import colorama
from typing import Union

class betterText(object):
    """Modify text in fun ways in the python terminal. Great for command line/text games.
    
    commands:
        foreground.{color}(string) -- changes the foreground color of a string in the python terminal.
        background.{color}(string) -- changes the background color of a string in the python terminal.

        reverse(string) -- reverses the string. 'hello world' -> 'dlrow olleh'
        flip(string) -- reverses the order of the string. "hello world" -> "world hello"
        vertical(string) -- puts one letter on each line.
        typewrite(string, time) -- types out a sting letter by letter every time increment.
        number(string, start, step, delimiter) -- numbers each word in the string starting with start, going up by step, and seperating by delimiter.
        repeat(string, amount, delimiter) -- repeat each word amount amount of times seperated by delimiter.
        hashtag(string) -- makes string into a hashtag with all words starting with capital, and no spaces.
        abreviate(string, delimiter, upper) -- makes abreviation of word seperated by delimiter, and uppercase if upper is True.
        blink(string, time, length) -- string blinks every time for length. Note: nothing can happen during blinking phase.
    """
    def __init__(self):
        pass
    class foreground:
        """Change the foreground color of python terminal text.

        usage: betterText.foreground.color(string)
        returns: String with specified foreground color
        """
        def __init__(self):
            pass
        
        def red(s: str) -> str:
            return f"{colorama.Fore.RED}{s}{colorama.Fore.RESET}"
        def yellow(s: str) -> str:
            return f"{colorama.Fore.YELLOW}{s}{colorama.Fore.RESET}"
        def green(s: str) -> str:
            return f"{colorama.Fore.GREEN}{s}{colorama.Fore.RESET}"
        def blue(s: str) -> str:
            return f"{colorama.Fore.LIGHTBLUE_EX}{s}{colorama.Fore.RESET}"
        def cyan(s: str) -> str:
            return f"{colorama.Fore.CYAN}{s}{colorama.Fore.RESET}"
        def indigo(s: str) -> str:
            return f"{colorama.Fore.BLUE}{s}{colorama.Fore.RESET}"
        def magenta(s: str) -> str:
            return f"{colorama.Fore.MAGENTA}{s}{colorama.Fore.RESET}"
        def lime(s: str) -> str:
            return f"{colorama.Fore.LIGHTGREEN_EX}{s}{colorama.Fore.RESET}"
        def black(s: str) -> str:
            return f"{colorama.Fore.BLACK}{s}{colorama.Fore.RESET}"
        def white(s: str) -> str:
            return f"{colorama.Fore.WHITE}{s}{colorama.Fore.RESET}"
        
    class background:
        """Change the background color of python terminal text.

        usage: betterText.background.color(string)
        returns: String with specified background color
        """
        def __init__(self):
            pass
        
        def red(s: str) -> str:
            return f"{colorama.Back.RED}{s}{colorama.Back.RESET}"
        def yellow(s: str) -> str:
            return f"{colorama.Back.YELLOW}{s}{colorama.Back.RESET}"
        def green(s: str) -> str:
            return f"{colorama.Back.GREEN}{s}{colorama.Back.RESET}"
        def blue(s: str) -> str:
            return f"{colorama.Back.LIGHTBLUE_EX}{s}{colorama.Back.RESET}"
        def cyan(s: str) -> str:
            return f"{colorama.Back.CYAN}{s}{colorama.Back.RESET}"
        def indigo(s: str) -> str:
            return f"{colorama.Back.BLUE}{s}{colorama.Back.RESET}"
        def magenta(s: str) -> str:
            return f"{colorama.Back.MAGENTA}{s}{colorama.Back.RESET}"
        def lime(s: str) -> str:
            return f"{colorama.Back.LIGHTGREEN_EX}{s}{colorama.Back.RESET}"
        def black(s: str) -> str:
            return f"{colorama.Back.BLACK}{s}{colorama.Back.RESET}"
        def white(s: str) -> str:
            return f"{colorama.Back.WHITE}{s}{colorama.Back.RESET}"
    
    def reverse(s: str) -> str:
        return s[::-1]
    
    def flip(s: str) -> str:
        return " ".join(s.split()[::-1])

    def vertical(s: str) -> str:
        return "\n".join(char for char in s)
    
    def typewrite(s: str, t: Union[float, int] = 0.25) -> None:
        for char in s:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(t)
        sys.stdout.write("\n")
    
    def number(s: str, start: int = 1, step: int = 1, delimiter: str = "") -> str:
        return " ".join([f"{char}{delimiter}{(n+start)*step}" for n,char in enumerate(s.split())])
    
    def toadify(s: str) -> str:
        return " toad ".join(s.split()) + " toad"

    def repeat(s: str, amount: int = 10, delimiter: str = "") -> str:
        return "".join(f"{s}{delimiter}"*amount)

    def hashtag(s: str) -> str:
        return f"#{''.join(s.title().split())}"
    
    def abbreviate(s: str, delimiter: str = ".", upper: bool = True) -> str:
        return delimiter.join(char[0].upper() if upper else char[0] for char in s.split())

    def blink(s: str, t: Union[int, float] = 1.0, length: int = 60) -> None:
        blink_length=0
        while length/(t*2) > blink_length:
            sys.stdout.write('\r' + f'{s} ')
            sys.stdout.flush()
            time.sleep(t)
            sys.stdout.write('\r' + '            ')
            sys.stdout.flush()
            time.sleep(t)
            blink_length+=1
