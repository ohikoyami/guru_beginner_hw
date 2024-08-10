import zipfile
import os


def test_zip_file(add_in_zip_fixture, read_file_content_in_zip_fixture, delete_zip_fixture):
    # Переменная для общего сбора содержимого файлов
    content_files = []

    # Назвние для zip файла
    zip_file_name = 'zip_with_files.zip'

    # Список файлов, с которым мы работаем
    name_files = ['pdf.pdf', 'txt.txt', 'xlsx.xlsx']

    # Вызов добавления файлов в zip
    add_in_zip_fixture(zip_file_name, name_files)

    # Проверка корректности добавления файлов
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zip_content = zipf.namelist()
        assert zip_content.sort() == name_files.sort()

    # Проверка содержимого файлов относительно самих файлов
    for item in name_files:
        if item == 'txt.txt':
            content_txt = read_file_content_in_zip_fixture(zip_file_name, item)
            content_files.append(content_txt)
            assert content_txt == 'txt'
        elif item == 'pdf.pdf':
            content_pdf = read_file_content_in_zip_fixture(zip_file_name, item)
            content_files.append(content_pdf)
            assert content_pdf == 'pdf'
        else:
            content_xslx = read_file_content_in_zip_fixture(zip_file_name, item)
            content_files.append(content_xslx)
            assert content_xslx == 'xslx'

    # Общая проверка содержимого файлов без привязки к самим файлам (опционально)

    assert content_files == ['pdf', 'txt', 'xslx']

    delete_zip_fixture(zip_file_name)
