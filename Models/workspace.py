workspace_list = []


def get_last_id():
    if workspace_list:
        last_workspace = workspace_list[-1]
    else:
        return 1
    return last_workspace + 1


class Workspace:

    def __init__(self, name, workspace_type):
        self.id = get_last_id()
        self.name = name
        self.workspace_type = workspace_type
        self.is_publish = False


@property
def data(self):
    return {
        'id': self.id,
        'name': self.name,
        'workspace_type': self.workspace_type
    }
