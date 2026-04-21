

from typing import List, Tuple
import json
import mysql.connector # Must include .connector


table_name = "movie_urls"
DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "actowiz",
    "port" : "3306",
    "database" : "rotten_tomatoes_db"
}

def get_connection():
    try:
        ## here ** is unpacking DB_CONFIG dictionary.
        connection = mysql.connector.connect(**DB_CONFIG)
        ## it is protect to autocommit
        connection.autocommit = False
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

def create_db():
    connection = get_connection()
    # connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS rotten_tomatoes_db;")
    connection.commit()
    connection.close()
# create_db()


def create_movie_urls_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                movie_name VARCHAR(200),
                movie_url TEXT,
                status VARCHAR(100)
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

batch_size_length = 100
def data_commit_batches_wise(connection, cursor, sql_query : str, sql_query_value: List[Tuple], batch_size: int = batch_size_length ):
    ## this is save data in database batches wise.
    batch_count = 0
    for index in range(0, len(sql_query_value), batch_size):
        batch = sql_query_value[index: index + batch_size]
        cursor.executemany(sql_query, batch)
        batch_count += 1
        connection.commit()
    return batch_count


def insert_movie_urls_table(list_data : list):
    connection = get_connection()
    cursor = connection.cursor()
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("movie_name"), 
                dict_data.get("movie_url"),
                dict_data.get("status")
            ))

        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()


def fetch_movie_urls_table():
    connection = get_connection()
    cursor = connection.cursor()
    query = f"SELECT id, movie_name, movie_url, status FROM {table_name} WHERE status = 'pending' ;"
 
    cursor.execute(query)
    rows = cursor.fetchall()

    result = []
    for row in rows:
        data = {
            "id": row[0],
            "movie_name": row[1],
            "movie_url": row[2],
            "status": row[3]
        }
        result.append(data)

    cursor.close()
    connection.close()
    return result

def update_movie_urls_status(country_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    sql_query = f"UPDATE {table_name} SET status = %s  WHERE id = %s ;"
    values = (status, country_id)
    cursor.execute(sql_query, values)
    connection.commit()
    cursor.close()
    connection.close()



# second table 
movie_detail_table_name = "movie_details"

def create_movie_details_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        query =  f"""
                CREATE TABLE IF NOT EXISTS {movie_detail_table_name}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                movie_name VARCHAR(200),
                description TEXT,   
                image_url TEXT,
                reviews VARCHAR(100),
                scorePercent VARCHAR(100),
                cast_and_crew JSON, 
                review_data_details JSON, 
                video_url JSON
        ); """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print("Table creation failed")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def insert_movie_details_table(list_data : list):
    print("-----insert_movie_details_table--------")
    connection = get_connection()
    cursor = connection.cursor()
    dict_data = list_data[0]
    columns = ", ".join(list(dict_data.keys()))
    values = "".join([len(dict_data.keys()) * '%s,']).strip(',')
    parent_sql = f"""INSERT INTO {movie_detail_table_name} ({columns}) VALUES ({values})"""
    try:
        product_values = []
        for dict_data in list_data:
            product_values.append( (
                dict_data.get("movie_name"),
                dict_data.get("description"),   
                dict_data.get("image_url"),
                dict_data.get("reviews"),
                dict_data.get("scorePercent"),
                dict_data.get("cast_and_crew"), 
                dict_data.get("review_data_details"), 
                dict_data.get("video_url")
            ))

        try:
            batch_count = data_commit_batches_wise(connection, cursor, parent_sql, product_values)
            print(f"Parent batches executed count={batch_count}")
        except Exception as e:
            print(f"batch can not. Error : {e} ")

        cursor.close()
        connection.close()

    except Exception as e:
        ## this exception execute when error occur in try block and rollback until last save on database .
        connection.rollback()
        # print(f"Transaction failed, rolled back. Error: {e}")
        print("Transaction failed. Rolling back")
    except:
        print("except error raise ")
    finally:
        connection.close()