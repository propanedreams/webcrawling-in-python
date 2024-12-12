import sqlite3
import csv

def display_visited_sites():
    """Fetch and display all visited sites from the database."""
    try:
        conn = sqlite3.connect('visited_sites.db')
        cursor = conn.cursor()
        
        # Query to select all data from visited_sites
        cursor.execute('SELECT id, url, title, meta_description, h1_tags, timestamp FROM visited_sites ORDER BY id')
        rows = cursor.fetchall()
        
        if rows:
            print(f"{'ID':<5} {'URL':<50} {'Title':<30} {'Meta Description':<50} {'H1 Tags':<50} {'Timestamp'}")
            print("=" * 200)
            for row in rows:
                print(f"{row[0]:<5} {row[1]:<50} {row[2]:<30} {row[3]:<50} {row[4]:<50} {row[5]}")
        else:
            print("No data found in the database.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def export_to_csv():
    """Export the data to a CSV file."""
    try:
        conn = sqlite3.connect('visited_sites.db')
        cursor = conn.cursor()
        
        # Query to select all data from visited_sites
        cursor.execute('SELECT id, url, title, meta_description, h1_tags, timestamp FROM visited_sites ORDER BY id')
        rows = cursor.fetchall()
        
        if rows:
            # Define the output CSV file name
            csv_file = 'visited_sites.csv'
            with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(['ID', 'URL', 'Title', 'Meta Description', 'H1 Tags', 'Timestamp'])
                # Write rows
                writer.writerows(rows)
            print(f"Data successfully exported to {csv_file}")
        else:
            print("No data to export.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error exporting to CSV: {e}")

# Run the functions
if __name__ == "__main__":
    print("Displaying visited sites:")
    display_visited_sites()
    
    export = input("\nWould you like to export the data to a CSV file? (yes/no): ").strip().lower()
    if export == 'yes':
        export_to_csv()
