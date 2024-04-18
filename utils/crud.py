def read(users:list[dict])->None:
    for user in users[1:]:
        print(f'Twój znajomy {user["name"]} opublikował: {user["posts"]}')

    def create_user(users: list[dict]) -> None:
        imię: string = input("podaj imię użytkownika: ")
        surname: string = input("popdaj nazwsiko użytkownika:")
        posts: string = input("podaj liczbę postów: ")
        user: dict = {"name": name, "surname": surname, "posts": posts}
        users.append(user)