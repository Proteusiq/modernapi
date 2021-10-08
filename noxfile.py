import nox


@nox.session
def clean_cache(session):

    session.run("rm", "-rf", "$(find ./mapi/**/*cache*)", external=True)
    session.run("rm", "-rf", "__pycache__", external=True)
