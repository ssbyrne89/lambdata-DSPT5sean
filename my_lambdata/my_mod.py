
#my_mod.py


def enlarge(n):
    return n * 100

if __name__ == "__main__":
    #only runs the code below if executing this script from the command line
    #otherwise don't run it (for ex. if we're trying to import something)

    x = 5
    print(enlarge(x))

    y = int(input("please choose a number (e.g. 5): "))

    print(enlarge(y))