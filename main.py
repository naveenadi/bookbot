import sys
from pathlib import Path
from stats import get_num_words

def chars_count(file_contents):
    contents = file_contents.lower()
    char_dict = {}
    for char in contents:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def dict_to_dictlist(dict):
    lst = []
    for key, value in dict.items():
        if key.isalpha():
            lst.append({"letter": key, "times": value})
    return lst

def sort_on(dict):
    return dict["times"]

def main() -> int:

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = Path(sys.argv[1])

    try:
        with open(path_to_book) as f:
            file_contents = f.read()
            print("--- Begin report of books/frankenstein.txt ---")
            print("{} words found in the document\n".format(get_num_words(file_contents)))
            chars_dict_count = chars_count(file_contents)
            letters_list = dict_to_dictlist(chars_dict_count)
            letters_list.sort(key=sort_on, reverse=True)
            for dict in letters_list:
                #print("The '{}' character was found {} times".format(dict["letter"], dict["times"]))
                print(f"{dict["letter"]}: {dict["times"]}")
            print("--- End report ---")
    except FileNotFoundError:
        print(f"Error: Could not find file {path_to_book}")
        return 1
    except IOError as e:
        print(f"Error reading file {path_to_book}: {e}")
        return 1
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
