def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 == char2:
                continue
            current_length = 0
            prev_char = None
            valid = True

            for char in s:
                if char == char1 or char == char2:
                    if char == prev_char:
                        valid = False
                        break
                    prev_char = char
                    current_length += 1

            if valid and current_length > max_length:
                max_length = current_length

    return max_length
