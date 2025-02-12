# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProvInfoListAllParams"]


class ProvInfoListAllParams(TypedDict, total=False):
    dataset_status: Literal["qa", "new", "published"]
    """Case insensitive string indicating the current status of a dataset"""

    format: Literal["json", "tsv"]
    """A case insensitive string.

    Any value besides 'json' will have no effect. If the string is 'json',
    provenance info will be returned as a json. Otherwise, it will be returned as a
    tsv file
    """

    group_uuid: str
    """The uuid of the group"""

    has_rui_info: Literal["true", "false"]
    """A case insensitive string.

    Any value besides true or false will cause a 400 exception.
    """

    organ: str
    """Case insensitive string for 2 character organ code.

    Values must be present on organ yaml or a 400 exception is raised
    """
