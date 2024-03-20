"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild

from .group_0092 import CustomPropertyValue


class ReposOwnerRepoPropertiesValuesPatchBody(GitHubModel):
    """ReposOwnerRepoPropertiesValuesPatchBody"""

    properties: List[CustomPropertyValue] = Field(
        description="A list of custom property names and associated values to apply to the repositories."
    )


model_rebuild(ReposOwnerRepoPropertiesValuesPatchBody)

__all__ = ("ReposOwnerRepoPropertiesValuesPatchBody",)
