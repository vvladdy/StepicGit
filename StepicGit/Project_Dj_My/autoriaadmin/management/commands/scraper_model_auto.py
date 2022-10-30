from django.core.management.base import BaseCommand, CommandError

from autoriaadmin.parser_model import main

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            main()
        except Exception as error:
            raise CommandError('Ошибка парсинга', error)
