import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbv_dj_doc.settings")
django.setup()

from faker import Faker
from blog.models import Publisher, Author, Book

fake = Faker()


def publisher_dummy(n):
    for _ in range(n):
        data = {'name': fake.name(), 'address': fake.address(),
                'city': fake.city(), 'state_province': fake.state(),
                'country': fake.country(), 'website': fake.url()}
        Publisher.objects.create(**data)


def author_dummy(n):
    for _ in range(n):
        data = {'salutation': fake.name(), 'name': fake.name(),
                'email': fake.email(), }
        Author.objects.create(**data)


def book_dummy(n):
    for _ in range(n):
        a = Author.objects.all()
        author = random.choice(a)
        p = Publisher.objects.all()
        publi = random.choice(p)

        book = Book(title=fake.text(), publisher=publi, publication_date=fake.date())
        book.save()
        book.authors.add(author)


# author_dummy(10)
book_dummy(10)


"""
if name in ('first_name','firstname'): return lambda x: generator.firstName()
if name in ('last_name','lastname'): return lambda x: generator.lastName()
if name in ('username','login','nickname'): return lambda x:generator.userName()
if name in ('email','email_address'): return lambda x:generator.email()
if name in ('phone_number','phonenumber','phone'): return lambda x:generator.phoneNumber()
if name == 'address' : return lambda x:generator.address()
if name == 'city' : return lambda x: generator.city()
if name == 'streetaddress' : return lambda x: generator.streetaddress()
if name in ('postcode','zipcode'): return lambda x: generator.postcode()
if name == 'state' : return lambda x: generator.state()
if name == 'country' : return lambda x: generator.country()
if name == 'title' : return lambda x: generator.sentence()
if name in ('body','summary', 'description'): return lambda x: generator.text()
"""