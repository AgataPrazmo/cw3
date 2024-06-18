Skrypt test_api.py służy do automatycznego testowania endpointów API pod kątem statusu odpowiedzi HTTP oraz obecności kluczowych elementów w odpowiedziach JSON.

Wymagania:
- Python 3.x
- Biblioteka requests (można zainstalować za pomocą pip install requests)

Użycie:
python skrypt.py

Dla każdego testu raportowane są następujące informacje:
- URL endpointu
- Status odpowiedzi HTTP (PASSED lub FAILED)
- Wynik testu obecności kluczowych elementów JSON (PASSED lub FAILED oraz lista brakujących kluczy, jeśli test nie powiedzie się)
