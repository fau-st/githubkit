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


class WebhookInstallationTargetRenamedType(TypedDict):
    """WebhookInstallationTargetRenamed"""

    account: WebhookInstallationTargetRenamedPropAccountType
    action: Literal["renamed"]
    changes: WebhookInstallationTargetRenamedPropChangesType
    enterprise: NotRequired[EnterpriseWebhooksType]
    installation: SimpleInstallationType
    organization: NotRequired[OrganizationSimpleWebhooksType]
    repository: NotRequired[RepositoryWebhooksType]
    sender: NotRequired[SimpleUserWebhooksType]
    target_type: str


class WebhookInstallationTargetRenamedPropAccountType(TypedDict):
    """WebhookInstallationTargetRenamedPropAccount"""

    archived_at: NotRequired[Union[str, None]]
    avatar_url: str
    created_at: NotRequired[str]
    description: NotRequired[None]
    events_url: NotRequired[str]
    followers: NotRequired[int]
    followers_url: NotRequired[str]
    following: NotRequired[int]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    has_organization_projects: NotRequired[bool]
    has_repository_projects: NotRequired[bool]
    hooks_url: NotRequired[str]
    html_url: str
    id: int
    is_verified: NotRequired[bool]
    issues_url: NotRequired[str]
    login: NotRequired[str]
    members_url: NotRequired[str]
    name: NotRequired[str]
    node_id: str
    organizations_url: NotRequired[str]
    public_gists: NotRequired[int]
    public_members_url: NotRequired[str]
    public_repos: NotRequired[int]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    slug: NotRequired[str]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    updated_at: NotRequired[str]
    url: NotRequired[str]
    website_url: NotRequired[None]


class WebhookInstallationTargetRenamedPropChangesType(TypedDict):
    """WebhookInstallationTargetRenamedPropChanges"""

    login: NotRequired[WebhookInstallationTargetRenamedPropChangesPropLoginType]
    slug: NotRequired[WebhookInstallationTargetRenamedPropChangesPropSlugType]


class WebhookInstallationTargetRenamedPropChangesPropLoginType(TypedDict):
    """WebhookInstallationTargetRenamedPropChangesPropLogin"""

    from_: str


class WebhookInstallationTargetRenamedPropChangesPropSlugType(TypedDict):
    """WebhookInstallationTargetRenamedPropChangesPropSlug"""

    from_: str


__all__ = (
    "WebhookInstallationTargetRenamedType",
    "WebhookInstallationTargetRenamedPropAccountType",
    "WebhookInstallationTargetRenamedPropChangesType",
    "WebhookInstallationTargetRenamedPropChangesPropLoginType",
    "WebhookInstallationTargetRenamedPropChangesPropSlugType",
)
