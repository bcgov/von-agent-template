[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# von-agent-template
Template for a von-x based agent

# Getting Help or Reporting an Issue
To report bugs/issues/feature requests, please file an [issue](../../issues).

# How to Contribute
If you have found this project helpful, please contribute back to the project as you find new and better ways to use SonarQube in your projects.

If you would like to contribute, please see our [CONTRIBUTING](./CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). 
By participating in this project you agree to abide by its terms.

# HOWTO Build and Configure a Credential Issuer/Verifier using the VON-X Agent Template

## Setup (or connect to) an instance of TheOrgBook

T.B.D.

## Fork and Clone this repository

T.B.D.

## Configure your Local VON-X Agent Instance

1. Define the schema for the credential you intend to issue

von-x-agent/config/schemas.yml
von-x-agent/testdata/test.json

1a. Determine pre-requisites (proof requests)

T.B.D.

2. Configure the VON-X Agent UI

von-x-agent/config/services.yml
von-x-agent/config/routes.yml
von-x-agent/assets/img/tbd-logo-square.jpg

3. Configure other application settings

von-x-agent/config/settings.yml

4. Setup manage and Docker build scripts

docker/docker-compose.yml
docker/manage


## Run and Test Your VON-X Agent Instance

T.B.D.
