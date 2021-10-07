from invoke import task


@task
def clear_cache(session):

    commands = [
        "rm -rf **/*cache",
        "rm -rf .cache",
        "rm -rf *cache*",
        "rm -rf *cache",
    ]

    for command in commands:
        print(f"Execute_ {command}")
        session.run(command, hide=True, warn=True)
