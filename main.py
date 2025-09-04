from src.client.http_client import HttpClient

def main() -> None:
    url: str = "https://www.hotains.com.tw/download/terms/car/1"
    client = HttpClient(timeout=10.0, duration=0.0)
    print(client.get(url))

if __name__ == "__main__":
    main()