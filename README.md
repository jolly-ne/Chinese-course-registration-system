# Contact Form Web Application (Flask + MySQL)

A simple contact form web application built using **HTML with internal CSS**, **Python (Flask)**, and **MySQL**.
The project allows users to submit their contact details and message, which are securely stored in a database and viewed through an admin page.

---

## 📌 Project Features

* Contact form to collect:

  * Name
  * Email address
  * Message
* Glassmorphism-inspired UI design
* Internal CSS styling (no external frameworks)
* Server-side processing using Flask
* Secure storage of data in MySQL database
* Input validation (client-side and server-side)
* Admin page to view submitted messages
* Uses XAMPP as the database server
* Beginner-friendly project structure

---

## 🎨 User Interface Design

The UI uses a **glassmorphism design style**, which includes:

* Semi-transparent containers and form elements
* Blurred background effects using `backdrop-filter`
* Rounded corners for inputs and buttons
* High-contrast white text for readability

This improves the overall user experience and visual appeal.

---

## 🛠️ Technologies Used

* **Frontend:**

  * HTML5
  * Internal CSS

* **Backend:**

  * Python
  * Flask Framework

* **Database:**

  * MySQL

* **Server:**

  * XAMPP (Apache & MySQL)

* **Version Control:**

  * Git & GitHub

---

## 📂 Project Structure

```
contact-form-flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── contact.html
│   └── admin.html
```

---

## 🗄️ Database Structure

**Database Name:** `contact_db`

**Table:** `contacts`

| Column     | Type                              |
| ---------- | --------------------------------- |
| id         | INT (Primary Key, Auto Increment) |
| name       | VARCHAR(100)                      |
| email      | VARCHAR(100)                      |
| message    | TEXT                              |
| created_at | TIMESTAMP                         |

---

## ▶️ How to Run the Project

1. Start **Apache** and **MySQL** from the XAMPP Control Panel
2. Create the database `contact_db` and table `contacts` in phpMyAdmin
3. Install dependencies:

   ```bash
   pip install flask mysql-connector-python
   ```
4. Run the Flask application:

   ```bash
   python app.py
   ```
5. Open the application in your browser:

   ```
   http://127.0.0.1:5000/
   ```
6. Access the admin page:

   ```
   http://127.0.0.1:5000/admin
   ```

---

## 🔐 Validation & Security

* Required field validation on all inputs
* Email format validation
* Parameterized SQL queries to prevent SQL injection
* POST method used for form submission

---

## 📈 Future Improvements

* Admin authentication (login system)
* Ability to delete or reply to messages
* Pagination for admin messages
* Email notifications
* Improved accessibility support

---

## 👤 Author

**J C**

---

## 📄 License

This project is for educational purposes.
