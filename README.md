## Overview
PyGPT-DBManager is a database management system built from scratch using object-oriented Python. It features a simple SQL parser and leverages a private GPT Language Model (LLM) to convert natural language queries into SQL commands. The system also utilizes Python's HTTPS library to send GET and POST requests at port 1000, enabling SQL command retrieval from any language.

## Features
- **Object-Oriented Database Management System**: Built using Python, this DBMS stores data in a Tab Separated Value (TSV) file.
- **SQL Parser**: A simple SQL parser that processes SQL commands.
- **Private GPT LLM Integration**: Converts natural language queries into SQL commands.
- **HTTPS Requests**: Uses Python's HTTPS library to send GET and POST requests at port 1000, allowing for SQL command retrieval from any language.
- **Multi-Language Support**: Example implementations in JavaScript and Java for sending natural language queries to the DBMS.

## Usage
To use PyGPT-DBManager, send a natural language query as a string via a POST request to port 1000. The private GPT LLM will convert the query into an SQL command, which is then processed by the SQL parser. The resulting command is executed on the database, and the data is stored in a TSV file.

## Note
The private GPT LLM is not included in this repository due to its proprietary nature.

## Contributions
Contributions are welcome! Please read the contributing guidelines before making any changes.

