from starlette_admin.contrib.sqla import Admin, ModelView

from .db import engine
from .models import User

admin = Admin(
    engine,
    title="FastAPI HTMX Admin",
)


class UserView(ModelView):
    sortable_fields = ["id", "role", "is_active"]


admin.add_view(UserView(User))
