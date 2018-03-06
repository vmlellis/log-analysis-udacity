# Logs Analysis

This is a solution for the Log Analysis project in Udacity Full Stack Web Developer course.
In this project, a large database (> 1000k rows) is explored by building complex SQL queries to extract interesting data.

The database in question has 3 tables;
- `articles`
- `authors`
- `log`

## Pre-Requisites
- Linux
  - You use the virtual machine from the course:
    - Download Vagrant and Virtual Box.
    - Download or clone fullstack-nanodegree-vm repository.
    - Runs the vm (`vagrant up`).
    - Runs the terminal (`vagrant ssh`).
  - Or you can directly on Linux, but you have to create the vagrant user on database before: `postgres -c 'createuser -dRS vagrant'`.
- Postgress.
- Python 3.
- Make sure you have `newsdata.sql`. It can be downloaded from the Udacity course page.
- Run the following command to execute it in `news` database.

```sh
psql -d news -f newsdata.sql
```

- Finally run the script.


## How to Run Project

```sh
python3 newsdata.py
```
