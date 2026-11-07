filename = 'dox.txt'
print("tell name:")
print("(enter)")
while True:
    name = input()
    if name.lower() == 'q':
        break
    print(f"Hi {name}!\n")
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
