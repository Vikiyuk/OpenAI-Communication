import openai

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_api_key(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

#
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

#Mozemy skorzystac z tej funkcji, albo recznie stworzyc template.html
#W przypadku recznego tworzenie musimy zmienic w funkcji main inicjalizacje pliku template.html
def create_template_file(template_path):
    template_content = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f4f4f4;
                padding: 20px;
                max-width: 800px;
                margin: 0 auto;
            }
            h1, h2, h3 {
                color: #0056b3;
                margin-top: 20px;
            }
            p {
                margin: 10px 0;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 10px auto;
            }
            figcaption {
                text-align: center;
                font-style: italic;
                color: #555;
                margin-bottom: 20px;
            }
            figure {
                margin: 20px 0;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <!-- Wklej wygenerowaną treść artykułu tutaj -->
    
        <script>
            // Funkcja do dynamicznego ładowania obrazków, jeśli są oznaczone jako "image_placeholder.jpg"
            document.addEventListener("DOMContentLoaded", () => {
                const images = document.querySelectorAll("img[src='image_placeholder.jpg']");
                images.forEach((img, index) => {
                    img.src = `https://via.placeholder.com/800x400?text=Grafika+${index + 1}`;
                    img.alt = "Przykładowa grafika - zastąp ją odpowiednią grafiką";
                });
    
                console.log("Obrazki zastąpione przykładowymi grafikami.");
            });
        </script>
    </body>
    </html>

    """
    with open(template_path, 'w', encoding='utf-8') as file:
        file.write(template_content)

def create_preview_file(html_content, template_content, preview_path):
    # Wstrzyknięcie wygenerowanej treści do szablonu w miejsce <!-- Wklej wygenerowaną treść artykułu tutaj -->
    preview_content = template_content.replace("<!-- Wklej wygenerowaną treść artykułu tutaj -->", html_content)
    with open(preview_path, 'w', encoding='utf-8') as file:
        file.write(preview_content)
def save_html_to_file(html_content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
def main():
    input_file = 'tresc_artykulu.txt'
    output_file = 'artykul.html'
    api_key_file = 'openai_key.txt'
    template_file = 'szablon.html'
    preview_file = 'podglad.html'
    api_key = load_api_key(api_key_file)
    article = read_file(input_file)
    print("Api key = ",api_key)
    print("Artykul = ", article)
    api_key = load_api_key(api_key_file)

    # Treść promptu dla OpenAI
    prompt = (
        "Przekształć poniższy artykuł na kod HTML, z użyciem odpowiednich tagów HTML. "
        "Z miejscami na grafiki, które umieścic za pomocą: \" \"<img src=\"image_placeholder.jpg\" alt=\"wygeneruj grafikę pokazującą ...\">\". "
        "Dodaj podpisy pod grafikami za pomocą tagu <figcaption>. "
        "Nie używaj znaczników <html>, <head> ani <body>. Nie zmieniaj treści artykułu. Nie dodawaj dodatkowego tekstu albo znaczników oprócz tagów. ")

    # Odczyt artykułu
    article_content = read_file(input_file)

    # Generowanie kodu HTML
    html_content = generate_html_from_article(article_content, prompt, api_key)

    # Zapisanie do pliku
    save_html_to_file(html_content, output_file)
    print(f"Plik HTML został zapisany jako {output_file}")


    #Tworzenie szablonu
    create_template_file(template_file)
    print(f"Szablon HTML został zapisany jako {template_file}")

    #Tworzenie podgladu
    template_content = read_file(template_file)
    create_preview_file(html_content, template_content, preview_file)
    print(f"Podgląd artykułu został zapisany jako {preview_file}")

if __name__ == "__main__":
    main()