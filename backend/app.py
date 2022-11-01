from flask import Flask
import git  # GitPython library

app = Flask(__name__)


# Route for the GitHub webhook
@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./club-flask')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200

@app.route('/')
def index():
    return 'flask es una mierda'

if __name__ == '__main__':
    app.run()
