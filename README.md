# Task-7
# Bookstore Data Analysis with Python

This project contains a Python script (sales_summary.py) that performs a basic analysis of bookstore data stored in a SQLite database (bookstore_data.db).

## Project Overview

The script performs the following actions:

1.  *Creates a SQLite Database:* Generates a database file named bookstore_data.db if it doesn't exist.
2.  *Creates a Table:* Creates a table named books within the database to store book information.
3.  *Inserts Sample Data:* Populates the books table with sample data, including book ID, title, author, price, and quantity in stock.
4.  *Queries Data:* Executes a SQL query to retrieve and summarize book data, calculating the total number of books and the total inventory value for each author.
5.  *Displays Results:*
    * Prints a table to the console showing the summarized data.
    * Generates a bar chart visualizing the total inventory value for each author.

## Files

* sales_summary.py:  The Python script.
* bookstore_data.db: The SQLite database file (created by the script).

## How to Run the Script

1.  Ensure Python is installed.
2.  Install the required libraries:
    bash
    pip install pandas matplotlib
    
3.  Save the sales_summary.py file.
4.  Navigate to the directory where you saved the file in your terminal or command prompt.
5.  Run the script:
    bash
    python sales_summary.py
    

## Output
The script will produce:

* Console output:  A table summarizing book data by author.
* A bar chart:  Visual representation of the total value of book inventory for each author.
