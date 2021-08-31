Поднять проект docker-compose up -d --build

Протестировать бота:
docker-compose exec django bash
python manage.py shell_plus
from social_network.services.utils import start_bot
start_bot()
