#/bin/bash

echo This script updates the names of your issuer in the VON-IVy configuration data.

if [ -z ${MY_ORG+x} ]; then
    read -p 'Please provide a name for your permit-issueing organization (e.g. yourname-org): ' MY_ORG
fi

# MY ORG name stripped from white spaces to avoid issues with paths
MY_ORG=`echo ${MY_ORG// /} | xargs`

# Generate the seed from MY_ORG, making sure it is 32 characters long
export MY_SEED=`echo ${MY_ORG}_00000000000000000000000000000000 | cut -c 1-32`

# BC DEV ledger:
#export LEDGER=http://159.89.115.24
# BC TEST ledger:
export LEDGER=http://138.197.138.255

# Register DID
# https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
echo ""
echo Registering DID on Ledger ${LEDGER}
echo ""
echo \{\"role\":\"TRUST_ANCHOR\",\"alias\":\"${MY_ORG}\",\"did\":null,\"seed\":\"${MY_SEED}\"\} >tmp.json
MY_DID=`curl -s -d "@tmp.json" -X POST ${LEDGER}/register | awk -F'"' '/did/ { print $4 }'`
rm tmp.json
echo ""

find von-x-agent/config -name "*.yml" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/testdata -name "sample*.json" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/8HkrLGCUemkvspADWnJu4e/$MY_DID/g {} +
sed -i s/bc_von_x_dev_0000000000000000000/$MY_SEED/g von-x-agent/config/settings.yml

echo -------------------------
echo The following updates were made to the configuration files:
echo ""

grep -r "${MY_ORG}" von-x-agent/config

