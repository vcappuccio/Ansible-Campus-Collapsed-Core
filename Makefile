DOCKER_IMG = packetferret/ansible-vxlan-evpn-for-campus
DOCKER_TAG = 0.0.1

build:
	docker build -t $(DOCKER_IMG):$(DOCKER_TAG) files/docker/ansible/

run:
	docker run -it \
	-v $(PWD):/home/tmp/files \
	-w /home/tmp/files \
	$(DOCKER_IMG):$(DOCKER_TAG) /usr/bin/zsh
