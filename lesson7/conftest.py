import os
import zipfile

import pytest
from selene import browser


@pytest.fixture
# Добавление файлов в zip
def add_in_zip_fixture():
    def add_in_zip(zip_name, files):
        with zipfile.ZipFile(zip_name, 'a') as zip_write:
            for file in files:
                zip_write.write(file)

    return add_in_zip


@pytest.fixture
# Чтение содержимого файлов в zip с декодированием
def read_file_content_in_zip_fixture():
    def read_file_content_in_zip(zip_name, file):
        with zipfile.ZipFile(zip_name, 'r') as zip_read:
            with zip_read.open(file) as file:
                file_content = file.read()
                return file_content.decode('utf-8')

    return read_file_content_in_zip


@pytest.fixture
# Удаление zip файла
def delete_zip_fixture():
    def delete_zip(zip_name):
        os.remove(zip_name)

    return delete_zip
