import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def read_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                words.append((parts[0], int(parts[1])))
    return words

def filter_adjectives(words):
    adjectives = []
    for word, count in words:
        tagged_word = pos_tag([word])
        if tagged_word[0][1] in ['NN', 'NNS', 'NNP','NNPS']:
            if not tagged_word[0][1] in ['JJ','JJR','JJS']: 
                    adjectives.append((word, count))
    return adjectives

def plot_top_words(words, top_n=50, save_path='result/top_words_filtered_n.png'):
    top_words = words[:top_n]
    labels, counts = zip(*top_words)
    plt.figure(figsize=(15, 10))
    plt.barh(labels, counts, color='skyblue')
    plt.xlabel('Counts')
    plt.ylabel('Adjectives')
    plt.title('Top 50 Adjectives Frequency')
    plt.gca().invert_yaxis()
    plt.savefig(save_path)
    plt.show()

def main():
    file_path = 'sample.out'
    words = read_file(file_path)
    words.sort(key=lambda x: x[1], reverse=True)
    adjectives = filter_adjectives(words)
    plot_top_words(adjectives)

if __name__ == "__main__":
    main()
