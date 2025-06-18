import os

def get_user_mappings():
    user_mapping = {}
    print("Let's set up your custom file type mappings.")
    try:
        count = int(input("How many file types would you like to map? "))
    except ValueError:
        print("Invalid number, defaulting to 0.")
        count = 0

    for _ in range(count):
        ext = input("Enter a file extension (include the dot, e.g., .txt): ").lower()
        folder = input("Enter the folder name for this file type: ")
        user_mapping[ext] = folder

    return user_mapping

def organize_files(folder_path, mapping):
    for root, dirs, files in os.walk(folder_path):
        # Avoid processing sorting folders themselves
        if os.path.abspath(root) != os.path.abspath(folder_path):
            if os.path.basename(root) in set(mapping.values()).union({'Others'}):
                continue

        for filename in files:
            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                target_folder = mapping.get(file_extension, 'Others')
                target_path = os.path.join(folder_path, target_folder)

                if not os.path.exists(target_path):
                    os.makedirs(target_path)

                new_file_path = os.path.join(target_path, filename)

                try:
                    os.rename(file_path, new_file_path)
                    print(f'Moved {filename} to {target_folder}')
                except Exception as e:
                    print(f'Error moving file {filename}: {e}')

    print("File organization complete!")

def main():
    print("Welcome to the File Organizer!\n\nThis program automatically sorts files in a folder into subfolders based on their file types, helping you keep your files organized.\n")

    # Get folder path from user and validate
    while True:
        folder_path = input("Enter the full path of the folder to organize: ")
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            break
        else:
            print("Invalid folder path. Please try again.\n")

    # Get custom mappings
    mapping = get_user_mappings()

    if not mapping:
        mapping = {
            '.pdf': 'PDFs',
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.png': 'Images',
            '.docx': 'Documents',
            '.txt': 'TextFiles',
        }
        print("\nNo custom mappings provided, using default mappings.")

    organize_files(folder_path, mapping)
    print("Task is complete.")

if __name__ == "__main__":
    main()


