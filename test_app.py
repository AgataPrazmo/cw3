import unittest
from app import dodaj

class TestDodaj(unittest.TestCase):
	def test_dodaj(self):
		wynik = dodaj(3, 5)
		self.assertEqual(wynik, 8)

		wynik = dodaj(-1, 1)
		self.assertEqual(wynik, 0)

		wynik = dodaj(2.5, 1.5)
		self.assertEqual(wynik, 4.0)

if __name__ == "__main__":
	unittest.main()
