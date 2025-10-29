import requests
from dataclasses import dataclass

@dataclass
class JokeResult:
    joke: str
    error: str

    is_success = property(lambda self: self.error == "")

    @classmethod
    def success(cls, joke_str: str) -> "JokeResult":
        return cls(joke=joke_str, error="")

    @classmethod
    def failure(cls, error: str) -> "JokeResult":
        return cls(joke="", error=error)


def get_chuck_joke() -> JokeResult:
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        fetched_joke = data.get("value", "")
        return JokeResult.success(fetched_joke) if fetched_joke else JokeResult.failure("No joke found.")
    except requests.RequestException as e:
        return JokeResult.failure(f"Error fetching joke: {e}")


if __name__ == "__main__":
    result = get_chuck_joke()
    if result.is_success:
        print("Here's a Chuck Norris joke for you:")
        print(result.joke)
    else:
        print("Failed to fetch a joke:")
        print(result.error)