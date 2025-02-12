# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Donor", "Contact", "Creator", "ImageFile", "Metadata", "MetadataLivingDonorData", "MetadataOrganDonorData"]


class Contact(BaseModel):
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


class Creator(BaseModel):
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


class ImageFile(BaseModel):
    description: Optional[str] = None
    """A description of the file.

    The Dataset.thumbnail_file does not have this file description.
    """

    file_uuid: Optional[str] = None
    """The HuBMAP unique identifier for the file."""

    filename: Optional[str] = None
    """The name of the file."""


class MetadataLivingDonorData(BaseModel):
    code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS source vocabulary terms.
    """

    concept_id: Optional[str] = None
    """This is the Concept ID from the HuBMAP Knowledge Graph.

    Currently limited to UMLS concepts.
    """

    data_type: Optional[Literal["Nominal", "Numeric"]] = None
    """This is the data type of thw record.

    Numeric types will generally have non-null data_value. Nominal types will
    generally have null data_value.
    """

    data_value: Optional[str] = None
    """The data value of the record."""

    end_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the end of this event (this is to construct time series records of clinical data
    for event-level data not donor-level data). An epty of zero value designates
    missing data or that this field is not applicable for the concept
    """

    graph_version: Optional[str] = None
    """
    This is the version of the HuBMAP Knowledge Graph that the Concept appears in,
    currently the version of UMLS that is used.
    """

    grouping_code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS vocabulary codes. This code corresponds to the grouping_concept.
    """

    grouping_concept: Optional[str] = None
    """
    This is the Concept ID from the HuBMAP Knowledge Graph, currently limited to
    UMLS concetps, that is to be used for grouping the record.
    """

    grouping_concept_preferred_term: Optional[str] = None
    """
    This is the preferred display term for the facet in which this record should be
    counted for faceted search in the portal. It may or may not correspond to a term
    in UMLS for the grouping concept.
    """

    grouping_sab: Optional[str] = None
    """
    This is a grouping for the source vocabulary in the HuBMAP Knowledge Graph,
    currently limited to UMLS source vocabularies.. This sab corresponds to the
    grouping_code.
    """

    numeric_operator: Optional[Literal["EQ", "GT", "LT"]] = None
    """
    This is the numeric operator for the data value .This enables inputing
    thresholds and ranges for data values by using greater than or less than.
    """

    preferred_term: Optional[str] = None
    """This is the preferred display term for the item.

    It may or may not correspond to a term in UMLS for this concept.
    """

    sab: Optional[str] = None
    """This is the source vocabulary in the HuBMAP Knowledge Graph.

    Currently limited to UMLS source vocabularies.
    """

    start_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the start of this event (this is to construct time series records of clinical
    data for event-level data not donor-level data). An empty or zero value
    designates missing data or that this field is not applicable for the concept.
    """

    units: Optional[str] = None
    """This are the units for the data value."""


class MetadataOrganDonorData(BaseModel):
    code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS source vocabulary terms.
    """

    concept_id: Optional[str] = None
    """This is the Concept ID from the HuBMAP Knowledge Graph.

    Currently limited to UMLS concepts.
    """

    data_type: Optional[Literal["Nominal", "Numeric"]] = None
    """This is the data type of thw record.

    Numeric types will generally have non-null data_value. Nominal types will
    generally have null data_value.
    """

    data_value: Optional[str] = None
    """The data value of the record."""

    end_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the end of this event (this is to construct time series records of clinical data
    for event-level data not donor-level data). An epty of zero value designates
    missing data or that this field is not applicable for the concept
    """

    graph_version: Optional[str] = None
    """
    This is the version of the HuBMAP Knowledge Graph that the Concept appears in,
    currently the version of UMLS that is used.
    """

    grouping_code: Optional[str] = None
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS vocabulary codes. This code corresponds to the grouping_concept.
    """

    grouping_concept: Optional[str] = None
    """
    This is the Concept ID from the HuBMAP Knowledge Graph, currently limited to
    UMLS concetps, that is to be used for grouping the record.
    """

    grouping_concept_preferred_term: Optional[str] = None
    """
    This is the preferred display term for the facet in which this record should be
    counted for faceted search in the portal. It may or may not correspond to a term
    in UMLS for the grouping concept.
    """

    grouping_sab: Optional[str] = None
    """
    This is a grouping for the source vocabulary in the HuBMAP Knowledge Graph,
    currently limited to UMLS source vocabularies.. This sab corresponds to the
    grouping_code.
    """

    numeric_operator: Optional[Literal["EQ", "GT", "LT"]] = None
    """
    This is the numeric operator for the data value .This enables inputing
    thresholds and ranges for data values by using greater than or less than.
    """

    preferred_term: Optional[str] = None
    """This is the preferred display term for the item.

    It may or may not correspond to a term in UMLS for this concept.
    """

    sab: Optional[str] = None
    """This is the source vocabulary in the HuBMAP Knowledge Graph.

    Currently limited to UMLS source vocabularies.
    """

    start_datetime: Optional[int] = None
    """
    This is the approximate time difference in seconds between the procurement and
    the start of this event (this is to construct time series records of clinical
    data for event-level data not donor-level data). An empty or zero value
    designates missing data or that this field is not applicable for the concept.
    """

    units: Optional[str] = None
    """This are the units for the data value."""


class Metadata(BaseModel):
    living_donor_data: Optional[List[MetadataLivingDonorData]] = None
    """Information about the donor who's tissue was used.

    The tissue was obtained during a procedure. Only living_donor_data or
    organ_donor_data, not both can be defined for a single donor.
    """

    organ_donor_data: Optional[List[MetadataOrganDonorData]] = None
    """Information about the donor who's organ(s) was/were used.

    The organ was obtained via an organ donation program from a deceaced donor. Only
    living_donor_data or organ_donor_data, not both can be defined for a single
    donor.
    """


class Donor(BaseModel):
    contacts: Optional[List[Contact]] = None
    """
    A list of the people who are the main contacts to get information about the
    entity.
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

    creators: Optional[List[Creator]] = None
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    data_access_level: Optional[Literal["consortium", "public"]] = None
    """One of the values: public, consortium"""

    description: Optional[str] = None
    """Free text description of the donor"""

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

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

    image_files: Optional[List[ImageFile]] = None
    """List of uploaded image files and descriptions of the files.

    Stored in db as a stringfied json array.
    """

    lab_donor_id: Optional[str] = None
    """A lab specific identifier for the donor."""

    label: Optional[str] = None
    """Lab provided, de-identified name for the donor"""

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

    metadata: Optional[Metadata] = None
    """Donor metadata as an array of UMLS codes and descriptions"""

    protocol_url: Optional[str] = None
    """
    The protocols.io doi url pointing the protocol describing the donor selection,
    inclusion/exclusion criteria
    """

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    submission_id: Optional[str] = None
    """The hubmap internal id with embedded semantic information e.g.: VAN0003.

    This id is generated at creation time which tracks the lab, donor, organ and
    sample hierarchy per the following:
    https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing
    """

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """
