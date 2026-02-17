from dataclasses import asdict
from typing import List
from pathlib import Path
from sqlalchemy.orm import Session
from entity.user_entity import UserEntity
from model.user import User
import pandas as pd

def write_users_to_db(users: List[User], db_session: Session):
    try:
        entities = []
        for u in users:
            entity = UserEntity(
                name=u.name,
                password=u.password,
                language=u.language,
                enable_notifications=u.enable_notifications,
                create_date=u.create_date,
                enabled=u.enabled,
                display_name=u.display_name
            )
            entities.append(entity)

        db_session.add_all(entities)
        db_session.commit()
        print(f" Успешно: {len(entities)} пользователей записано в БД")
    except Exception as e:
        db_session.rollback()
        print(f" Критическая ошибка БД ({type(e).__name__}): {e}")
        raise e

def write_users_to_csv(
        users: List[User],
        filename: str = "boomq_generated_users.csv",
        folder: str = "generated",
):
    try:
        output_dir = Path(folder)
        output_dir.mkdir(parents=True, exist_ok=True)

        file_path = output_dir / filename

        data = [asdict(u) for u in users]
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, encoding="utf-8")
        print(f" Успешно: Данные записаны в {file_path.absolute()}")

    except Exception as e:
        print(f" Ошибка при записи CSV: {e}")