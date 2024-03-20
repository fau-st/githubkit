"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0005 import Integration
from .group_0188 import DeploymentSimple
from .group_0161 import PullRequestMinimal


class CheckRun(GitHubModel):
    """CheckRun

    A check performed on the code of a given code change
    """

    id: int = Field(description="The id of the check.")
    head_sha: str = Field(description="The SHA of the commit that is being checked.")
    node_id: str = Field()
    external_id: Union[str, None] = Field()
    url: str = Field()
    html_url: Union[str, None] = Field()
    details_url: Union[str, None] = Field()
    status: Literal[
        "queued", "in_progress", "completed", "waiting", "requested", "pending"
    ] = Field(
        description="The phase of the lifecycle that the check is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check runs."
    )
    conclusion: Union[
        None,
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
        ],
    ] = Field()
    started_at: Union[datetime, None] = Field()
    completed_at: Union[datetime, None] = Field()
    output: CheckRunPropOutput = Field()
    name: str = Field(description="The name of the check.")
    check_suite: Union[CheckRunPropCheckSuite, None] = Field()
    app: Union[None, Integration] = Field()
    pull_requests: List[PullRequestMinimal] = Field(
        description="Pull requests that are open with a `head_sha` or `head_branch` that matches the check. The returned pull requests do not necessarily indicate pull requests that triggered the check."
    )
    deployment: Missing[DeploymentSimple] = Field(
        default=UNSET,
        title="Deployment",
        description="A deployment created as the result of an Actions check run from a workflow that references an environment",
    )


class CheckRunPropOutput(GitHubModel):
    """CheckRunPropOutput"""

    title: Union[str, None] = Field()
    summary: Union[str, None] = Field()
    text: Union[str, None] = Field()
    annotations_count: int = Field()
    annotations_url: str = Field()


class CheckRunPropCheckSuite(GitHubModel):
    """CheckRunPropCheckSuite"""

    id: int = Field()


model_rebuild(CheckRun)
model_rebuild(CheckRunPropOutput)
model_rebuild(CheckRunPropCheckSuite)

__all__ = (
    "CheckRun",
    "CheckRunPropOutput",
    "CheckRunPropCheckSuite",
)
