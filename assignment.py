import requests
import time

def is_website_reachable(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException as e:
        return False

def check_website_periodically(url, duration_minutes, interval_seconds):
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        reachable = is_website_reachable(url)
        status = "reachable" if reachable else "not reachable"
        print(f"{url} is {status}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    website_url = "https://www.google.co.in"
    duration_minutes = 10
    interval_seconds = 60  
    check_website_periodically(website_url, duration_minutes, interval_seconds)


import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        return f"Error fetching public IP: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Your public IP address is: {public_ip}")
