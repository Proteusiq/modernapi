import nox


@nox.session
def clear_cache(session):

    commands = [
        "-find . -name '*.pyc' -exec rm -rf {}",
        "-find . -name '__pycache__' -exec rm -rf {}",
        "-find . -name 'Thumbs.db' -exec rm -rf {}",
        "-find . -name '*~' -exec rm -rf {}",
        "-rm -rf .cache",
    ]

    for command in commands:
        session.run(command.split(" "), external=True)
    # session.run("ls", "-lh", external=True)
