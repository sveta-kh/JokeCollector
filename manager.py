from models import Joke
from api import JokeAPI
from storage import JokeStorage

#ხუმრობის მართვის კლასი
class JokeManager:
    def __init__(self) -> None:
        self.api = JokeAPI()
        self.storage = JokeStorage()
        self.__jokes: list [Joke] = self.storage.load_jokes()

    #API-დან ხუმრობის მიღება და შენახვა
    def collect_jokes(self, category: str = "Any") -> None:
        joke = self.api.get_joke(category)
        self.__jokes.append(joke)
        self.storage.save_jokes(self.__jokes)

        print("\n" + "-" * 40)
        print("               YOUR JOKE")
        print("-" * 40)
        print(joke.get_info())
        print("-" * 40 + "\n")

    #შენახული ხუმრობების ჩვენება
    def show_jokes(self) -> None:
        if not self.__jokes:
            print("\nJoke history is empty.\n")
            return
        print("\n" + "-" * 40)
        print("             JOKE HISTORY")
        print("-" * 40)
        
        for joke in self.__jokes:
            print(joke.get_info())
            print("\n" + "-" * 40 + "\n")

        print()

    #ხუმრობების კატეგორიების მიხედვით გაფილტვრა
    def filter_jokes(self, category: str) -> None:
        found = False

        print("\n" + "-" * 40)
        print(f"       CATEGORY: {category}")
        print("-" * 40)

        for joke in self.__jokes:
            if joke.category.lower() == category.lower():
                print(joke.get_info())
                print("\n" + "-" * 40 + "\n")
                found = True
        if not found:
            print("\nNo jokes found in this category.")

    # ხუმრობის ID-ის მიხედვით წაშლა
    def delete_joke(self, joke_id: int) -> None:
        for joke in self.__jokes:
            if joke.id == joke_id:
                self.__jokes.remove(joke)
                self.storage.save_jokes(self.__jokes)
                print("\nJOKE DELETED SUCCESSFULLY\n")
                return
        print("\nJoke not found.\n")
            

