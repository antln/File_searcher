import os
import glob


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

    matches = search(folder, text)
    for m in matches:
        print(type(m))
        print(m)

    return


def header():
    print("-----------------------------------------")
    print("            FILE SEARCH APP              ")
    print("-----------------------------------------")
    print(" ")

    return


def what_directory():
    folder = input("What folder do you want to search: ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def what_string():
    print("")
    text = input("What are you searching for [single phrase only]: ")
    return text.lower()


def search(folder, text):
    # print("Would search {} for {} ".format(folder, text))
    all_matches = []
    # items = os.listdir(folder)
    items = glob.glob(os.path.join(folder, '*'))

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue

        matches = search_files(full_item, text)
        all_matches.extend(matches)


    return all_matches


def search_files(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        for line in fin:
            if line.lower().find(search_text) >= 0:
                matches.append(line)

    return matches

if __name__ == '__main__':
    main()
