# Can you translate this driver code to unit tests?

from anagram2 import anagrams_for 

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds", "reduces", "secured", "seducer", "cheaters", "hectares", "saltier", "realist", "repaint", "pertain"]

print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
print(anagrams_for("apple", list_of_words) == [])
print(anagrams_for("rescued", list_of_words) == ["reduces", "secured", "seducer"])
print(anagrams_for("teachers", list_of_words) == ["cheaters", "hectares"])
print(anagrams_for("retails", list_of_words) == ["saltier", "realist"])
print(anagrams_for("painter", list_of_words) == ["repaint", "pertain"])
print(anagrams_for(" ", list_of_words) == [])
print(anagrams_for("", list_of_words) == [])