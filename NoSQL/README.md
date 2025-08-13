## Resources

**Read or watch**:

*   [NoSQL Databases Explained](/rltoken/0HR2bZ3XFJzkttuEVF5Rug "NoSQL Databases Explained")
*   [What is NoSQL ?](/rltoken/JGxz6PJsAN9cjBBT_WVCAg "What is NoSQL ?")
*   [MongoDB with Python Crash Course - Tutorial for Beginners](/rltoken/PkdXgnfXUfJIk5iqf9Wp4A "MongoDB with Python Crash Course - Tutorial for Beginners")
*   [MongoDB Tutorial 2 : Insert, Update, Remove, Query](/rltoken/y6ncfHy0Hn7uqaIyitWQRg "MongoDB Tutorial 2 : Insert, Update, Remove, Query")
*   [Aggregation](/rltoken/sIORcQADQT2Wf2opdMu30Q "Aggregation")
*   [Introduction to MongoDB and Python](/rltoken/BLt93wwWTkVQWVlSDerI1g "Introduction to MongoDB and Python")
*   [mongo Shell Methods](/rltoken/q-RfEFpmN-fGiX-SvmQjHA "mongo Shell Methods")
*   [The mongo Shell](/rltoken/fmrWM3wzfC2d2-WHqzzPBQ "The mongo Shell")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/2Kw4G-iwbeaF3gBMQiUZJg "explain to anyone"), **without the help of Google**:

### General

*   What NoSQL means
*   What is difference between SQL and NoSQL
*   What is ACID
*   What is a document storage
*   What are NoSQL types
*   What are benefits of a NoSQL database
*   How to query information from a NoSQL database
*   How to insert/update/delete information from a NoSQL database
*   How to use MongoDB

## Requirements

### MongoDB Command File

*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `MongoDB` (version 4.4)
*   All your files should end with a new line
*   The first line of all your files should be a comment: `// my comment`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   The length of your files will be tested using `wc`

### Python Scripts

*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9) and `PyMongo` (version 4.8.0)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5.\*)
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
*   Your code should not be executed when imported (by using `if __name__ == "__main__"`:)

## Tasks

### 1.

Write a script that lists all databases in MongoDB.
```
guillaume@ubuntu:~/$ cat 0-list\_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$
```


### 2.

Write a script that creates or uses the database `my_db`:
```
guillaume@ubuntu:~/$ cat 0-list\_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 1-use\_or\_create\_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my\_db
bye
guillaume@ubuntu:~/$
```


### 3.

Write a script that inserts a document in the collection `school`:

*   The document must have one attribute `name` with value “Holberton school”
*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 2-insert | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/$
```


### 4.

Write a script that lists all documents in the collection `school`:

*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 3-all | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
{ "\_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/$
```


### 5.

Write a script that lists all documents with `name="Holberton school"` in the collection `school`:

*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 4-match | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
{ "\_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/$
```


### 6.

Write a script that displays the number of documents in the collection `school`:

*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 5-count | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/$
```


### 7.

Write a script that adds a new attribute to a document in the collection `school`:

*   The script should update only document with `name="Holberton school"` (all of them)
*   The update should add the attribute `address` with the value “972 Mission street”
*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 6-update | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 4-match | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
{ "\_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/$
```


### 8.

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:

*   The database name will be passed as option of `mongo` command
```
guillaume@ubuntu:~/$ cat 7-delete | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 4-match | mongo my\_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my\_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/$
```


### 9.

Write a Python function that lists all documents in a collection:

*   Prototype: `def list_all(mongo_collection):`
*   Return an empty list if no document in the collection
*   `mongo_collection` will be the `pymongo` collection object
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list\_all = \_\_import\_\_('8-all').list\_all

if \_\_name\_\_ == "\_\_main\_\_":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school\_collection = client.my\_db.school
    schools = list\_all(school\_collection)
    for school in schools:
        print("\[{}\] {}".format(school.get('\_id'), school.get('name')))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./8-main.py
\[5a8f60cfd4321e1403ba7ab9\] Holberton school
\[5a8f60cfd4321e1403ba7aba\] UCSD
guillaume@ubuntu:~/$
```


### 10.

Write a Python function that inserts a new document in a collection based on `kwargs`:

*   Prototype: `def insert_school(mongo_collection, **kwargs):`
*   `mongo_collection` will be the `pymongo` collection object
*   Returns the new `_id`
```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/env python3
""" 9-main """
from pymongo import MongoClient
list\_all = \_\_import\_\_('8-all').list\_all
insert\_school = \_\_import\_\_('9-insert\_school').insert\_school

if \_\_name\_\_ == "\_\_main\_\_":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school\_collection = client.my\_db.school
    new\_school\_id = insert\_school(school\_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new\_school\_id))

    schools = list\_all(school\_collection)
    for school in schools:
        print("\[{}\] {} {}".format(school.get('\_id'), school.get('name'), school.get('address', "")))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./9-main.py
New school created: 5a8f60cfd4321e1403ba7abb
\[5a8f60cfd4321e1403ba7ab9\] Holberton school
\[5a8f60cfd4321e1403ba7aba\] UCSD
\[5a8f60cfd4321e1403ba7abb\] UCSF 505 Parnassus Ave
guillaume@ubuntu:~/$
```


### 11.

Write a Python function that changes all topics of a school document based on the name:

*   Prototype: `def update_topics(mongo_collection, name, topics):`
*   `mongo_collection` will be the `pymongo` collection object
*   `name` (string) will be the school name to update
*   `topics` (list of strings) will be the list of topics approached in the school
```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/env python3
""" 10-main """
from pymongo import MongoClient
list\_all = \_\_import\_\_('8-all').list\_all
update\_topics = \_\_import\_\_('10-update\_topics').update\_topics

if \_\_name\_\_ == "\_\_main\_\_":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school\_collection = client.my\_db.school
    update\_topics(school\_collection, "Holberton school", \["Sys admin", "AI", "Algorithm"\])

    schools = list\_all(school\_collection)
    for school in schools:
        print("\[{}\] {} {}".format(school.get('\_id'), school.get('name'), school.get('topics', "")))

    update\_topics(school\_collection, "Holberton school", \["iOS"\])

    schools = list\_all(school\_collection)
    for school in schools:
        print("\[{}\] {} {}".format(school.get('\_id'), school.get('name'), school.get('topics', "")))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./10-main.py
\[5a8f60cfd4321e1403ba7abb\] UCSF
\[5a8f60cfd4321e1403ba7aba\] UCSD
\[5a8f60cfd4321e1403ba7ab9\] Holberton school \['Sys admin', 'AI', 'Algorithm'\]
\[5a8f60cfd4321e1403ba7abb\] UCSF
\[5a8f60cfd4321e1403ba7aba\] UCSD
\[5a8f60cfd4321e1403ba7ab9\] Holberton school \['iOS'\]
guillaume@ubuntu:~/$
```


### 12.

Write a Python function that returns the list of school having a specific topic:

*   Prototype: `def schools_by_topic(mongo_collection, topic):`
*   `mongo_collection` will be the `pymongo` collection object
*   `topic` (string) will be topic searched
```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/env python3
""" 11-main """
from pymongo import MongoClient
list\_all = \_\_import\_\_('8-all').list\_all
insert\_school = \_\_import\_\_('9-insert\_school').insert\_school
schools\_by\_topic = \_\_import\_\_('11-schools\_by\_topic').schools\_by\_topic

if \_\_name\_\_ == "\_\_main\_\_":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school\_collection = client.my\_db.school

    j\_schools = \[
        { 'name': "Holberton school", 'topics': \["Algo", "C", "Python", "React"\]},
        { 'name': "UCSF", 'topics': \["Algo", "MongoDB"\]},
        { 'name': "UCLA", 'topics': \["C", "Python"\]},
        { 'name': "UCSD", 'topics': \["Cassandra"\]},
        { 'name': "Stanford", 'topics': \["C", "React", "Javascript"\]}
    \]
    for j\_school in j\_schools:
        insert\_school(school\_collection, \*\*j\_school)

    schools = schools\_by\_topic(school\_collection, "Python")
    for school in schools:
        print("\[{}\] {} {}".format(school.get('\_id'), school.get('name'), school.get('topics', "")))

guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./11-main.py
\[5a90731fd4321e1e5a3f53e3\] Holberton school \['Algo', 'C', 'Python', 'React'\]
\[5a90731fd4321e1e5a3f53e5\] UCLA \['C', 'Python'\]
guillaume@ubuntu:~/$
```


### 13.

Write a Python script that provides some stats about Nginx logs stored in MongoDB:

*   Database: `logs`
*   Collection: `nginx`
*   Display (same as the example):
    *   first line: `x logs` where `x` is the number of documents in this collection
    *   second line: `Methods:`
    *   5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
    *   one line with the number of documents with:
        *   `method=GET`
        *   `path=/status`

You can use this dump as data sample: [dump.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/645541f867bb79ae47b7a80922e9a48604a569b9.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250813%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250813T072832Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=1c64f5daad3591b8e349715867e96734feed941ebf25a31a7147d50483bb7704 "dump.zip")

The output of your script **must be exactly the same as the example**
```
guillaume@ubuntu:~/$ curl -o dump.zip -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip"
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ unzip dump.zip
Archive:  dump.zip
   creating: dump/
   creating: dump/logs/
  inflating: dump/logs/nginx.metadata.json
  inflating: dump/logs/nginx.bson
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ mongorestore dump
2018-02-23T20:12:37.807+0000    preparing collections to restore from
2018-02-23T20:12:37.816+0000    reading metadata for logs.nginx from dump/logs/nginx.metadata.json
2018-02-23T20:12:37.825+0000    restoring logs.nginx from dump/logs/nginx.bson
2018-02-23T20:12:40.804+0000    \[##......................\]  logs.nginx  1.21MB/13.4MB  (9.0%)
2018-02-23T20:12:43.803+0000    \[#####...................\]  logs.nginx  2.88MB/13.4MB  (21.4%)
2018-02-23T20:12:46.803+0000    \[#######.................\]  logs.nginx  4.22MB/13.4MB  (31.4%)
2018-02-23T20:12:49.803+0000    \[##########..............\]  logs.nginx  5.73MB/13.4MB  (42.7%)
2018-02-23T20:12:52.803+0000    \[############............\]  logs.nginx  7.23MB/13.4MB  (53.8%)
2018-02-23T20:12:55.803+0000    \[###############.........\]  logs.nginx  8.53MB/13.4MB  (63.5%)
2018-02-23T20:12:58.803+0000    \[#################.......\]  logs.nginx  10.1MB/13.4MB  (74.9%)
2018-02-23T20:13:01.803+0000    \[####################....\]  logs.nginx  11.3MB/13.4MB  (83.9%)
2018-02-23T20:13:04.803+0000    \[######################..\]  logs.nginx  12.8MB/13.4MB  (94.9%)
2018-02-23T20:13:06.228+0000    \[########################\]  logs.nginx  13.4MB/13.4MB  (100.0%)
2018-02-23T20:13:06.230+0000    no indexes to restore
2018-02-23T20:13:06.231+0000    finished restoring logs.nginx (94778 documents)
2018-02-23T20:13:06.232+0000    done
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ ./12-log\_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
guillaume@ubuntu:~/$
```
