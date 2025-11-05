def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in characters:
            characters[lower_char] = 1
        else:
            characters[lower_char] += 1
    return characters

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    