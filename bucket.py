from inspect import signature

from models import TaskMetaInfo


class BaseTask(object):
    def __init__(self, func, meta_info: TaskMetaInfo, params: tuple):
        self.func = func
        self.meta_info = meta_info
        self.signature = signature(self.func)

    def run(self):
        raise NotImplementedError

