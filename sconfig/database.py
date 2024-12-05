from pathlib import Path
from sqlmodel import create_engine, Session, SQLModel

engine = create_engine("sqlite:///database.db")


def get_session() -> Session:  # type: ignore
    with Session(engine) as session:
        yield session


def create_db_and_tables(app_dir: Path, db_file_name: str = "database.db"):
    engine = create_engine(f"sqlite:///{str(app_dir)}/{db_file_name}")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
