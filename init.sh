#/bin/bash

echo This script updates the names of your issuer in the VON-IVy configuration data.

if [ -z ${MY_ORG+x} ]; then
    read -p 'Please provide a name for your permit-issueing organization (e.g. yourname-org): ' MY_ORG
fi

echo ""

# Generate the seed from MY_ORG, making sure it is 32 characters long
export MY_SEED=`echo ${MY_ORG}_00000000000000000000000000000000 | cut -c 1-32`
export MY_DID=someBigHexString

find von-x-agent/config -name "*.yml" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/8HkrLGCUemkvspADWnJu4e/$MY_SEED/g {} +
sed -i s/bc_von_x_dev_0000000000000000000/$MY_SEED/g von-x-agent/config/settings.yml

echo -------------------------
echo The following updates were made to the configuration files:
echo ""

grep -r ${MY_ORG} von-x-agent/config