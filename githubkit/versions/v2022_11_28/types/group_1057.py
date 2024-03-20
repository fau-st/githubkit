"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoMilestonesPostBodyType(TypedDict):
    """ReposOwnerRepoMilestonesPostBody"""

    title: str
    state: NotRequired[Literal["open", "closed"]]
    description: NotRequired[str]
    due_on: NotRequired[datetime]


__all__ = ("ReposOwnerRepoMilestonesPostBodyType",)
