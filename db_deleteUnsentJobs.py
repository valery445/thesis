import mysql.connector
import sys

def db_deleteUnsentJobs(appname, batch):
    # We suppose that batch is the iteration
    # And appname is contained within result and wu_name as the starting string
    # like {appname}_{batch}_...
    # TODO: Parse data about db from config.xml
    db_user = "boincadm"
    db_name = "boincdocker"
    db_passwd = "12345"

    cnx = mysql.connector.connect(user=db_user, database=db_name, password=db_passwd)
    cursor = cnx.cursor()

    # Get the ids of the rows to be deleted from the result table
    result_query = ("""
        SELECT id
        FROM result
        WHERE batch = %s
        AND name LIKE %s
        AND server_state = 2;
    """)
    cursor.execute(result_query, (batch, f"{appname}%"))
    result_ids = cursor.fetchall()
    result_count = len(result_ids)

    # Get the ids of the rows to be deleted from the workunit table
    workunit_query = ("""
        SELECT workunit.id
        FROM result
        INNER JOIN workunit
        ON result.workunitid = workunit.id
        WHERE result.batch = %s
        AND result.name LIKE %s
        AND result.server_state = 2;
    """)
    cursor.execute(workunit_query, (batch, f"{appname}%"))
    workunit_ids = cursor.fetchall()
    workunit_count = len(workunit_ids)

    # Delete the rows from both tables
    delete_query = ("""
        DELETE result, workunit
        FROM result
        INNER JOIN workunit
        ON result.workunitid = workunit.id
        WHERE result.batch = %s
        AND result.name LIKE %s
        AND result.server_state = 2;
    """)
    cursor.execute(delete_query, (batch, f"{appname}%"))
    cnx.commit()

    # Format the output string
    output_str = f"Batch number: {batch}\n"
    output_str += f"Appname: {appname}\n"
    output_str += f"Deleted {result_count} rows from the result table with ids: {', '.join(str(id[0]) for id in result_ids)}\n"
    output_str += f"Deleted {workunit_count} rows from the workunit table with ids: {', '.join(str(id[0]) for id in workunit_ids)}"

    cursor.close()
    cnx.close()

    return output_str
    
if __name__ == "__main__": 
    if len(sys.argv) < 3:
        print("Error: expecting two arguments - appname, batch (iteration number)")
        sys.exit(1)

    appname = sys.argv[1]
    batch = int(sys.argv[2])
    print(db_deleteUnsentJobs(appname, batch))
