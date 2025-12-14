# Pot Bot: protections of teams and groups
Bot Telegram służący do ochrony grup i kanałów przed spamem oraz niepożądanymi użytkownikami. Wymaga pełnej rejestracji z weryfikacją wiedzy z zakresu cyberbezpieczeństwa.

## Główne funkcje

- **Pełna rejestracja użytkownika**:
  - Imię i nazwisko (z walidacją – tylko litery, spacje, myślniki i apostrofy)
  - Numer telefonu (pobierany bezpiecznie przez przycisk kontaktowy Telegrama)
- **Matematyczna CAPTCHA** po wprowadzeniu danych
- **Losowe pytanie z cyberbezpieczeństwa** po poprawnej CAPTCHA (40 pytań w bazie, odpowiedzi a/b/c na inline keyboard)
- **Zapis do bazy danych** tylko po przejściu wszystkich weryfikacji (CAPTCHA + pytanie bezpieczeństwa)
- **System antyspam** - blokada po 5 nieudanych próbach rejestracji w ciągu godziny (liczy każdą wiadomość w trakcie procesu)
- **Bezpieczna baza danych SQLite** (lokalny plik `db.sqlite3`)
- **Czysty interfejs użytkownika**:
  - Usuwanie klawiatur po każdym kroku
  - Placeholder w polu tekstowym przy CAPTCHA
  - Walidacja odpowiedzi na CAPTCHA (tylko cyfry)

## Wymagania
- Python 3.10+
- aiogram 3.x
- SQLAlchemy 2.x

## Instalacja i uruchomienie
```bash
# Sklonuj repozytorium
git clone <adres-repo>
cd potbot

# Utwórz środowisko wirtualne (zalecane)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# lub .venv\Scripts\activate  # Windows

# Zainstaluj zależności
pip install -r requirements.txt

# Skopiuj plik konfiguracyjny i uzupełnij token
cp .env.example .env
# Edytuj .env i wklej swój BOT_TOKEN od @BotFather

# Uruchom bota
python main.py
