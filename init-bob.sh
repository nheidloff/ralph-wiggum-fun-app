chmod 777 ralph/iteration.sh
chmod 777 ralph/loop.sh

podman build -t bob-cli -f containers/Dockerfile-bob .