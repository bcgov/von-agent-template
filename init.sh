#/bin/bash

echo This script updates the names of your issuer in the VON-IVy configuration data.

if [ -z ${MY_ORG+x} ]; then
    read -p 'Please provide a name for your permit-issueing organization (e.g. yourname-org): ' MY_ORG
fi

echo ""

# Generate the seed from MY_ORG, making sure it is 32 characters long
export MY_SEED=`echo ${MY_ORG}_00000000000000000000000000000000 | cut -c 1-32`

# BC DEV ledger:
export LEDGER=http://159.89.115.24

# Register DID
# https://gist.github.com/subfuzion/08c5d85437d5d4f00e58
echo ""
echo Registering DID on Ledger ${LEDGER}
echo ""
echo \{\"role\":\"TRUST_ANCHOR\",\"alias\":\"${MY_ORG}\",\"did\":null,\"seed\":\"${MY_SEED}\"\} >tmp.json
curl -d "@tmp.json" -X POST ${LEDGER}/register
rm tmp.json
echo ""
# Find DID on ledger
PAGE=1
export MY_DID=""
# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html
while [ "${MY_DID}" == "" ]; do
    export MY_DID=`curl -s ${LEDGER}/ledger/domain?page=${PAGE} | grep ${MY_ORG} -A 2 | grep dest | sed 's/^.*: \"//' | sed 's/\",//'`
    let PAGE=PAGE+1
    if [ ${PAGE} -eq 5 ]; then
        echo 'Error: I really tried, but I could not find DID (supposedly) written to the Ledger. Exiting.'
        exit 1
    fi
done

find von-x-agent/config -name "*.yml" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/8HkrLGCUemkvspADWnJu4e/$MY_SEED/g {} +
sed -i s/bc_von_x_dev_0000000000000000000/$MY_SEED/g von-x-agent/config/settings.yml

echo -------------------------
echo The following updates were made to the configuration files:
echo ""

grep -r ${MY_ORG} von-x-agent/config