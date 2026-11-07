# kids get their fruits, every line has its own RGB color and a fruit emoji

RESET = "\033[0m"
F_RGB_RED = "\033[38;2;210;74;67m"
F_RGB_GREEN = "\033[38;2;69;159;34m"
F_RGB_BLUE = "\033[38;2;30;60;187m"
F_RGB_MAGENTA = "\033[38;2;187;30;185m"

names = ["marina", "peta", "vasa", "masha"]
frts = ["mandarin", "apple", "orange", "pear"]
emj = ["🍊", "🍏", "🟠", "🍐"]
str_clrs = [F_RGB_RED, F_RGB_GREEN, F_RGB_BLUE, F_RGB_MAGENTA]

for i in range(len(names)):
    print(f"{str_clrs[i]}{names[i]} get {frts[i]} {emj[i]}{RESET}")