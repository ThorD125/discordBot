import mysql.connector
import os
from dotenv import load_dotenv

def get_list_from_mariadb():
    try:
        # Replace these with your actual database credentials
        
        load_dotenv()

    # Get the bot token from the environment variable
        host=os.getenv("host")
        user=os.getenv("user")
        password=os.getenv("password")
        database=os.getenv("database")
        if host is None or user is None or password is None or database is None:
            print("Error: Bot token not found in .env file.")
            exit(1)

        

        # Connect to the database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute a SELECT query to retrieve the data
        query = "SELECT * FROM text;"
        cursor.execute(query)

        result = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Extract the data from the result and return as a list
        print(result)
        data_list = [item[0] for item in result]
        return data_list

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    data_list = get_list_from_mariadb()
    print(data_list)
