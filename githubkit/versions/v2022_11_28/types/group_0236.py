"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0237 import EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType


class EnvironmentPropProtectionRulesItemsAnyof1Type(TypedDict):
    """EnvironmentPropProtectionRulesItemsAnyof1"""

    id: int
    node_id: str
    prevent_self_review: NotRequired[bool]
    type: str
    reviewers: NotRequired[
        List[EnvironmentPropProtectionRulesItemsAnyof1PropReviewersItemsType]
    ]


__all__ = ("EnvironmentPropProtectionRulesItemsAnyof1Type",)
