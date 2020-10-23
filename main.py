import sys
from commands import *


if len(sys.argv) > 1:
    if sys.argv[1] == "base10" and len(sys.argv) > 2:
        any_base_number = sys.argv[3].split(".")
        base = sys.argv[2]
        to_base_10(base, any_base_number)
    else:
        print("command requires an argument")

else:
    print("Invalid command usage")
