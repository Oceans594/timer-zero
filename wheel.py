import time
from datetime import datetime
from typing import Dict, List, Union

from bucket import BaseTask


class BaseTimerWheelClass:
    def __init__(self):
        self.current_time = self.get_current_time()  # 当前时间
        self.tick: int = 1  # 时间跨度
        self.interval: int = 1000  # 总跨度/时间格数
        self.bucket: Dict[int, List[BaseTask]] = {t: [] for t in range(0, self.interval)}  # 存储桶

    @staticmethod
    def get_current_time():
        return int(time.time() * 1000)

    def add_task(self, task: BaseTask, *, delay: Union[int, datetime] = None):
        current_tick = self.get_current_time()
        bucket_index = 0
        if isinstance(delay, int):
            bucket_index = (current_tick + delay) % self.interval

        if isinstance(delay, datetime):
            bucket_index = int(delay.timestamp() * 1000) % self.interval

        self.bucket[bucket_index].append(task)

    def delete_task(self, task: BaseTask):
        for k, v in self.bucket.copy().items():
            for bucket_task in v:
                if bucket_task == task:
                    self.bucket[k].remove(bucket_task)

    def turning(self):
        while True:
            self.current_time = self.get_current_time()
            task_list = self.bucket[self.current_time % self.interval]
            if len(task_list) > 0:
                self._run_tasks(task_list)
                self.bucket[self.current_time % self.interval] = []

    @staticmethod
    def _run_tasks(tasks: List[BaseTask]):
        for task in tasks:
            task.run()



class SingleTimerWheel(BaseTimerWheelClass):
    def __init__(self, tick=1, interval=1000):
        super(SingleTimerWheel).__init__()
        self.current_time = self.get_current_time()
        self.tick: int = tick
        self.interval = interval
        self.bucket: Dict[int, List[BaseTask]] = {t: [] for t in range(0, self.interval)}  # 存储桶
