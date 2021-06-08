from django.apps import AppConfig

class NewspaperConfig(AppConfig):
    name = 'NewsPaper'
    #def ready(self):
     #   from . import jobs
        #jobs.schedule.every(3).minutes.do(jobs.job)