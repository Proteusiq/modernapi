from invoke import task


@task
def clean_cache(session):
    for c in (
        "$(find ./mapi/**/__pycache__)",
        "$(find ./mapi/__pycache__)",
        "__pycache__",
    ):
        print(f"executing rm -rf {c!r}")
        result = session.run("rm -rf {c}", hide=True, warn=True)
        print(result.ok)


@task
def init_db(session):

    command = "PYTHONPATH=./mapi python mapi/database/configuration.py"
    print(f"executing {command!r}")
    result = session.run(command, hide=True, warn=True)
    print(f"{result.ok} - {result.stdout.splitlines()[-1]}")
    result = session.run("mv database.db mapi/database.db", hide=True, warn=True)
    print(result.ok)
