# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["Upload"]


class Upload(TypedDict, total=False):
    dataset_uuids_to_link: List[str]
    """List of datasets to add to the Upload.

    Provide as a json array of the dataset uuids like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    dataset_uuids_to_unlink: List[str]
    """List of datasets to remove from a Upload.

    Provide as a json array of the dataset uuids like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    description: str
    """Free text description of the data being submitted."""

    group_uuid: str
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    status: str
    """One of: New|Valid|Invalid|Error|Submitted"""

    title: str
    """Title of the datasets, a sentance or less"""

    validation_message: str
    """
    A message from the validataion tools describing what is invalid with the upload.
    """
