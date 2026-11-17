from pydantic import BaseModel, field_validator

#ხუმრობის(მშობელი) კლასი და საერთო ატრიბუტები
class Joke(BaseModel):
    id: int
    category: str
    type: str
    
    #საერთო ინფორმაციის დაბრუნება
    @field_validator("type")
    @classmethod
    def validate_type(cls, value: str) -> str:
        if value not in ["single", "twopart"]:
            raise ValueError("Invalid joke type.")
        return value

    def get_info(self) -> str:
        return f"ID: {self.id} \nCategory: {self.category}"

#ერთნაწილიანი ხუმრობის (შვილობილი)კლასი
class SingleJoke(Joke):
    joke: str

    #ინფორმაციის დაბრუნება(მშობლის კლასის ატრებუტები + შვილობილი კლასის ატრიბუტი)
    def get_info(self) -> str:
        return super().get_info() + f"\n\nJoke: {self.joke}"

#ორ ეტაპიანი ხუმრობა(შვილობილი) კლასი
class TwoPartJoke(Joke):
    setup: str
    delivery: str

    #ინფორმაციის დაბრუნება (მშობლის კლასის ატრებუტები + შვილობილი კლასის ატრიბუტები)
    def get_info(self) -> str:
        return super().get_info() + f"\n\n{self.setup}\n {self.delivery}"
