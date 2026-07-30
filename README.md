# Corporate Asset Management System

A web-based Corporate Asset Management System developed using Django. This system helps organizations manage company assets, employees, maintenance records, asset assignments, and employee requests.

---

## Features

- User Authentication (Login & Logout)
- Role-Based Access Control
- Dashboard
- Employee Management
- Department & Designation Management
- Asset Management
- Asset Assignment & Return
- Maintenance Management
- Employee Asset Requests
- Reports Dashboard
- CSV Export
- Search Functionality
- Bootstrap Responsive UI

---

## Technology Stack

- Python 3
- Django 6
- SQLite3
- Bootstrap 5
- HTML5
- CSS3

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Fatema-Keya/CorporateAssetManagementSystem.git
```

### 2. Go to the Project Directory

```bash
cd CorporateAssetManagementSystem
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Now open:

```
http://127.0.0.1:8000/
```

---

## Default User Roles

### Administrator

- Full System Access
- Reports
- User Management
- Maintenance
- Asset Management

### Staff

- Employee Management
- Asset Management
- Maintenance
- Employee Requests

### Employee

- Dashboard
- Submit Asset Requests

---

## Project Structure

```
accounts/
assets/
employees/
maintenance/
requests_app/
reports/
dashboard/
utils/
templates/
static/
config/
```

---

## Author

**Fatema Akter Keya**

Junior Django Developer