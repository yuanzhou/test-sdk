# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["Donor", "Contact", "Creator", "Metadata", "MetadataLivingDonorData", "MetadataOrganDonorData"]


class Contact(TypedDict, total=False):
    affiliation: str
    """The institution that the person is affiliated with."""

    first_name: str
    """The full name of the person."""

    last_name: str
    """The last name of the person."""

    middle_name_or_initial: str
    """The middle name or initial of the person."""

    orcid_id: str
    """The ORCID iD of the person."""


class Creator(TypedDict, total=False):
    affiliation: str
    """The institution that the person is affiliated with."""

    first_name: str
    """The full name of the person."""

    last_name: str
    """The last name of the person."""

    middle_name_or_initial: str
    """The middle name or initial of the person."""

    orcid_id: str
    """The ORCID iD of the person."""


class MetadataLivingDonorData(TypedDict, total=False):
    code: str
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS source vocabulary terms.
    """

    concept_id: str
    """This is the Concept ID from the HuBMAP Knowledge Graph.

    Currently limited to UMLS concepts.
    """

    data_type: Literal["Nominal", "Numeric"]
    """This is the data type of thw record.

    Numeric types will generally have non-null data_value. Nominal types will
    generally have null data_value.
    """

    data_value: str
    """The data value of the record."""

    end_datetime: int
    """
    This is the approximate time difference in seconds between the procurement and
    the end of this event (this is to construct time series records of clinical data
    for event-level data not donor-level data). An epty of zero value designates
    missing data or that this field is not applicable for the concept
    """

    graph_version: str
    """
    This is the version of the HuBMAP Knowledge Graph that the Concept appears in,
    currently the version of UMLS that is used.
    """

    grouping_code: str
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS vocabulary codes. This code corresponds to the grouping_concept.
    """

    grouping_concept: str
    """
    This is the Concept ID from the HuBMAP Knowledge Graph, currently limited to
    UMLS concetps, that is to be used for grouping the record.
    """

    grouping_concept_preferred_term: str
    """
    This is the preferred display term for the facet in which this record should be
    counted for faceted search in the portal. It may or may not correspond to a term
    in UMLS for the grouping concept.
    """

    grouping_sab: str
    """
    This is a grouping for the source vocabulary in the HuBMAP Knowledge Graph,
    currently limited to UMLS source vocabularies.. This sab corresponds to the
    grouping_code.
    """

    numeric_operator: Literal["EQ", "GT", "LT"]
    """
    This is the numeric operator for the data value .This enables inputing
    thresholds and ranges for data values by using greater than or less than.
    """

    preferred_term: str
    """This is the preferred display term for the item.

    It may or may not correspond to a term in UMLS for this concept.
    """

    sab: str
    """This is the source vocabulary in the HuBMAP Knowledge Graph.

    Currently limited to UMLS source vocabularies.
    """

    start_datetime: int
    """
    This is the approximate time difference in seconds between the procurement and
    the start of this event (this is to construct time series records of clinical
    data for event-level data not donor-level data). An empty or zero value
    designates missing data or that this field is not applicable for the concept.
    """

    units: str
    """This are the units for the data value."""


class MetadataOrganDonorData(TypedDict, total=False):
    code: str
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS source vocabulary terms.
    """

    concept_id: str
    """This is the Concept ID from the HuBMAP Knowledge Graph.

    Currently limited to UMLS concepts.
    """

    data_type: Literal["Nominal", "Numeric"]
    """This is the data type of thw record.

    Numeric types will generally have non-null data_value. Nominal types will
    generally have null data_value.
    """

    data_value: str
    """The data value of the record."""

    end_datetime: int
    """
    This is the approximate time difference in seconds between the procurement and
    the end of this event (this is to construct time series records of clinical data
    for event-level data not donor-level data). An epty of zero value designates
    missing data or that this field is not applicable for the concept
    """

    graph_version: str
    """
    This is the version of the HuBMAP Knowledge Graph that the Concept appears in,
    currently the version of UMLS that is used.
    """

    grouping_code: str
    """
    This is a Code from a source vocabulary in the HuBMAP Knowledge Graph, currently
    limited to UMLS vocabulary codes. This code corresponds to the grouping_concept.
    """

    grouping_concept: str
    """
    This is the Concept ID from the HuBMAP Knowledge Graph, currently limited to
    UMLS concetps, that is to be used for grouping the record.
    """

    grouping_concept_preferred_term: str
    """
    This is the preferred display term for the facet in which this record should be
    counted for faceted search in the portal. It may or may not correspond to a term
    in UMLS for the grouping concept.
    """

    grouping_sab: str
    """
    This is a grouping for the source vocabulary in the HuBMAP Knowledge Graph,
    currently limited to UMLS source vocabularies.. This sab corresponds to the
    grouping_code.
    """

    numeric_operator: Literal["EQ", "GT", "LT"]
    """
    This is the numeric operator for the data value .This enables inputing
    thresholds and ranges for data values by using greater than or less than.
    """

    preferred_term: str
    """This is the preferred display term for the item.

    It may or may not correspond to a term in UMLS for this concept.
    """

    sab: str
    """This is the source vocabulary in the HuBMAP Knowledge Graph.

    Currently limited to UMLS source vocabularies.
    """

    start_datetime: int
    """
    This is the approximate time difference in seconds between the procurement and
    the start of this event (this is to construct time series records of clinical
    data for event-level data not donor-level data). An empty or zero value
    designates missing data or that this field is not applicable for the concept.
    """

    units: str
    """This are the units for the data value."""


class Metadata(TypedDict, total=False):
    living_donor_data: Iterable[MetadataLivingDonorData]
    """Information about the donor who's tissue was used.

    The tissue was obtained during a procedure. Only living_donor_data or
    organ_donor_data, not both can be defined for a single donor.
    """

    organ_donor_data: Iterable[MetadataOrganDonorData]
    """Information about the donor who's organ(s) was/were used.

    The organ was obtained via an organ donation program from a deceaced donor. Only
    living_donor_data or organ_donor_data, not both can be defined for a single
    donor.
    """


class Donor(TypedDict, total=False):
    contacts: Iterable[Contact]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    creators: Iterable[Creator]
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    description: str
    """Free text description of the donor"""

    group_uuid: str
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    image_files_to_add: List[str]
    """List of temporary file ids with an optional description.

    Provide as a json array with an temp_file_id and description attribute for each
    element like {"files":
    [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
    one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}
    """

    image_files_to_remove: List[str]
    """List of image files previously uploaded to delete.

    Provide as a json array of the file_uuids of the file like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    lab_donor_id: str
    """A lab specific identifier for the donor."""

    label: str
    """Lab provided, de-identified name for the donor"""

    metadata: Metadata
    """Donor metadata as an array of UMLS codes and descriptions"""

    protocol_url: str
    """
    The protocols.io doi url pointing the protocol describing the donor selection,
    inclusion/exclusion criteria
    """

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """
