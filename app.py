import openai

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_api_key(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()
def main():
    input_file = 'tresc_artykulu.txt'
    output_file = 'artykul.html'
    api_key_file = 'openai_key.txt'
    api_key = load_api_key(api_key_file)
    article = read_article(input_file)
    print("Api key = ",api_key)
    print("Artykul = ", article)
if __name__ == "__main__":
    main()