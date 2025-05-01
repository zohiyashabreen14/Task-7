import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the SQLite database (or create it)
conn = sqlite3.connect('bookstore_data.db')
cursor = conn.cursor()

# Create a 'books' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        price REAL,
        quantity_in_stock INTEGER
    )
''')

# Insert some sample data into the 'books' table
books_data = [
    (101, 'The Great Novel', 'Jane Author', 25.99, 50),
    (102, 'Mystery Island', 'John Writer', 19.95, 100),
    (103, 'Sci-Fi Adventure', 'Emily Roberts', 32.50, 30),
    (104, 'Historical Fiction', 'David Smith', 28.00, 60),
    (105, 'Poetry Collection', 'Sarah Williams', 15.00, 80)
]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?)", books_data)
conn.commit()
print("Sample book data created and inserted.")
print("-" * 40)

# 2. Define the SQL query (a different query this time)
query = """
SELECT
    author,
    SUM(quantity_in_stock) AS total_books_by_author,
    SUM(price * quantity_in_stock) AS total_value_by_author
FROM books
GROUP BY author
ORDER BY total_value_by_author DESC;
"""

# 3. Execute the SQL query and load into a pandas DataFrame
df_books = pd.read_sql_query(query, conn)

# 4. Print the DataFrame (descriptive output)
print("Book Summary by Author:")
print(df_books)
print("-" * 40)

# 5. Plot a bar chart (with different labels and style)
plt.figure(figsize=(12, 6))  # Increased figure size for better readability
plt.bar(df_books['author'], df_books['total_value_by_author'], color='darkseagreen') # Changed color
plt.xlabel("Author Name", fontsize=12) # Added fontsize
plt.ylabel("Total Value of Books in Stock", fontsize=12)
plt.title("Total Value of Inventory by Author", fontsize=14, fontweight='bold') # Added fontsize and fontweight
plt.xticks(rotation=45, ha='right', fontsize=10) # Added fontsize
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# 6. Close the database connection
conn.close()