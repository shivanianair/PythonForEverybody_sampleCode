def longest_common_substring(str1, str2):
    word_grid = []

    # keeps track of the length of the longest common substring
    substring_len = 0

    # keeps track of the end index of the longest common substring
    str_end_index = None

    # creates a grid (2-dimensional array) with len(str1) rows and len(str2) columns
    for i in range(len(str1)):
        word_grid.append([0] * len(str2))


    for index1, char1 in enumerate(str1):

        for index2, char2 in enumerate(str2):

            if char1 == char2:
                word_grid[index1][index2] = word_grid[index1 - 1][index2 - 1] + 1

                if word_grid[index1][index2] > substring_len:
                    substring_len += 1
                    str_end_index = index1

    longest_substring = ''

    for j in range(substring_len):
        # prepends each character to the string starting from the end index of the longest common substring
        longest_substring = str1[str_end_index - j] + longest_substring

    # Outputs None if there is no common substring
    return longest_substring or None
