response = {"username": "username", "password": "pass"}
db = list()


def add_user(user_obj):
    password = response.get("password")
    if len(password) < 5:
        return "Password is shorter than 5 characters."
    else:
        db.append(user_obj)
        return "User has been added."


print(add_user(response))
print(db)
