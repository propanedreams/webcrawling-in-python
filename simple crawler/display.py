import sqlite3

def display_visited_sites():
    """Fetch and display all visited sites from the database."""
    try:
        conn = sqlite3.connect('visited_sites.db')
        cursor = conn.cursor()
        
        # Query to select all data from visited_sites
        cursor.execute('SELECT id, url, timestamp FROM visited_sites ORDER BY id')
        rows = cursor.fetchall()
        
        if rows:
            print(f"{'ID':<5} {'URL':<50} {'Timestamp'}")
            print("=" * 80)
            for row in rows:
                print(f"{row[0]:<5} {row[1]:<50} {row[2]}")
        else:
            print("No data found in the database.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Run the function
if __name__ == "__main__":
    display_visited_sites()
