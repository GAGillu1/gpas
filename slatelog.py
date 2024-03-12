import pandas as pd
from connection import get_db_connection

def slate_log(slateid, scale, gpa):
    try:
        conn = get_db_connection()
        query = "INSERT INTO public.slatelog(slateid, universityscale, gpa) VALUES (%s, %s, %s)"
        values = (slateid, scale, gpa)

        # Create a DataFrame with the values
        df = pd.DataFrame([values], columns=["slateid", "universityscale", "gpa"])

        # Print the prepared statement query
        prepared_query = df.to_sql(name="slatelog", con=conn, if_exists="append", index=False)
        print(prepared_query)

    except Exception as error:
        print(error)
    finally:
        conn.close()

