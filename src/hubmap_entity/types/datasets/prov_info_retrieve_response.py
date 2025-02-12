# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProvInfoRetrieveResponse"]


class ProvInfoRetrieveResponse(BaseModel):
    dataset_created_by_email: Optional[str] = None
    """the email address of the person who created the dataset"""

    dataset_data_types: Optional[str] = None
    """
    the data/assay types (can be multiple types for pipeline derived data, so a
    comma separated list for tsv output or a json array for json output)
    """

    dataset_date_time_created: Optional[str] = None
    """the date/time that the dataset was created"""

    dataset_date_time_modified: Optional[str] = None
    """the date/time that the dataset was last modified"""

    dataset_group_name: Optional[str] = None
    """name of the data provider group who created the dataset"""

    dataset_group_uuid: Optional[str] = None
    """internal id for the data provider group"""

    dataset_hubmap_id: Optional[str] = None
    """The HuBMAP ID of the dataset like HBM123.ABCD.456"""

    dataset_lab_id: Optional[str] = None
    """identifier used by the data provider"""

    dataset_modified_by_email: Optional[str] = None
    """the email address of the person who last modified the dataset"""

    dataset_portl_url: Optional[str] = None
    """the url to open the dataset in the data portal"""

    dataset_status: Optional[str] = None
    """status of the dataset New, QA, Published, etc ..."""

    dataset_uuid: Optional[str] = None
    """The uuid of the dataset"""

    donor_group_name: Optional[List[str]] = None

    donor_hubmap_id: Optional[List[str]] = None

    donor_uuid: Optional[List[str]] = None

    donor_submission_id: Optional[List[str]] = FieldInfo(alias="donor:submission_id", default=None)

    first_sample_hubmap_id: Optional[List[str]] = None

    first_sample_portal_url: Optional[List[str]] = None

    first_sample_submission_id: Optional[List[str]] = None

    first_sample_type: Optional[List[str]] = None

    first_sample_uuid: Optional[List[str]] = None

    organ_hubmap_id: Optional[List[str]] = None

    organ_submission_id: Optional[List[str]] = None

    organ_type: Optional[List[str]] = None

    organ_uuid: Optional[List[str]] = None

    rui_location_hubmap_id: Optional[List[str]] = None

    rui_location_submission_id: Optional[List[str]] = None

    rui_location_uuid: Optional[List[str]] = None

    sample_metadata_hubmap_id: Optional[List[str]] = None

    sample_metadata_submission_id: Optional[List[str]] = None

    sample_metadata_uuid: Optional[List[str]] = None
