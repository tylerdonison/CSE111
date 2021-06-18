# Example 1

def main():
    # Read the contents of a text file
    # named provinces.txt into a list.
    text_list = read_list("provinces.txt")

    # Print the entire list.
    print(text_list)

    text_list.pop(0)
    list_length = len(text_list) - 1
    text_list.pop(list_length)
    print(text_list)

    list_length = len(text_list)
    for i in range(list_length):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"
    
    occurances = 0
    for i in range(list_length):
        if text_list[i] == "Alberta":
            occurances += 1
    print(f"Alberta occurs {occurances} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()