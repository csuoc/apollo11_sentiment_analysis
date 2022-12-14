# Import box
from config.sql_connection import engine
import pandas as pd

# Defining queries

def get_everything ():
    query = """SELECT * FROM apollo11;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_speaker (name):
    query = f"""SELECT * 
    FROM apollo11
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_everything_from_multiple_speaker (name1,name2,name3,name4):
    query = f"""SELECT comms, mission_time, speaker 
    FROM apollo11
    WHERE (speaker = '{name1}' OR speaker = '{name2}' OR speaker = '{name3}' OR speaker = '{name4}');"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_comms (name):
    query = f"""SELECT comms 
    FROM apollo11
    WHERE speaker = '{name}';"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def get_just_multiple_comms (name1, name2, name3, name4):
    query = f"""SELECT comms 
    FROM apollo11
    WHERE (speaker = '{name1}' OR speaker = '{name2}' OR speaker = '{name3}' OR speaker = '{name4}');"""

    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (mission_time, comms, speaker):
    query = f"""INSERT INTO apollo11
     (mission_time, comms, speaker) 
        VALUES ({mission_time}, '{comms}', '{speaker}');
    """
    engine.execute(query)
    return f"Correctly introduced!"

def delete_one_row (speaker):
    query = f"""DELETE FROM apollo11
            WHERE speaker = '{speaker}';
            """
    engine.execute(query)
    return f"Sucessfully deleted!"