# This string is specific to Docker Playground
# Get and format the IP address of this container within the docker playground network
myhost=`ifconfig eth1 | grep inet | cut -d':' -f2 | cut -d' ' -f1 | sed 's/\./\-/g'`
export ENDPOINT_HOST="ip${myhost}-${SESSION_ID}-5001.direct.labs.play-with-docker.com"
