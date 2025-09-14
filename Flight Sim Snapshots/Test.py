import Functions

while True:
    print("1 - Save Snapshot")
    print("2 - Enact Snapshot")
    choice = input()
    print()

    if choice == "1":
        Functions.save_location()
    elif choice == "2":
        Functions.set_location()
