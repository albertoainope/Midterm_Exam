def ocurrence_f(file_name):
    """

    :param file_name: The text file
    :return: Words that follow the pattern
    """
    ocurrences = []
    punctuation = ",.?'\n\t"
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p, "")
            words = line.split(" ")
            for word in words:
                if (word.startswith("C") and word.endswith("jeb")):
                    ocurrences.append(word)
    print(len(ocurrences))

ocurrence_f("jeb.txt")