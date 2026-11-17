import json
from models import Joke, SingleJoke, TwoPartJoke

#ხუმრობის შენახვისა და წაკითხვის კლასი
class JokeStorage:
    #მონაცემთა ფაილის განსაზღვრა
    def __init__(self, filename: str ="jokes.json") -> None:
        self.filename = filename

    #ხუმრობების JSON ფაილში შენახვა (Serialization)
    def save_jokes(self, jokes: list[Joke]) -> None:
        data = []

        #ობიექტის ლექსიკონად გარდაქმნა
        for joke in jokes:
            data.append(joke.model_dump())

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except OSError:
            raise OSError("Unable to save joke.")

    #JSON ფაილიდან ხუმრობების წაკითხვა (Drserialization)
    def load_jokes(self) -> list[Joke]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Invalid joke history file.")
        except OSError:
            raise OSError("Unable to read joke history")

        #ხუმრობის ობიექტის სიის შექმნა
        jokes: list[Joke] = []

        #დესერიალიზაცია
        for item in data:
            joke : Joke

            if item.get("type") == "single":
                joke = SingleJoke.model_validate(item)
            elif item.get("type") == "twopart":
                joke = TwoPartJoke.model_validate(item)
            else:
                raise ValueError("Unexpected joke format.")
            
            jokes.append(joke)
        return jokes