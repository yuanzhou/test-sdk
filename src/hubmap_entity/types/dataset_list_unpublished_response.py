# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DatasetListUnpublishedResponse"]


class DatasetListUnpublishedResponse(BaseModel):
    data_types: Optional[str] = None
    """the data_types of the unpublished dataset"""

    donor_hubmap_id: Optional[str] = None
    """the hubmap_id of the unpublished dataset's donor"""

    donor_submission_id: Optional[str] = None
    """the submission id of the unpublished dataset's donor"""

    hubmap_id: Optional[str] = None
    """the hubmap_id of the unpublished dataset"""

    organ: Optional[str] = None
    """
    the organ type of the sample with sample_category organ above the unpublished
    dataset if applicable
    """

    organization: Optional[str] = None
    """the group_name of the unpublished dataset"""

    provider_experiment_id: Optional[str] = None
    """the lab_dataset_id of the unpublished dataset"""

    uuid: Optional[str] = None
    """The unique identifier for the unpublished dataset"""
