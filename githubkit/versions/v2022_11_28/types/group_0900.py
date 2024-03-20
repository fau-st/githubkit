"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired


class OrgsOrgPropertiesSchemaCustomPropertyNamePutBodyType(TypedDict):
    """OrgsOrgPropertiesSchemaCustomPropertyNamePutBody"""

    value_type: Literal["string", "single_select"]
    required: NotRequired[bool]
    default_value: NotRequired[Union[str, None]]
    description: NotRequired[Union[str, None]]
    allowed_values: NotRequired[Union[List[str], None]]


__all__ = ("OrgsOrgPropertiesSchemaCustomPropertyNamePutBodyType",)
