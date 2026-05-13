print('Hello from repository!')
from dotenv import load_dotenv
import os


from dotenv import load_dotenv
import os

def get_author():
    load_dotenv()  # Загружаем переменные из .env
    author = os.getenv("AUTHOR")  # Читаем значение переменной AUTHOR
    return author

# Вызов функции и вывод результата
author_name = get_author()
print(f"Автор проекта: {author_name}")
