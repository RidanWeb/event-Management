import os
import random
import django
from faker import Faker

# Set up Django environment — replace 'event_management' with your actual project directory name if different
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_management.settings")
django.setup()

# Import your newly designed models (replace 'events_app' with your actual app name)
from events.models import Category, Event, Participant


def populate_db():
    fake = Faker()

    # 1. Create Categories
    category_names = [
        "AI & ML",
        "Web Dev",
        "Cybersecurity",
        "Cloud Computing",
        "DevOps",
    ]
    categories = []
    for name in category_names:
        category, created = Category.objects.get_or_create(
            name=name, defaults={"description": fake.paragraph()}
        )
        categories.append(category)
    print(f"Created/Found {len(categories)} categories.")

    # 2. Create Events
    events = []
    for _ in range(15):
        event = Event.objects.create(
            category=random.choice(categories),
            name=f"{fake.catch_phrase()} Summit",
            description=fake.paragraph(nb_sentences=3),
            date=fake.date_this_year(before_today=False, after_today=True),
            time=fake.time(),
            location=f"{fake.city()} Main Hall {random.choice(['A', 'B', 'C'])}",
        )
        events.append(event)
    print(f"Created {len(events)} events.")

    # 3. Create Participants & Assign to Events
    participants = []
    for _ in range(30):
        participant = Participant.objects.create(
            name=fake.name(), email=fake.unique.email()
        )
        # Randomly assign 1 to 4 events to each participant
        assigned_events = random.sample(events, random.randint(1, 4))
        participant.events.set(assigned_events)
        participants.append(participant)

    print(f"Created {len(participants)} participants and assigned to events.")
    print("Database populated successfully!")


if __name__ == "__main__":
    populate_db()