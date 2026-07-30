# Corporate Asset Management System

A web-based Corporate Asset Management System built with Django.

## Features

- User Authentication
- Role Based Access Control
- Dashboard
- Employee Management
- Department Management
- Designation Management
- Asset Management
- Asset Assignment
- Asset Return
- Maintenance Management
- Employee Asset Requests
- Reports Dashboard
- CSV Export
- Search
- Status Badges
- Bootstrap Responsive UI

---

## Technology Stack

- Python 3.14
- Django 6
- SQLite3
- Bootstrap 5
- HTML5
- CSS3

---

## User Roles

### Administrator

- Full Access
- Reports
- User Management
- System Management

### Staff

- Employees
- Assets
- Assignments
- Maintenance

### Employee

- Dashboard
- Submit Asset Requests

---

## Installation

Clone Repository

```bash
git clone https://github.com/Fatema-Keya/CorporateAssetManagementSystem.git
```

Go to Project

```bash
cd CorporateAssetManagementSystem
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

---

## Project Structure

```
accounts/
employees/
assets/
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

## Screenshots

- Login
- Dashboard
- Employee Management
- Asset Management
- Reports Dashboard

(Add screenshots later)

---

## Author

Fatema Akter Keya

Junior Django Developer
