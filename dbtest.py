import mysql.connector
import os
from dotenv import load_dotenv

def get_list_from_mariadb(column="*", table="text"):
    try:
        load_dotenv()

        host=os.getenv("host")
        user=os.getenv("user")
        password=os.getenv("password")
        database=os.getenv("database")
        if host is None or user is None or password is None or database is None:
            print("Error: Bot token not found in .env file.")
            exit(1)

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()

        query = f"SELECT {column} FROM {table};"
        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    data_list = get_list_from_mariadb()
    print(data_list)
