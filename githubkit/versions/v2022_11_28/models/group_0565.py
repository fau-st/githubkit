"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1(GitHubModel):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1"""

    account: Missing[
        WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropAccount
    ] = Field(default=UNSET)
    billing_cycle: Missing[str] = Field(default=UNSET)
    free_trial_ends_on: Missing[Union[str, None]] = Field(default=UNSET)
    next_billing_date: Union[str, None] = Field()
    on_free_trial: Missing[bool] = Field(default=UNSET)
    plan: Missing[
        WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropPlan
    ] = Field(default=UNSET)
    unit_count: Missing[int] = Field(default=UNSET)


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropAccount(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropAccount"""

    id: Missing[int] = Field(default=UNSET)
    login: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    organization_billing_email: Missing[Union[str, None]] = Field(default=UNSET)
    type: Missing[str] = Field(default=UNSET)


class WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropPlan(
    GitHubModel
):
    """WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropPlan"""

    bullets: Missing[List[Union[str, None]]] = Field(default=UNSET)
    description: Missing[str] = Field(default=UNSET)
    has_free_trial: Missing[bool] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    monthly_price_in_cents: Missing[int] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    price_model: Missing[Literal["FREE", "FLAT_RATE", "PER_UNIT"]] = Field(
        default=UNSET
    )
    unit_name: Missing[Union[str, None]] = Field(default=UNSET)
    yearly_price_in_cents: Missing[int] = Field(default=UNSET)


model_rebuild(WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1)
model_rebuild(
    WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropAccount
)
model_rebuild(
    WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropPlan
)

__all__ = (
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropAccount",
    "WebhookMarketplacePurchasePendingChangePropMarketplacePurchaseAllof1PropPlan",
)
