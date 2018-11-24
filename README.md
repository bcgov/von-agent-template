[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# von-agent-template
Template for a von-x based Indy agent. This generic template is intended to be used as a base code for setting up an Issuer or a Verifier components for Indy-based networks (i.e. Sovrin). Organizations that wish to issuer/verify certain types of credentials will add customization on top of the code base included in this repo. One von-x agent instance can support multiple types of credentials and in most cases an organization would only need to run a single  von-x agent to process all credential types they need. The von-x agent uses Docker containers to run and therefore load balancing and high availability for the agent would typically be delivered using capabilities of the container management platform that the organisation uses (i.e. OpenShift, IBM Cloud Private, etc). The steps below explain how to run a local instance of a von-x agent for development and testing purposes only.

# Getting Help or Reporting an Issue
To report bugs/issues/feature requests, please file an [issue](../../issues).

# How to Contribute
If you have found this project helpful, please contribute back to the project as you find new and better ways to use SonarQube in your projects.

If you would like to contribute, please see our [CONTRIBUTING](./CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). 
By participating in this project you agree to abide by its terms.

# HOWTO Build and Configure a Credential Issuer/Verifier using the VON-X Agent Template

## Setup a local instance of Indy network

A Credential Issuer is required to register their DID with (and publish a DID Doc to) a decentralized identity network ledger that uses the Hyperldger Indy technology. A Verifier would use the published DID of the Issuer to verify authenticity of the credential presented to them.

For testing purposes, it is recommended to run a local instance of an Indy network that is available in the bcgov/von-network repo. A complete how-to for running an instance of von-network is available [here](https://github.com/bcgov/von-network). High level steps to  run a local instance of von-network are as follows:

```
$ git clone https://github.com/bcgov/von-network.git
$ cd von-network
$ ./manage build
$ ./manage start
```

Open `http://localhost:9000` to access the web UI for the network and browse data on the ledger.

<sub><sup>NOTE: Since it is a test instance, all data published to the ledger is not persisted. If you kill the `start` process, all published data will be lost and all DIDs will need to be re-registered again. To start from a clean slate , always run `./manage rm` (a couple of times) to remove previously started Docker containers and then rebuild using `./manage build` before starting the von-network again `./manage start`.</sup></sub>

## Setup a local instance of TheOrgBook

TheOrgBook is an instance of an Indy Enterprise Wallet (with web UI and API interface) that can be used to simulate the receiving end when issuing credentials from a von-x Agent instance.  The how-to for running a local instance of TheOrgBook is available [here] (https://github.com/bcgov/TheOrgBook/blob/master/README.md)

However, the steps to run a local TheOrgBook instance are:

```
$ git clone https://github.com/bcgov/TheOrgBook.git
$ cd TheOrgBook/docker
$ ./manage build
$ ./manage start seed=<my seed>
```

... where <my seed> is a unique 32-character string

If all goes well, a local instance of TheOrgBook will be available at `http://localhost:8080` (web UI) and `http://localhost:8081` (API endpoints)

**Make sure von-network is up and running BEFORE you start TheOrgBook.**

## Fork and Clone this repository

On GitHub, navigate to the bcgov/von-agent-template. 
In the top-right corner of the page, click Fork.

In your favourite cli, clone YOUR FORK of the repo:

```
$ git clone https://github.com/YOUR_GITHUB_USERNAME/von-agent-template.git
```

Add the bcgov/von-agent-template repo as upstream to have access to the latest updates.

```
$ git remote add upstream https://github.com/bcgov/von-agent-template.git
```

Run the commands below to pull changes from the main repo to your fork and to your local repo:

```
$ git fetch upstream
$ git merge upstream/master master
$ git push
```

To push the changes from the local repo to your fork:

```$ git add .
$ git commit -m "YOUR COMMENT"
$ git push
```

<sub><sup>NOTE: If you wish to contribute back to the main bcgov repo, submit a Pull Request on the GitHub page of your fork repo. Always include a description of the proposed changes in the Pull Request and make sure the changes can merge successfully with the master branch of the main repo. Refer to [CONTRIBUTING](./CONTRIBUTING.md) guidelines for a complete set of intstructions.</sup></sub>


## Run and Test Your local VON-X Agent Instance

Check out configurations of other von-x agents like [bcgov/BC Registry](https://github.com/bcgov/von-bc-registries-agent/tree/master/bcreg-x/config) and [ongov/Ontario Business Registry](https://github.com/weiiv/onbis-x) to help you get started.

Verify and configure application settings.  The defaults should work but you may need to change depending on your local environment:

```
von-x-agent/config/settings.yml
```

**Make sure that both von-network and TheOrgBook are up and running BEFORE you start VON-X Agent.**

```
$ cd YOUR_LOCAL_REPO/docker/
$ ./manage build
$ ./manage start
```

Open a browser at http://localhost:9000/ and verify that your local ledger browser home page loads.

Open a browser at http://localhost:8080/ and verify that TheOrgBook home page loads.

First create a sample organization based on some pre-set test data:

Open a web service client (such as PostMan) and POST the test data at `YOUR_LOCAL_REPO/von-x-agent/testdata/test.json` to http://localhost:5001/myorg/issue-credential.  The response should include a series of responses similar to the following:

```
{
    "success": true,
    "result": "f93adc90-9cbf-48a1-971a-926c3724260d",
    "served_by": "7a8dabb4a3c3"
}
```

In your TheOrgBook browser instance, refresh the home page (should increment the counts under Current Statistics) and search for "Bob".  Navigate to the organization page for "Bob's Burgers".

Next create a new organization of your own choosing:

Open a web browser and navigate to http://localhost:5001/myorg/incorporation.  Fill in the form values (leave expiry_date empty) and submit.  Verify there are no errors.

Now return to yout TheOrgBook browser instance and search for the organization name you just created.  It should be available with a single credential.  Make a note of the Organization Id (something like "3fcb0d9e-3d3a-4be5-83f2-0c8f29eb6df2") - you will need to copy this value for subsequent web requests.

Navigate to "http://localhost:5001/myorg/tax?org_id=<your org id>" (use the value from the previous step).  Note that the org id and org name are automatically populated - this is from the dependant proof request.  Fill in the required values and submit.

Now return to yout TheOrgBook browser instance and search for this organization again.  There should now be two credentials.

Repeat the above steps with:

```
http://localhost:5001/myorg/liquor?org_id=<your org id>
http://localhost:5001/myorg/myorg-credential?org_id=<your org id>
```


## Create a new VON-X Agent Schema

Check out configurations of other von-x agents like [bcgov/BC Registry](https://github.com/bcgov/von-bc-registries-agent/tree/master/bcreg-x/config) and [ongov/Ontario Business Registry](https://github.com/weiiv/onbis-x) to help you get started.

1. Define the schema for the credential you intend to issue

```
von-x-agent/config/schemas.yml
von-x-agent/testdata/test.json
```

1a. Determine pre-requisites (proof requests)

T.B.D.

2. Configure the VON-X Agent UI

```von-x-agent/config/services.yml
von-x-agent/config/routes.yml
von-x-agent/assets/img/tbd-logo-square.jpg
```

HTML templates are located in von-x-agent/templates.  This application uses Jinja2 templates: http://jinja.pocoo.org/docs/2.10/.

3. Configure other application settings

```
von-x-agent/config/settings.yml
```

4. Setup manage and Docker build scripts

```
docker/docker-compose.yml
docker/manage
```

## Updating Your local VON-X Agent Instance

To test code changes, kill the running instance:

```
./manage stop
./manage build
./manage start
```
