# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypeAlias

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = [
    "EntityListCollectionsResponse",
    "EntityListCollectionsResponseItem",
    "EntityListCollectionsResponseItemContact",
    "EntityListCollectionsResponseItemContributor",
]


class EntityListCollectionsResponseItemContact(BaseModel):
    affiliation: Optional[str] = None
    """The institution that the person is affiliated with."""

    first_name: Optional[str] = None
    """The full name of the person."""

    last_name: Optional[str] = None
    """The last name of the person."""

    middle_name_or_initial: Optional[str] = None
    """The middle name or initial of the person."""

    orcid_id: Optional[str] = None
    """The ORCID iD of the person."""


class EntityListCollectionsResponseItemContributor(BaseModel):
    affiliation: Optional[str] = None
    """The institution that the person is affiliated with."""

    first_name: Optional[str] = None
    """The full name of the person."""

    last_name: Optional[str] = None
    """The last name of the person."""

    middle_name_or_initial: Optional[str] = None
    """The middle name or initial of the person."""

    orcid_id: Optional[str] = None
    """The ORCID iD of the person."""


class EntityListCollectionsResponseItem(BaseModel):
    contacts: Optional[List[EntityListCollectionsResponseItemContact]] = None
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contributors: Optional[List[EntityListCollectionsResponseItemContributor]] = None
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

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
    """The datasets that are contained in the Collection."""

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

    entity_type: Optional[str] = None
    """One of the normalized entity types: Dataset, Collection, Sample, Donor"""

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

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    title: Optional[str] = None
    """The title of the Collection"""

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """


EntityListCollectionsResponse: TypeAlias = List[EntityListCollectionsResponseItem]

from .shared.dataset import Dataset

if PYDANTIC_V2:
    EntityListCollectionsResponseItem.model_rebuild()
    EntityListCollectionsResponseItemContact.model_rebuild()
    EntityListCollectionsResponseItemContributor.model_rebuild()
else:
    EntityListCollectionsResponseItem.update_forward_refs()  # type: ignore
    EntityListCollectionsResponseItemContact.update_forward_refs()  # type: ignore
    EntityListCollectionsResponseItemContributor.update_forward_refs()  # type: ignore
