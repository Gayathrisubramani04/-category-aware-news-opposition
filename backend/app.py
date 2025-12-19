import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from __init__ import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000)
