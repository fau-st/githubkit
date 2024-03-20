"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0005 import IntegrationType
from .group_0188 import DeploymentSimpleType
from .group_0362 import SimpleCheckSuiteType
from .group_0161 import PullRequestMinimalType


class CheckRunWithSimpleCheckSuiteType(TypedDict):
    """CheckRun

    A check performed on the code of a given code change
    """

    app: Union[None, IntegrationType]
    check_suite: SimpleCheckSuiteType
    completed_at: Union[datetime, None]
    conclusion: Union[
        None,
        Literal[
            "waiting",
            "pending",
            "startup_failure",
            "stale",
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
        ],
    ]
    deployment: NotRequired[DeploymentSimpleType]
    details_url: str
    external_id: str
    head_sha: str
    html_url: str
    id: int
    name: str
    node_id: str
    output: CheckRunWithSimpleCheckSuitePropOutputType
    pull_requests: List[PullRequestMinimalType]
    started_at: datetime
    status: Literal["queued", "in_progress", "completed", "pending"]
    url: str


class CheckRunWithSimpleCheckSuitePropOutputType(TypedDict):
    """CheckRunWithSimpleCheckSuitePropOutput"""

    annotations_count: int
    annotations_url: str
    summary: Union[str, None]
    text: Union[str, None]
    title: Union[str, None]


__all__ = (
    "CheckRunWithSimpleCheckSuiteType",
    "CheckRunWithSimpleCheckSuitePropOutputType",
)
