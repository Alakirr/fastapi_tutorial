from fastapi import FastAPI, Path
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse

# print('Hi, body!')
app = FastAPI()

'''
Далее в терминале запускаем следующую команду:
uvicorn main:app --reload
- - - - - - - - - - - - - - - - - - -
uvicorn - веб-сервер, который будет обслуживать наше приложение
main - название файла (этого файла)
app - название класса (см. строчку выше)
- - - - - - - - - - - - - - - - - - -
После запуска строчки выше в терминале,
мы создали веб-сервис на локальном сервере.
Вот его адрес: 
http://127.0.0.1:8000 
- - - - - - - - - - - - - - - - - - -
В FastAPI аннотация типов является реальным фильтром,
т.е. работает жесткая типизация!
- - - - - - - - - - - - - - - - - - -
Ссылка на репозиторий по данному проекту на GitHib:
https://github.com/Alakirr/fastapi_tutorial.git
'''

@app.get('/') # декоратор, который будет обслуживать метод get, который обрабатывает http запрос (вместо / можно написать адрес локального хоста)
def root():
    return {'message':'Hello, student!'}

@app.get('/add')
def add(x: int, y: int) -> int:
    return x + y

@app.get('/double/{number}')
def double(number: int) -> int:
    return number * 2

@app.get('/welcome/{name}')
def welcome(name: str = Path(min_length=2, max_length=20)) -> str:
    return f'Good luck, {name}!'

# вариант с двумя переменными
# @app.get('/welcome/{name}/{surname}')
# def welcome(name: str = Path(min_length=2, max_length=20), surname: str = Path(min_length=2, max_length=20)) -> str:
#     return f'Good luck, {surname} {name}!'


@app.get('/phone/{number}')
def phone_number(number: str = Path(regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')):
    return {'phone': number}


@app.get('/text')
def get_text():
    content = 'Здоровки, братюни!'
    return PlainTextResponse(content=content)

# @app.get('/html')
# def get_html():
#     content = '<h2>HTML!!!</h2>'
#     return HTMLResponse(content=content)

@app.get('/file')
def get_file():
    content = 'index.html'
    return FileResponse(content, media_type='application/octet-stream', filename='index_2.html')


@app.get('/html', response_class=HTMLResponse)
def get_html():
    content = '<h2>HTML!!!</h2>'
    return content