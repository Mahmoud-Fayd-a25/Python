# Automating database management tasks using the psycopg2 library for PostgreSQL and pymysql library for MySQL.
# Install these libraries using (pip install psycopg2 pymysql).
# Replace "your_postgres_host", "your_database", "your_username", "your_password" with actual database connection parameters.
# Replace "your_mysql_host", "your_database", "your_username", "your_password" with MySQL connection parameters.

import psycopg2
import pymysql

# PostgreSQL connection parameters
postgres_params = {
    "host": "your_postgres_host",
    "database": "your_database",
    "user": "your_username",
    "password": "your_password",
}

# MySQL connection parameters
mysql_params = {
    "host": "your_mysql_host",
    "database": "your_database",
    "user": "your_username",
    "password": "your_password",
}

# Example 1: Connecting to PostgreSQL database


def connect_to_postgres():
    conn = psycopg2.connect(**postgres_params)
    print("Connected to PostgreSQL database")
    return conn

# Example 2: Connecting to MySQL database


def connect_to_mysql():
    conn = pymysql.connect(**mysql_params)
    print("Connected to MySQL database")
    return conn

# Example 3: Creating a table in PostgreSQL


def create_table_in_postgres():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    print("Table 'users' created in PostgreSQL")

# Example 4: Creating a table in MySQL


def create_table_in_mysql():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)
    conn.commit()
    print("Table 'users' created in MySQL")

# Example 5: Inserting data into PostgreSQL table


def insert_data_into_postgres():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                   ("John Doe", "john@example.com"))
    conn.commit()
    print("Data inserted into PostgreSQL table")

# Example 6: Inserting data into MySQL table


def insert_data_into_mysql():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                   ("Jane Smith", "jane@example.com"))
    conn.commit()
    print("Data inserted into MySQL table")

# Example 7: Retrieving data from PostgreSQL table


def retrieve_data_from_postgres():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Example 8: Retrieving data from MySQL table


def retrieve_data_from_mysql():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Example 9: Dropping PostgreSQL table


def drop_table_in_postgres():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    print("Table 'users' dropped in PostgreSQL")

# Example 10: Dropping MySQL table


def drop_table_in_mysql():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    print("Table 'users' dropped in MySQL")

# Execute examples


def main():
    print("Example 1:")
    connect_to_postgres()
    print()

    print("Example 2:")
    connect_to_mysql()
    print()

    print("Example 3:")
    create_table_in_postgres()
    print()

    print("Example 4:")
    create_table_in_mysql()
    print()

    print("Example 5:")
    insert_data_into_postgres()
    print()

    print("Example 6:")
    insert_data_into_mysql()
    print()

    print("Example 7:")
    retrieve_data_from_postgres()
    print()

    print("Example 8:")
    retrieve_data_from_mysql()
    print()

    print("Example 9:")
    drop_table_in_postgres()
    print()

    print("Example 10:")
    drop_table_in_mysql()
    print()


if __name__ == "__main__":
    main()
