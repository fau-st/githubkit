import openapi_schema_pydantic as oas

from ...source import Source
from .schema import IntSchema


def build_int_schema(source: Source) -> IntSchema:
    try:
        data = oas.Schema.parse_obj(source.data)
    except Exception as e:
        raise TypeError(f"Invalid Schema from {source.uri}") from e

    return IntSchema(
        title=data.title,
        description=data.description,
        default=data.default,
        examples=data.examples or (data.example and [data.example]),
        multiple_of=data.multipleOf,
        maximum=data.maximum,
        exclusive_maximum=data.exclusiveMaximum,
        minimum=data.minimum,
        exclusive_minimum=data.exclusiveMinimum,
    )
