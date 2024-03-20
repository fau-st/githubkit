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


class WebhookDeployKeyDeletedType(TypedDict):
    """deploy_key deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    key: WebhookDeployKeyDeletedPropKeyType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: RepositoryWebhooksType
    sender: SimpleUserWebhooksType


class WebhookDeployKeyDeletedPropKeyType(TypedDict):
    """WebhookDeployKeyDeletedPropKey

    The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-
    deploy-key) resource.
    """

    added_by: NotRequired[Union[str, None]]
    created_at: str
    id: int
    key: str
    last_used: NotRequired[Union[str, None]]
    read_only: bool
    title: str
    url: str
    verified: bool


__all__ = (
    "WebhookDeployKeyDeletedType",
    "WebhookDeployKeyDeletedPropKeyType",
)
