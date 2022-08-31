"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, Union, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import Root, ApiOverview

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class MetaClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def root(
        self,
    ) -> "Response[Root]":
        url = "/"

        return self._github.request(
            "GET",
            url,
            response_model=Root,
        )

    async def async_root(
        self,
    ) -> "Response[Root]":
        url = "/"

        return await self._github.arequest(
            "GET",
            url,
            response_model=Root,
        )

    def get(
        self,
    ) -> "Response[ApiOverview]":
        url = "/meta"

        return self._github.request(
            "GET",
            url,
            response_model=ApiOverview,
        )

    async def async_get(
        self,
    ) -> "Response[ApiOverview]":
        url = "/meta"

        return await self._github.arequest(
            "GET",
            url,
            response_model=ApiOverview,
        )

    def get_octocat(
        self,
        s: Union[Unset, str] = UNSET,
    ) -> "Response[str]":
        url = "/octocat"

        params = {
            "s": s,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=str,
        )

    async def async_get_octocat(
        self,
        s: Union[Unset, str] = UNSET,
    ) -> "Response[str]":
        url = "/octocat"

        params = {
            "s": s,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=str,
        )

    def get_zen(
        self,
    ) -> "Response[str]":
        url = "/zen"

        return self._github.request(
            "GET",
            url,
            response_model=str,
        )

    async def async_get_zen(
        self,
    ) -> "Response[str]":
        url = "/zen"

        return await self._github.arequest(
            "GET",
            url,
            response_model=str,
        )
