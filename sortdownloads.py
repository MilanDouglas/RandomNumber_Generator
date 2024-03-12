import os

file_path = 'C:/Users/Malan.Douglas/Downloads/ENROLMENT FORMS 2024-signed.PDF'


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("This file does NOT exist")


delete_file(file_path)