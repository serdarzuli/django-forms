# Django Forms Project

## 📌 Project Overview
This project is a Django-based web application that enables users to submit contact forms, including fields like email, username, and phone number. Additionally, an admin panel is provided for managing the submitted form data efficiently.

## 🚀 Features
- **User-friendly Contact Form**: Users can submit details such as name, email, and phone number.
- **Database Integration**: Stores submitted form data in a relational database.
- **Django Admin Panel**: Provides an interface to manage form submissions.
- **Form Validation**: Ensures valid data entry through Django's built-in validation system.
- **Responsive Design**: The form is designed to be accessible on various devices.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-forms.git
   cd django-forms
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 🖥️ Usage
- Open your browser and navigate to `http://127.0.0.1:8000/` to access the contact form.
- Go to `http://127.0.0.1:8000/admin/` to manage form submissions (log in with the superuser credentials you created).

## 📂 Project Structure
```
📦 django-forms
├── contactform/       # Contact form app
├── home/              # Main app with templates
├── db.sqlite3         # Database file
├── manage.py          # Django project manager
├── requirements.txt   # Required dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignored files
```

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to fork this repository and contribute! Pull requests are welcome.

## 📬 Contact
For any inquiries, reach out to:
📧 Email: serdar.zuli@gmail.com
🌐 Website: [www.thezuli.com](https://www.thezuli.com)

