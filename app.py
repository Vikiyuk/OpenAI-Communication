import openai

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_api_key(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()


def generate_html_from_article(article_text, prompt, api_key):
    openai.api_key = api_key
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Jesteś asystentem, który generuje kod HTML."},
            {"role": "user", "content": f"{prompt}\n\n{article_text}"}
        ],
        max_tokens=2000,
        temperature=0.7
    )

    return response.choices[0].message.content


def save_html_to_file(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
def main():
    input_file = 'tresc_artykulu.txt'
    output_file = 'artykul.html'
    api_key_file = 'openai_key.txt'
    api_key = load_api_key(api_key_file)
    article = read_article(input_file)
    print("Api key = ",api_key)
    print("Artykul = ", article)
    api_key = load_api_key(api_key_file)

    # Treść promptu dla OpenAI
    prompt = (
        "Przekształć poniższy artykuł na kod HTML, z użyciem odpowiednich tagów HTML. "
        "Z miejscami na grafiki, które umieścic za pomocą: \" \"<img src=\"image_placeholder.jpg\" alt=\"wygeneruj grafikę pokazującą ...\">\". "
        "Nie używaj znaczników <html>, <head> ani <body>. Nie zmieniaj treści artykułu. Nie dodawaj dodatkowego tekstu albo znaczników oprócz tagów. ")

    # Odczyt artykułu
    article_content = read_article(input_file)

    # Generowanie kodu HTML
    html_content = generate_html_from_article(article_content, prompt, api_key)

    # Zapisanie do pliku
    save_html_to_file(html_content, output_file)
    print(f"Plik HTML został zapisany jako {output_file}")
if __name__ == "__main__":
    main()