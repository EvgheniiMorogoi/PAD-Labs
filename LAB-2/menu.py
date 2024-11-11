import threading
import os
import time

# Funcție pentru pornirea serverului broker
def start_broker():
    os.system("python broker_server.py")

# Funcție pentru pornirea publisher-ului pentru Topic1
def start_publisher1():
    os.system("python publisher.py")

# Funcție pentru pornirea publisher-ului pentru Topic2
def start_publisher2():
    os.system("python publisher2.py")

# Funcție pentru pornirea subscriber-ului pentru Topic1
def start_subscriber1():
    os.system("python subscriber.py")

# Funcție pentru pornirea subscriber-ului pentru Topic2
def start_subscriber2():
    os.system("python subscriber2.py")

# Funcție pentru afișarea meniului
def show_menu():
    print("\n===== MENIU =====")
    print("1. Start Broker")
    print("2. Start Publisher1 (Topic1)")
    print("3. Start Subscriber1 (Topic1)")
    print("4. Start Subscriber2 (Topic2)")
    print("5. Start Publisher2 (Topic2)")
    print("6. Exit")
    print("=================\n")

# Funcția principală
def main():
    threads = {}

    while True:
        show_menu()
        choice = input("Alege o opțiune: ")

        if choice == "1":
            if "broker" not in threads or not threads["broker"].is_alive():
                print("Pornesc Broker-ul...")
                threads["broker"] = threading.Thread(target=start_broker)
                threads["broker"].start()
                time.sleep(1)
            else:
                print("Broker-ul este deja pornit.")
        
        elif choice == "2":
            print("Pornesc Publisher-ul pentru Topic1...")
            threads["publisher1"] = threading.Thread(target=start_publisher1)
            threads["publisher1"].start()

        elif choice == "3":
            print("Pornesc Subscriber-ul pentru Topic1...")
            threads["subscriber1"] = threading.Thread(target=start_subscriber1)
            threads["subscriber1"].start()

        elif choice == "4":
            print("Pornesc Subscriber-ul pentru Topic2...")
            threads["subscriber2"] = threading.Thread(target=start_subscriber2)
            threads["subscriber2"].start()

        elif choice == "5":
            print("Pornesc Publisher-ul pentru Topic2...")
            threads["publisher2"] = threading.Thread(target=start_publisher2)
            threads["publisher2"].start()

        elif choice == "6":
            print("Ieșire...")
            break

        else:
            print("Opțiune invalidă! Încearcă din nou.")

if __name__ == "__main__":
    main()
