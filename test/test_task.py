from inspect import signature

from bucket import BaseTask
from models import TaskMetaInfo


class Task(BaseTask):
    def __init__(self, func, meta_info: TaskMetaInfo, params: tuple):
        super().__init__(func, meta_info, params)
        self.func = func
        self.meta_info = meta_info
        self.signature = signature(self.func)

    def run(self):
        print(self.func, self.meta_info, self.signature)


def test_func(param):
    print(param)


if __name__ == '__main__':
    meta_info = TaskMetaInfo(
        delay_timestamp=3
    )
    task = Task(test_func, meta_info, ("测试",))
    task.run()
