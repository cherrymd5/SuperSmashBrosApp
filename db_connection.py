import psycopg2

def get_matches():
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="Huntee123",
                                    host="super-smash-bros.cjzzgdbitg4q.us-east-1.rds.amazonaws.com",
                                    port="5432",
                                    database="super_smash_bros_db")
        cursor = connection.cursor()
        query = "select * from smash_match_history"

        cursor.execute(query)
        print("Selecting rows from smash_match_history table using cursor.fetchall")
        match_records = cursor.fetchall()

        return match_records

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



def write_match(player, opponent, result):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="Huntee123",
                                    host="super-smash-bros.cjzzgdbitg4q.us-east-1.rds.amazonaws.com",
                                    port="5432",
                                    database="super_smash_bros_db")
        cursor = connection.cursor()
        query = "INSERT INTO smash_match_history(match_time, update_time, player_name, opponent_name, result) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, %s, %s, %s);"

        cursor.execute(query, (player, opponent, result))
        connection.commit()
        connection.close()


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



