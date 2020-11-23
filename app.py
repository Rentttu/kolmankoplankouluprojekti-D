from flask import Flask
from flask_restful import Api

from resources.workspace import WorkspaceListResource, WorkspaceResource, WorkspacePublishResource

app = Flask(__name__)
api = Api(app)

api.add_resource(WorkspaceListResource, '/workspaces')
api.add_resource(WorkspaceResource, '/workspaces/<int:workspace_id>')
api.add_resource(WorkspacePublishResource, '/workspaces/<int:workspace_id>/publish')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
