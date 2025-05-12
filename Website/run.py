from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Получаем порт из переменной окружения, если она есть, иначе по умолчанию используем порт 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Запускаем приложение на всех интерфейсах (0.0.0.0) с заданным портом
    app.run(debug=True, host='0.0.0.0', port=port)

