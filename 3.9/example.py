def what_is_love(dct: dict[str, str]):
    for key, value in dct.items():
        print(key)
        print(value)
    print("\n")


love = {"What is love?": "Oh baby, don't hurt me"}
shrek = {"Don't hurt me": "No more"}

verse = love | shrek
#what_is_love(verse)


love |= shrek
#what_is_love(love)

print("hod alpert".removeprefix("hod"))

print("hod alpert".removesuffix("alpert"))