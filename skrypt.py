import requests
import json

# Lista endpointów do testowania
endpoints = [
	"https://jsonplaceholder.typicode.com/posts/1",
	"https://jsonplaceholder.typicode.com/comments/1",
	"https://jsonplaceholder.typicode.com/users/1"
]

def send_get_request(url):
	try:
		response = requests.get(url)
		return response
	except requests.exceptions.RequestException as e:
		print(f"Error: {e}")
		return None

def test_api():
	for i, endpoint in enumerate(endpoints):
		print(f"Testing {endpoint}:")
        
		# Wysyłanie żądania GET
		response = send_get_request(endpoint)
        
		if response:
			# Sprawdzanie statusu odpowiedzi HTTP
			if response.status_code == 200:
				print("Status: 200 OK - PASSED")
                
				# Próba parsowania odpowiedzi JSON
				try:
					data = response.json()
                    
					# Sprawdzanie obecności kluczowych elementów
					required_keys = ['id', 'userId', 'title']
					missing_keys = [key for key in required_keys if key not in data]
                    
					if len(missing_keys) == 0:
						print("JSON keys check: PASSED")
					else:
						print(f"JSON keys check: FAILED - Missing keys: {', '.join(missing_keys)}")
                
				except json.JSONDecodeError as e:
					print(f"Error parsing JSON: {e}")
					print("JSON keys check: FAILED - Invalid JSON format")
            
			else:
				print(f"Status: {response.status_code} - FAILED")
        
		print()

if __name__ == "__main__":
	test_api()

