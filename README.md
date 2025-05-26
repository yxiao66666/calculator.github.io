# 🧮 Simple Calculator App (React + Flask)

This is a full-stack web application that performs basic arithmetic operations using a **React** frontend and a **Flask** backend API.

## 🔧 Features

- Perform addition, subtraction, multiplication, and division
- Built with React for the frontend and Flask for the backend
- Backend logic exposed via a simple REST API
- JSON communication between client and server
- CORS enabled for smooth frontend-backend interaction

---

## 📁 Project Structure

```
calculator-app/
├── frontend/                # React App (Calculator UI)
│   └── Calculator.js
├── backend/                 # Flask App (API)
│   └── server.py
└── README.md
```
---

## 🚀 Getting Started

### Prerequisites

- Node.js and npm
- Python 3.x
- `pip` for Python package management

---

### 🖥️ Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```
Runs on http://localhost:3000 by default

---

### 🧠 Backend Setup (Flask)
```bash
cd backend
pip install flask flask-cors
python server.py
```
Runs on http://localhost:5000

---

### 📡 API Endpoint
POST `/calculate`
Request Body (JSON):
```bash
{
  "num1": 10,
  "num2": 5,
  "operation": "plus"
}
```

Supported Operations:
- plus
- minus
- multiply
- divide

Response (JSON):
```bash
{
  "result": 15
}
```
---

### 🖼️ UI Preview
Yet to come.

---

### 📝 Notes
- Handles edge cases like division by zero
- Easy to extend with more operations or validation
- Modify the backend URL in Calculator.js if deploying

---

### 📃 License
This project is licensed under the MIT License. 

---

### 🙌 Acknowledgements
Built with ❤️ using React and Flask.

---

## Contributors
- [yxiao66666](https://www.linkedin.com/in/yxiao66666/) 
