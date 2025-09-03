import requests

def main():
    # Example: Fetch a random joke from an open API
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            print("Here's a random joke:")
            print(f"{data['setup']} ... {data['punchline']}")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request related Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
