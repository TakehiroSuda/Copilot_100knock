def alternate_merge(str1, str2):
    merged_str = ''.join(a + b for a, b in zip(str1, str2))
    # If one string is longer, append the remaining part
    merged_str += str1[len(str2):] + str2[len(str1):]
    return merged_str

# Example usage
if __name__ == "__main__":
    s1 = "abc"
    s2 = "12345"
    print(alternate_merge(s1, s2))  # Output: a1b2c345