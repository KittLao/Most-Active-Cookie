import argparse

from Database import Database
from CookieSession import CookieSession
from Query import Query

def read_csv(csv_file, delimeter=','):
    try:
        with open(csv_file, 'r') as file:
            rows = [row.split(delimeter) for row in file.readlines()]
            # Empty file case.
            if len(rows) == 0: return []
            # rows[1:] to remove header.
            logs = [CookieSession(cookie, ts) for cookie, ts in rows[1:]]
            return logs
    except IOError:
        print(f"Error: File {csv_file} not found.")


def main():
    # Command line processing.
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=str)
    parser.add_argument("-d", "--day", type=str)
    args = vars(parser.parse_args())
    csv_file, day = args["csv_file"], args["day"]

    # Initialize database to store and retrieve cookies.
    cookie_sessions = read_csv(csv_file)
    cookie_jar = Database(cookie_sessions)
    query = Query(day, "-d", '-')
    most_active = cookie_jar.get_most_active(query)

    for cookie in most_active:
        print(cookie)

main()

