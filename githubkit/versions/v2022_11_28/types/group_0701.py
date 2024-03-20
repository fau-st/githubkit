"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0704 import WebhookReleasePublishedPropReleaseAllof0PropReactionsType
from .group_0702 import WebhookReleasePublishedPropReleaseAllof0PropAssetsItemsType


class WebhookReleasePublishedPropReleaseAllof0Type(TypedDict):
    """Release

    The [release](https://docs.github.com/rest/releases/releases/#get-a-release)
    object.
    """

    assets: List[WebhookReleasePublishedPropReleaseAllof0PropAssetsItemsType]
    assets_url: str
    author: Union[WebhookReleasePublishedPropReleaseAllof0PropAuthorType, None]
    body: Union[str, None]
    created_at: Union[datetime, None]
    discussion_url: NotRequired[str]
    draft: bool
    html_url: str
    id: int
    name: Union[str, None]
    node_id: str
    prerelease: bool
    published_at: Union[datetime, None]
    reactions: NotRequired[WebhookReleasePublishedPropReleaseAllof0PropReactionsType]
    tag_name: str
    tarball_url: Union[str, None]
    target_commitish: str
    upload_url: str
    url: str
    zipball_url: Union[str, None]


class WebhookReleasePublishedPropReleaseAllof0PropAuthorType(TypedDict):
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
    "WebhookReleasePublishedPropReleaseAllof0Type",
    "WebhookReleasePublishedPropReleaseAllof0PropAuthorType",
)
