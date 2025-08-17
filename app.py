from flask import Flask, request, jsonify, render_template
from library import Library

app = Flask(__name__)
lib = Library()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    data = request.json
    try:
        lib.add_book(data["title"], data["author"], int(data["copies"]))
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/register_member", methods=["POST"])
def register_member():
    data = request.json
    try:
        lib.register_member(data["name"])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/borrow_book", methods=["POST"])
def borrow_book():
    data = request.json
    try:
        lib.borrow_book(data["member"], data["title"])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/return_book", methods=["POST"])
def return_book():
    data = request.json
    try:
        lib.return_book(data["member"], data["title"])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/list_books")
def list_books():
    books_list = [
        {"title": b.title, "author": b.author, "copies": b.copies}
        for b in lib.books.values()
    ]
    return jsonify(books_list)

if __name__ == "__main__":
    app.run(debug=True)
