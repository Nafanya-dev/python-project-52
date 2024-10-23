from enum import Enum


class Template(str, Enum):
    update_create = 'update_create_form.html'
    delete = 'delete_form.html'
