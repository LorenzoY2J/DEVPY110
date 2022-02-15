import json
import re
from typing import Iterable, Dict

pattern_name = r'\w+'
pattern_surname = r'\w+'
pattern_sex = r'([m]|[f])'
pattern_tel = r'([+7]-\d\d\d\-\d\d\d-\d\d-\d\d)'
pattern_email = r'(\w+\@\w+\.\w+)'
pattern_site = r'(\w+.\w+.(\w+?))'



def dropper(func, drop_incorrect=False):
    def wrapper(*args, **kwargs):
        if drop_incorrect is False:
            for user in func(*args, **kwargs):
                yield user
        else:
            for user in func(*args, **kwargs):
                if re.fullmatch(pattern_name, user['name']) is None:
                    continue
                if re.fullmatch(pattern_surname, user['surname']) is None:
                    continue
                if re.fullmatch(pattern_sex, user['sex']) is None:
                    continue
                if type(user['age']) != int or (int(user['age']) < 18 or int(user['age']) > 99):
                    continue
                if user['contacts']['tel'] is None or re.fullmatch(pattern_tel, user['contacts']['tel']) is not None:
                    continue
                if user['contacts']['email'] is None or re.fullmatch(pattern_email, user['contacts']['email']) is not None:
                    continue
                if user['contacts']['site'] is None or re.fullmatch(pattern_site, user['contacts']['site']) is not None:
                    continue
            yield user

    return wrapper




def user_generator(file_name: str) -> Iterable[Dict]:
    with open(file_name, "r") as f:
        users = json.load(f)
        for i in users:
            yield i


file_name = "users_2240.json"

for user_ in dropper(user_generator)(file_name, drop_incorrect=False):
    print(user_)
