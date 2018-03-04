#!/usr/bin/env python3
import psycopg2

class DBClient:
  def __init__(self, database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
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

  arr = [
    {
      'question': 'What are the most popular three articles of all time?',
      'suffix': 'views'
    },
    {
      'question': 'Who are the most popular article authors of all time?',
      'suffix': 'views'
    },
    {
      'question': 'On which days did more than 1% of requests lead to errors?',
      'suffix': '% errors'
    }
  ]

  for idx, el in enumerate(arr):
    print(el['question'])
    sql = open_sql('question' + str(idx + 1))
    result = dbClient.execute_query(sql)
    print_results(result, el['suffix'])

  dbClient.close()
