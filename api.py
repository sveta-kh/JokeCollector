import requests
from models import Joke, SingleJoke, TwoPartJoke
from pydantic import ValidationError

#API-ის საბაზისო მისამართი(კონსტანტა)
BASE_URL = "https://v2.jokeapi.dev/joke"

#API-სთან კომუნიკაციის კლასი
class JokeAPI:
    #API-დან ხუმრობის მიღება
    def get_joke(self, category: str = "Any") -> Joke:
        try:
            response = requests.get(f"{BASE_URL}/{category}?safe-mode", timeout=10)

            #HTTP სტატუსის შემოწმება
            if response.status_code != 200:
                raise ValueError("Unable to load the joke.")

            #JSON-ის ლექსიკონად გარდაქმნა
            data = response.json()

            #API-ის მიერ დაბრუნებული შეცდომის შემოწმება
            if data.get("error"):
                raise ValueError("No jokes found for the selected category.")

            #ვალიდაცია და შესაბამისი ობიექტის შექმნა
            if data.get("type") == "single":
                return SingleJoke.model_validate(data)
            elif data.get("type") == "twopart":
                return TwoPartJoke.model_validate(data)
            else:
                raise ValueError("Unexpected joke format. Please try again.")

        except requests.RequestException:
            raise ValueError("Connection failed. Please check your internet connection and try again.")
        except ValidationError:
            raise ValueError("Invalid joke data. Please try again.")
    