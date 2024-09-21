from app.subscription.models import Plan


class Seeder:
    @staticmethod
    async def run():
        await Plan.first_or_create(filter=Plan.system_name == 'start',
                                   name="Базовый",
                                   price=5,
                                   system_name="start",
                                   with_ai=False,
                                   with_indicator=False,
                                   )
        await Plan.first_or_create(filter=Plan.system_name == 'advanced',
                                   name="Продвинутый",
                                   price=15,
                                   system_name="advanced",
                                   with_ai=True,
                                   with_indicator=False,
                                   )
        await Plan.first_or_create(filter=Plan.system_name == 'pro',
                                   name="Профессиональный",
                                   price=25,
                                   system_name="pro",
                                   with_ai=True,
                                   with_indicator=False,
                                   )
