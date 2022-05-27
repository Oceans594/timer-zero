from inspect import signature

from bucket import BaseTask
from models import TaskMetaInfo
from wheel import SingleTimerWheel


class Task(BaseTask):
    def __init__(self, func, meta_info: TaskMetaInfo, params: tuple):
        super().__init__(func, meta_info, params)
        self.func = func
        self.meta_info = meta_info
        self.signature = signature(self.func)

    def run(self):
        print("="* 30)
        print(self.func, "\n", self.meta_info, "\n", self.signature)


wheel = SingleTimerWheel(tick=1000, interval=1000)


def test_func(param):
    print(param)


meta_info = TaskMetaInfo(
    delay_timestamp=3
)
task = Task(test_func, meta_info, ("测试",))

wheel.add_task(task, delay=3)
wheel.add_task(task, delay=4)
wheel.add_task(task, delay=5)


print(wheel.bucket)

# wheel.delete_task(task)

print(wheel.bucket)

wheel.turning()