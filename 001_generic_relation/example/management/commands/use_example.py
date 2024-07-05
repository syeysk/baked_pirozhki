from django.core.management.base import BaseCommand

from example.models import YourMain, YourFirst, YourSecond


class Command(BaseCommand):
    help = 'Show using the example'

    def handle(self, *args, **options):
        first = YourFirst.objects.create()
        second = YourSecond.objects.create()

        YourMain.objects.create(content_object=first)
        YourMain.objects.create(content_object=second)

        for main in YourMain.objects.all():
            self.stdout.write(str(main.content_object))
            self.stdout.write(str(main.first))
            self.stdout.write(str(main.second))

        self.stdout.write(str(YourMain.objects.filter(first__isnull=False).first().content_object))
        self.stdout.write(str(YourMain.objects.filter(second__isnull=False).first().content_object))

        YourMain.objects.all().delete()
        YourFirst.objects.all().delete()
        YourSecond.objects.all().delete()
