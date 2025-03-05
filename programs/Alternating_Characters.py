def alternatingCharacters(s):
    delete_characters = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            delete_characters += 1
    return delete_characters
