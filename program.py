import os


def main():
    header()
    folder = what_directory()
    if not folder:
        print("Sorry, we can't search that location.")
        return

    text = what_string()
    if not text:
        print("We can't search for nothing !")
        return

    search(folder, text)

    return


def header():

    print("-----------------------------------------")
    print("            FILE SEARCH APP              ")
    print("-----------------------------------------")
    print(" ")

    return

def what_directory():
    folder = input("What directory do you want to search: ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def what_string():
    print("")
    text = input("What string are you looking for: ")
    return text


def search(folder, text):
    print("Would search {} for {} ".format(folder, text))
    return text


if __name__ == '__main__':
    main()