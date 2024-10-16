<h1>Task Manager</h1>

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nafanya-dev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Nafanya-dev/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8bc87c38c65db89213ea/test_coverage)](https://codeclimate.com/github/Nafanya-dev/python-project-52/test_coverage)

## About

A task management web application built with Python and Django framework. It allows you to set tasks, assign performers and change their statuses.
Registration and authentication are required to work with the system.
The project uses the Bootstrap framework.

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

#### PostgreSQL or SQLite

As database the PostgreSQL database system is being used. You need to install it first. You can download the ready-to-use package from [official website](https://www.postgresql.org/download/) or use apt:
```bash
>> sudo apt update
>> sudo apt install postgresql
```

Or

You can skip this step and use SQLite database locally.

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
SECRET_KEY={your secret key}
```
If you choose to use SQLite DBMS, do not add DATABASE_URL variable.

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
