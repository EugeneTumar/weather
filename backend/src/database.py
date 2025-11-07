from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

from .settings import settings

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

Base = declarative_base()
engine = create_engine(settings.database_conn)
session_maker = sessionmaker(engine, expire_on_commit=False)
Base.metadata.create_all(engine)

def check_conn():
    try:
        with engine.connect() as connection:
            res = connection.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False
    
check_conn()



def connection(method):
    def wrapper(*args, **kwargs):
        with session_maker() as session:
            try:
                res = method(session=session, *args, **kwargs)
            
                session.commit()
                session.close() 

                return res
            except Exception as e:
                session.rollback() 
                raise e 
            finally:
                session.close() 
    return wrapper
