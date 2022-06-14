import os
import sys
import hashlib


# get all md5 value of files
def file_hash(file_path):
    hasher = hashlib.md5()

    try:
        with open(file_path, 'rb') as open_file:
            content = open_file.read()
            hasher.update(content)

            return hasher.hexdigest()

    except OSError as error:
        print('could not read/open: ', error)


# search for all files inside given folder
def scan_file_system(path):
    all_files = {}
    count = 0

    try:
        for root, dir, files in os.walk(path):
            for name in files:
                all_files[count] = {
                    'name': name,
                    'path': os.path.join(root, name),
                    'MD5': file_hash(os.path.join(root, name))
                }

                count += 1

    except OSError as error:
        print("error: ", error)

    if all_files:
        return all_files
    else:
        print('No files were found in given path.'
              ' Please start program with different path')
        sys.exit(0)
