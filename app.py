from flask import Flask, request, render_template

app = Flask(__name__)


# Главная страница (GET)
@app.route('/')
def index():
    return render_template('index.html'), 200, {'Content-Type': 'text/html'}


# Страница контактов: GET и POST
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Выводим в консоль
        print("=== Получены данные из POST-запроса ===")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")
        print("=====================================\n")

        # Возвращаем страницу с уведомлением об успехе
        return render_template('contacts.html', success=True), 200, {'Content-Type': 'text/html'}

    # GET-запрос: показать страницу контактов
    return render_template('contacts.html'), 200, {'Content-Type': 'text/html'}


# Явное использование контекстного менеджера with open (для демонстрации)
@app.route('/read-contacts')
def read_contacts():
    try:
        with open('templates/contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content, 200, {'Content-Type': 'text/html'}
    except FileNotFoundError:
        return "<h1>404</h1><p>Файл не найден</p>", 404, {'Content-Type': 'text/html'}


# Обработчик 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404, {'Content-Type': 'text/html'}


# Обработчик 500
@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500</h1><p>Внутренняя ошибка сервера</p>", 500, {'Content-Type': 'text/html'}


if __name__ == '__main__':
    app.run(debug=True)