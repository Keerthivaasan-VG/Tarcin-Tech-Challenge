import csv

def language_kpis(path):
    try:
        with open(path, 'r') as f:
            text = f.read()
    except Exception as e:
        print("Error reading file:", e)
        return {}

    # Normalize text
    text = text.replace('\n', ' ').strip().lower()
    words = text.split()

    total_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)

    total_chars = sum(len(w) for w in words)
    avg_word_length = round(total_chars / total_words, 2) if total_words > 0 else 0

    # Trigram counts
    trigram_counts = {}
    for i in range(len(words) - 2):
        trigram = (words[i], words[i+1], words[i+2])
        trigram_counts[trigram] = trigram_counts.get(trigram, 0) + 1

    top5_trigrams = sorted(trigram_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Save KPIs into CSV
    with open("language_kpis_summary.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['KPI', 'Value'])
        writer.writerow(['Total words', total_words])
        writer.writerow(['Unique words', num_unique_words])
        writer.writerow(['Average word length', avg_word_length])
        writer.writerow(['Top 5 Trigrams', top5_trigrams])

    kpis = {
        "Total words": total_words,
        "Unique words": num_unique_words,
        "Average word length": avg_word_length,
        "Top 5 Trigrams": top5_trigrams
    }
    return kpis


if __name__ == "__main__":
    path = "input.txt"
    result = language_kpis(path)
    print("Language KPIs:")
    for k, v in result.items():
        print(f"{k}: {v}")
