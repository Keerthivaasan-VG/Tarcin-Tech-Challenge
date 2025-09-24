def normalize_text(file_path):
    normalized_data = []

    with open(file_path, "r") as f:
        for line in f:
            # Convert line to lowercase
            line = line.lower()

            # Split line into words
            words = line.split()

            # Keep only unique words in order
            seen = set()
            unique_words = []
            for w in words:
                if w not in seen:
                    seen.add(w)
                    unique_words.append(w)

            normalized_data.append(unique_words)

    return normalized_data


if __name__ == "__main__":
    input_file = "dirty_text.txt"  # Example file

    result = normalize_text(input_file)

    print("Normalized Text (list of lists):")
    for row in result:
        print(row)
