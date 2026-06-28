from services.registry_service import RegistryService


class SchedulerService:

    def __init__(self):

        self.registry = RegistryService()

    def overview(self):

        return {

            "jobs": self.registry.jobs_list()

        }
