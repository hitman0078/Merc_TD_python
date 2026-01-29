from database import DatabaseManager
from menu import show_menu


def main():
    db = DatabaseManager()

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            db.insert_user(name, age)

        elif choice == "2":
            users = db.fetch_users()
            if users:
                print("\n--- Users List ---")
                for user in users:
                    print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
            else:
                print("⚠️ No users found.")

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            if db.update_user(user_id, name, age):
                print("✅ User updated successfully.")
            else:
                print("❌ User not found.")

        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            if db.delete_user(user_id):
                print("✅ User deleted successfully.")
            else:
                print("❌ User not found.")

        elif choice == "5":
            db.close()
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
