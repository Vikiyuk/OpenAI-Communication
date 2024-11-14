# 📄 OpenAI-Communication

## Opis projektu

Aplikacja w Pythonie, która generuje artykuł w formacie HTML na podstawie dostarczonego pliku tekstowego. Projekt wykorzystuje API OpenAI do przekształcenia tekstu w strukturalny kod HTML, zawierający odpowiednie tagi oraz miejsca na grafiki. Wygenerowane pliki HTML są zapisywane w folderze `public_html`.

## Wymagania

- **Python 3.x**
- **Konto OpenAI oraz klucz API**

## Instalacja

1. **Sklonuj repozytorium** lub pobierz pliki projektu.

2. **Zainstaluj wymagane biblioteki**:

   ```bash
   pip install openai
   ```

## Przygotowanie klucza API

1. **Utwórz plik `openai_key.txt` w folderze projektu.**

2. **Wprowadź swój klucz API OpenAI** do pliku `openai_key.txt`:

   ```bash
   sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```

> **Uwaga:** Klucz API jest wymagany, aby aplikacja mogła łączyć się z API OpenAI.

## Przygotowanie pliku z artykułem

1. **Utwórz plik tekstowy `tresc_artykulu.txt` w folderze projektu.**

2. **Wprowadź treść artykułu**, który chcesz przekształcić w HTML.

## Jak korzystać z programu?

1. **Uruchom aplikację**, korzystając z poniższego polecenia:

   ```bash
   python main.py
   ```

2. **Pliki wynikowe** zostaną zapisane w folderze `public_html`:

   - `artykul.html` – wygenerowany kod HTML artykułu.
   - `szablon.html` – szablon HTML, gotowy na wklejenie wygenerowanej treści.
   - `podglad.html` – pełny podgląd artykułu z użyciem szablonu.

## Struktura projektu

```
📁 Projekt
├── main.py
├── openai_key.txt
├── tresc_artykulu.txt
├── public_html/
│   ├── artykul.html
│   ├── szablon.html
│   └── podglad.html
```

## Przykład uruchomienia

```bash
$ python main.py
Plik artykułu został zapisany jako public_html/artykul.html
Szablon HTML został zapisany jako public_html/szablon.html
Podgląd artykułu został zapisany jako public_html/podglad.html
```

## Uwagi

- Program wymaga połączenia z internetem, aby korzystać z API OpenAI.
- **Klucz API OpenAI należy przechowywać bezpiecznie** i nie udostępniać go publicznie.
- Jeśli folder `public_html` nie istnieje, program utworzy go automatycznie.
