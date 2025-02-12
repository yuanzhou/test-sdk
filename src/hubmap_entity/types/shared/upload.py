# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Upload"]


class Upload(BaseModel):
    created_by_user_displayname: Optional[str] = None
    """The name of the person or process authenticated when creating the object"""

    created_by_user_email: Optional[str] = None
    """
    The email address of the person or process authenticated when creating the
    object.
    """

    created_by_user_sub: Optional[str] = None
    """
    The subject id as provided by the authorization mechanism for the person or
    process authenticated when creating the object.
    """

    created_timestamp: Optional[int] = None
    """The timestamp of when the node was created.

    The format is an integer representing milliseconds since midnight Jan 1, 1970
    """

    datasets: Optional[List["Dataset"]] = None
    """The datasets that are contained in this Upload."""

    description: Optional[str] = None
    """Free text description of the data being submitted."""

    entity_type: Optional[str] = None
    """One of the normalized entity types: Dataset, Collection, Sample, Donor, Upload"""

    group_name: Optional[str] = None
    """
    The displayname of globus group which the user who created this entity is a
    member of
    """

    group_uuid: Optional[str] = None
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    hubmap_id: Optional[str] = None
    """
    A HuBMAP Consortium wide unique identifier randomly generated in the format
    HBM###.ABCD.### for every entity.
    """

    last_modified_timestamp: Optional[int] = None
    """The timestamp of when the object was last modified.

    The format is an integer representing milliseconds since midnight, Jan 1, 1970
    """

    last_modified_user_displayname: Optional[str] = None
    """
    The name of the person or process which authenticated when the object was last
    modified.
    """

    last_modified_user_email: Optional[str] = None
    """
    The email address of the person or process which authenticated when the object
    was last modified.
    """

    last_modified_user_sub: Optional[str] = None
    """
    The subject id of the user who last modified the entity as provided by the
    authorization mechanism for the person or process authenticated when the object
    was modified.
    """

    status: Optional[str] = None
    """One of: New|Valid|Invalid|Error|Submitted"""

    title: Optional[str] = None
    """Title of the datasets, a sentance or less"""

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """

    validation_message: Optional[str] = None
    """
    A message from the validataion tools describing what is invalid with the upload.
    """


from .dataset import Dataset

if PYDANTIC_V2:
    Upload.model_rebuild()
else:
    Upload.update_forward_refs()  # type: ignore
