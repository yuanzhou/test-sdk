# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DatasetRetrieveSankeyDataResponse"]


class DatasetRetrieveSankeyDataResponse(BaseModel):
    dataset_data_types: Optional[str] = None
    """the data/assay types (if more than one, output is a comma separated string)"""

    dataset_group_name: Optional[str] = None
    """
    The displayname of globus group which the user who created this entity is a
    member of
    """

    dataset_status: Optional[str] = None
    """status of the dataset New, QA, Published, etc ..."""

    organ_type: Optional[str] = None
    """The organ type of the organ associated to this dataset in the provenance chain"""
