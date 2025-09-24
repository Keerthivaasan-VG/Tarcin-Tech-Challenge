w = None
try:
    file_name = input("Enter a file name: ")
    file = open(file_name, 'r')
except Exception as e:
    print("Error opening file:", e)
    exit()
try:
    text = file.read()
    file.close()
except Exception as e:
    print("Error reading file:", e)
    text = ''
text = text.lower()
text = text.replace('\n', ' ')
words = text.split()
words_count = dict()
for w in words:
    words_count[w] = words_count.get(w, 0) + 1
def top_words(n):
    items = list(words_count.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    top_n = sorted_items[:int(n)]
    return top_n
print(top_words(5))
