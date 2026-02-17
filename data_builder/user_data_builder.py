import random
from functools import lru_cache
import bcrypt
from faker import Faker
from model.user import User

fake = Faker()

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def generate_random_users(count: int = 2000) -> list[User]:
    users = []
    print(f"--- Генерация {count} пользователей ---")
    languages = ["EN", "RU", "DE"]

    for _ in range(count):
        raw_password = fake.password(length=12)
        hashed_password = bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()

        user = User(
            name=fake.name(),
            password=hashed_password,
            language=random.choice(languages),
            enable_notifications=fake.boolean(),
            create_date=fake.date_time_between(start_date='-1y', end_date='now'),
            enabled=fake.boolean(),
            display_name=fake.user_name(),
        )
        users.append(user)
    return users