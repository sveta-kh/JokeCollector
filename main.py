from manager import JokeManager

#მომხმარებლის ინტერფეისის მართვის კლასი
class JokeApp:
    def __init__(self) -> None:
        self.manager = JokeManager()

    #მთავარიმენიუს ჩვენება
    @staticmethod
    def show_menu() -> None:
        print("\n" + "=" * 40)
        print("         JOKE DAILY COLLECTOR")
        print("=" * 40)
        print("1. Get a random joke")
        print("2. Get a joke by category")
        print("3. Show joke history")
        print("4. Filter jokes by category")
        print("5. Delete a joke")
        print("6. EXIT")
        print("=" * 40)

    #ხუმრობის კატეგორიის არჩევა და ვალიდაცია
    @staticmethod
    def select_category() -> str:
        categories =  ["Programming", "Misc", "Pun", "Spooky", "Christmas"]
        print("\nAvailable categories:\n")
        
        for category in categories:
            print(category)
        print("\nBack - Return to main menu")
        print("-" * 40)

        while True:
            category = input("\nEnter category: ").strip().title()
            if category == "Back":
                return category
            
            if category in categories:
                return category

            print("\nPlease select a valid category.\n")

    #მომხმარებლის მიერ შეყვანილი ID-ის შემოწმება
    @staticmethod
    def get_valid_id() -> int:
        while True:
            try:
                joke_id = int(input("Enter joke ID: "))
                return joke_id
            except ValueError:
                print("\nPlease enter a whole number.\n")

    #პროგრამის მთავარი ციკლი
    def run(self) -> None:
        while True:
            self.show_menu()
            choice = input ("Enter your choice: ").strip()
            try:
                if choice == "1":
                    self.manager.collect_jokes()

                elif choice =="2":
                    while True:
                        category = self.select_category()
                        
                        if category == "Back":
                            break
                        try:
                            self.manager.collect_jokes(category)
                            break
                        except ValueError as e:
                            print(f"\nERROR: {e}\n")

                elif choice == "3":
                    self.manager.show_jokes()

                elif choice == "4":
                    category = self.select_category()

                    if category != "Back":
                        self.manager.filter_jokes(category)

                elif choice == "5":
                    joke_id = self.get_valid_id()
                    self.manager.delete_joke(joke_id)

                elif choice =="6":
                    print("\n" + "=" * 40)
                    print("          THANK YOU FOR USING")
                    print("         JOKE DAILY COLLECTOR")
                    print("           HAVE A NICE DAY!")
                    print("               GOODBYE!")
                    print("=" * 40 + "\n")
                    break

                else:
                    print("\nPlease select a valid option.\n")

            except (ValueError, OSError) as e:
                print(f"\nERROR: {e}\n")

#პროგრამის გაშვება
if __name__ == "__main__":
    try:
        app = JokeApp()
        app.run()

    except (ValueError, OSError) as e:
        print(f"\nERROR: {e}\n")
