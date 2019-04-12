pgbackup
========

Python 3.7 CLI for backing up remote PostgreSQL databases locally or to AWS S3

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Setup](#setup)
	- [Installation From Source](#installation-from-source)
	- [Setup a sample PostgreSQL DB](#setup-a-sample-postgresql-db)
	- [Preparing your Python Development Env](#preparing-your-python-development-env)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
	- [pgbackup - Running cli.py interactively to test parse_args](#pgbackup-running-clipy-interactively-to-test-parseargs)
	- [pgbackup - Running pgdump.py interactively to test local backup.](#pgbackup-running-pgdumppy-interactively-to-test-local-backup)
	- [pgbackup - Running storage.py interactively to test S3 backup.](#pgbackup-running-storagepy-interactively-to-test-s3-backup)
	- [pgbackup - Using pdb to troubleshoot in interactive mode](#pgbackup-using-pdb-to-troubleshoot-in-interactive-mode)
- [Python Packages](#python-packages)
	- [Python - Creating this Package](#python-creating-this-package)
	- [Python - Creating Deployable Install File](#python-creating-deployable-install-file)

<!-- /TOC -->
# Setup
Install this utility to backup your postgres data and setup your local environment so you can test and enhance as needed.

## Installation From Source

To install the package after you've cloned the repository:

```
$ cd ./pgbackup
$ pip install --user -e .
```

## Setup a sample PostgreSQL DB

You can use any PostgreSQL DB you have a route to.  If you want to do local development you can create one using these steps.


Make sure you have docker installed and access to the internet.  The db_setup.sh script will ask you to set db $POSTGRES_USER / $POSTGRES_PASSWORD, and defaults the $POSTGRES_DB='sample'.  It will import 1000 rows of sample data and setup the container to list on ports 80 and 5432
```
cd docker/scripts
./db_setup.sh
```

Test your connectivity with PostgreSQL client (psql)
```
psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:80/sample -c "SELECT count(id) FROM employees;"

count
-------
  1000
(1 row)
```
You can do this same test using a docker container if you dont have the client locally installed.

```
docker run -it --rm postgres psql postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MY_IP}:80/sample -c "SELECT count(id) FROM employees;"
```

## Preparing your Python Development Env

I'm doing most things inside a container to keep a clean system.  My custom python 3.7 container includes additional python dependencies, pip, pipenv, and awscli.  You can use the included Dockerfile to build/run this or install these things locally.

Follow these steps to start developing with this project:

1. Ensure `pip`, `pipenv`, and `awscli` are installed
2. Clone repository: `git clone https://github.com/ppresto/pgbackup.git`
3. `cd` into the repository (./pgbackup)
4. Setup pipenv for new project only: `pipenv --python python3.7`
4. Activate virtualenv: `pipenv shell`
5. Install dependencies from Pipfile.lock: `pipenv install`
6. (Optional) Install pgbackup CLI utility (from ./pgbackup): `pipenv install -e .`
  1. You may have already used pip to install this earlier.  THis will only install in your virtual env.

Verify the utility is available
```
pgbackup -h
```

# Usage

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

```
$ pgbackup postgres://dbadmin@example.com:5432/db1 --driver s3 dbadmin.bucket.for.backups
```

Local Example w/ local path:

```
$ pgbackup postgres://dbadmin@example.com:5432/db1 --driver local /var/local/db1/backups
```

# Troubleshooting

## pgbackup - Running cli.py interactively to test parse_args
```
cd ./pgbackup
python -i src/pgbackup/cli.py
parser = create_parser()
args = parser.parse_args(['https://some_url', '--driver', 's3', 'bucket_name'])
type(args)
args.url
args.driver
args.destination
parser.parse_args()
```
## pgbackup - Running pgdump.py interactively to test local backup.
```
cd ./pgbackup
PYTHONPATH=./src python
from pgbackup import pgdump
dump = pgdump.dump('postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${MY_IP}:80/sample')
f = open('dump.sql', 'w+b')
f.write(dump.stdout.read())
f.close()
```

## pgbackup - Running storage.py interactively to test S3 backup.
You should already have your ~/.aws/credentials properly setup,
with write access to your bucket_name.  Login to the console and look for a new backup file after this test.
```
cd ./pgbackup
PYTHONPATH=./src python
import boto3
from pgbackup import storage
client = boto3.client('s3')
infile = open('example.txt', 'rb')
storage.s3(client, infile, 'bucket_name', infile.name)
```

## pgbackup - Using pdb to troubleshoot in interactive mode
You can iterate every step of yourScript.py in interactive mode by running `python -m pdb yourScript.py`.  Because your in interactive mode you can output or assign values at every step to see what your code is doing making this a good troubleshooting process.

You can target specific loops and functions easily by including the library at the top of your script temporarily by adding:
`import pdb`

Then set the start of your trace by adding this line exactly where you want to be looking and save.
`pdb.set_trace()`

Run yourScript.py: `python -i yourScript.py`

Some helpful pdb commands:
```
h     # help
ll    # list script
n     # next
a     # print current function args
r     # continue until current function returns
q     # quit

```

# Python Packages
## Python - Creating this Package
```
cd ./pgbackup
mkdir -p src/pgbackup
vi setup.py # create package setup.py
touch src/pgbackup/__init__.py
touch src/pgbackup/.gitkeep
vi src/pgbackup/cli.py  # create initial CLI code.
vi src/pgbackup/pgdump.py
vi src/pgbackup/storage.py
vi README.md
```

## Python - Creating Deployable Install File

```
cd ./pgbackup
python setup.py bdist_wheel   #creates dist and build dirs
ls ./dist/pgbackup-0.1.0-py3-none-any.whl
```
Now we can install the pgbackup utility with pip from a local file or http:// if you have it hosted somewhere.

`pip install dist/pgbackup-0.1.0-py3-none-any.whl`
