# loop(for, while) and color lines 1 to 100

RESET = "\033[0m"
F_RED = "\033[31m"
F_YELLOW = "\033[33m"
F_GREEN = "\033[32m"

# count down from 100 to 1 (0 is not included)
for n in range(100, 0, -1): # 100 - Start 0 - Stop -1 - Step
    if n > 66:
        clr = F_RED
    elif n > 33:
        clr = F_YELLOW
    else:
        clr = F_GREEN
    print(f"{clr}line {n}{RESET}")
