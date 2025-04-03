def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    dict = {}

    lowered = text.lower()
    for c in lowered:
        if c in dict:
            dict[c] += 1
        else: 
            dict[c] = 1

    return dict

def get_sorted_list(char_dict):
    temp = []
    for key in char_dict:
        temp.append({"char": key, "num": int(char_dict[key])})

    temp.sort(reverse=True, key=sort_on)
    
    return temp


def sort_on(dict):
    return dict["num"]