# Training Operator Rock

[![Build & Scan](https://github.com/canonical/training-operator-rock/actions/workflows/on_pull_request.yaml/badge.svg)](https://github.com/canonical/training-operator-rock/actions/workflows/on_pull_request.yaml)
[![Publish](https://github.com/canonical/training-operator-rock/actions/workflows/on_push.yaml/badge.svg)](https://github.com/canonical/training-operator-rock/actions/workflows/on_push.yaml)

[Rocks](https://canonical-rockcraft.readthedocs-hosted.com/en/latest/) for [Kubeflow Training Operator](https://github.com/kubeflow/training-operator).
This repository holds all the necessary files and CI to build and publish Kubeflow Training Operator rock.

Automations takes care of:
* Running unit tests for rocks
* Building rocks on merge
* Publishing rocks on merge, to docker.io/charmedkubeflow repository
