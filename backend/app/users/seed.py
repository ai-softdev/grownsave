from sqlalchemy import and_

from app.repository.models import Language
from app.users.auth import get_hashed_password
from app.users.models import Role, User


class Seeder:
    @staticmethod
    async def run():
        print('users seed start')
        await Language.first_or_create(filter=Language.code == 'ru', code="ru", name="Русский")
        await Language.first_or_create(filter=Language.code == 'uz', code="uz", name="Узбекский")
        await Language.first_or_create(filter=Language.code == 'en', code="en", name="Английский")

        admin_role = await Role.first_or_create(
            filter=Role.system_name == 'admin',
            system_name="admin")
        user_role = await Role.first_or_create(
            filter=Role.system_name == 'user', system_name="user")
        admin = await User.first_or_create(filter=User.email == 'admin@admin.com',
                                           role_id=admin_role.id,
                                           email='admin@admin.com',
                                           hashed_password=get_hashed_password("admin@admin.com"))
