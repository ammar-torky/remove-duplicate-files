import os
import hashlib

def hash_file(file_path):
    """Generate SHA-1 hash for the file."""
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def remove_duplicates(folder_path):
    hashes = {}
    duplicates = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_hash = hash_file(file_path)
            if file_hash in hashes:
                duplicates.append(file_path)
            else:
                hashes[file_hash] = file_path

    for duplicate in duplicates:
        os.remove(duplicate)
        print(f"Removed: {duplicate}")

folder_path = r"D:\me\linux"  # استبدل هذا بالمسار الخاص بالفولدر
remove_duplicates(folder_path)
