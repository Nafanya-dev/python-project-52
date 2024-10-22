from django.utils.translation import gettext_lazy as _


PERMISSION_MESSAGE = _("""You do not have permission to change another user.""")
REGISTER_USER_SUCCESS_MESSAGE = _("User successfully registered")
UPDATE_USER_SUCCESS_MESSAGE = _("User successfully changed")
DELETE_USER_SUCCESS_MESSAGE = _("User deleted successfully")
DELETE_USER_PROTECT_MESSAGE = _('Cannot delete user because it is in use')

USERS_LIST_TITLE_TEXT = _('Users')
SIGN_UP_TITLE_TEXT = _("Registration")
UPDATE_USER_TITLE_TEXT = _("Edit user")
DELETE_USER_TITLE_TEXT = _("Delete user")
