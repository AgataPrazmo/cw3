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

Zadanie 2 to przykładowy projekt aplikacji Pythonowej, która wykonuje dodawanie dwóch liczb.

Instalacja:
git clone https://github.com/Toxic-player/cw3.git
cd moja_aplikacja

Instalacja zależności:
make install

Uruchomienie aplikacjiL
make run

Testy jednostkowe:
make test

Struktura plików:
moja_aplikacja/
│
├── app.py # Główny plik aplikacji
├── test_app.py # Plik z testami jednostkowymi
├── Makefile # Plik Makefile z definicjami reguł
└── README.md # Ten plik README

Autor: Agata Prażmo
