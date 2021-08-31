Поднять проект docker-compose up -d --build

Протестировать бота:
1.docker-compose exec django bash

2.python manage.py shell_plus

3.from social_network.services.utils import start_bot

4.start_bot()
