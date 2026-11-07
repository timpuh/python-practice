# loops through Linux command groups by color

RESET = "\033[0m"
F_RED = "\033[31m"
F_BLUE = "\033[34m"
F_MAGENTA = "\033[35m"

ctgrs = ["📁 Navigation", "👤 Users", "🔒 Permissions"]
ctgr_clr = [F_RED, F_BLUE, F_MAGENTA]

navigation = ["pwd - show where I am", "ls - list files", "cd - change folder", "mkdir - make folder"]
users = ["whoami - show current user", "sudo - run one command as admin", "su - switch user", "adduser - create user"]
permissions = ["chmod - change permissions", "chown - change owner", "ls -l - show permissions"]

for i in range(len(ctgrs)):
    print(f"{ctgr_clr[i]}{ctgrs[i]}{RESET}")
    match i:
        case 0:
            # nested loop
            for command in navigation:
                print(f"  {command}")
        case 1:
            for command in users:
                print(f"  {command}")
        case 2:
            for command in permissions:
                print(f"  {command}")
    print()