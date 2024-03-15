from Controller import Controller


class App:
    def __init__(self):
        app = Controller()
        app.view.main()


if __name__ == "__main__":
    App()
