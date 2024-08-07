import zipfile
import os


def test_zip_file():

    # Добавление файлов в zip
    def add_in_zip(zip_name, files):
        with zipfile.ZipFile(zip_name, 'a') as zip_write:
            for file in files:
                if os.path.isfile(file):
                    zip_write.write(file, os.path.basename(file))
                else:
                    print(f'Файл {file} не является файлом или не существует')

    # Чтение содержимого файлов в zip с декодированием
    def read_file_in_zip(zip_name, file):
        with zipfile.ZipFile(zip_name, 'r') as zip_read:
            with zip_read.open(file) as file:
                file_content = file.read()
                return file_content.decode('utf-8')

    # Переменная для общего сбора содержимого файлов
    content_files = ''

    # Назвние для zip файла
    zip_file_name = 'zip_with_files.zip'

    # Список файлов, с которым мы работаем
    name_files = ['pdf.pdf', 'txt.txt', 'xlsx.xlsx']

    # Вызов добавления файлов в zip
    add_in_zip(zip_file_name, name_files)

    # Проверка корректности добавления файлов
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zip_content = zipf.namelist()
        assert zip_content.sort() == name_files.sort()

    # Проверка содержимого файлов относительно самих файлов
    for item in name_files:
        if item == 'txt.txt':
            content_txt = read_file_in_zip(zip_file_name, item)
            content_files = f"{content_txt} " + content_files
            assert content_txt == 'txt'
        elif item == 'pdf.pdf':
            content_pdf = read_file_in_zip(zip_file_name, item)
            content_files = f"{content_pdf} " + content_files
            assert content_pdf == 'pdf'
        else:
            content_xslx = read_file_in_zip(zip_file_name, item)
            content_files = f"{content_xslx} " + content_files
            assert content_xslx == 'xslx'

    # Общая проверка содержимого файлов без привязки к самим файлам (опционально)
    content_files = sorted(content_files.split())
    assert content_files == ['pdf', 'txt', 'xslx']

    os.remove(zip_file_name)