import psycopg2
from psycopg2 import OperationalError

# Database connection parameters
db_config = {
    'host': 'localhost',  # or your PostgreSQL server address
    'database': 'Kipcodes',  # your database name
    'user': 'postgres',  # your PostgreSQL username
    'password': 'Kipcodes2025',  # your PostgreSQL password
    'port': '5432'  # default PostgreSQL port
}

# Function to create a connection
def create_connection(db_config):
    connection = None
    try:
        connection = psycopg2.connect(**db_config)
        print("Connection to PostgreSQL DB successful!")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()  # Commit the transaction
        print("Query executed successfully!")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Function to fetch data
def fetch_data(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Example usage
if __name__ == "__main__":
    # Create a connection
    connection = create_connection(db_config)

    if connection:
        # Example: Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT,
            email TEXT NOT NULL UNIQUE
        );
        """
        execute_query(connection, create_table_query)

        # Example: Insert data
        insert_query = """
        INSERT INTO users (name, age, email) VALUES
        ('Alice', 30, 'alice@example.com'),
        ('Bob', 25, 'bob@example.com');
        """
        execute_query(connection, insert_query)

        # Example: Fetch data
        select_query = "SELECT * FROM users;"
        data = fetch_data(connection, select_query)
        print("Data from the database:")
        for row in data:
            print(row)

        # Close the connection
        connection.close()
        print("Connection closed.")