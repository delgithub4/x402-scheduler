from jobs.payment_job import PaymentJob
from jobs.notify_job import NotifyJob
from jobs.analytics_job import AnalyticsJob
from jobs.cleanup_job import CleanupJob


class RegistryService:

    def __init__(self):

        self.jobs = [

            PaymentJob(),

            NotifyJob(),

            AnalyticsJob(),

            CleanupJob()

        ]

    def jobs_list(self):

        return [

            job.info()

            for job in self.jobs

        ]
