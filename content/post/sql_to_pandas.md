+++
date = '2022-03-05'
slug = "sql-to-python-pandas"
title = "Sequel to Pandas"
author = "Nelson Gonzabato"
description= "sql-to-pandas"
tags=["python","sql","data-analysis","open-source", "database",
"reflection"]
categories = ["python", "open-source", "development", "sql"]
+++

One of the most important parts of the data analysis pipeline is the ability to collate data obtained from different sources. While the CSV file format remains the most popular form of data input, a lot of times production level data analysis requires that one fetch data from an internet source which in the simplest form may involve downloading a CSV file from a remote source. Often, however, the data fetch process requires interaction with a database which therefore necessitates that one have an understanding of relational databases and how to interact with them.

For this reason, I have spent the past week or two (at the time of this post) to improving my knowledge of relational databases, and more specifically finally learning SQL. [SQL](https://en.wikipedia.org/wiki/SQL) has its origins at IBM where the motivation was to ["manipulate and retrieve data stored in IBM's original quasirelational database management system"](https://en.wikipedia.org/wiki/SQL). Over the years, the language has grown to be extremely useful and powerful with several different variants now available that differ in syntax and a few other aspects.

With the importance of SQL highlighted, it is time to take a look at how one can run SQL queries within python and finally converting the retrieved data to the familiar `DataFrame` format. 

**Required Libraries**

This blog post uses `sqlite3`, the `python` SQL interface that comes with the standard lib and `pandas` (1.3.4), the most popular data analysis library. First, we import these as required 


```python
import sqlite3
import pandas as pd 

```

**Define helper functions**

Next, to ease our SQL query handling, we define two helper functions, one to create a SQL table and one to execute our sQL queries. These are defined next below 

```python
def create_connection(db_path=None): 
    try:
        conn = sqlite3.connect(db_path)
    except:
        raise 
    else:
        return conn
```

The above function simply creates a SQL connection to a database via the `connect` method from `sqlite3`. We use a `try-else-finally` to ensure that we can raise errors whenever they occur and return a connection once successful.

```python 
def execute_sql(conn, sql_command):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_command)
        res = cursor.fetchall()
    except:
        raise 
    else:
        return res

```

The `execute_sql` function briefly takes a `sqlite3` [Connection](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection) and command as its arguments. The [Cursor](https://docs.python.org/3/library/sqlite3.html) object allows us to execute SQL queries via the `exceute` method. Finally, we use `fetchall` to fetch all data. We use a `try-except-else` again as above to ease our error handling. 

**Run SQL Queries**

With our functions in place, we can now run our `SQL` queries in python. First, we need to create a connection. One thing to note is that the `create_connection` method requires a path to a database `.db` file. If the provided path does not exist, one will be created with that name. For purposes of this blog post, we supply a non-existent database name (`sample.db`) meaning that this will be created for us.

```python
conn = create_connection("sample.db")
```


Next, for our table, I chose to create a table with gene id as a primary key and gene expression values. 

```python
res = execute_sql(conn, """
CREATE TABLE IF NOT EXISTS genes ([gene_id] TEXT PRIMARK KEY,
[gene_expression] NUMERIC)
""")
```

In `SQL`, to add values to a database, we need to use the `INSERT` command. While preparing this blog post, I noticed that if one uses the `INSERT` method, values may be inserted but the user may not see this unless they add a `print` to the `exceute_sql` call. However, even then sometimes values would return empty lists despite values being added. For this reason, I use `INSERT OR REPLACE INTO`


```python

res = list(map(lambda gene, value: execute_sql(conn, f"INSERT OR REPLACE INTO genes VALUES ('{gene}', {value})"),
               ("RAN1", "RAN2", "RAN3", "RAN4", "RAN5", "RAN6"),
    (0.01, 0.02, 0.03, 0.00001, 0.01, 0.00004)))

```

As one may quickly realize, it can get quickly tiring/boring to have to always manually type out the values to insert. For this blog post, I use a `lambda-map` approach to semi-automate the insertion process. 


With the above, we have successfully created a SQL table with random gene ids and random gene expression values. 


**SQL to Pandas**


Finally, with out pre-sequel in place, it's time to convert this to a pandas `DataFrame`. We do this by simply calling `DataFrame` on our result. Here I have used a select within select as I found this really fun to work with and also because if misused it can result in disaster.  

```python
pd.DataFrame(execute_sql(conn,"""
SELECT * FROM genes WHERE gene_expression < (SELECT gene_expression from genes where gene_id = 'RAN2')
""") , columns = ["geneid", "expression"])
```

This gives us

```shell
0   RAN1     0.01000
1   RAN4     0.00001
2   RAN5     0.01000
3   RAN6     0.00004
```

**Outro**

As always, this has been a short walk through (mostly for reinforcement of concepts) of how to move from a SQL query to a pandas `DataFrame`. I hope that this may motivate a reader to use SQL more in their own work. The full notebook used in this code is availabe [here](https://github.com/Nelson-Gon/nelson-gon.github.io/blob/fce053b641bb9d0de34c63af1ccb13f6da01d9af/code/python_notebooks/explore-sql.ipynb).  


Thank you for reading

Nelson

**Recommended resources**



- https://docs.python.org/3/library/sqlite3.html

- https://www.w3schools.com/sql/

- https://sqlzoo.net/wiki/SQL_Tutorial

