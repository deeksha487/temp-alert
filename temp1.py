import sys

# check if argument is given
if len(sys.argv) < 2:
    print("Please give temperature as argument.")
else:
    temp = float(sys.argv[1])

    if temp < 15:
        print("Cold")
    elif temp <= 30:
        print("Normal")
    else:
        print("Hot")
