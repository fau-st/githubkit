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

from .group_0001 import SimpleUser
from .group_0005 import Integration


class TimelineAssignedIssueEvent(GitHubModel):
    """Timeline Assigned Issue Event

    Timeline Assigned Issue Event
    """

    id: int = Field()
    node_id: str = Field()
    url: str = Field()
    actor: SimpleUser = Field(title="Simple User", description="A GitHub user.")
    event: Literal["assigned"] = Field()
    commit_id: Union[str, None] = Field()
    commit_url: Union[str, None] = Field()
    created_at: str = Field()
    performed_via_github_app: Union[None, Integration] = Field()
    assignee: SimpleUser = Field(title="Simple User", description="A GitHub user.")


model_rebuild(TimelineAssignedIssueEvent)

__all__ = ("TimelineAssignedIssueEvent",)
