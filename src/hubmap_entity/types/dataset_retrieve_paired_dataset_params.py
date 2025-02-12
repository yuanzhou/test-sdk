# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetRetrievePairedDatasetParams"]


class DatasetRetrievePairedDatasetParams(TypedDict, total=False):
    data_type: Required[str]
    """The desired data_type to be searched for"""

    search_depth: int
    """
    The maximum number of generations of datasets beneath the sample to search for
    the paired dataset
    """
