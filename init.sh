#/bin/bash

export MY_ORG=ianco-org
export MY_SEED=bc_von_x_dev_0000000000000000666
export MY_DID=someBigHexString

find von-x-agent/config -name "*.yml" -exec sed -i s/my-organization/$MY_ORG/g {} +
find von-x-agent/config -name "*.yml" -exec sed -i s/8HkrLGCUemkvspADWnJu4e/$MY_SEED/g {} +
sed -i s/bc_von_x_dev_0000000000000000000/$MY_SEED/g von-x-agent/config/settings.yml
