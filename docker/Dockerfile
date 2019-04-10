FROM python:3.7-stretch

# extra dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		tk-dev \
		uuid-dev \
		wget \
		build-essential \
		libffi-dev \
		libgdbm-dev \
		libc6-dev \
		libssl-dev \
		zlib1g-dev \
		libbz2-dev \
		libreadline-dev \
		libsqlite3-dev \
		libncurses5-dev \
		libncursesw5-dev \
		xz-utils \
		libgdbm-dev \
		&& rm -rf /var/lib/apt/lists/*

# Install postgresql client
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> /etc/apt/sources.list.d/pgdg.list \
		&& apt-get update && apt-get install -y --no-install-recommends --allow-unauthenticated postgresql-client \
		&& rm -rf /var/lib/apt/lists/*

# Install pipenv and awscli tools
RUN pip install awscli pipenv

# Add Profiles for custom command line and vimrc
COPY bashrc /root/.bashrc
COPY vimrc /root/.vimrc
