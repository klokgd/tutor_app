import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    if re.match('[Hh+][Ee+][Ll+][Pp+]', subj):
        return True

    return False

a = is_stressful('H E L P')
print(a)
