
import functools, collections

# 2. find anagrams


def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


print(find_anagrams(["string1", "string2", "1string", "2string"]))

