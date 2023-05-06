# Учебный проект api_yamdb
## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
#### Технологии
Python 3.9
Django 2.2.19
## Установка и запуск
- Клонировать репозиторий и перейти в него в командной строке:
git clone git@github.com:lilchiken/api_yamdb.git
cd api_yamdb
- Установите и активируйте виртуальное окружение
python3 -m venv env или python -m venv venv
Если у вас Linux/macOS
source env/bin/activate
Если у вас windows
source venv/scripts/activate
python -m pip install --upgrade pip
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Документация к API проекта Yatube (v1)

К проекту подключен REDOC: http://127.0.0.1:8000/redoc/
Там вы можете ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода.

## Авторы
- Илья Андрюхин lilchiken
- Михаил Матвеев Matf2six
- Никита Истомин itsqntz
