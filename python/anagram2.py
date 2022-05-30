from character_match import is_character_match as is_anangram

def anagrams_for(target, list_of_words):
	matching_words = []

	if len(target) == 0:
		return []
	for word in list_of_words:
		if is_anangram(word, target):
			matching_words.append(word)

	return matching_words