import nox


@nox.session
def clean_cache(session):

    session.run("rm", "-rf", "$(find ./mapi/**/__pycache__)", external=True)
    session.run("rm", "-rf", "$(find ./mapi/__pycache__)", external=True)
    session.run("rm", "-rf", "__pycache__", external=True)
