# Ansible VXLAN-EVPN for Campus

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/3/31/Juniper_Networks_logo.svg)](https://www.juniper.net/documentation/solutions/en_US/campus)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Overview

`Ansible-VXLAN-EVPN-for-Campus` is an easier way to deploy a VXLAN / EVPN fabric with Juniper's campus solutions. 

This project is based on [Infrastructure-As-Code](https://dev.to/fedekau/infrastructure-as-code-a-beginners-perspective-2l8k) concepts, where all elements of a device's configuration as stored in a format of `key:value` pairs and stored in a source-code management system such as Github or Gitlab. While not required for successful deployments, we at Juniper encourage network devops teams to [leverage best practicies with git](https://dev.to/bholmesdev/git-github-best-practices-for-teams-opinionated-28h7).

## Execution

The execution of this playbook can be acheived in multiple ways, experiment with each to find out your organization's preference.

### Running the Ansible playbook from your local workstation

As you will see throughout the documentation, we have provided a `Makefile` to act as a shortcut for many of our project's commands. To run the Ansible Playbook on your local workstation, simply run the following command in the project's root directory:

```sh
make ansible
```

### Running inside a Docker container

This is a personal preference, but this is a very clean method to run the playbook as it already manages all of your Python package dependencies. Within the root directory, you will run two commands to build and run the dedicated docker container.

```sh
make build
make run
```

> *note*: the make build command only needs to be ran once; subsequent executions of the command will not hurt anything, but will add a second or two delay

## New Features

- `Makefile` included to shortcut many of the commands
- Docker container provided for those that want execute in an isolated environment.

## Dependencies

The dependencies required come back to your preferred deployment method.

### Ansible on your local workstation

You will need to install the Python packages to your local workstation. We highly encourage you to [leverage python virtual environments](https://realpython.com/python-virtual-environments-a-primer/) to avoid situations where you may overwrite your system's local python packages.

Install the required python packages:

```sh
pip install -r files/docker/ansible/files/requirements.txt
```

### Ansible from within a Docker container

If using Docker as your execution engine, you may not be surprised to learn that you'll need Docker installed on your local workstation. That's it!

*[Docker](https://docs.docker.com/get-docker/)

## An Important

Please make sure to create your own `secrets.yml` file and store it in `group_vars/all` directory. This file hosts many variables necessary to complete the ansible playbook, without this file all of your plans for an automated Campus network will be destroyed.

The `secrets_example.yml` file from the root directory of this project will get you started, simply update the variables with the values appropriate for your environment and move it to `group_vars/all` directory, overwriting the current file there.

This should do the trick nicely

```sh
$ mv secrets_example.yml ./group_vars/all/secrets.yml
```

### Optional:
> Leverage Ansible-Vault to encrypt the `secrets.yml` file before hosting on the public internet

> `ansible-vault encrypt secrets.yml`

## Development

Want to contribute? Great!

Submit a PR and let's work on this together :D
