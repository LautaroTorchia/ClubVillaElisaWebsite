from pathlib import Path
from src.web import create_app


static_folder = Path(__file__).parent.joinpath("public")
app = create_app(static_folder=static_folder)


def main():
    app.run()


if __name__ == "__main__":
    main()
