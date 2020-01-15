import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_requirements(req_file):
    """ Detect deployment constraints (e.g. heroku slug size) and compile requirements
        to suit those constraints """
    requirements = []
    dependency_links = []
    lines = read(req_file).split("\n")
    for line in lines:
        if line.startswith("git+"):
            dependency_links.append(line)
        elif line.startswith("-e "):
            dependency_links.append(line.replace("-e ", ""))
        else:
            requirements.append(line)
    return requirements, dependency_links
    return [req for req in read(req_file).split("\n")]

if os.environ.get("HEROKU"):
    core_reqs = get_requirements("requirements_slim.txt")
else:
    core_reqs = get_requirements("requirements.txt")

setup(
    install_requires=core_reqs
)
