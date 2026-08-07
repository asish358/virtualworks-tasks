import json
import urllib.request

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            print("\n" + "=" * 40)
            print(f" Setup:     {data['setup']}")
            print(f" Punchline: {data['punchline']}")
            print("=" * 40 + "\n")
            
    except Exception as error:
        print(f"Failed to fetch joke: {error}")

if __name__ == "__main__":
    get_random_joke()
