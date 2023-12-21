import sys
from app import App

WIDTH = 500
HEIGHT = 450

def main():
    try:
        app = App(WIDTH, HEIGHT)
        app.run()
    except Exception as error:
        sys.exit(error.args)


if __name__ == "__main__":
    main()
