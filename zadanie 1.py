import json
from typing import Dict, Iterable

def user_generator(f: str) -> Iterable[Dict]:
    with open("users_2240.json", "r") as f:
        dict_ = json.load(f)
        for i in dict_:
            yield i


for user in user_generator("dict_"):
    print(user)





