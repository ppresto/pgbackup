from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='patrick',
    author_email='pgpresto@gmail.com'
    description = 'A utility for backing up PostgreSQL db',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url='https://github.com/ppresto/pgbackup',
    packages=find_packages('src')
)
