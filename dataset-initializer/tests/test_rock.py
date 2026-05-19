# Copyright 2026 Canonical Ltd.
# See LICENSE file for licensing details.

import subprocess

from charmed_kubeflow_chisme.rock import CheckRock


def test_rock():
    """Test rock."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"

    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            LOCAL_ROCK_IMAGE,
            "exec",
            "python3.11",
            "-c",
            "import pkg.initializers.dataset",
        ],
        check=True,
    )
