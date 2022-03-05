from invoke import task, watchers


class Watcher(watchers.StreamWatcher):                                 
    def __init__(self):                                                         
        super().__init__()                                                      
        self.len = 0                                                            
                                                                                
    def submit(self, stream):                                                   
        new = stream[self.len:]                                                 
        print(new, end='')                                                      
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
        print(f"executing rm -rf {c!r}")
        result = session.run(f"rm -rf {c}", hide=True, warn=True)
        print(result.ok)


@task
def init_db(session):

    command = "PYTHONPATH=./mapi python mapi/database/configuration.py"
    print(f"executing {command!r}")
    result = session.run(command, hide=True, warn=True)

    try:
        output = result.stdout.splitlines()[-1]
    except IndexError:
        output = result.stdout.splitlines()
    print(f"{result.ok} - {output}")
    result = session.run("mv database.db mapi/database.db", hide=True, warn=True)
    print(result.ok)


@task(pre=[init_db], post=[clean_start])
def app(session):

    watcher = Watcher()
    command = "cd mapi && uvicorn main:app --reload"
    session.run(command, hide=True, warn=True, pty=True, watchers=[watcher])

    
