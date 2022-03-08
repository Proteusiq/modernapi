# -*- coding: utf-8 -*-
from invoke import task, watchers
from mapi.settings.lazylogger import logger


class Watcher(watchers.StreamWatcher):
    def __init__(self):
        super().__init__()
        self.len = 0

    def submit(self, stream):
        new = stream[self.len :]
        logger.info(new, end="")
        self.len = len(stream)
        return []


@task
def clean_start(session):
    for c in (
        "$(find ./mapi/**/__pycache__)",
        "$(find ./mapi/__pycache__)",
        "__pycache__",
        # "./mapi/*.db"
    ):
        logger.info(f"executing rm -rf {c!r}")
        result = session.run(f"rm -rf {c}", hide=True, warn=True)
        logger.info(result.ok)


@task(post=[clean_start])
def app(session):

    watcher = Watcher()
    command = "cd mapi && uvicorn main:app --reload"
    session.run(command, hide=True, warn=True, pty=True, watchers=[watcher])
