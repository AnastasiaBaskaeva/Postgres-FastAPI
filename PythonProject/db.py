from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL подключения к базе данных PostgreSQL.
# Синтаксис: postgresql://<username>:<password>@<host>/<database_name>
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@192.168.56.101/mydb"

# Создание движка SQLAlchemy — объект, отвечающий за соединение с базой.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание фабрики сессий — позволяет получать объекты для работы с БД.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Базовый класс для всех моделей ORM.
Base = declarative_base()