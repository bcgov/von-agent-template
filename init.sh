#/bin/bash

ORG_TITLE=my-org-full-name
MY_ORG=my-organization
MY_PERMIT=my-permit

echo This script initializes some config data a run of a new VON Issuer/Verifier Agent.
echo Please answer the following questions and we will get things all set up for you.

if [ -z ${ORG_TITLE+x} ]; then
    read -p 'Please provide a descriptive title for your permit-issuing organization (e.g. City of Victoria): ' ORG_TITLE
fi

if [ -z ${MY_ORG+x} ]; then
    read -p 'Please provide a domain for your permit-issuing organization - no spaces (e.g. city-of-victoria): ' MY_ORG
fi
# Strip white spaces, just to be sure
MY_ORG=`echo ${MY_ORG// /} | xargs`

if [ -z ${MY_PERMIT+x} ]; then
    read -p 'Please provide the name of the permit your organization will issue - no spaces (e.g. museum-permit): ' MY_PERMIT
fi
# Strip white spaces, just to be sure
MY_PERMIT=`echo ${MY_PERMIT// /} | xargs`

echo ""

# Generate the seed from MY_ORG, making sure it is 32 characters long
export MY_SEED=`echo ${MY_ORG}_00000000000000000000000000000000 | cut -c 1-32`

echo How will you be the VON Issuer/Verifier Agent:
echo
echo 1 - Using Play with Docker in your browser
echo 2 - Using docker on your own machine - with local von-network and TheOrgBook instances
echo 3 - Some other way

# Determine the example to expand and expand it
select example in "1" "2" "3"; do
    case $example in
        1 ) 
            myhost=`ifconfig eth1 | grep inet | cut -d':' -f2 | cut -d' ' -f1 | sed 's/\./\-/g'`
            export ENDPOINT_HOST="ip${myhost}-${SESSION_ID}-5001.direct.labs.play-with-docker.com"
            export LEDGER=http://138.197.138.255
            export GENESIS_URL=${LEDGER}/genesis

            break;;
        2 ) 
            export ENDPOINT_HOST=localhost:5001
            export DOCKERHOST=${APPLICATION_URL-$(docker run --rm --net=host codenvy/che-ip)}
            export LEDGER=http://${DOCKERHOST}:9000
            export GENESIS_URL=${LEDGER}/genesis

            break;;
        3 ) 
            read -p "Enter the agent host you are using (e.g. localhost:5001): " __AGENTHOST
            export ENDPOINT_HOST=${__AGENTHOST}
            read -p "Enter the URL of the ledger you are using: " __LEDGER
            export LEDGER=${__LEDGER}
            export GENESIS_URL=${LEDGER}/genesis

            break;;
    esac
done
echo ""

find von-x-agent/config -name "*.yml" -exec sed -i "s/my-org-full-name/$ORG_TITLE/g" {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/my-permit/$MY_PERMIT/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/MY-DID/$MY_DID/g {} +
sed -i s/MY-SEED/$MY_SEED/g von-x-agent/config/settings.yml

# Register DID
# https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
echo ""
echo Registering DID on Ledger ${LEDGER} - the Ledger MUST be running for this to work
echo ""
echo \{\"role\":\"TRUST_ANCHOR\",\"alias\":\"${MY_ORG}\",\"did\":null,\"seed\":\"${MY_SEED}\"\} >tmp.json
MY_DID=`curl -s -d "@tmp.json" -X POST ${LEDGER}/register | awk -F'"' '/did/ { print $4 }'`
echo My DID was registered as: $MY_DID
rm tmp.json
echo ""

echo -------------------------
echo The following updates were made to the configuration files:
echo ""

grep "${ORG_TITLE}" von-x-agent/config/*.yml
grep ${MY_ORG} von-x-agent/config/*.yml
grep ${MY_PERMIT} von-x-agent/config/*.yml
grep ${MY_DID} von-x-agent/config/*.yml
grep ${MY_SEED} von-x-agent/config/*.yml

