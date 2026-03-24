from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            for obj in Activity.objects.all():
                obj.delete()
            for obj in Leaderboard.objects.all():
                obj.delete()
            for obj in Workout.objects.all():
                obj.delete()
            for obj in User.objects.all():
                obj.delete()
            for obj in Team.objects.all():
                obj.delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='marvel', description='Marvel Team')
            dc = Team.objects.create(name='dc', description='DC Team')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
            steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
            bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
            clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name)

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=tony, type='run', duration=30, date='2023-01-01')
            Activity.objects.create(user=steve, type='cycle', duration=45, date='2023-01-02')
            Activity.objects.create(user=bruce, type='swim', duration=60, date='2023-01-03')
            Activity.objects.create(user=clark, type='run', duration=50, date='2023-01-04')

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
            Workout.objects.create(name='Situps', description='Do situps', difficulty='medium')
            Workout.objects.create(name='Squats', description='Do squats', difficulty='hard')

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(team=marvel, points=200)
            Leaderboard.objects.create(team=dc, points=180)

            self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
