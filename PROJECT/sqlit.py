import sqlite3

def setup_database():
    conn = sqlite3.connect('GYM WORKOUT.db')
    cursor = conn.cursor()

    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        time TEXT NOT NULL
        )
''')
    conn.commit()
    conn.close()
    print("Database and table setup complete.")

def get_connection():
    return sqlite3.connect('GYM WORKOUT.db')

def list_workouts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    user = cursor.fetchall()
    
    if user:
        print("\n ---All Workouts---")
        print("ID | Username | Time")
        print("-" * 40)

        for row in user:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    else:
        print("No workouts found.")

    conn.close()

def add_workout(username, time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, time) VALUES (?, ?)", (username, time))
    conn.commit()
    print(f"User '{username}' added successfully.")
    conn.close()

def update_workout(user_id, new_username, new_time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = ?, time = ? WHERE id = ?", (new_username, new_time, user_id))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"User with ID {user_id} updated successfully.")
    else:
        print(f"No user found with ID {user_id}.")
    conn.close()

def delete_workout(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"User with ID {user_id} deleted successfully.")
    else:
        print(f"No user found with ID {user_id}.")
    conn.close()

def main():
    setup_database()
    while True:
        print("\n -----Workout Manager-----")
        print("1. List all Workout")
        print("2. Add a Workout")
        print("3. Update a Workout")
        print("4. Delete a Workout")
        print("5. Exit")
        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_workouts()
            case '2':
                username = input("Enter username: ")
                time = input("Enter time: ")
                add_workout(username, time)
            case '3':
                user_id = int(input("Enter the user ID to update: "))
                new_username = input("Enter the new username: ")
                new_time = input("Enter the new time: ")
                update_workout(user_id, new_username, new_time)
            case '4':
                user_id = int(input("Enter the user ID to delete: "))
                delete_workout(user_id)
            case '5':
                break
            case _:
                print("Invalid choice please select within the options")

if __name__ == "__main__":
    main()
