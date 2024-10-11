from django.utils.translation import gettext_lazy as _

# === GENERAL ===
# BUTTONS
SIGN_UP_BUTTON_TEXT = _('Sign up')
EDIT_BUTTON_TEXT = _('Edit')
DELETE_BUTTON_TEXT = _("Yes, Delete")
CREATE_BUTTON_TEXT = _('Create')

# MESSAGES
AUTHORIZATION_MESSAGE = _("You are not authorized! Please log in.")

# ----


# --- SETTINGS.PY ---
PASSWORD_VALIDATOR_MESSAGE = _("Your password must contain at least 3 characters.")

# ----


# === USERS ===
# -- TASK_MANAGER.USERS.VIEWS.PY -- TASK.MANAGER.VIEWS.PY --
# MESSAGES
PERMISSION_MESSAGE = _("""You do not have permission to change another user.""")

REGISTER_USER_SUCCESS_MESSAGE = _("User successfully registered")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
DELETE_USER_SUCCESS_MESSAGE = _("User deleted successfully")

LOGIN_SUCCESS_MESSAGE = _("You are logged in")
LOGOUT_INFO_MESSAGE = _("You are logged out")


# TITLES
USERS_LIST_TITLE_TEXT = _('Users')
SIGN_UP_TITLE_TEXT = _("Registration")
UPDATE_USER_TITLE_TEXT = _("Edit user")
DELETE_USER_TITLE_TEXT = _("Delete user")


# -- USERS FORMS.PY --
# LABELS
FIRST_NAME_LABEL_USER_FORM = _("First name")
LAST_NAME_LABEL_USER_FORM = _("Last name")
USERNAME_LABEL_USER_FORM = _("Username")
PASSWORD1_LABEL_USER_FORM = _("Password")
PASSWORD2_LABEL_USER_FORM = _("Password confirmation")

# HELP TEXTS
USERNAME_HELP_TEXT_USER_FORM = _("Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.")
PASSWORD1_HELP_TEXT_USER_FORM = _("Your password must contain at least 3 characters.")
PASSWORD2_HELP_TEXT_USER_FORM = _("To confirm, please enter your password again.")

# MESSAGES
USERNAME_VALIDATION_ERROR_MESSAGE_USER_FORM = _("A user with that username already exists.")

# ----


# === STATUSES ===
# -- TASK_MANAGER.STATUSES.VIEWS.PY --
CREATE_STATUS_TEXT = _('Create Status')

# MESSAGES
CREATE_STATUS_SUCCESS_MESSAGE = _('Status successfully created')
UPDATE_STATUS_SUCCESS_MESSAGE = _('Status successfully changed')
DELETE_STATUS_SUCCESS_MESSAGE = _('Status successfully deleted')


# TITLES
STATUSES_LIST_TITLE_TEXT = _('Statuses')
UPDATE_STATUS_TITLE_TEXT = _('Change Status')
DELETE_STATUS_TITLE_TEXT = _('Delete status')

# -- TASK_MANAGER.STATUSES.FORMS.PY --

# LABELS
NAME_LABEL_STATUS_FORM = _('Name')

# ----


# === TASKS ===
# -- TASK_MANAGER.TASKS.VIEWS.PY --
CREATE_TASK_TEXT = _('Create a task')

# TITLES
TASKS_LIST_TITLE_TEXT = _('Tasks')

# ----
