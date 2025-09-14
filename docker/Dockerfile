ARG SOURCE_IMAGE=
ARG SOURCE_TAG=
FROM "${SOURCE_IMAGE}:${SOURCE_TAG}"

# Labels
ARG BUILD_DATE
ARG GIT_COMMIT
ARG VERSION
ENV BUILD_DATE=${BUILD_DATE}
ENV GIT_COMMIT=${GIT_COMMIT}
ENV VERSION=${VERSION}
LABEL maintainer="PMI"
# hadolint ignore=DL3053
LABEL build-date="${BUILD_DATE}"
# hadolint ignore=DL3055
LABEL git-commit="${GIT_COMMIT}"
# hadolint ignore=DL3056
LABEL version="${VERSION}"
LABEL description="Image for testing CI pipelines"

# Don't use PIP_EXTRA_INDEX_URL because it is found/used by default by pip
ARG PMI_PIP_INDEX_URL

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
VOLUME /app

# install dependencies (NOTE: this assumes Debian is underlying linux distro)
ARG DEBIAN_FRONTEND=noninteractive
# hadolint ignore=DL3015,DL3008
RUN apt-get update -yq --fix-missing \
 # temporary fix for debian release transition
 && sed -i '/deb http:\/\/security.debian.org\/debian-security stable-security main/d' /etc/apt/sources.list \
 && apt-get update -yq \
 && apt-get install -yq --no-install-recommends --reinstall \
    apt-transport-https \
    build-essential \
    ca-certificates \
    curl \
    git \
    gnupg \
    krb5-user \
    lsb-release \
    nano \
    unixodbc \
    unixodbc-dev \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Microsoft SQL connector prereqs
# Note: these apparently need to be distinct RUN steps
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
# hadolint ignore=DL3015,DL3008
RUN apt-get update \
 && ACCEPT_EULA=Y apt-get install -yq --no-install-recommends msodbcsql18 \
 && ACCEPT_EULA=Y apt-get install -yq --no-install-recommends mssql-tools18 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Add MSSQL stuff to path
ENV PATH="${PATH}:/opt/mssql-tools18/bin"


COPY requirements.txt /home/
RUN python3 -m pip install --quiet --no-cache-dir opencensus-ext-azure \
 && python3 -m pip install --quiet --no-cache-dir -r /home/requirements.txt \
 && python3 -m pip install --quiet --no-cache-dir --no-deps --index-url="${PIP_EXTRA_INDEX_URL}" \
    "pmi-dtsc-utilities>=1.0.0" \
 && python3 -m pip cache purge

# copy everything excluded from .dockerignore
COPY ././docker/host.json /home/site/wwwroot/host.json
COPY ././docker// /home/site/wwwroot//
COPY ./src/ /home/site/wwwroot/src/

# CMD []
# ENTRYPOINT []
