# Running the BC Registries Event Processor using Docker

## Checkout the repository.

If you are planning on submitting Pull Requests to this project, fork the repo and clone your on fork.

```
git clone https://github.com/bcgov/von-bc-registries-agent.git
cd von-bc-registries-agent/data-pipeline
```

The database configuration is defined using environment variables defined in the docker/docker-compose.yml file.  You can accept defaults, edit the yml file (be careful about what you check in) or set environment variables to override the values in the yml file.

## Run the application:

* Open 5 (wow!) shells. The last one is just for running any commands you might need.
* In the first shell, build and start the von-network. See the quick start guide in the von-network repo. Check the operation at: http://localhost:9000
* In the second shell, build and start TheOrgBook. See the quick start guide in TheOrgBook repo. Check the operation at: http://localhost:8080
* In the third shell, you have to port forward a port on your localhost to a BC Gov OpenShift instance running a database connected to a test BC Registries database.
    * Login to the BC Gov Pathfinder OpenShift instance (you must have been given access)
    * Get a login string w/token to access the BC Gov Pathfinder OpenShift from the command line.
    * Paste the login string into the shell to login.
    * Change to the BC Reg Dev project: `oc project devex-von-bc-registries-agent-dev`
    * Run `get pods` and find the name of the postgres data wrapper pod (e.g. `postgresql-oracle-fdw-1-nhdlv`)
    * Start the port forwarding using the command `oc port-forward postgresql-oracle-fdw-1-nhdlv 5454:5432`
        * You should get a status message and **not** get a command line project back - leave the shell like that.
* In the fourth shell, navigate to this project's repo, go into the docker folder and build the needed docker image:
    * `./manage build`
* Assuming the build works, you need to get the user ID and password for the BC Registries database.  To get that:
    * Login to the BC Gov Pathfinder OpenShift instance and navigate to the BC Reg Dev project.
    * Navigate to (right menu) Resources and Secrets and the `postgresql-oracle-fdw` secret.
    * Click "Reveal Secret"
    * Use the values of `database-user` and `database-password`
* Back to the fourth shell and run the command:
    * `BC_REG_DB_USER=<user> BC_REG_DB_PASSWORD=<password> ./manage start`
    * After the startup completes (the logging stops - it will take about a minute to fully start up), go in the browser to `http://localhost:5050`

## To stop the application:

* Hit ctrl-c in each of the 4 shells.

## To reset the application data

* Use the reset instructions for `von-network` and `TheOrgBook` (they are pretty similar to the instructions below...)
* In the 4th shell - the one for this repo:
    * Change into the `docker` folder
    * Run the command: `./manage rm`