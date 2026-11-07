filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(f"\n--- Đang đọc file: {filename} ---")
    try:
        with open(filename, 'r', encoding='utf-8') as file_object:
            content = file_object.read()
            print(content.strip())    
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
