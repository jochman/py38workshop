from typing import Dict, Union

def backstreet_singer(obj: Union[Dict[str, str], str]):
    if isinstance(obj, str):
        print(obj)
    else:
        flag = False
        for key, value in obj.items():
            if flag := value == "Tell me why":
                key, value = value, key
            print(key)
            print(value)
        if flag:
            print("I want it that way")
    print("\n")

if __name__ == "__main__":
    backstreet_singer("Yeah\nOh yeah")