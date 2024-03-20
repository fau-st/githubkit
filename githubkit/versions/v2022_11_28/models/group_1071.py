"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from pydantic import Field

from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoPrivateVulnerabilityReportingGetResponse200(GitHubModel):
    """ReposOwnerRepoPrivateVulnerabilityReportingGetResponse200"""

    enabled: bool = Field(
        description="Whether or not private vulnerability reporting is enabled for the repository."
    )


model_rebuild(ReposOwnerRepoPrivateVulnerabilityReportingGetResponse200)

__all__ = ("ReposOwnerRepoPrivateVulnerabilityReportingGetResponse200",)
