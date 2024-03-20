"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0357 import EnterpriseWebhooksType
from .group_0358 import SimpleInstallationType
from .group_0360 import RepositoryWebhooksType
from .group_0361 import SimpleUserWebhooksType
from .group_0359 import OrganizationSimpleWebhooksType


class WebhookRepositoryRenamedType(TypedDict):
    """repository renamed event"""

    action: Literal["renamed"]
    changes: WebhookRepositoryRenamedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookRepositoryRenamedPropChangesType(TypedDict):
    """WebhookRepositoryRenamedPropChanges"""

    repository: WebhookRepositoryRenamedPropChangesPropRepositoryType


class WebhookRepositoryRenamedPropChangesPropRepositoryType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepository"""

    name: WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType


class WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType(TypedDict):
    """WebhookRepositoryRenamedPropChangesPropRepositoryPropName"""

    from_: str


__all__ = (
    "WebhookRepositoryRenamedType",
    "WebhookRepositoryRenamedPropChangesType",
    "WebhookRepositoryRenamedPropChangesPropRepositoryType",
    "WebhookRepositoryRenamedPropChangesPropRepositoryPropNameType",
)
