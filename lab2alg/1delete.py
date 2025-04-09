import os

def delete_specific_txt_files():
    # Список файлов, которые нужно удалить
    files_to_delete = [
        'sorted_books.txt',
        'decrypted_message.txt',
        'hanoi_result.txt',
        'grouped_characters.txt',
        'grouped_numbers.txt',
        'reversed_lines.txt'
    ]
    
    # Проходим по списку файлов и удаляем каждый
    for filename in files_to_delete:
        if os.path.exists(filename):  # Проверяем, существует ли файл
            try:
                os.remove(filename)  # Удаление файла
                print(f"Файл {filename} удалён.")
            except Exception as e:
                print(f"Не удалось удалить файл {filename}: {e}")
        else:
            print(f"Файл {filename} не существует.")

# Вызов функции для удаления конкретных файлов
delete_specific_txt_files()
