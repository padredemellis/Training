"""
Es el punto de entrada para ejecutar la aplicación HBnB.
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)