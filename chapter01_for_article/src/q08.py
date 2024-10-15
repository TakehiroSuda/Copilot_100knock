def cipher(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return ''.join(result)
