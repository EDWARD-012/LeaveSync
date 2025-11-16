from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import LeaveType, Company, WorkWeek, Holiday
from datetime import date

@receiver(post_migrate)
def create_default_data(sender, **kwargs):
    if sender.name != "core":
        return

    # 1. Leave Types
    defaults = [
        ("Casual Leave", 12),
        ("Sick Leave", 10),
        ("Earned Leave", 15),
    ]

    for name, days in defaults:
        LeaveType.objects.get_or_create(name=name, defaults={"default_allocation": days})

    # 2. Workweek
    for comp in Company.objects.all():
        WorkWeek.objects.get_or_create(company=comp, defaults={"working_days": [1,2,3,4,5]})

    # 3. Holidays
    fixed_holidays = [
        ("New Year’s Day", date(2025, 1, 1)),
        ("Republic Day", date(2025, 1, 26)),
        ("Independence Day", date(2025, 8, 15)),
        ("Gandhi Jayanti", date(2025, 10, 2)),
        ("Christmas Day", date(2025, 12, 25)),
        ("Holi", date(2025, 3, 14)),
        ("Good Friday", date(2025, 4, 18)),
        ("Eid al-Fitr", date(2025, 3, 31)),
        ("Eid al-Adha (Bakrid)", date(2025, 6, 7)),
        ("Raksha Bandhan", date(2025, 8, 9)),
        ("Janmashtami", date(2025, 8, 16)),
        ("Ganesh Chaturthi", date(2025, 8, 27)),
        ("Diwali", date(2025, 10, 20)),
    ]

    for comp in Company.objects.all():
        for name, d in fixed_holidays:
            Holiday.objects.get_or_create(
                company=comp,
                name=name,
                date=d,
                defaults={"recurring": True}
            )
