def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
for group in group_anagrams(words):
    print(group)