"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List
from datetime import datetime

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0157 import ActionsSecret


class ReposOwnerRepoEnvironmentsEnvironmentNameSecretsGetResponse200(GitHubModel):
    """ReposOwnerRepoEnvironmentsEnvironmentNameSecretsGetResponse200"""

    total_count: int = Field()
    secrets: List[ActionsSecret] = Field()


model_rebuild(ReposOwnerRepoEnvironmentsEnvironmentNameSecretsGetResponse200)

__all__ = ("ReposOwnerRepoEnvironmentsEnvironmentNameSecretsGetResponse200",)
