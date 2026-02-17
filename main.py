from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_builder.user_data_builder import generate_random_users
from data_writer.user_data_writer import write_users_to_csv, write_users_to_db

DATABASE_URL = "postgresql://myuser:mypass@localhost:5432/testdb" #Здесь заменить адрес БД
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    users_list = generate_random_users(2000)
    write_users_to_csv(users_list)

    with Session() as session:
        try:
            write_users_to_db(users_list, session)
            print("Все этапы выполнены успешно!")
        except Exception as e:
            print(f"Ошибка на этапе записи в БД: {e}")