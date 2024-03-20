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


class WebhookProjectDeletedType(TypedDict):
    """project deleted event"""

    action: Literal["deleted"]
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: NotRequired[SimpleInstallationType]
    organization: NotRequired[OrganizationSimpleWebhooksType]
    project: WebhookProjectDeletedPropProjectType
    repository: NotRequired[Union[None, RepositoryWebhooksType]]
    sender: NotRequired[SimpleUserWebhooksType]


class WebhookProjectDeletedPropProjectType(TypedDict):
    """Project"""

    body: Union[str, None]
    columns_url: str
    created_at: datetime
    creator: Union[WebhookProjectDeletedPropProjectPropCreatorType, None]
    html_url: str
    id: int
    name: str
    node_id: str
    number: int
    owner_url: str
    state: Literal["open", "closed"]
    updated_at: datetime
    url: str


class WebhookProjectDeletedPropProjectPropCreatorType(TypedDict):
    """User"""

    avatar_url: NotRequired[str]
    deleted: NotRequired[bool]
    email: NotRequired[Union[str, None]]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: int
    login: str
    name: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[Literal["Bot", "User", "Organization"]]
    url: NotRequired[str]


__all__ = (
    "WebhookProjectDeletedType",
    "WebhookProjectDeletedPropProjectType",
    "WebhookProjectDeletedPropProjectPropCreatorType",
)
