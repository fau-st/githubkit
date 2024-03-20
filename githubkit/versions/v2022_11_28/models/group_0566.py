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
from .group_0567 import (
    WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase,
)


class WebhookMarketplacePurchasePendingChangeCancelled(GitHubModel):
    """marketplace_purchase pending_change_cancelled event"""

    action: Literal["pending_change_cancelled"] = Field()
    effective_date: str = Field()
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
    marketplace_purchase: (
        WebhookMarketplacePurchasePendingChangeCancelledPropMarketplacePurchase
    ) = Field()
    organization: Missing[OrganizationSimpleWebhooks] = Field(
        default=UNSET,
        title="Organization Simple",
        description="A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an\norganization, or when the event occurs from activity in a repository owned by an organization.",
    )
    previous_marketplace_purchase: Missing[
        WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchase
    ] = Field(default=UNSET, title="Marketplace Purchase")
    repository: Missing[RepositoryWebhooks] = Field(
        default=UNSET,
        title="Repository",
        description="The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property\nwhen the event occurs from activity in a repository.",
    )
    sender: SimpleUserWebhooks = Field(
        title="Simple User",
        description="The GitHub user that triggered the event. This property is included in every webhook payload.",
    )


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchase(
    GitHubModel
):
    """Marketplace Purchase"""

    account: WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccount = (Field())
    billing_cycle: str = Field()
    free_trial_ends_on: None = Field()
    next_billing_date: Missing[Union[str, None]] = Field(default=UNSET)
    on_free_trial: bool = Field()
    plan: WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlan = (Field())
    unit_count: int = Field()


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseP
    ropAccount
    """

    id: int = Field()
    login: str = Field()
    node_id: str = Field()
    organization_billing_email: Union[str, None] = Field()
    type: str = Field()


class WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchaseP
    ropPlan
    """

    bullets: List[str] = Field()
    description: str = Field()
    has_free_trial: bool = Field()
    id: int = Field()
    monthly_price_in_cents: int = Field()
    name: str = Field()
    price_model: Literal["FREE", "FLAT_RATE", "PER_UNIT"] = Field()
    unit_name: Union[str, None] = Field()
    yearly_price_in_cents: int = Field()


model_rebuild(WebhookMarketplacePurchasePendingChangeCancelled)
model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchase
)
model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccount
)
model_rebuild(
    WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlan
)

__all__ = (
    "WebhookMarketplacePurchasePendingChangeCancelled",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchase",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropAccount",
    "WebhookMarketplacePurchasePendingChangeCancelledPropPreviousMarketplacePurchasePropPlan",
)
