import time
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import db_config


# Normal connection
def normal_connection():
    start_time = time.time()
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        port=db_config['port']
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchall()
    end_time = time.time()
    elapsed_time = end_time - start_time
    cursor.close()
    connection.close()
    return elapsed_time


# Connection pooling
def pooled_connection(session):
    start_time = time.time()
    session.execute("SELECT 1")
    session.commit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


if __name__ == "__main__":
    num_iterations = 10
    total_normal_time = 0
    total_pooled_time = 0

    # Pooled connection setup
    engine = create_engine(
        f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}",
        pool_size=7,
        max_overflow=5
    )
    Session = sessionmaker(bind=engine)

    # Pooled connection loop
    for _ in range(num_iterations):
        total_pooled_time += pooled_connection(Session())

    engine.dispose()

    # Normal connection loop
    for _ in range(num_iterations):
        total_normal_time += normal_connection()

    print(f"Total time taken for normal connections: {total_normal_time:.6f} seconds")
    print(f"Total time taken for pooled connections: {total_pooled_time:.6f} seconds")
