import sys
import json

# File for storing data
DATA_FILE = "data.txt"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            content = file.read()
            # Dacă fișierul este gol, returnează o listă goală
            if not content:
                return []
            return json.loads(content)  # Decodifică JSON-ul doar dacă fișierul conține date
    except (FileNotFoundError, json.JSONDecodeError):  # Tratare excepții și pentru fișierul inexistent
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

def create_item():
    name = input("Introduceti numele elementului: ")
    description = input("Introduceti descrierea elementului: ")

    if not name:
        print("Eroare: Numele este obligatoriu!")
        return

    data = load_data()
    item_id = len(data) + 1
    data.append({"id": item_id, "name": name, "description": description})
    save_data(data)

    print(f"Elementul cu ID-ul {item_id} a fost creat cu succes.")

def get_items():
    data = load_data()

    if not data:
        print("Nu exista elemente in baza de date.")
    else:
        for item in data:
            print(f"ID: {item['id']}, Nume: {item['name']}, Descriere: {item['description']}")

def get_item():
    item_id = input("Introduceti ID-ul elementului: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID-ul trebuie sa fie un numar.")
        return

    data = load_data()
    item = next((item for item in data if item['id'] == item_id), None)

    if not item:
        print("Elementul cu acest ID nu exista.")
    else:
        print(f"ID: {item['id']}, Nume: {item['name']}, Descriere: {item['description']}")

def update_item():
    item_id = input("Introduceti ID-ul elementului pe care doriti sa il actualizati: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID-ul trebuie sa fie un numar.")
        return

    data = load_data()
    item = next((item for item in data if item['id'] == item_id), None)

    if not item:
        print("Elementul cu acest ID nu a fost gasit.")
        return

    name = input("Introduceti noul nume: ")
    description = input("Introduceti noua descriere: ")

    item['name'] = name
    item['description'] = description
    save_data(data)

    print("Elementul a fost actualizat cu succes.")

def delete_item():
    item_id = input("Introduceti ID-ul elementului pe care doriti sa il stergeti: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("ID-ul trebuie sa fie un numar.")
        return

    data = load_data()
    initial_length = len(data)
    data = [item for item in data if item['id'] != item_id]

    if len(data) == initial_length:
        print("Elementul cu acest ID nu a fost gasit.")
    else:
        save_data(data)
        print("Elementul a fost sters cu succes.")

def show_menu():
    print("\n--- MENIU CRUD ---")
    print("1. Creare element nou")
    print("2. Vizualizare toate elementele")
    print("3. Vizualizare un element")
    print("4. Actualizare element")
    print("5. Stergere element")
    print("6. Iesire")

def main():
    while True:
        show_menu()
        choice = input("Alegeti o optiune: ")

        if choice == '1':
            create_item()
        elif choice == '2':
            get_items()
        elif choice == '3':
            get_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            print("Iesire din aplicatie.")
            sys.exit()
        else:
            print("Optiune invalida. Incercati din nou.")

if __name__ == '__main__':
    main()
