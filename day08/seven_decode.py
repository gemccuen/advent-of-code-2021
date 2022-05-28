import re

def remove_chars(s, chars):
    pattern = f"[{chars}]"
    return re.sub(pattern, "", s)

def get_correct_segments(inputs):
    num_map = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg"
    ]
    final_map = []

    len_map = {}
    seg_map = {}
    for input in inputs:
        key = str(len(input))
        if key not in len_map:
            len_map[key] = input
        else:
            if type(len_map[key]) != list:
                len_map[key] = [len_map[key]]
            len_map[key].append(input)
    possible_cf = len_map['2']
    
    seg_map['a'] = remove_chars(len_map['3'], possible_cf)
    
    possible_bd = remove_chars(len_map['4'], possible_cf)

    strip_string = f"{possible_cf}{seg_map['a']}{possible_bd}"

    for combo in len_map['5']:
        removed = remove_chars(combo, strip_string)
        if len(removed) == 1 and 'g' not in seg_map:
            seg_map['g'] = removed
        elif len(removed) == 2:
            seg_map['c'] = possible_cf[0] if possible_cf[0] in combo else possible_cf[1]
            seg_map['f'] = possible_cf[1] if possible_cf[0] in combo else possible_cf[0]
            seg_map['d'] = possible_bd[0] if possible_bd[0] in combo else possible_bd[1]
            seg_map['b'] = possible_bd[1] if possible_bd[0] in combo else possible_bd[0]
    
    seg_map['e'] = remove_chars("abcdefg", "".join(seg_map.values()))

    for num_str in num_map:
        raw_str = ""
        for c in num_str:
            raw_str += seg_map[c]
        final_str = "".join(sorted(raw_str))
        final_map.append(final_str)
    
    return final_map    

with open("input.txt", 'r') as infile:
    groups = [g.split(" | ") for g in infile.read().splitlines()]
    total = 0
    for group in groups:
        correct_map = get_correct_segments(group[0].split(" "))
        num_str = ""
        for output in group[1].split(" "):
            num_str += str(correct_map.index("".join(sorted(output))))
        total += int(num_str)
    
    print(total)