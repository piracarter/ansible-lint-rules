from ansiblelint import AnsibleLintRule

class ShellAltPatch(AnsibleLintRule):
    id = 'TWSH008'
    shortdesc = 'Use patch module'
    description = ''
    tags = ['shell']

    def matchtask(self, file, task):
        if task['action']['module'] not in ['shell', 'command']:
            return False
        if 'patch' in task['action']['module_arguments']:
            return True
        return False