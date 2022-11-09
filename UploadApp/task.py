from celery import shared_task
from time import sleep
from .models import Files
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def file_upload(self, files):
    progress_recorder = ProgressRecorder(self)
    n = len(files)
    print(n)
    for i in files:
        print('here')
        Files.objects.create (
            File = i
        )
        progress_recorder.set_progress(i+1, n, f'On iteration {i}')
    return None