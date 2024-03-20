"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoCodespacesDevcontainersGetResponse200(GitHubModel):
    """ReposOwnerRepoCodespacesDevcontainersGetResponse200"""

    total_count: int = Field()
    devcontainers: List[
        ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems
    ] = Field()


class ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems(
    GitHubModel
):
    """ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems"""

    path: str = Field()
    name: Missing[str] = Field(default=UNSET)
    display_name: Missing[str] = Field(default=UNSET)


model_rebuild(ReposOwnerRepoCodespacesDevcontainersGetResponse200)
model_rebuild(ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems)

__all__ = (
    "ReposOwnerRepoCodespacesDevcontainersGetResponse200",
    "ReposOwnerRepoCodespacesDevcontainersGetResponse200PropDevcontainersItems",
)
