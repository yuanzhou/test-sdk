# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Sample", "Contact", "Creator", "ImageFile", "Metadata", "MetadataFile"]


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


class Metadata(BaseModel):
    cold_ischemia_time_unit: Optional[str] = None
    """Time units that the cold_ischemia_time_value is reported in.

    Blank if not applicable.
    """

    cold_ischemia_time_value: Optional[int] = None
    """Time interval on ice to the start of preservation protocol.

    Blank if not applicable.
    """

    health_status: Optional[Literal["cancer", "relatively healthy", "chronic illness"]] = None
    """
    Donor from which the tissue sample came from's baseline physical condition prior
    to immediate event leading to organ/tissue acquisition. For example, if a
    relatively healthy patient suffers trauma, and as a result of reparative
    surgery, a tissue sample is collected, the subject will be deemed 'relatively
    healthy'. Likewise, a relatively healthy subject may have experienced trauma
    leading to brain death. As a result of organ donation, a sample is collected. In
    this scenario, the subject is deemed 'relatively healthy'.
    """

    organ_condition: Optional[Literal["healthy", "diseased"]] = None
    """Health status of the organ at the time of tissue sample recovery."""

    pathologist_report: Optional[str] = None
    """Further details on organ level QC checks."""

    perfusion_solution: Optional[Literal["UWS", "HTK", "Belzer MPS/KPS", "Formalin", "Unknown", "None"]] = None
    """Health status of the organ at the time of sample recovery."""

    procedure_date: Optional[str] = None
    """
    The date at which the organ from which the tissue sample came from was
    procurred, in the format YYYY-MM-DD
    """

    sample_id: Optional[str] = None
    """The HuBMAP Identifier for the sample."""

    specimen_preservation_temperature: Optional[str] = None
    """The temperature of the medium during the preservation process.

    Reported as preservation method, temperature and units, e.g. Freezer (-80
    Celsius)
    """

    specimen_quality_criteria: Optional[str] = None
    """RIN score. e.g. RIN: 8.7"""

    specimen_tumor_distance_unit: Optional[str] = None

    specimen_tumor_distance_value: Optional[str] = None
    """
    If surgical sample from a tumor biopsy, how far from the tumor was the sample
    obtained from. Typically a number of centimeters. Blank if not applicable or
    unknown.
    """

    vital_state: Optional[Literal["living", "deceased"]] = None
    """The vital state of the donor who the tissue sample came from."""

    warm_ischemia_time_unit: Optional[str] = None
    """Time units that the warm_ischemia_time_value is reported in.

    Blank if not applicable
    """

    warm_ischemia_time_value: Optional[int] = None
    """Time interval between cessation of blood flow and cooling to 4C.

    Blank if not applicable.
    """


class MetadataFile(BaseModel):
    description: Optional[str] = None
    """A description of the file.

    The Dataset.thumbnail_file does not have this file description.
    """

    file_uuid: Optional[str] = None
    """The HuBMAP unique identifier for the file."""

    filename: Optional[str] = None
    """The name of the file."""


class Sample(BaseModel):
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
    """One of the values: public, consortium."""

    description: Optional[str] = None
    """Free text description of the sample"""

    direct_ancestor: Optional[object] = None
    """The entitiy directly above this sample in the provenance graph (direct parent)."""

    doi_url: Optional[str] = None
    """The url from the doi registry for this entity.

    e.g. https://doi.org/10.35079/hbm289.pcbm.487
    """

    entity_type: Optional[str] = None
    """One of the normalized entity types: Dataset, Collection, Sample, Donor"""

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

    lab_tissue_sample_id: Optional[str] = None
    """Lab specific id for the sample."""

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
    """The sample specific metadata derived from the uploaded sample_metadata.tsv file.

    Returned as a json object.
    """

    metadata_files: Optional[List[MetadataFile]] = None
    """List of uploaded image files and descriptions of the files.

    Stored in db as a stringfied json array.
    """

    metadata_files_to_add: Optional[List[str]] = None
    """List of temporary file ids with an optional description.

    Provide as a json array with an temp_file_id and description attribute for each
    element like {"files":
    [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
    one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}
    """

    metadata_files_to_remove: Optional[List[str]] = None
    """List of image files previously uploaded to delete.

    Provide as a json array of the file_uuids of the file like:
    ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
    "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]
    """

    organ: Optional[
        Literal[
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
    ] = None
    """Organ code specifier, only set if sample_category == organ.

    Valid values found in:
    [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)
    """

    organ_other: Optional[str] = None
    """The organ type provided by the user if "other" organ type is selected"""

    protocol_url: Optional[str] = None
    """
    The protocols.io doi url pointing the protocol under wich the sample was
    obtained and/or prepared.
    """

    registered_doi: Optional[str] = None
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    rui_location: Optional[object] = None
    """
    The sample location and orientation in the ancestor organ as specified in the
    RUI tool. Returned as a json object.
    """

    sample_category: Optional[Literal["organ", "block", "section", "suspension"]] = None
    """A code representing the type of specimen.

    Must be an organ, block, section, or suspension
    """

    submission_id: Optional[str] = None
    """The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.

    This id is generated at creation time which tracks the lab, donor, organ and
    sample hierarchy per the following:
    https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing
    """

    uuid: Optional[str] = None
    """The HuBMAP unique identifier, intended for internal software use only.

    This is a 32 digit hexadecimal uuid e.g. 461bbfdc353a2673e381f632510b0f17
    """

    visit: Optional[str] = None
    """The visit id for the donor/patient when the sample was obtained."""
