"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild

from .group_0740 import (
    WebhookRepositoryVulnerabilityAlertCreatePropAlertAllof0PropDismisser,
)


class WebhookRepositoryVulnerabilityAlertCreatePropAlertAllof0(GitHubModel):
    """Repository Vulnerability Alert Alert

    The security alert of the vulnerable dependency.
    """

    affected_package_name: str = Field()
    affected_range: str = Field()
    created_at: str = Field()
    dismiss_reason: Missing[str] = Field(default=UNSET)
    dismissed_at: Missing[str] = Field(default=UNSET)
    dismisser: Missing[
        Union[
            WebhookRepositoryVulnerabilityAlertCreatePropAlertAllof0PropDismisser, None
        ]
    ] = Field(default=UNSET, title="User")
    external_identifier: str = Field()
    external_reference: Union[str, None] = Field()
    fix_reason: Missing[str] = Field(default=UNSET)
    fixed_at: Missing[datetime] = Field(default=UNSET)
    fixed_in: Missing[str] = Field(default=UNSET)
    ghsa_id: str = Field()
    id: int = Field()
    node_id: str = Field()
    number: int = Field()
    severity: str = Field()
    state: Literal["open", "dismissed", "fixed"] = Field()


model_rebuild(WebhookRepositoryVulnerabilityAlertCreatePropAlertAllof0)

__all__ = ("WebhookRepositoryVulnerabilityAlertCreatePropAlertAllof0",)
