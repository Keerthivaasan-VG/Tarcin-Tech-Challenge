def top_words(n):
    # Step 1: Read file
    f = open("input.txt", "r")
    text = f.read()
    f.close()

    # Step 2: Normalize (lowercase + split into words)
    words = text.lower().split()

    # Step 3: Count frequency using a dictionary
    freq = {}
    for w in words:
        # remove punctuation around word
        w = w.strip(".,!?;:'\"()[]{}")
        if w != "":
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

    # Step 4: Sort dictionary by frequency (descending)
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 5: Return top-n words
    return sorted_words[:n]


# Example usage
print(top_words(5))  # shows top 5 most frequent words
