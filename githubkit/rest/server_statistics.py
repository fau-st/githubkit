"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import ServerStatisticsItems

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class ServerStatisticsClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_server_statistics(
        self,
        enterprise_or_org: str,
        date_start: Union[Unset, str] = UNSET,
        date_end: Union[Unset, str] = UNSET,
    ) -> "Response[List[ServerStatisticsItems]]":
        url = f"/enterprise-installation/{enterprise_or_org}/server-statistics"

        params = {
            "date_start": date_start,
            "date_end": date_end,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[ServerStatisticsItems],
        )

    async def async_get_server_statistics(
        self,
        enterprise_or_org: str,
        date_start: Union[Unset, str] = UNSET,
        date_end: Union[Unset, str] = UNSET,
    ) -> "Response[List[ServerStatisticsItems]]":
        url = f"/enterprise-installation/{enterprise_or_org}/server-statistics"

        params = {
            "date_start": date_start,
            "date_end": date_end,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=List[ServerStatisticsItems],
        )
