import os

from app import create_app

app = create_app(os.getenv('PY_ENV') or 'dev')


def run():
    app.run()


if __name__ == "__main__":
    run()
