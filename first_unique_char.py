def first_unique_character(s):
    """
    Returns the first unique character in a string.
    
    Args:
        s (str): The input string
        
    Returns:
        str or None: The first unique character, or None if no unique character exists
    """
    # Count frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None


# Example usage
if __name__ == "__main__":
    # Test cases
    print(first_unique_character("leetcode"))      # Output: 'l'
    print(first_unique_character("loveleetcode"))  # Output: 'v'
    print(first_unique_character("aabb"))          # Output: None
    print(first_unique_character(""))              # Output: None
    print(first_unique_character("z"))             # Output: 'z'
