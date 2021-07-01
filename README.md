# Most-Active-Cookie

Program that reads in a csv file of cookie logs and find the most active one given a particular day.

# Instructions

To run the program with a particular log file,  run the command 

``` python3 src/most_active_cookie <path/to/file> -d <some query> ```.

To tun the test cases, change directory into tests and run the command 

``` python3 test.py ```

# Design

To maintain production level code (or atleast my best attempt at it), I made sure to approach this using
OOP and modularize each component to it's own file. Initially, I wanted to design my database using a 
hash table to map a date to a the cookie sesssions on that day. This would work for only a specific query 
type. So to make the database more robust, I redesigned it using a more complex datastructure to handle 
more types of querying.

## most_active_cookie.py

- Parses command line arguments.
- Reads csv file.
- Initializes database and performs the querying.

## CookieSession

Each cookie activity will be it's own object. The cookie identification and timestamp is stored.

## Query

The query is the request for information from the database. It is instantiated with the command 
line arguments. Queries also have a type, that will depend on the options provided.

## Database

The database stores all cookie sessions and is designed using the [trie](https://en.wikipedia.org/wiki/Trie) 
data structure. To instantiate the trie, a Node object is used. This database supports insertion and getting
the most active cookie by date.

## Node

This is the actual node for the trie. They keys that map to the childens are the keys from the timestamp 
(year/month/day, etc...). Each node will also store the cookie sessions for the current node and all it's
children. For the purpose of getting the most active cookie for a particular date, the data structure used
to hold the cookie sessions is a hash table that maps the cookie ID to the list of cookie sessions present.


