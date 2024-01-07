import matplotlib.pyplot as plt

def read_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                words.append((parts[0], int(parts[1])))
    return words

def plot_top_words(words, top_n=50, save_path='result/top_words.png'):
    top_words = words[:top_n]
    labels, counts = zip(*top_words)
    plt.figure(figsize=(15, 10))
    plt.barh(labels, counts, color='skyblue')
    plt.xlabel('Counts')
    plt.ylabel('Words')
    plt.title('Top 50 Words Frequency')
    plt.gca().invert_yaxis()
    plt.savefig(save_path)
    plt.show()

def main():
    file_path = 'sample.out'
    words = read_file(file_path)
    words.sort(key=lambda x: x[1], reverse=True) 
    plot_top_words(words)

if __name__ == "__main__":
    main()
