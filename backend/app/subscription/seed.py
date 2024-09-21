from app.subscription.models import Plan


class Seeder:
    @staticmethod
    async def run():
        await Plan.first_or_create(filter=Plan.system_name == 'start')
        await Plan.first_or_create(filter=Plan.system_name == 'advanced')
        await Plan.first_or_create(filter=Plan.system_name == 'pro')


