# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EntityListTupletsParams"]


class EntityListTupletsParams(TypedDict, total=False):
    property_key: Literal["uuid"]
    """A case insensitive string.

    Any value besides 'uuid' will raise an error. If property_key=uuid is provided,
    rather than entire dictionary representations of each node, only the list of
    matching uuid's will be returned
    """

    status: Literal["new", "qa", "published"]
    """A case insensitive string.

    Any value besides 'new', 'qa', and 'published' will raise an error. If a valid
    status is provided, only results matching that status (if they are datasets)
    will be returned
    """
