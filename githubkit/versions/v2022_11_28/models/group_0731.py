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

from .group_0097 import RepositoryRulesetConditions
from .group_0732 import (
    WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems,
)


class WebhookRepositoryRulesetEditedPropChangesPropConditions(GitHubModel):
    """WebhookRepositoryRulesetEditedPropChangesPropConditions"""

    added: Missing[List[RepositoryRulesetConditions]] = Field(default=UNSET)
    deleted: Missing[List[RepositoryRulesetConditions]] = Field(default=UNSET)
    updated: Missing[
        List[WebhookRepositoryRulesetEditedPropChangesPropConditionsPropUpdatedItems]
    ] = Field(default=UNSET)


model_rebuild(WebhookRepositoryRulesetEditedPropChangesPropConditions)

__all__ = ("WebhookRepositoryRulesetEditedPropChangesPropConditions",)
