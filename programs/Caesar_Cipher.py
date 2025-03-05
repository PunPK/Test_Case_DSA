def caesarCipher(s, k):
    codetext = ""
    k = k % 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nalphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet[k:]
    alphabet += nalphabet[0:k]
    for a in range(0, len(s)):
        if s[a].isalpha():
            if s[a].isupper():
                codetext += alphabet[nalphabet.index(s[a].lower())].upper()
            else:
                codetext += alphabet[nalphabet.index(s[a])]
        else:
            codetext += s[a]
    return codetext
