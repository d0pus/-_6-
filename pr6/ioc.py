from abc import ABC, abstractmethod

class TimeSourceInterface(ABC):
    @abstractmethod
    def get_time(self) -> str:
        pass
class CurrentTimeSource(TimeSourceInterface):
    def get_time(self) -> str:
        return "Текущее время"

class ConfiguredTimeSource(TimeSourceInterface):
    def __init__(self, time_str: str):
        self.time_str = time_str

    def get_time(self) -> str:
        return self.time_str

class ExternalServiceTimeSource(TimeSourceInterface):
    def get_time(self) -> str:
        return "Время от внешнего сервиса"
class TaskRunner:
    def __init__(self, time_source: TimeSourceInterface):
        self.time_source = time_source

    def run_task(self):
        print(f"Задача выполняется в {self.time_source.get_time()}")
task_runner_with_current_time = TaskRunner(CurrentTimeSource())
task_runner_with_configured_time = TaskRun-ner(ConfiguredTimeSource("12:00"))
task_runner_with_external_service_time = TaskRun-ner(ExternalServiceTimeSource())

task_runner_with_current_time.run_task()
task_runner_with_configured_time.run_task()
task_runner_with_external_service_time.run_task()
