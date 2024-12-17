import sqlite3
import csv
import os

def display_data_from_db():
    """Display data from the visited_sites database and offer export options."""
    db_file = 'visited_sites.db'
    
    if not os.path.exists(db_file):
        print("Database file not found. Please run the crawler first.")
        return
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Query to fetch all data from the visited_sites table
        cursor.execute('SELECT id, url, title, meta_description, h1_tags, links, images, tables, timestamp FROM visited_sites')
        rows = cursor.fetchall()

        if not rows:
            print("No data found in the database.")
            return

        # Display data in a readable format
        print(f"{'ID':<5} {'URL':<50} {'Title':<30} {'Timestamp'}")
        print("=" * 120)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<50} {row[2]:<30} {row[8]}")  # Display ID, URL, Title, Timestamp
        
        # Prompt user for export options
        export = input("\nWould you like to export the data to a CSV file? (yes/no): ").strip().lower()
        if export == "yes":
            export_to_csv(rows)
            print("Data successfully exported to 'visited_sites_export.csv'.")
        else:
            print("Export canceled.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def export_to_csv(rows):
    """Export data to a CSV file."""
    with open("visited_sites_export.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["ID", "URL", "Title", "Meta Description", "H1 Tags", "Links", "Images", "Tables", "Timestamp"])
        # Write rows
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    display_data_from_db()
