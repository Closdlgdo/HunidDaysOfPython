import requests


def get_public_ip():
    try:
        # Use a service like 'httpbin' to get the public IP
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json()['origin']

        print(f"Public IP Address: {public_ip}")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_public_ip()
