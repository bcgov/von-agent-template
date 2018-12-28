# VON Issuer/Verifier Agent Configuration

This folder contains the files used to configure a VON Issuer/Verifier. If you are going to be updating a VON Agent, please review this documentation thoroughly - looking particularly for changes that need to be made across several of the configuration files.

## Summary: The Configuration Files

The following sub-sections provide a summary of each of the files. We recommend that you open a second browser window so that you can look at the base configurations as you read about each file.

Each file is a [YAML file](https://en.wikipedia.org/wiki/YAML). It's important to remember when editing a YAML file that the indentations of the lines are important and must be consistent, and that the indenting must ONLY use spaces - never tab characters.

### File: [schemas.yml](schemas.yml)

`schemas.yml` holds the list of Credentials to be issued by the Agent. In this repo, the file starts with just a single Credential.  The file includes the following pieces of information:

- A few pieces of metadata about the schema (version, name, description, the HTTP path for the Credential).
- Some specific information used by TheOrgBook to control behaviour when a Credential is issued (topic, cardinality, effective date). More about this information later.
- An optional proof request that must be satisfied before this Credential can be issued.
- The list of attributes (claims) that can (or must) be populated in the Credential.

### File: [settings.yml](settings.yml)

This is the most obvious of the files - a list of environment variables that must be set appropriately to run the Agent. Of course the values change with each environment (e.g. Local, In Browser, Dev, Test and Prod), so managing the file does get interesting.

> You won't have to touch this file in this Guide.

### File: [routes.yml](routes.yml)

This file configures the Web Server routes for the API and Web Forms that are used in the application. The Agent Web Forms are unlikely ever to be used in a production instance of the VON-Agent, but the form is super useful for testing. It enables the display of dynamic form (based on the claim names and attributes) so that a user can fill in the fields for a Credential.  There should be a "form" section for each Credential, containing the following information: 

- Form metadata, including the URL for the form, the credential schema upon which it is based, titles to display, a form template to use, etc.
- A reference to a proof request.
  - If a proof request is included, on loading, the form contacts TheOrgBook to process the proof request.
- A list of the attributes to be displayed on the form.
  - If a proof request is executed before displaying the form, like named fields from the proof request will be pre-populated.
- A list of the attributes that are auto-populated with specific values - e.g. uuids, literals or the current date.

### File: [services.yml](services.yml)

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

> **To Do**: Provide more detailed documentation about the elements of each file.