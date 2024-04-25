# define project metadata and dependencies, 
# and to specify how the project should be packaged 
# and distributed.

from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Text2EmojiPrediction',
    version='0.11',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=requirements,
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.md', '*.sh'],
    },
)