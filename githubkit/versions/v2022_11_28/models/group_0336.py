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
from githubkit.compat import GitHubModel, model_rebuild

from .group_0050 import MinimalRepository
from .group_0335 import SearchResultTextMatchesItems


class CodeSearchResultItem(GitHubModel):
    """Code Search Result Item

    Code Search Result Item
    """

    name: str = Field()
    path: str = Field()
    sha: str = Field()
    url: str = Field()
    git_url: str = Field()
    html_url: str = Field()
    repository: MinimalRepository = Field(
        title="Minimal Repository", description="Minimal Repository"
    )
    score: float = Field()
    file_size: Missing[int] = Field(default=UNSET)
    language: Missing[Union[str, None]] = Field(default=UNSET)
    last_modified_at: Missing[datetime] = Field(default=UNSET)
    line_numbers: Missing[List[str]] = Field(default=UNSET)
    text_matches: Missing[List[SearchResultTextMatchesItems]] = Field(
        default=UNSET, title="Search Result Text Matches"
    )


class SearchCodeGetResponse200(GitHubModel):
    """SearchCodeGetResponse200"""

    total_count: int = Field()
    incomplete_results: bool = Field()
    items: List[CodeSearchResultItem] = Field()


model_rebuild(CodeSearchResultItem)
model_rebuild(SearchCodeGetResponse200)

__all__ = (
    "CodeSearchResultItem",
    "SearchCodeGetResponse200",
)
