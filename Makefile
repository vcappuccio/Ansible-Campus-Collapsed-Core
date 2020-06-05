DOCKER_IMG = packetferret/ansible-vxlan-evpn-for-campus
DOCKER_TAG = 0.0.1

build:
	docker build -t $(DOCKER_IMG):$(DOCKER_TAG) files/docker/ansible/

run:
	docker run -it \
	--rm \
	-v $(PWD)/files/:/home/tmp/files \
	-w /home/tmp/files/ansible/ \
	$(DOCKER_IMG):$(DOCKER_TAG) /usr/bin/zsh

ansible:
	docker run -it \
	--rm \
	-v $(PWD)/files/:/home/tmp/files \
	-w /home/tmp/files/ansible/ \
	$(DOCKER_IMG):$(DOCKER_TAG) ansible-playbook pb.configuration.network.yml
