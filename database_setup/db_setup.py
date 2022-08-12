from faker import Faker
import pandas as pd
import psycopg2
import psycopg2.extras as extras
import db_params

# SQL DB connection
conn = psycopg2.connect(
    "postgres://postgres:{db_params.password}@localhost:5433/imaginary-inc"
)

# --------------------------
# POPULATING customer TABLE |
# --------------------------

# Creating dataframe to populate 'customer' table using Faker package
fake = Faker()


def create_rows(num=1):
    output = [
        {
            "id": fake.random_number(digits=7),
            "name": fake.name(),
            "country": fake.country(),
            "email": fake.email(),
            "phone": fake.phone_number(),
        }
        for x in range(num)
    ]
    return output


customer_df = pd.DataFrame(create_rows(10))

# Sending dataframe to the SQL table
def execute_values(conn, df, table):

    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ",".join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()


execute_values(conn, customer_df, "customers")

