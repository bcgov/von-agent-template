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
  - [Step 3: Issuing a Credential using dFlow](#step-3-issuing-a-credential-using-dflow)
  - [Step 4: Issuing a Credential directly using the Agent Form](#step-4-issuing-a-credential-directly-using-the-agent-form)
  - [Step 5: Issuing a Credential using a JSON File](#step-5-issuing-a-credential-using-a-json-file)
  - [Step 6: Customizing your Credential](#step-6-customizing-your-credential)
  - [Step 7: Adding a second, multi-cardinality Credential](#step-7-adding-a-second-multi-cardinality-credential)

## Running in your Browser or on Local Machine

This guide can be run from within a browser, or if you are more technically inclined, you can run it on your local machine using Docker. In the following sections, there are sub-sections for `In Browser` and `Local Machine`, depending on how you want to run the guide.

This guide is aimed at both technical and non-technical audiences and provides two paths through parts of the process. Most people that want to quickly learn the concepts and components should use the `In Browser` path of the tutorial. Technical folks that will go from here to creating a new VON agent instance for their organization might want to use the `Local Machine` path.

## Prerequisites

### In Browser

The only prequisite (other than a browser) is an account with [Docker Hub](https://hub.docker.com). Docker Hub is the "Play Store" for the [Docker](https://docker.com) ecosystem.

### Local Machine

To run this guide on your local machine, you must have the following installed:

* Docker, including Docker Compose - Community Edition is fine.
  * If you do not already have Docker installed, go to [this link](https://docs.docker.com/install/#supported-platforms) and then click the link for the installation instructions for your platform.
  * Instructions for installing docker-compose for a variety of platforms can be found [here](https://docs.docker.com/compose/install/).
* git
  * [This link](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) provides installation instructions for Mac, Linux (including if you are running Linux using VirtualBox) and native Windows (without VirtualBox).
* a bash shell
  * bash is the default shell for Mac and Linux.
  * On Windows, the git-bash version of the bash shell is installed with git. You must use bash to run the guide - PowerShell or Cmd will not work.
* curl
  * An optional step in the guide uses the utility `curl`.
  * curl is included on Mac and Linux.
  * Instructions for installing curl on Windows can be found [here](https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows).

## VON Network Setup

### In Browser

Go to the [Play with Docker](https://labs.play-with-docker.com/) and (if necessary) login. This site is operated by Docker to support developers learning about Docker.

> If you want to learn more about the `Play with Docker` environment, look at the [About](https://training.play-with-docker.com/about/) and the Docker related tutorials at the Docker Labs [Training Site](https://training.play-with-docker.com). It's all great stuff created by the Docker Community. Kudos!

Click the "Start" button to start a Docker sandbox you can use to run the demo, and then click the `+Add an Instance` link to start a terminal in your browser.

At this point, you have an instance of a Linux container running.  We won't need that until Step 2 of this tutorial, so you can now go ahead to Step 1.

In the following steps, we'll ask you to edit files. There are two ways to do that in this environment.

- If you are comfortable with the `vi` editor, you can just use that.
- Alternatively, there is an `Editor` link near the top of the screen. Click that and you get a list of files in your home directory, and clicking a file will open it in an editor.  You will probably need to expand the editor window to see the file. Make the changes in the editor and click the "Save" button.
  - Don't forget to click the "Save" button.

The following are the URLs that will be used in the steps below for the different components:

- The `von-network` URL - [http://138.197.138.255/](http://138.197.138.255/). You'll see a Ledger Browser UI showing 4 nodes up and running (blue circles).
- The `TheOrgBook` URL  - [https://demo.orgbook.gov.bc.ca](https://demo.orgbook.gov.bc.ca) - You'll see the OrgBook interface with companies/credentials already loaded.
- The `permitify` URL - [https://dflow.orgbook.gov.bc.ca](https://dflow.orgbook.gov.bc.ca). You'll see the dFlow interface, with the "Credential" drop down having a list of at least the 7 "dflow" Credential types, and perhaps (many) more.

### Local Machine

On a local machine, you must install and start, in order, [von-network](https://github.com/bcgov/von-network), [TheOrgBook](https://github.com/bcgov/TheOrgBook) and [dFlow (currently called Permitify)](https://github.com/bcgov/permitify).

Quick setup guides are available for getting each component for running locally here is a quick'n'dirty summary of the steps:

```
# Start in the folder you keep your repos
$ git clone https://github.com/bcgov/von-network.git  # Replace von-network with "TheOrgBook" and "permitify" for the latter two
$ cd von-network      # For TheOrgBook and Permitify - cd into the "docker" folder
$ ./manage build
$ ./manage up         # For TheOrgBook run: ./manage up seed=the_org_book_0000000000000000000
```

**NOTE** the command to bring up TheOrgBook **must** be `./manage up seed=the_org_book_0000000000000000000`.

On the start of each, you will see the container logs running.  Let them run for awhile, watch for errors (stack traces) and once they stablize, verify the component is running before starting the next one. To verify each go to:

- The `von-network` URL - [http://localhost:9000](http://localhost:9000). You should see a Ledger Browser UI showing 4 nodes up and running (blue circles).
- The `TheOrgBook` URL  - [http://localhost:8080](http://localhost:8080). You should see the OrgBook interface with no companies/credentials loaded.
  - The URL for the api for `TheOrgBook` is running at [http://localhost:8081](http://localhost:8081)
- The `permitify` URL - [http://localhost:5000](http://localhost:5000). You should see the dFlow interface, with the "Credential" drop down having a list of 7 Credential types.
  - If you see some, but not all of the Credential types, wait and refresh the browser until all 7 are listed (Worksafe should be the bottom one).

**NOTE**: In the steps later in this guide, use the `localhost` URLs above when the components are referenced generically (e.g. TheOrgBook URL).

After verifying each component, go back to the bash command line, hit `Ctrl-C` to stop the logs display, and move on to start the next component or finish.

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

## Step 3: Issuing a Credential using dFlow

Now let's use some techniques to trigger your agent to issue a credential to the OrgBook so that you can look at it.

Go to the `dFlow URL` (local, in browser) and select your Credential as the target Credential you want to be issued. In the Company field, either leave it blank or select a company that you created in Step 1. Click `Begin` and you should see a dFlow with the dFlow "Registration" as the first Credential, and your Agent's Credential as the second. Go through the process to collect each Credential, to make sure everything is working.

Go into OrgBook (in browser, local), search for the company and review it's credentials. It should now have the first ever Credential issued by your Agent.  Cool!

Good stuff. You have a working Agent that issues a basic Credential.

## Step 4: Issuing a Credential directly using the Agent Form

- Entering the URL - no argument
- Getting the Credential ID
- Adding the Credential ID
- Completing the add

## Step 5: Issuing a Credential using a JSON File

- Edit file
- submit file using curl
- checking the results

## Step 6: Customizing your Credential

- Adding/changing fields
- Changing dependencies

## Step 7: Adding a second, multi-cardinality Credential

- Adding a second dependent credential with an Address and Address type
- Adding multiple instances of the credential