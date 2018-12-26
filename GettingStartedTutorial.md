# VON Agent Getting Started Tutorial

This Getting Started guide is to get someone new to VON Agents up and running with a VON Agent in about an hour.  We assume that if you are here, you have some background in the goals and purpose of the Verifiable Organizations Network (VON), OrgBook and Issuer/Verifier Agents.  If this is new to you, please learn more at https://vonx.io. On that site, we recommend the overview in the "About"section, and especially the Webinar linked at the top. 

## Table of Contents

- [VON Agent Getting Started Tutorial](#von-agent-getting-started-tutorial)
  - [Table of Contents](#table-of-contents)
  - [Running in your Browser or on Local Machine](#running-in-your-browser-or-on-local-machine)
  - [Prerequisites](#prerequisites)
    - [In Browser](#in-browser)
    - [Local Machine](#local-machine)
  - [VON Network Setup](#von-network-setup)
    - [In Browser](#in-browser-1)
    - [Local Machine](#local-machine-1)
  - [Step 1: Looking At What's Already Started](#step-1-looking-at-whats-already-started)
  - [Step 2: Get your VON-Agent Running](#step-2-get-your-von-agent-running)
  - [Step 3: Review the Configuration Files](#step-3-review-the-configuration-files)
    - [File: schemas.yml](#file-schemasyml)
    - [File: settings.yml](#file-settingsyml)
    - [File: routes.yml](#file-routesyml)
    - [File: services.yml](#file-servicesyml)
  - [Step 4: Issuing a Credential using dFlow](#step-4-issuing-a-credential-using-dflow)
  - [Step 5: Issuing a Credential using a JSON File](#step-5-issuing-a-credential-using-a-json-file)
  - [Step 7: Customizing your Credential](#step-7-customizing-your-credential)
  - [Step 8: Adding a second, multi-cardinality Credential](#step-8-adding-a-second-multi-cardinality-credential)

## Running in your Browser or on Local Machine

This guide can be run from within a browser, or if you are more technically inclined, you can run it on your local machine using Docker. In the following sections, there are sub-sections for `In Browser` and `Local Machine`, depending on how you want to run the guide. If you will be going from here to setting up a new VON agent instance for your organization might want to use the `Local Machine` path.

## Prerequisites

### In Browser

The only prequisite (other than a browser) is an account with [Docker Hub](https://hub.docker.com). Docker Hub is the "Play Store" for the [Docker](https://docker.com) ecosystem.

### Local Machine

To run this guide on your local machine, you must have the following installed:

* Docker - Community Edition is fine.
  * If you do not already have Docker installed, go to [the Docker installation page](https://docs.docker.com/install/#supported-platforms) and click the link for your platform.
* Docker Compose
  * Instructions for installing docker-compose on a variety of platforms can be found [here](https://docs.docker.com/compose/install/).
* git
  * [This link](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) provides installation instructions for Mac, Linux (including if you are running Linux using VirtualBox) and native Windows (without VirtualBox).
* a bash shell
  * bash is the default shell for Mac and Linux.
  * On Windows, the git-bash version of the bash shell is installed with git and it works well. You **must** use bash to run the guide - PowerShell or Cmd will not work.
* curl
  * An optional step in the guide uses the utility `curl`.
  * curl is included on Mac and Linux.
  * Instructions for installing curl on Windows can be found [here](https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows).

## VON Network Setup

### In Browser

Go to the [Play with Docker](https://labs.play-with-docker.com/) and (if necessary) click the login button. *Play With Docker* is operated by Docker to support developers learning to use Docker.

> If you want to learn more about the `Play with Docker` environment, look at the [About](https://training.play-with-docker.com/about/) and the Docker related tutorials at the Docker Labs [Training Site](https://training.play-with-docker.com). It's all great stuff created by the Docker Community. Kudos!

Click the "Start" button to start a Docker sandbox you can use to run the demo, and then click `+Add an Instance` to start a terminal in your browser. You have an instance of a Linux container running and have a bash command line.  We won't need to use the command line until Step 2 of this tutorial.

From time to time in the Steps of the Guide we'll ask you to edit files. There are two ways to do that in this environment.

- If you are comfortable with the `vi` editor, you can just use that. If you don't know `vi`, don't try it. It's a little scary.
- Alternatively, there is an `Editor` link near the top of the screen. Click that and you get a list of files in your home directory, and clicking a file will open it in an editor.  You will probably need to expand the editor window to see the file. Make the changes in the editor and click the "Save" button.
  - Don't forget to click the "Save" button.

The following URLs are used in the steps below for the different components:

- The `von-network` URL - [http://138.197.138.255/](http://138.197.138.255/). You'll see a Ledger Browser UI showing 4 nodes up and running (blue circles).
- The `TheOrgBook` URL  - [https://demo.orgbook.gov.bc.ca](https://demo.orgbook.gov.bc.ca) - You'll see the OrgBook interface with companies/credentials already loaded.
- The `permitify` URL - [https://dflow.orgbook.gov.bc.ca](https://dflow.orgbook.gov.bc.ca). You'll see the dFlow interface, with the "Credential" drop down having a list of at least the 7 "dflow" Credential types, and perhaps (many) more.

You can open those sites now or later. They'll be referenced by name (e.g. "The von-network URL...") in the guide steps.

### Local Machine

On a local machine upon which the prerequistes are setup, we will be installing and starting, in order, instances of [von-network](https://github.com/bcgov/von-network), [TheOrgBook](https://github.com/bcgov/TheOrgBook) and [dFlow (currently called Permitify)](https://github.com/bcgov/permitify).

Quick setup guides are available in the respective repos for getting each component for running locally. Here is a quick'n'dirty summary of the steps if you are daring. Repeat with the indicated adjustments for each component.

```
# Start in the folder you keep your repos
$ git clone https://github.com/bcgov/von-network.git  # Replace von-network with "TheOrgBook" and "permitify" for the latter two
$ cd von-network      # For TheOrgBook and Permitify - cd into the "docker" folder
$ ./manage build
$ ./manage up         # For TheOrgBook run: ./manage up seed=the_org_book_0000000000000000000
```

> **NOTE** the command to bring up TheOrgBook **must** be `./manage up seed=the_org_book_0000000000000000000`.

On the start of each, you will see the container logs running.  Let them run for awhile, watch for errors (stack traces) and once they stablize, verify the component is running before starting the next one. To verify each go to:

- The `von-network` URL - [http://localhost:9000](http://localhost:9000). You should see a Ledger Browser UI showing 4 nodes up and running (blue circles).
- The `TheOrgBook` URL  - [http://localhost:8080](http://localhost:8080). You should see the OrgBook interface with no companies/credentials loaded.
  - The URL for the api for `TheOrgBook` is running at [http://localhost:8081](http://localhost:8081)
- The `permitify` URL - [http://localhost:5000](http://localhost:5000). You should see the dFlow interface, with the "Credential" drop down having a list of 7 Credential types.
  - If you see some, but not all of the Credential types, wait and refresh your browser until all 7 are listed (Worksafe should be the bottom one).

> **NOTE**: In the Guide steps below, use the `localhost` URLs above when the components are referenced generically (e.g. TheOrgBook URL).

After verifying the current component, go back to the bash command line, hit `Ctrl-C` to stop the logs display, and move on to start the next component or finish.

When you want to bring down the instances, `cd` to the folder where the `./manage` script resides for each component and run `./manage down`. That will stop the instances and remove the persistence (docker volumes) so that you can start another clean run.

## Step 1: Looking At What's Already Started

> To Do: Add details to this section

- Ledger Browser
- TheOrgBook
- Permitify - get a Credential
- TheOrgBook - review the Credential

## Step 2: Get your VON-Agent Running

In this step, we'll get an instance of the VON Issuer/Verifier Agent running and issuing Credentials. The steps are the same whether you are running `In Browser` or `Local Machine`, starting from the home directory (`In Browser`) or in the folder where you store your cloned repos (`Local Machine`).

Clone the repo, and run the initialization script.

```
# Start in folder with repos (Local Machine) or home directory (In Browser)
$ git clone https://github.com/bcgov/von-agent-template
$ cd von-agent-template
$ ./init.sh  # And follow the prompts
```

The init script does a number of things:

1. Prompts for some names to use for your basic Agent.
2. Prompts for whether you are running with Play With Docker or locally and sets some variables accordingly.
3. Registers a DID for you on the Ledger that you are using.
4. Shows you the lines that were changed in the Agent configuration files - in [von-x-agent/config](von-x-agent/config)

The initial Agent you have created issues one Credential - using the name you gave it, with a handful of claims - Permit ID, Permit Type, etc. That Credential depends on the applying Organization already having the dFlow "Registration" credential. Without already having that Credential, an applying organization won't be able to get your Agent's credential.

To start your agent, run through these steps:

```
cd docker   # Assumes you were already in the root of the cloned repo
./manage build
./manage start
```

After the last command, you will see a stream of logging commands as the Agent starts up. The logging should stabilize with an "Indy sync complete" entry.

To verify your agent is running:

1. Go to the `Agent URL`, where you should see a "404" (not found) error message. That signals the Agent is running, but does not respond to that route.
   1. For In Browser, click the "5001" link at the top of the screen. That's the path to your Agent.
   2. For `Local Machine`, go to [http://localhost:5001](http://localhost:5001).
2. Go to the `dFlow URL` (in browser, local) where in the Credential drop down, you should be able to see your Agent's Credential.
   1. The Credential dropdown box is a search box, so just type the name of your organization or credential in it.

All good?  Whoohoo!

## Step 3: Review the Configuration Files

Your Agent is configured using the YAML files in the [von-x-agent/config](von-x-agent/config) folder in this repo. Let's take a look at the files in that folder. If you browse the files in your installation, you'll see the `./init.sh` updates you made to the names.

In this step, we'll quickly review the current files to get a feel for them. No need to learn all the details - when the time comes, documentation for the files can be found in the [VON Agent Configuration Guide](von-x-agent/config/ConfigurationGuide.md). 

### File: [schemas.yml](von-x-agent/config/schemas.yml)

`schemas.yml` holds the list of Credentials to be issued by the Agent. In this repo, the file starts with just a single Credential.  The file includes the following pieces of information:

- A few pieces of metadata about the schema (version, name, description, the HTTP path for the Credential).
- Some specific information used by TheOrgBook to control behaviour when a Credential is issued (topic, cardinality, effective date). More about this information later.
- An optional proof request that must be satisfied before this Credential can be issued.
- The list of attributes (claims) that can (or must) be populated in the Credential.

### File: [settings.yml](von-x-agent/config/settings.yml)

This is the most obvious of the files - a list of environment variables that must be set appropriately to run the Agent. Of course the values change with each environment (e.g. Local, In Browser, Dev, Test and Prod), so managing the file does get interesting.

> You won't have to touch this file in this Guide.

### File: [routes.yml](von-x-agent/config/routes.yml)

This file configures the Web Server routes for the API and Web Forms that are used in the application. The Agent Web Forms are unlikely ever to be used in a production instance of the VON-Agent, but the form is super useful for testing. It enables the display of dynamic form (based on the claim names and attributes) so that a user can fill in the fields for a Credential.  There should be a "form" section for each Credential, containing the following information: 

- Form metadata, including the URL for the form, the credential schema upon which it is based, titles to display, a form template to use, etc.
- A reference to a proof request.
  - If a proof request is included, on loading, the form contacts TheOrgBook to process the proof request.
- A list of the attributes to be displayed on the form.
  - If a proof request is executed before displaying the form, like named fields from the proof request will be pre-populated.
- A list of the attributes that are auto-populated with specific values - e.g. uuids, literals or the current date.

### File: [services.yml](von-x-agent/config/services.yml)

The fourth file, `services.yml` is the least obvious of the files. It's primary purpose is to provide information to the TheOrgBook about the Issuer Organization and issued the Credentials. The following sections are in the file:

- The "issuers" section has information about the Issuers and the issued Credentials
  - Metadata about the Issuer - name, website, email contact, logo etc.
  - Configuration information about the Agent's Wallet/database.
  - A section about each issued Credential type. Additional detail is given below about this section.
- A "verifiers" section with information about the connection to TheOrgBook for verifying Proof Requests.
- A "proof-requests" section with details about the proof-requests upon which the issued Credentials depend.

The "Credentials" provides information for TheOrgBook to process a newly issued credential. Specifically:

- "topic" is the attribute that links an Issued credential with the Organization that is the subject of the Credential.
- "cardinality_fields" tells TheOrgBook what to do when the additional instances of a Credential Type is received for an Organization.
  - Notably, should the previous version by marked as "revoked" or can multiple instances of the Credential be active at the same time.
- "mappings" tell TheOrgBook what attributes in the Credential should be added to which of TheOrgBook's Search indices.
  - TheOrgBook has search indices for Names, Addresses, Dates, Attributes, and Credential Types.
  - TheOrgBook does not "know" the structure of any Credential, so the Issuer must tell TheOrgBook which of the attributes are searchable in what way.

We'll see how these work later in this Guide.

Enough with the configurations - let's get on with issueing credentials.

## Step 4: Issuing a Credential using dFlow

Now let's use some techniques to trigger your agent to issue a credential to the OrgBook so that you can look at it.  We'll start with the easiest way - using dFlow.

Go to the `dFlow URL` (local, in browser) and select your Credential as the target Credential you want to be issued. In the Company field, either leave it blank or select a company that you created in Step 1. Click `Begin` and you should see a dFlow with the dFlow "Registration" as the first Credential, and your Agent's Credential as the second. Go through the process to collect each Credential, to make sure everything is working.

Go into OrgBook (in browser, local), search for the company and review it's credentials. It should now have the first ever Credential issued by your Agent.  Cool! If you want, go back and try to issue a few more credentials.

Good stuff. You have a working Agent that issues a basic Credential.

## Step 5: Issuing a Credential using a JSON File

Now that we have seen how a user can trigger the issuance of a Verifiable Credential via a Web form, let's look at how an app can issue a one via an API call. In most production cases, Verifiable Credentials will be issued using the API - an existing backend application for a Service will be adjusted so that when a permit or licence is issued or updated, an "issue Verifiable Credential" API call is made with the Credential data passed in a chunk of JSON. Let's see how that works.

> **NOTE:** If you are running this using the "Local Machine" approach - make sure that you have curl installed. At the command just run "curl" and see if the command is found. If not, see the prerequisites for how you can install it.

Rememeber that your credential is set up to depend on a dFlow Registration credential. To populate the JSTON structure, we need to get some information from an existing Registration credential. Recall one that you have already issued (or issue a new one using dFlow), and then find it in the OrgBook on a screen where you can see the  Registration ID and the Legal Name of the company. Recall that in the dFlow run we did previously, those fields came from the Proof Request. In this case, we're not going to do the Proof Request, so we need to (correctly!) populate them in the JSON for the API call.

The JSON File we're going to submit is in the `von-agent-template` repo, in the `von-x-agent/testdata` folder. Edit that file and the following changes:

- set the "corp_num" field to the "Registration ID" field from OrgBook
- set the "legal_name" field to the legal name of the company from OrgBook.
- change "my-permit" and "my-organization" in the "schema" name to the permit and organization fields that you entered when you initialized the settings.
- as you want - update any of the other data elements, making sure that you retain the JSON structure.

Save your file and then, from the root folder of the `von-agent-template`, execute this command REPLACING "my-organization" with the name of your organization:

```
$ curl -vX POST http://$ENDPOINT_HOST/my-organization/issue-credential -d @von-x-agent/testdata/sample_permit.json --header "Content-Type: application/json"
```

You should see the results from the `curl` command with an HTTP response of `200` (success) and 

- checking the results

## Step 7: Customizing your Credential

- Adding/changing fields
- Changing dependencies

## Step 8: Adding a second, multi-cardinality Credential

- Adding a second dependent credential with an Address and Address type
- Adding multiple instances of the credential