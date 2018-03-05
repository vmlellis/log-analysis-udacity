#!/usr/bin/env python3
import psycopg2


class DBClient:
    def __init__(self, database_name="news"):
        """Connects to the PostgreSQL database"""
        try:
            self.db = psycopg2.connect("dbname={}".format(database_name))
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)

    def execute_query(self, query):
        """Return query results for given query """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection """
        self.db.close()


def open_sql(sql_name):
    with open(sql_name + '.sql', 'r') as f:
        return f.read()


def print_results(result, suffix):
    for i in range(len(result)):
        print('\t', i + 1, '.', result[i][0], '-', result[i][1], suffix)


if __name__ == '__main__':
    dbClient = DBClient()

    questions = [
        'What are the most popular three articles of all time?',
        'Who are the most popular article authors of all time?',
        'On which days did more than 1% of requests lead to errors?'
    ]

    list = [
        {'question': questions[0], 'suffix': 'views'},
        {'question': questions[1], 'suffix': 'views'},
        {'question': questions[2], 'suffix': '% errors'}
    ]

    for idx, el in enumerate(list):
        print(el['question'])
        sql = open_sql('question' + str(idx + 1))
        result = dbClient.execute_query(sql)
        print_results(result, el['suffix'])

    dbClient.close()
