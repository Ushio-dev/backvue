from .app.app import app
from contacts import contacts
import os
from dotenv import load_dotenv

load_dotenv()


app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(port=os.getenv("PORT"), debug=True)