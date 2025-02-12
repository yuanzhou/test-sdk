# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "EntityCreateParams",
    "Donor",
    "DonorContact",
    "DonorCreator",
    "DonorMetadata",
    "DonorMetadataLivingDonorData",
    "DonorMetadataOrganDonorData",
    "Sample",
    "SampleContact",
    "SampleCreator",
    "SampleMetadata",
    "Dataset",
    "DatasetAntibody",
    "DatasetContact",
    "DatasetCreator",
    "DatasetFile",
    "Upload",
]


class Donor(TypedDict, total=False):
    contacts: Iterable[DonorContact]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    creators: Iterable[DonorCreator]
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

    metadata: DonorMetadata
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


class DonorContact(TypedDict, total=False):
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


class DonorCreator(TypedDict, total=False):
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


class DonorMetadataLivingDonorData(TypedDict, total=False):
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


class DonorMetadataOrganDonorData(TypedDict, total=False):
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


class DonorMetadata(TypedDict, total=False):
    living_donor_data: Iterable[DonorMetadataLivingDonorData]
    """Information about the donor who's tissue was used.

    The tissue was obtained during a procedure. Only living_donor_data or
    organ_donor_data, not both can be defined for a single donor.
    """

    organ_donor_data: Iterable[DonorMetadataOrganDonorData]
    """Information about the donor who's organ(s) was/were used.

    The organ was obtained via an organ donation program from a deceaced donor. Only
    living_donor_data or organ_donor_data, not both can be defined for a single
    donor.
    """


class Sample(TypedDict, total=False):
    contacts: Iterable[SampleContact]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    creators: Iterable[SampleCreator]
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

    metadata: SampleMetadata
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


class SampleContact(TypedDict, total=False):
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


class SampleCreator(TypedDict, total=False):
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


class SampleMetadata(TypedDict, total=False):
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


class Dataset(TypedDict, total=False):
    antibodies: Iterable[DatasetAntibody]
    """A list of antibodies used in the assay that created the dataset"""

    calculated_metadata: object
    """Calculated metadata outputted from the processing pipeline."""

    contacts: Iterable[DatasetContact]
    """
    A list of the people who are the main contacts to get information about the
    entity.
    """

    contains_human_genetic_sequences: bool
    """True if the data contains any human genetic sequence information.

    Can only be set at CREATE/POST time
    """

    creation_action: str
    """The associated action that represents the creation of that dataset"""

    creators: Iterable[DatasetCreator]
    """
    A list of the people who created the entity with full name, email, ORCID iD,
    institution, etc.. This is analogus to the author list on a publication.
    """

    data_types: List[
        Literal[
            "AF",
            "ATACseq-bulk",
            "bulk_atacseq",
            "cell-dive",
            "CODEX",
            "codex_cytokit",
            "DART-FISH",
            "image_pyramid",
            "IMC",
            "3D-IMC",
            "lc-ms_label-free",
            "lc-ms_labeled",
            "lc-ms-ms_label-free",
            "lc-ms-ms_labeled",
            "LC-MS-untargeted",
            "Lightsheet",
            "MALDI-IMS-neg",
            "MALDI-IMS-pos",
            "MxIF",
            "PAS",
            "bulk-RNA",
            "salmon_rnaseq_bulk",
            "SNAREseq",
            "sc_atac_seq_snare_lab",
            "sc_atac_seq_snare",
            "scRNA-Seq-10x",
            "salmon_rnaseq_10x",
            "sc_rna_seq_snare_lab",
            "salmon_rnaseq_snareseq",
            "sciATACseq",
            "sc_atac_seq_sci",
            "sciRNAseq",
            "salmon_rnaseq_sciseq",
            "seqFish",
            "seqFish_lab_processed",
            "snATACseq",
            "sn_atac_seq",
            "snRNAseq",
            "salmon_sn_rnaseq_10x",
            "Slide-seq",
            "Targeted-Shotgun-LC-MS",
            "TMT-LC-MS",
            "WGS",
        ]
    ]
    """The data or assay types contained in this dataset as a json array of strings.

    Each is an assay code from
    [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).
    """

    dbgap_sra_experiment_url: str
    """A URL linking the dataset to the associated uploaded data at dbGaP."""

    dbgap_study_url: str
    """A URL linking the dataset to the particular study on dbGap it belongs to"""

    description: str
    """Free text description of the dataset"""

    error_message: str
    """
    An open text field that holds the last error message that arose from pipeline
    validation or analysis.
    """

    files: Iterable[DatasetFile]
    """A list of files associated with the dataset."""

    group_uuid: str
    """The uuid of globus group which the user who created this entity is a member of.

    This is required on Create/POST if the user creating the Donor is a member of
    more than one write group. This property cannot be set via PUT (only on
    Create/POST).
    """

    ingest_metadata: object
    """Information associated with running the ingest and processing pipelines."""

    intended_dataset_type: str
    """
    The dataset type of the intended datasets that will be uploaded as part of the
    Upload.
    """

    intended_organ: str
    """
    The organ code representing the organ type that the data contained in the upload
    will be registered/associated with.
    """

    metadata: object
    """Metadata associated with the ingested experimental data."""

    previous_revision_uuid: str
    """The uuid of previous revision dataset. Can only be set at Create/POST time."""

    previous_revision_uuids: List[str]
    """The uuids of previous revision datasets. Can only be set at Create/POST time."""

    registered_doi: str
    """The doi of a the registered entity.

    e.g. 10.35079/hbm289.pcbm.487. This is set during the publication process and
    currently available for certain Collections and Datasets.
    """

    retraction_reason: str
    """Information recorded about why a the dataset was retracted."""

    status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"]
    """One of: New|Processing|QA|Published|Error|Hold|Invalid"""

    sub_status: str
    """A sub-status provided to further define the status.

    The only current allowable value is "Retracted"
    """

    thumbnail_file_to_add: str
    """Just a temporary file id.

    Provide as a json object with an temp_file_id like
    {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}
    """

    thumbnail_file_to_remove: str
    """The thumbnail image file previously uploaded to delete.

    Provide as a string of the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"
    """

    title: str
    """The dataset title."""


class DatasetAntibody(TypedDict, total=False):
    antibody_name: str
    """The name of the antibody."""

    channel_id: str
    """The assay specific identifier for the channel corresponding to the antibody."""

    conjugated_cat_number: str
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    conjugated_tag: str
    """An antibody may be conjugated to a fluorescent tag or a metal tag for detection.

    Conjugated antibodies may be purchased from commercial providers. Blank if not
    applicable.
    """

    dilution: str
    """The dilition ratio, e.g. 1/200 for the antibody. Blank if not applicable."""

    lot_number: str
    """The antibody lot number from the vendor."""

    rr_id: str
    """
    The unique antibody identifier from the Antibody Registry
    (https://antibodyregistry.org).
    """

    uniprot_accession_number: str
    """
    The unique identifier for the target protein in the UniProt database
    (https://www.uniprot.org).
    """


class DatasetContact(TypedDict, total=False):
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


class DatasetCreator(TypedDict, total=False):
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


class DatasetFile(TypedDict, total=False):
    description: str
    """A description of the file.

    The Dataset.thumbnail_file does not have this file description.
    """

    file_uuid: str
    """The HuBMAP unique identifier for the file."""

    filename: str
    """The name of the file."""


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


EntityCreateParams: TypeAlias = Union[Donor, Sample, Dataset, Upload]
