pgbackup
========

Python CLI for backing up remote PostgreSQL databases locally or to AWS S3.

## Usage

Pass in a full database URL, the storage driver, and destination.

* S3 Example w/ bucket name:

```
$ pgbackup postgres://dbadmin@example.com:5432/db1 --driver s3 dbadmin.bucket.for.backups
```

* Local Example w/ local path:

```
$ pgbackup postgres://dbadmin@example.com:5432/db1 --driver local /var/local/db1/backups
```

## Installation From Source

To install the package after you've cloned the repository:

```
$ cd ./pgbackup
$ pip install --user -e .
```

## Preparing your Python Development Env

I'm doing most things inside my docker container to keep my system clean.  My custom python 3.7 container includes additional python dependencies, pip, pipenv, and awscli.  You can use this or install these things locally.

Follow these steps to start developing with this project:

1. Ensure `pip`, `pipenv`, and `awscli` are installed
2. Clone repository: `git clone git@github.com:ppresto/pgbackup`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`

## Setting up a sample PostgreSQL DB

Build
