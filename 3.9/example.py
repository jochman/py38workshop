from typing import Dict

def what_is_love(dct: Dict[str, str]):
    for key, value in dct.items():
        print(key)
        print(value)
    print("\n")


love = {"What is love?": "Oh baby, don't hurt me"}
shrek = {"Don't hurt me": "No more"}

verse = dict(**love, **shrek)
what_is_love(verse)


love.update(shrek)
what_is_love(love)