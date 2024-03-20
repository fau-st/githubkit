"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild

from .group_0357 import EnterpriseWebhooks
from .group_0358 import SimpleInstallation
from .group_0360 import RepositoryWebhooks
from .group_0361 import SimpleUserWebhooks
from .group_0359 import OrganizationSimpleWebhooks
from .group_0650 import WebhookPullRequestEditedPropPullRequest


class WebhookPullRequestEdited(GitHubModel):
    """pull_request edited event"""

    action: Literal["edited"] = Field()
    changes: WebhookPullRequestEditedPropChanges = Field(
        description="The changes to the comment if the action was `edited`."
    )
    enterprise: Missing[EnterpriseWebhooks] = Field(
        default=UNSET,
        title="Enterprise",
        description='An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured\non an enterprise account or an organization that\'s part of an enterprise account. For more information,\nsee "[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts)."\n',
    )
    installation: Missing[SimpleInstallation] = Field(
        default=UNSET,
        title="Simple Installation",
        description='The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured\nfor and sent to a GitHub App. For more information,\nsee "[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps)."',
    )
    number: int = Field(description="The pull request number.")
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    pull_request: WebhookPullRequestEditedPropPullRequest = Field()
    repository: RepositoryWebhooks = Field(
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: Missing[SimpleUserWebhooks] = Field(
        default=UNSET,
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookPullRequestEditedPropChanges(GitHubModel):
    """WebhookPullRequestEditedPropChanges

    The changes to the comment if the action was `edited`.
    """

    base: Missing[WebhookPullRequestEditedPropChangesPropBase] = Field(default=UNSET)
    body: Missing[WebhookPullRequestEditedPropChangesPropBody] = Field(default=UNSET)
    title: Missing[WebhookPullRequestEditedPropChangesPropTitle] = Field(default=UNSET)


class WebhookPullRequestEditedPropChangesPropBody(GitHubModel):
    """WebhookPullRequestEditedPropChangesPropBody"""

    from_: str = Field(
        alias="from",
        description="The previous version of the body if the action was `edited`.",
    )


class WebhookPullRequestEditedPropChangesPropTitle(GitHubModel):
    """WebhookPullRequestEditedPropChangesPropTitle"""

    from_: str = Field(
        alias="from",
        description="The previous version of the title if the action was `edited`.",
    )


class WebhookPullRequestEditedPropChangesPropBase(GitHubModel):
    """WebhookPullRequestEditedPropChangesPropBase"""

    ref: WebhookPullRequestEditedPropChangesPropBasePropRef = Field()
    sha: WebhookPullRequestEditedPropChangesPropBasePropSha = Field()


class WebhookPullRequestEditedPropChangesPropBasePropRef(GitHubModel):
    """WebhookPullRequestEditedPropChangesPropBasePropRef"""

    from_: str = Field(alias="from")


class WebhookPullRequestEditedPropChangesPropBasePropSha(GitHubModel):
    """WebhookPullRequestEditedPropChangesPropBasePropSha"""

    from_: str = Field(alias="from")


model_rebuild(WebhookPullRequestEdited)
model_rebuild(WebhookPullRequestEditedPropChanges)
model_rebuild(WebhookPullRequestEditedPropChangesPropBody)
model_rebuild(WebhookPullRequestEditedPropChangesPropTitle)
model_rebuild(WebhookPullRequestEditedPropChangesPropBase)
model_rebuild(WebhookPullRequestEditedPropChangesPropBasePropRef)
model_rebuild(WebhookPullRequestEditedPropChangesPropBasePropSha)

__all__ = (
    "WebhookPullRequestEdited",
    "WebhookPullRequestEditedPropChanges",
    "WebhookPullRequestEditedPropChangesPropBody",
    "WebhookPullRequestEditedPropChangesPropTitle",
    "WebhookPullRequestEditedPropChangesPropBase",
    "WebhookPullRequestEditedPropChangesPropBasePropRef",
    "WebhookPullRequestEditedPropChangesPropBasePropSha",
)
