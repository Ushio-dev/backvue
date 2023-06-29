from app import app, contacts
import os


app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(port=os.environ['PORT'], debug=True)