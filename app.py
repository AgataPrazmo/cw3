def dodaj(a, b):
	return a + b

if __name__ == "__main__":
	print("Witaj w mojej aplikacji!")
	print("Dodawanie liczb:")
	liczba1 = float(input("Podaj pierwszą liczbę: "))
	liczba2 = float(input("Podaj drugą liczbę: "))
	wynik = dodaj(liczba1, liczba2)
	print(f"Wynik dodawania: {wynik}")
