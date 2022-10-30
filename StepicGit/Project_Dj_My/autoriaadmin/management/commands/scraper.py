from django.core.management.base import BaseCommand, CommandError

from autoriaadmin.parser import AutoParser

# создали команду. Проверить ее наличие можно python manage.py -h

class Command(BaseCommand):
    help = 'Парсинг авто'

    def handle(self, *args, **options):
        with open(r'C:\Users\User\PycharmProjects\StepicGit\Project_Dj_My'
                  r'\autoriaadmin\media\Files\model_auto.txt', 'r') as file:
            for mod in file:
                model = mod.replace('\n', '')
                print(model)

                try:
                    car = AutoParser(str(model))
                    car.main()
                except Exception as error:
                    raise CommandError('Ошибка парсинга', error)

        self.stdout.write(self.style.SUCCESS('Successfully parsed'))
