# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .shared_params import dataset

__all__ = ["DatasetCreateComponentsParams", "Dataset"]


class DatasetCreateComponentsParams(TypedDict, total=False):
    creation_action: str
    """the action event that will describe the activity node.

    Allowed valuese are "Multi-Assay Split"
    """

    datasets: Iterable[Dataset]

    direct_ancestor_uuids: str
    """the uuid for the parent multi assay dataset"""

    group_uuid: str
    """the group uuid for the new component datasets"""


class Dataset(dataset.Dataset):
    dataset_link_abs_dir: str
    """
    The file path to the component's sub-directory beneath the ancestor dataset on
    globus. The created symbolic link will point to this subdirectory
    """
