"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0189 import CheckRunType


class ReposOwnerRepoCommitsRefCheckRunsGetResponse200Type(TypedDict):
    """ReposOwnerRepoCommitsRefCheckRunsGetResponse200"""

    total_count: int
    check_runs: List[CheckRunType]


__all__ = ("ReposOwnerRepoCommitsRefCheckRunsGetResponse200Type",)
