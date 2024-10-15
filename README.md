<h1>Task Manager</h1>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nafanya-dev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Nafanya-dev/python-project-52/actions)


## About

A task management web application built with Python and Django framework. It allows you to set tasks, assign performers and change their statuses.
Registration and authentication are required to work with the system.
To provide users with a convenient, adaptive, modern interface, the project uses the Bootstrap framework.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

#### The demo version is available on Render platform: [https://task-manager-1esk.onrender.com](https://task-manager-1esk.onrender.com)

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.10 or higher installed:

```bash
>> python --version
Python 3.10+
```
#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### PostgreSQL

As database the PostgreSQL database system is being used. You need to install it first. You can download the ready-to-use package from [official website](https://www.postgresql.org/download/) or use apt:
```bash
>> sudo apt update
>> sudo apt install postgresql
```

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/Nafanya-dev/python-project-52.git && cd python-project-52
```

Then you have to install all necessary dependencies:

```bash
>> make install
```

Create `.env` file in the root folder and add following variables:
```dotenv
DATABASE_URL=postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY={your secret key} # Django will refuse to start if SECRET_KEY is not set
```

To create the necessary tables in the database, start the migration process:
```bash
>> make migrate
```

---

## Usage

Start the Gunicorn Web-server by running:

```shell
>> make start
```

By default, the server will be available at http://127.0.0.0:8000.
