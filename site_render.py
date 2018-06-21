from staticjinja import make_site


context_index = {
    'user_name': 'Леонид Федорович',
    'wholesalers_number': 105,
    'producers_number': 25,
    'applications': [
        {
            'application_time': 'вчера, в 21:30',
            'application_description': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.',
            'customer_name': 'Алексей',
            'view_number': '12',
        }
    ]*4,
    'reviews': [
        {
            'reviewer_name': 'Кирилл, 29 лет, г. Барабинск',
            'review_text': 'Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер!',
        }
    ]*3
}

context_applications = {
    'user_name': 'Леонид Федорович',
    'applications': [
        {
            'application_time': 'вчера, в 21:30',
            'application_description': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.',
            'customer_name': 'Алексей',
            'view_number': '12',
        }
    ]*8
}


if __name__ == "__main__":
    site = make_site(
        contexts=[
            ('index.html', context_index),
            ('applications.html', context_applications)
        ],
        searchpath='templates/'
    )
    site.render()
