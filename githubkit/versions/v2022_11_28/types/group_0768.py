"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0769 import WebhookSecurityAndAnalysisPropChangesPropFromType


class WebhookSecurityAndAnalysisPropChangesType(TypedDict):
    """WebhookSecurityAndAnalysisPropChanges"""

    from_: NotRequired[WebhookSecurityAndAnalysisPropChangesPropFromType]


__all__ = ("WebhookSecurityAndAnalysisPropChangesType",)
