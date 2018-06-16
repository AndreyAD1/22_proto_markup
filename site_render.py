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
        },
        {
            'application_time': 'вчера, в 21:30',
            'application_description': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.',
            'customer_name': 'Алексей',
            'view_number': '12',
        },
        {
            'application_time': 'вчера, в 21:30',
            'application_description': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.',
            'customer_name': 'Алексей',
            'view_number': '12',
        },
        {
            'application_time': 'вчера, в 21:30',
            'application_description': '60 шт. ПК от 72-15 до ПК 21-15, Криводановка, с доставкой.',
            'customer_name': 'Алексей',
            'view_number': '12',
        }
    ],
    'reviews': [
        {
            'reviewer_name': 'Кирилл, 29 лет, г. Барабинск',
            'review_text': 'Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер!',
        },
        {
            'reviewer_name': 'Кирилл, 29 лет, г. Барабинск',
            'review_text': 'Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер!',
        },
        {
            'reviewer_name': 'Кирилл, 29 лет, г. Барабинск',
            'review_text': 'Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер! Бла-бла, мне помогло, все супер!',
        }
    ]
}


if __name__ == "__main__":
    site = make_site(contexts=[('index.html', context_index)], searchpath='static/templates')
    # enable automatic reloading
    site.render()
