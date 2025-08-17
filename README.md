# 📚 Mini Library System with Pytest

A simple **Python-based library management system** with tests written in **pytest**.  
This project was built for practicing **unit testing, boundary testing, error handling, and object-oriented design**.

---

## 🚀 Features
- Add books and members
- Borrow and return books
- Prevent negative copies
- Limit members to max 3 borrowed books
- Raise clear errors for missing books or members
- Full pytest coverage with different test cases

---

## 📂 Project Structure
library_web/
│
├── library.py # Core library logic (OOP classes: Book, Member, Library)
├── test_library.py # Pytest test cases
├── app.py # Flask backend (optional - web version)
├── templates/
│ └── index.html # HTML frontend
└── static/
├── style.css # CSS styling
└── script.js # JS for interactivity

1. Clone the repo:
   ```bash
   git clone https://github.com/GivenTerbulance/library-system-test.git
   cd library_system
2. Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
   pip install pytest flask
   
🌐 Running the Web Version

Start the Flask backend:

python app.py


Open in your browser:
http://127.0.0.1:5000

🧪 Test Cases

Borrow a book successfully

Borrow when no copies available → raises ValueError

Member tries to borrow more than 3 books → blocked

Returning a book increases copies

Borrowing a missing book/member raises error

🎯 Learning Goals

Practice object-oriented programming

Apply unit testing & pytest

Understand boundary testing & error handling

Explore how the same logic could extend to a web app (Flask + HTML/CSS/JS)

📌 Next Steps

Add database support (SQLite)

Expand frontend

Add more advanced tests (integration, mocks)

👨‍💻 Author: [Given Teboho Ikaneng]
