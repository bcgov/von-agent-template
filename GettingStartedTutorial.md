# VON Agent Getting Started Tutorial

This Getting Started Guide is to get someone new to VON Issuer/Verifier Agents up and running in about an hour.  We assume that if you are here, you have some background in the goals and purpose of the Verifiable Organizations Network (VON), OrgBook, VON Issuer/Verifier Agents and dFlow (decentralized workflow).  If any of this is new to you, please learn more at [https://vonx.io](https://vonx.io). On that site, we recommend the overview in the "About" section, and especially, the webinar linked at the top.

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
  - [Step 1: Investigating VON](#step-1-investigating-von)
  - [Step 2: Get Your VON Issuer/Verifier Agent Running](#step-2-get-your-von-issuerverifier-agent-running)
    - [In Browser](#in-browser-2)
    - [Local Machine](#local-machine-2)
    - [Clone, Initialize and Start Your Agent](#clone-initialize-and-start-your-agent)
  - [Step 3: Review the Configuration Files](#step-3-review-the-configuration-files)
  - [Step 4: Issuing a Credential Using dFlow](#step-4-issuing-a-credential-using-dflow)
  - [Step 5: Issuing a Credential Using a JSON File](#step-5-issuing-a-credential-using-a-json-file)
  - [Step 6: Customizing Your Credential](#step-6-customizing-your-credential)
    - [Stopping and Restarting Your Agent](#stopping-and-restarting-your-agent)
  - [Step 7: Changing a Proof Request Prerequisite](#step-7-changing-a-proof-request-prerequisite)
  - [Step 7: Adding a Second, Multi-Cardinality Credential](#step-7-adding-a-second-multi-cardinality-credential)
    - [schemas.yml](#schemasyml)
    - [In `routes.yml`](#in-routesyml)
    - [In `services.yml`](#in-servicesyml)
    - [Stop and Start the Agent](#stop-and-start-the-agent)
  - [Conclusion](#conclusion)
    - [Next Steps](#next-steps)

## Running in your Browser or on Local Machine

This guide can be run from within a browser, or if you are more technically inclined, you can run it on your local machine using Docker. In the following sections, there are sub-sections for `In Browser` and `Local Machine`, depending on how you want to run the guide. If you will be going from here to setting up a new VON Issuer/Verifier Agent instance for your organization, you might want to use the `Local Machine` path.

## Prerequisites

### In Browser

The only prequisite (other than a browser) is an account with [Docker Hub](https://hub.docker.com). Docker Hub is the "Play Store" for the [Docker](https://docker.com) ecosystem.

### Local Machine

To run this guide on your local machine, you must have the following installed:

* Docker (Community Edition is fine)
  * If you do not already have Docker installed, go to [the Docker installation page](https://docs.docker.com/install/#supported-platforms) and click the link for your platform.
* Docker Compose
  * Instructions for installing docker-compose on a variety of platforms can be found [here](https://docs.docker.com/compose/install/).
* git
  * [This link](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) provides installation instructions for Mac, Linux (including if you are running Linux using VirtualBox) and native Windows (without VirtualBox).
* a bash shell
  * bash is the default shell for Mac and Linux.
  * On Windows, the git-bash version of the bash shell is installed with git and it works well. You **must** use bash to run the guide (PowerShell or Cmd will not work).
* curl
  * An optional step in the guide uses the utility `curl`.
  * curl is included on Mac and Linux.
  * Instructions for installing curl on Windows can be found [here](https://stackoverflow.com/questions/9507353/how-do-i-install-and-use-curl-on-windows).

## VON Network Setup

### In Browser

Go to the [Play with Docker](https://labs.play-with-docker.com/) and (if necessary) click the login button. *Play With Docker* is operated by Docker to support developers learning to use Docker.

> If you want to learn more about the `Play with Docker` environment, look at the [About](https://training.play-with-docker.com/about/) and the Docker related tutorials at the Docker Labs [Training Site](https://training.play-with-docker.com). It's all great stuff created by the Docker Community. Kudos!

Click the "Start" button to start a Docker sandbox you can use to run the demo, and then click `+Add an Instance` to start a terminal in your browser. You have an instance of a Linux container running and have a bash command line.  We won't need to use the command line until Step 2 of this tutorial.

From time to time in the steps in this guide, we'll ask you to edit files. There are two ways to do that in this environment:

- If you are comfortable with the `vi` editor, you can just use that. If you don't know `vi`, don't try it. It's a little scary.
- Alternatively, there is an `Editor` link near the top of the screen. Click that and you get a list of files in your home directory, and clicking a file will open it in an editor.  You will probably need to expand the editor window to see the file. Make the changes in the editor and click the "Save" button.
  - Don't forget to click the "Save" button.

The following URLs are used in the steps below for the different components:

- The `von-network` URL - [http://dflow.bcovrin.vonx.io](http://138.197.138.255/). You'll see a ledger browser UI showing four nodes up and running (blue circles).
- The `OrgBook` URL  - [https://demo.orgbook.gov.bc.ca](https://demo.orgbook.gov.bc.ca) - You'll see the OrgBook interface with companies/credentials already loaded.
- The `dFlow` URL - [https://dflow.orgbook.gov.bc.ca](https://dflow.orgbook.gov.bc.ca). You'll see the dFlow interface, with the "Credential" drop down having a list of at least the seven "dflow" credential types, and perhaps (many) more.

You can open those sites now or later. They'll be referenced by name (e.g. "The von-network URL...") in the guide steps.

### Local Machine

On a local machine upon which the prerequisites are setup, we will be installing and starting, in order, instances of [von-network](https://github.com/bcgov/von-network), [OrgBook](https://github.com/bcgov/TheOrgBook) and [dFlow - decentralized workFlow](https://github.com/bcgov/dFlow).

Use the [VON Network Quick Start Guide](https://github.com/bcgov/dFlow/blob/master/docker/VONQuickStartGuide.md) to start the prerequisite instances and verify that they are running.

## Step 1: Investigating VON

If you are new to VON, see the instructions in the respective repos for how to use the running instances of [von-network](https://github.com/bcgov/von-network), [OrgBook](https://github.com/bcgov/TheOrgBook) and [dFlow](https://github.com/bcgov/dFlow).

Our goal in this guide is to configure a new permit and/or licence VON Issuer/Verifier  Agent so that the credential will be available from the "Credentials" drop down in dFlow.

## Step 2: Get Your VON Issuer/Verifier Agent Running

In this step, we'll get an instance of the VON Issuer/Verifier Agent running and issuing credentials. 

### In Browser

Start in the root folder of your Docker instance&mdash;where you began.

### Local Machine

Use a different shell from the one used to start the three other components. After opening the new shell, start in the folder where you normally put the clones of your GitHub repos.

### Clone, Initialize and Start Your Agent

Clone the repo, and run the initialization script.

```
# Start in the folder with repos (Local Machine) or home directory (In Browser)
$ git clone https://github.com/bcgov/von-agent-template
$ cd von-agent-template
$ . init.sh  # And follow the prompts
```

The `init.sh` script does a number of things:

1. Prompts for some names to use for your basic agent.
2. Prompts for whether you are running with Play With Docker or locally and sets some variables accordingly.
3. Registers a DID for you on the ledger that you are using.
4. Shows you the lines that were changed in the agent configuration files (in [von-x-agent/config](von-x-agent/config)).

The initial agent you have created issues one credential, using the name you gave it, with a handful of claims: permit ID, permit type, etc. That credential depends on the applying organization already having the dFlow "registration" credential. Without already having that credential, an applying organization won't be able to get your agent's credential.

To start your agent, run through these steps:

```
cd docker   # Assumes you were already in the root of the cloned repo
./manage build
./manage start
```

After the last command, you will see a stream of logging commands as the agent starts up. The logging should stabilize with an "Indy sync complete" entry.

To verify your agent is running:

1. Go to the `Agent URL`, where you should see a "404" (not found) error message. That signals the agent is running, but does not respond to that route.
   1. For In Browser, click the "5001" link at the top of the screen. That's the path to your agent.
   2. For `Local Machine`, go to [http://localhost:5001](http://localhost:5001).
2. Go to the `dFlow URL` (in browser, local) where in the Credential drop down, you should be able to see your agent's credential.
   1. The Credential dropdown box is a search box, so just type the name of your organization or credential in it.

All good?  Whoohoo!

## Step 3: Review the Configuration Files

Your aAgent is configured using the YAML files in the [von-x-agent/config](von-x-agent/config) folder in this repo. Let's take a look at the files in that folder. If you browse the files in your installation, you'll see the `./init.sh` updates you made to the names.

In this step, we'll quickly review the current files to get a feel for them. No need to learn all the details&mdash;when the time comes, documentation for the files can be found in the [VON Agent Configuration Guide](von-x-agent/config/Readme.md). Jump into the documentation and scan the information. We'll be working with these files as we go through the tutorial.

Enough with the configurations - let's get on with issuing credentials.

## Step 4: Issuing a Credential Using dFlow

Now let's use some techniques to trigger your agent to issue a credential to the OrgBook so that you can look at it.  We'll start with the easiest way&mdash;using dFlow.

Go to the `dFlow URL` (local, in browser) and select your credential as the target credential you want to be issued. In the Company field, either leave it blank or select a company that you created in Step 1. Click `Begin` and you should see a dFlow with the dFlow "Registration" as the first credential, and your agent's credential as the second. Go through the process to collect each credential to make sure everything is working.

Go into OrgBook (in browser, local), search for the company and review its credentials. It should now have the first ever credential issued by your agent.  Cool! If you want, go back and try to issue a few more credentials.

Good stuff. You have a working aAgent that issues a basic aredential.

## Step 5: Issuing a Credential Using a JSON File

Now that we have seen how a user can trigger the issuance of a verifiable credential via a web form, let's look at how an app can issue one via an API call. In most production cases, verifiable credentials will be issued using the API&mdash;an existing backend application for a service will be adjusted so that when a permit or licence is issued or updated, an "issue verifiable credential" API call is made with the credential data passed in a chunk of JSON. Let's see how that works.

> **NOTE:** If you are running this using the "Local Machine" approach, make sure that you have curl installed. At the command line just run "curl" and see if the command is found. If not, see the prerequisites for how you can install it.

Remember that your credential is set up to depend on a dFlow registration credential. To populate the JSON structure, we need to get some information from an existing registration credential. Recall one that you have already issued (or issue a new one using dFlow), and then find it in OrgBook on a screen where you can see the  registration ID and the legal name of the company. Recall that in the dFlow run we did previously, those fields came from the proof request. In this case, we're not going to do the proof request, so we need to (correctly!) populate them in the JSON for the API call.

The JSON file we're going to submit is in the `von-agent-template` repo, in the `von-x-agent/testdata` folder. Edit that file and the following changes:

- set the "corp_num" field to the "registration ID" field from OrgBook
- set the "legal_name" field to the legal name of the company from OrgBook
- change "my-permit" and "my-organization" in the "schema" name to the permit and organization fields that you entered when you initialized the settings
- as you want, update any of the other data elements, making sure that you retain the JSON structure

Save your file and then, from the root folder of the `von-agent-template`, execute this command REPLACING "my-organization" with the name of your organization:

```
$ curl -vX POST http://$ENDPOINT_HOST/my-organization/issue-credential -d @von-x-agent/testdata/sample_permit.json --header "Content-Type: application/json"
```

You should see the results from the `curl` command with an HTTP response of `200` (success) and JSON structure with the status, something like this:

```
[{"success": true, "result": "05da7e24-c24b-4162-b201-157d8afe7a04", "served_by": "b2179bc0df16"}]
```

If the `curl` command failed - check for typos in your JSON structure and the command you submitted.  Did you remember to change "my-organization" to the name of your organization?

Once the `curl` command succeeds and the verifiable credential has been issued, go into OrgBook, find the organization again and verify that the credential was indeed issued.  If you want, update the dates on the attributes and re-submit the curl command again. Each time you do, OrgBook will make sure that:

- the latest issued credential is "active"
- older credentials are tagged as "revoked" and will not be used for creating proofs

Note that it's up to the issuer to make sure that the dates make sense. OrgBook has very few business rules and knows nothing about the process your organization uses for issuing or revoking credentials. As such, the business rules for making sure the right verifiable credentials are issued with the right dates must come the (backend) code that issues the permits and licences.

So, we now have a working agent, and we can issue credentials using a form or an API.  Time to make some changes to the credential we are issuing.

## Step 6: Customizing Your Credential

Now that we have a working agent, let's make some changes and really make it our own. We'll start simple and make some changes to the attributes (claims) within your credential&mdash;changing the name of an attribute and adding a new one.

- The "permit_type" field is really about what authorization is being asked for or issued, so let's change that field name to "permit_authorization"
- Let's add another field "permit_notes" that is a free form text field that can be used to add any notes/conditions/limitations about the permit.


If you want, you can make other changes, within limits.  You can't change the "corp_num" or "legal_name" fields, since they come from the prerequisite verifiable credential, dFlow registration. All others can be renamed and new fields can be added as needed.

Things to remember as you make the changes:

1. The files to be edited are in the `von-x-agent/config` folder - `schema.yml`, `routes.yml` and `services.yml`. No need to change `settings.yml`
2. If you rename a credential attribute, check in all three files for the name and change it in all three.
3. If you add an attribute, you need only add it in `schema.yml` and `routes.yml`. Recall that in `routes.yml` you are defining how to populate the attribute when submitting the credential data via a form. Best choice for this exercise is to add it as a visible form field (for example just below `permit_type`).
4. See the `Stopping and restarting` notes below to see if you need to change the `version` of your schema. **Hint**: Because you are changing the credential schema in this exercise, you do have to bump the version.
5. Remember to save your files.
6. If you are using `Play with Docker` and the `Play with Docker` editor, be warned: it has a bad habit of deleting characters at the bottom of a file (it's a known problem to that service).  If you have a problem doing this exercise, check for that.

### Stopping and Restarting Your Agent

When you make changes to the configuration, you will need to stop, rebuild and redeploy your agent.  Here's some guidance about doing that.

1. To stop the agent but keep its wallet, go to the agent's docker folder and run the command `./manage stop`. To stop the agent *AND* delete the wallet, run the command `./manage down`.
2. Once you've made your changes, stopped your agent and are ready to test, run the commands `./manage build` and `./manage start`. You **must** run the `build` command to pick up your configuration changes.
3. If you change any of the defined schema and the ledger you are using is persistent (e.g. always when using Play With Docker and locally, when you don't bring down and redeploy the ledger between runs), you will need to bump the `version` of your schema in `schemas.yml`.

Once you have restarted your agent, try the steps we went through previously to issue a new credential using dFlow.  Notice that both the old (1.0.0) and new (1.0.1) versions of the schema are listed in dFlow. That's to be expected (at least for now, we may change/fix that in the future). Note that when you run locally and do restart the ledger and all the components from scratch, you can go back to version 1.0.0 of the credential if you want.

All good? Great! If not, make sure you carried out all the steps and try again.

## Step 7: Changing a Proof Request Prerequisite

Let's also change the proof request prerequisites for your credential.  We'll add another credential to the prerequisites. To do that, we need to edit the `services.yml` file and add a second proof request dependency. In the following, we're going to add the dFlow `PST Number` credential as a dependency, but feel free to add others. Here's what you have to do in the `services.yml` file:

1. Add `pst_number` after `dflow_registration` in the `depends_on` config element.
2. Copy the `dflow_registration` sub-section of yaml, within `proof_requests` (bottom of the file), and paste immediately below so there are two sections in `proof_requests`.
3. Update the fields as appropriate for the credential you are using.
   1. To get the values for `did`, `name` and `version`, go to the ledger and look up the schema. Click "Domain" and then search for "pst" (or whatever credential you want to use) and use the `From nym`, `Schema Name` and `Schema version` fields, respectively.
   2. Ensure that only attributes that are in the selected schema are in the "attributes" section.
      1. You can remove the attributes section entirely if you want (that would be used to prove that the holder has the required verifiable credential without requesting to any of the data within the credential).
4. Save the file.
5. Stop, build and restart the agent as per the instructions in the previous step.

Once you have done that, go to the dFlow app and select your agent's credential as the one to be acquired. On the workflow screen you'll see a graph of the new requirements.

Once you have acquired the aredentials for a newly registered organization, try requesting the credential for an organization that already has an instance of the credential. You might find that while the organization has the desired credential, it doesn't have all of the prerequisite(s). This is as expected, just like a paper-based permit-issuing organization changing their business rules on the fly, existing credentials (probably) should continue to be valid, but new applications must meet the new requirements. Of course, a service changing its rules could choose to revoke the credentials issued to organizations that don't already have the new prerequisite, asking or requiring that they 'proof' they have that credential before being re-authorized.

## Step 7: Adding a Second, Multi-Cardinality Credential

The final exercise is the biggest&mdash;think of it as your final exam.  In this step we'll add an entire new credential, one dependent on the credential already issued by your agent. Here's the business scenario:

The service offers a "multiple location" permit that extends the authority of the existing permit to several locations.  If an organization can prove it has been issued the first verifiable credential, it can get the subsequent permits for other named locations by supplying a "multiple location" name and address.

The following are the tasks to be done and notes about the changes to be made to the files in `von-x-agent/config`:

### schemas.yml

`schemas.yml` describes the credentials. To add the second credential, copy the existing one (the entire `name` element of the YAML), paste it as a second instance, and edit the following:

- Update the `name`, and `version` for the new credential
- Keep `topic` the same, that associates the credential with the subject organization
- Change `proof_request` to the name of your first credential (more on that later)

Update the list of attributes:

- Keep `corp_num`, `permit_id`, `effective_date`, `permit_issued_date` and remove the others. You might note the names of the fields you remove for later.
- Add the name and address attributes - `location_name`, `addressee`, `civic_address`, `city`, `province`, `postal_code` and `country`

Final change: near the top of the new credential, below `topic` and the following:

```
  cardinality: location_name
```

`Cardinality` enables an organization to be the subject of multiple of these credentials for multiple locations. If the `location_name` in a verifiable credential for an organization has not been seen before by OrgBook, the credential is assumed to be a new one.  If the `location_name` has been seen before for that organization, OrgBook assumes it's a reissuance and revokes the old credential and makes the new one current. See the VON Issuer/Verifier Agent documentation for more details.

OK, Done! Save your work.

### In `routes.yml`
  - 
`routes.yml` describes the form to be displayed for collecting information about the new credential.  Again, we'll do a big copy and paste to get started. Copy everything from the line below `forms`&mdash;that's the entire entry for the first credential&mdash;and  paste it below.  Once done, start making changes:

- Remove the sub-sections that reference the fields that you removed from `schemas.yml`.
- Change the name of the credential, the path, the schema name, page_title, title, description and explanation. It should be fairly obvious what to put for each.
- Change `id` under `proof_request` to be the name of the existing credential. More on that later. 
- Recall that we added the location name and address fields to the schema, and we have to add them here as well. In `routes.yml`, there is a shortcut for adding addresses to a form as you'll see below. Add the following text within the `fields` list. Note that indenting in YAML matters, so make sure the section lines up with the rest of the elements of the `fields` list and only put spaces at the start of lines.

```
      - name: location_name
        label: Location Name
        type: text
        required: true

      - name: address
        label: Mailing Address
        type: address
        required: true
```

- Remove `permit_id` from the `mapping` section and add it back into the `fields` section. Put it below `corp_num` with the same `type` and `text` values.

Those are a lot of changes, but we're done with that file. Save your work!

### In `services.yml`

As we did in the previous files, we'll copy and paste the existing credential to make the new one and edit from there.  In this case, copy the text from the `description` element below `credential_types` down through the end of the last `model: attribute` element and paste all of that below the existing credential.  The edits to be made are the following:

- Update `description`, `schema` and `issuer_url` for the new credential.
- Change `dflow_registration` under `depends_on` to the new of the existing credential.
- Leave the `credential` and `topic` elements as is.
- Add in the following `cardinality_fields` section, to match what is in the `schemas.yml` section. Again, check your indenting!

```
      cardinality_fields:
        - additionl_cred_type_attr

```

- In the mapping, remove all of the mappings for attributes removed from the schema.
- Add in an `address` section. OrgBook "knows" about addresses and so we want to map the address attributes to OrgBook's address search fields.  The YAML for that is below.

```
        - model: address
          fields:
            addressee:
              input: addressee
              from: claim
            civic_address:
              input: address_line_1
              from: claim
            city:
              input: city
              from: claim
            province:
              input: province
              from: claim
            postal_code:
              input: postal_code
              from: claim
            country:
              input: country
              from: claim
```

Make sure that the indenting is with spaces and the same as the other `model` elements.

The final section to update is the `proof_requests` at the bottom of the file. Once again, we want to copy the existing elements, paste them and edit them.

- Copy from `dflow_registration` to the list of attributes and paste it immediately below.
- Rename the element to the name of the first credential, as you have earlier for other references to proof requests.
- Look on the ledger for your first credential to get the `did`, `name` and `version` values.
- For attributes, list `corp_num` and `permit_id`.

That's it, you should have be good to go.  Time to test.

### Stop and Start the Agent

Use the process presented early in this tutorial to stop the agent (without deleting its wallet), building it and starting it again.

Use dFlow to test that you can issue the new credential (do you get the correct workflow?) via the form. dFlow doesn't yet support issuing multiple of the same credential for a single organization, so we'll have to use `curl` to test that. We've added a JSON file ([von-x-agent/testdata/sample-location.json](von-x-agent/testdata/sample-location.json)) that you can edit and use to issue multiple credentials to the same organization. Make sure to update the fields to the correct values (especially corp_num and permit_id) before running the curl command.  Try issuing multiple credentials with different dates but the same `location_name` value to see how OrgBook handles that situation. Look in OrgBook to see the results.

## Conclusion

With that, you should have a pretty good idea of how VON Issuer/Verifier Agents are configured and deployed. See the agent configuration documentation for more details about all of the elements of the YAML files.

If you discovered any problems in completing this tutorial, please let us know either by submitting an issue to the source GitHub repo, or by updating the files or documentation and submitting a Pull Request. If you want to compare your config files with our version of the completed tutorial, look at files in the folder [von-x-agent/testdata/completed](von-x-agent/testdata/completed).  

### Next Steps

If you are going to be deploying a production agent, you have a few things to consider that become possible within a VON Issuer/Verifier Agent:

- What credentials (registrations, permits, licences, authorizations, etc.) does your service issue? Which of these should be issued as verifiable credentials?
- What events in your existing system trigger the (re)issuance of each of those credentials?
- Within the credentials, what attributes would be useful for an organization to have in their sallet when they need to prove they hold the credentials?
- What are the prerequisites for an entity to be issued your service's credentials?
- What changes could be made in your existing process to support verifiable credentials?
  - What steps can be bypassed by receiving a proof that an organization holds prerequisite verifiable credentials?
  - What data elements can be pulled from a prerequisite verifiable credentials such that they need not be retyped by the process participants?
  - When  credentials be issued in your existing process?