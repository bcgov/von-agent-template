[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# von-agent-template
This repo is a template for creating an instance of a Verifiable Organizations Network (VON) Issuer/Verifier Agent running against a Hyperledger Indy network such as Sovrin. If you are new to VON and want to learn more about the approach we are using to enable Service Organizations to issue Verifiable Credentials, please https://vonx.io.

An Issuer/Verifier agent and [OrgBook](https://github.com/bcgov/TheOrgBook) are the two major components of local VON ecosystem. OrgBook is an instance of Credential Repository from which a VON Agent instance receives proofs of Verifiable Claims and to which a VON Agent issues Verifiable Credentials. VON Issuer/Verifier Agent instances are configured, deployed and operated by registration, permit and licence issuing Service Organizations that want to issue/verify Verifiable Credentials. One Issuer/Verifier agent instance can support multiple types of credentials and in most cases an organization would only need to run a single agent to process all credential types they need. An agent based on this template is deployed using Docker containers, enabling load balancing and high availability capabilities through a container management platform such as Red Hat's OpenShift, Kubernetes on AWS, Azure or Google Cloud, etc.

In the future, instances of VON Agent will also be able to communicate directly with Personal and Organizational Agents/Wallets and will be able to Issue/Verify Credentials based on different underlying DID Method implementations.

# Getting Started
Use this [VON Issuer/Verifier Getting Started Tutorial](GettingStartedTutorial.md) to go through the basics of configuring a VON Issuer/Verifier Agent created from this template.

# Configuration Guide
Much of the work in configuring a VON agent is in setting up the YAML files in the [von-x-agent/config](von-x-agent/config) folder. A [Configuration Guide](von-x-agent/config/ConfigurationGuide.md) documents those files.

# Managing Your Agent Repo
If you are creating an Agent for a Service Organization that will become a VON Issuer/Verifier, most of the changes you will make in this repo will be for your own organization's use and will not be pushed back into the base repo. As such, we suggest you use one of following methods for managing this repo. We recommend the first, but would welcome suggestions of other approaches that might have more upside and less downside. Please add an issue to tell us about a better way.

1. Make a snapshot (not a fork or clone - a text copy) of this repo to use as the base repo for your organization's Agent from there. The benefit of that approach is that your developers can fork the snapshot repo and manage everything through the common GitHub Pull Request (PR) model.  The downside is that periodically you should look for code updates to this ([von-agent-template](https://github.com/bcgov/von-agent-template)) repo and apply them to your copy. There are relatively easy ways to track such changes, such as keeping a fork of von-agent-template, using GitHub's `compare` capability to find the differences and apply them to your snapshot repo.

2. Make a fork of this repo, and in that, create a branch that you will use as the deployment branch for your Agent instance. The benefit of this approach is that you can stay up to date with the base repo by applying commits to your branch from the `master`. The downside is a much more complex branching model for your developers and a non-typical deployment model for your code.

3. Likely, the two mechanisms above can be combined, and branches could be created in the main repo for the different instances. This might be an approach that, for example, the BC Gov could use - creating a branch for each Issuer/Verifier Agent in BC Gov. However, we think that the complexity of such a scheme will not be worth the benefits.

# Getting Help or Reporting an Issue
To report bugs/issues/feature requests, please file an [issue](../../issues).

# How to Contribute
If you have found this project helpful, please contribute back to the project as you find new and better ways to use SonarQube in your projects.

If you would like to contribute, please see our [CONTRIBUTING](./CONTRIBUTING.md) guidelines.

Please note that this project is released with a [Contributor Code of Conduct](./CODE_OF_CONDUCT.md). 
By participating in this project you agree to abide by its terms.