# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RetrieveSamplesProvenanceInfoRetrieveSamplesProvenanceInfoResponse"]


class RetrieveSamplesProvenanceInfoRetrieveSamplesProvenanceInfoResponse(BaseModel):
    donor_has_metadata: Optional[str] = None
    """True or false value corresponding to whether the donor has metadata info"""

    donor_uuid: Optional[str] = None
    """The UUID of the donor associated to this sample in the provenance chain"""

    lab_tissue_sample_id: Optional[str] = None
    """identifier used by the data provider"""

    organ_has_metadata: Optional[str] = None
    """True or false value corresponding to whether the organ has metadata info"""

    organ_type: Optional[str] = None
    """
    The organ type of the organ associated to this sample in the provenance chain
    (return the organ code resolved to the organ name via the organ.yaml file)
    """

    organ_uuid: Optional[str] = None
    """UUID of the organ associated to this sample in the provenance chain.

    If the sample is itself an organ, the id will be the same as sample uuid.
    """

    sample_ancestor_entity: Optional[str] = None
    """the entity type of the nearest ancestor to the sample.

    Will be a donor or another sample
    """

    sample_ancestor_id: Optional[str] = None
    """uuid of the donor or sample nearest to this dataset in the provenance chain"""

    sample_created_by_email: Optional[str] = None
    """the email address of the person who created the sample"""

    sample_group_name: Optional[str] = None
    """name of the data provider group who created the sample"""

    sample_has_metadata: Optional[str] = None
    """True or false value corresponding to whether the sample has metadata info"""

    sample_has_rui_info: Optional[bool] = None
    """True or false value corresponding to whether the sample has rui_location info."""

    sample_uuid: Optional[str] = None
    """The uuid of the sample"""
