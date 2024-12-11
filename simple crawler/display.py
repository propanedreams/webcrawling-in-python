import sqlite3
import csv

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
            
            # Ask the user if they want to export to a CSV
            export = input("\nDo you want to export the data to a CSV file? (y/n): ").strip().lower()
            if export == 'y':
                write_to_csv(rows)
                print("Data has been successfully exported to 'visited_sites.csv'.")
        else:
            print("No data found in the database.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def write_to_csv(data):
    """Write the visited sites data to a CSV file."""
    try:
        with open('visited_sites.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(['ID', 'URL', 'Timestamp'])
            # Write the data
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# Run the function
if __name__ == "__main__":
    display_visited_sites()
