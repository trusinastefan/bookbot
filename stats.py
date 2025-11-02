def get_num_words(text):
    return len(text.split())

def get_char_stats(text):
    char_dict = {}
    for c in text:
        c_lower = c.lower()
        if c_lower not in char_dict:
            char_dict[c_lower] = 0
        char_dict[c_lower] += 1
    return char_dict

def get_sorted_list_of_dicts(char_dict):
    list_of_dicts = []
    for char in char_dict:
        if char.isalpha():
            list_of_dicts.append({"char": char, "num": char_dict[char]})
    list_of_dicts.sort(reverse=True, key=lambda d: d["num"])
    return list_of_dicts
