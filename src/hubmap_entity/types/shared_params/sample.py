# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["Sample", "Contact", "Creator", "Metadata"]


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


class Metadata(TypedDict, total=False):
    cold_ischemia_time_unit: str
    """Time units that the cold_ischemia_time_value is reported in.

    Blank if not applicable.
    """

    cold_ischemia_time_value: int
    """Time interval on ice to the start of preservation protocol.

    Blank if not applicable.
    """

    health_status: Literal["cancer", "relatively healthy", "chronic illness"]
    """
    Donor from which the tissue sample came from's baseline physical condition prior
    to immediate event leading to organ/tissue acquisition. For example, if a
    relatively healthy patient suffers trauma, and as a result of reparative
    surgery, a tissue sample is collected, the subject will be deemed 'relatively
    healthy'. Likewise, a relatively healthy subject may have experienced trauma
    leading to brain death. As a result of organ donation, a sample is collected. In
    this scenario, the subject is deemed 'relatively healthy'.
    """

    organ_condition: Literal["healthy", "diseased"]
    """Health status of the organ at the time of tissue sample recovery."""

    pathologist_report: str
    """Further details on organ level QC checks."""

    perfusion_solution: Literal["UWS", "HTK", "Belzer MPS/KPS", "Formalin", "Unknown", "None"]
    """Health status of the organ at the time of sample recovery."""

    procedure_date: str
    """
    The date at which the organ from which the tissue sample came from was
    procurred, in the format YYYY-MM-DD
    """

    sample_id: str
    """The HuBMAP Identifier for the sample."""

    specimen_preservation_temperature: str
    """The temperature of the medium during the preservation process.

    Reported as preservation method, temperature and units, e.g. Freezer (-80
    Celsius)
    """

    specimen_quality_criteria: str
    """RIN score. e.g. RIN: 8.7"""

    specimen_tumor_distance_unit: str

    specimen_tumor_distance_value: str
    """
    If surgical sample from a tumor biopsy, how far from the tumor was the sample
    obtained from. Typically a number of centimeters. Blank if not applicable or
    unknown.
    """

    vital_state: Literal["living", "deceased"]
    """The vital state of the donor who the tissue sample came from."""

    warm_ischemia_time_unit: str
    """Time units that the warm_ischemia_time_value is reported in.

    Blank if not applicable
    """

    warm_ischemia_time_value: int
    """Time interval between cessation of blood flow and cooling to 4C.

    Blank if not applicable.
    """


class Sample(TypedDict, total=False):
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

    data_access_level: Literal["consortium", "public"]
    """One of the values: public, consortium."""

    description: str
    """Free text description of the sample"""

    direct_ancestor_uuid: str
    """The uuid of source entity from which this new entity is derived from.

    Used on creation or edit to create an action and relationship to the ancestor.
    The direct ancestor must be a Donor or Sample. If the direct ancestor is a
    Donor, the sample must be of type organ.
    """

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

    lab_tissue_sample_id: str
    """Lab specific id for the sample."""

    metadata: Metadata
    """The sample specific metadata derived from the uploaded sample_metadata.tsv file.

    Returned as a json object.
    """

    metadata_files_to_add: List[str]
    """List of temporary file ids with an optional description.

    Provide as a json array with an temp_file_id and description attribute for each
    element like {"files":
    [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
    one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}
    """

    metadata_files_to_remove: List[str]
    """List of image files previously uploaded to delete.

    Provide as a json array of the file_uuids of the file like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    organ: Literal[
        "AO",
        "BL",
        "BD",
        "BM",
        "BR",
        "LF",
        "RF",
        "HT",
        "LB",
        "LE",
        "LI",
        "LK",
        "LL",
        "LN",
        "LV",
        "LY",
        "LO",
        "RO",
        "OT",
        "PA",
        "PL",
        "RB",
        "RE",
        "RK",
        "RL",
        "RN",
        "SI",
        "SK",
        "SP",
        "ST",
        "TH",
        "TR",
        "UR",
        "UT",
    ]
    """Organ code specifier, only set if sample_category == organ.

    Valid values found in:
    [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)
    """

    organ_other: str
    """The organ type provided by the user if "other" organ type is selected"""

    protocol_url: str
    """
    The protocols.io doi url pointing the protocol under wich the sample was
    obtained and/or prepared.
    """

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    rui_location: object
    """
    The sample location and orientation in the ancestor organ as specified in the
    RUI tool. Returned as a json object.
    """

    sample_category: Literal["organ", "block", "section", "suspension"]
    """A code representing the type of specimen.

    Must be an organ, block, section, or suspension
    """

    submission_id: str
    """The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.

    This id is generated at creation time which tracks the lab, donor, organ and
    sample hierarchy per the following:
    https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing
    """

    visit: str
    """The visit id for the donor/patient when the sample was obtained."""
