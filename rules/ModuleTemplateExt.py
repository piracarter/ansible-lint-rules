from ansiblelint import AnsibleLintRule
import os

class ModuleTemplateExt(AnsibleLintRule):
    id = 'E402'
    shortdesc = "Template file should has '.j2' extention"
    description = ''
    tags = ['module']

    def matchtask(self, file, task):
        if task['action']['module'] != 'template':
            return False
        ext = os.path.splitext(task['action']['src'])
        if ext[1] != ".j2":
            return True
        return False