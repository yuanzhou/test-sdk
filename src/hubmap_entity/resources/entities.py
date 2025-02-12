# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Iterable, cast
from typing_extensions import Literal, overload

import httpx

from ..types import (
    entity_create_params,
    entity_update_params,
    entity_list_tuplets_params,
    entity_list_uploads_params,
    entity_list_siblings_params,
    entity_list_collections_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.instanceof import Instanceof
from ..types.entity_create_response import EntityCreateResponse
from ..types.entity_update_response import EntityUpdateResponse
from ..types.entity_retrieve_response import EntityRetrieveResponse
from ..types.entity_list_tuplets_response import EntityListTupletsResponse
from ..types.entity_list_uploads_response import EntityListUploadsResponse
from ..types.entity_list_siblings_response import EntityListSiblingsResponse
from ..types.entity_list_collections_response import EntityListCollectionsResponse
from ..types.entity_list_ancestor_organs_response import EntityListAncestorOrgansResponse
from ..types.entity_create_multiple_samples_response import EntityCreateMultipleSamplesResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return EntitiesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.DonorMetadata | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          description: Free text description of the donor

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_donor_id: A lab specific identifier for the donor.

          label: Lab provided, de-identified name for the donor

          metadata: Donor metadata as an array of UMLS codes and descriptions

          protocol_url: The protocols.io doi url pointing the protocol describing the donor selection,
              inclusion/exclusion criteria

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.SampleContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.SampleCreator] | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.SampleMetadata | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_access_level: One of the values: public, consortium.

          description: Free text description of the sample

          direct_ancestor_uuid: The uuid of source entity from which this new entity is derived from. Used on
              creation or edit to create an action and relationship to the ancestor. The
              direct ancestor must be a Donor or Sample. If the direct ancestor is a Donor,
              the sample must be of type organ.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_tissue_sample_id: Lab specific id for the sample.

          metadata: The sample specific metadata derived from the uploaded sample_metadata.tsv file.
              Returned as a json object.

          metadata_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          metadata_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          organ: Organ code specifier, only set if sample_category == organ. Valid values found
              in:
              [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)

          organ_other: The organ type provided by the user if "other" organ type is selected

          protocol_url: The protocols.io doi url pointing the protocol under wich the sample was
              obtained and/or prepared.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          rui_location: The sample location and orientation in the ancestor organ as specified in the
              RUI tool. Returned as a json object.

          sample_category: A code representing the type of specimen. Must be an organ, block, section, or
              suspension

          submission_id: The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.
              This id is generated at creation time which tracks the lab, donor, organ and
              sample hierarchy per the following:
              https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing

          visit: The visit id for the donor/patient when the sample was obtained.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        entity_type: str,
        *,
        antibodies: Iterable[entity_create_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contacts: Iterable[entity_create_params.DatasetContact] | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DatasetCreator] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_create_params.DatasetFile] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          antibodies: A list of antibodies used in the assay that created the dataset

          calculated_metadata: Calculated metadata outputted from the processing pipeline.

          contacts: A list of the people who are the main contacts to get information about the
              entity.

          contains_human_genetic_sequences: True if the data contains any human genetic sequence information. Can only be
              set at CREATE/POST time

          creation_action: The associated action that represents the creation of that dataset

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_types: The data or assay types contained in this dataset as a json array of strings.
              Each is an assay code from
              [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).

          dbgap_sra_experiment_url: A URL linking the dataset to the associated uploaded data at dbGaP.

          dbgap_study_url: A URL linking the dataset to the particular study on dbGap it belongs to

          description: Free text description of the dataset

          error_message: An open text field that holds the last error message that arose from pipeline
              validation or analysis.

          files: A list of files associated with the dataset.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          ingest_metadata: Information associated with running the ingest and processing pipelines.

          intended_dataset_type: The dataset type of the intended datasets that will be uploaded as part of the
              Upload.

          intended_organ: The organ code representing the organ type that the data contained in the upload
              will be registered/associated with.

          metadata: Metadata associated with the ingested experimental data.

          previous_revision_uuid: The uuid of previous revision dataset. Can only be set at Create/POST time.

          previous_revision_uuids: The uuids of previous revision datasets. Can only be set at Create/POST time.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          retraction_reason: Information recorded about why a the dataset was retracted.

          status: One of: New|Processing|QA|Published|Error|Hold|Invalid

          sub_status: A sub-status provided to further define the status. The only current allowable
              value is "Retracted"

          thumbnail_file_to_add: Just a temporary file id. Provide as a json object with an temp_file_id like
              {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}

          thumbnail_file_to_remove: The thumbnail image file previously uploaded to delete. Provide as a string of
              the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"

          title: The dataset title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        entity_type: str,
        *,
        dataset_uuids_to_link: List[str] | NotGiven = NOT_GIVEN,
        dataset_uuids_to_unlink: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        validation_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          dataset_uuids_to_link: List of datasets to add to the Upload. Provide as a json array of the dataset
              uuids like: ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          dataset_uuids_to_unlink: List of datasets to remove from a Upload. Provide as a json array of the dataset
              uuids like: ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          description: Free text description of the data being submitted.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          status: One of: New|Valid|Invalid|Error|Submitted

          title: Title of the datasets, a sentance or less

          validation_message: A message from the validataion tools describing what is invalid with the upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.DonorMetadata
        | entity_create_params.SampleMetadata
        | object
        | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        antibodies: Iterable[entity_create_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_create_params.DatasetFile] | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"]
        | str
        | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        dataset_uuids_to_link: List[str] | NotGiven = NOT_GIVEN,
        dataset_uuids_to_unlink: List[str] | NotGiven = NOT_GIVEN,
        validation_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        return self._post(
            f"/entities/new/{entity_type}",
            body=maybe_transform(
                {
                    "contacts": contacts,
                    "creators": creators,
                    "description": description,
                    "group_uuid": group_uuid,
                    "image_files_to_add": image_files_to_add,
                    "image_files_to_remove": image_files_to_remove,
                    "lab_donor_id": lab_donor_id,
                    "label": label,
                    "metadata": metadata,
                    "protocol_url": protocol_url,
                    "registered_doi": registered_doi,
                    "data_access_level": data_access_level,
                    "direct_ancestor_uuid": direct_ancestor_uuid,
                    "lab_tissue_sample_id": lab_tissue_sample_id,
                    "metadata_files_to_add": metadata_files_to_add,
                    "metadata_files_to_remove": metadata_files_to_remove,
                    "organ": organ,
                    "organ_other": organ_other,
                    "rui_location": rui_location,
                    "sample_category": sample_category,
                    "submission_id": submission_id,
                    "visit": visit,
                    "antibodies": antibodies,
                    "calculated_metadata": calculated_metadata,
                    "contains_human_genetic_sequences": contains_human_genetic_sequences,
                    "creation_action": creation_action,
                    "data_types": data_types,
                    "dbgap_sra_experiment_url": dbgap_sra_experiment_url,
                    "dbgap_study_url": dbgap_study_url,
                    "error_message": error_message,
                    "files": files,
                    "ingest_metadata": ingest_metadata,
                    "intended_dataset_type": intended_dataset_type,
                    "intended_organ": intended_organ,
                    "previous_revision_uuid": previous_revision_uuid,
                    "previous_revision_uuids": previous_revision_uuids,
                    "retraction_reason": retraction_reason,
                    "status": status,
                    "sub_status": sub_status,
                    "thumbnail_file_to_add": thumbnail_file_to_add,
                    "thumbnail_file_to_remove": thumbnail_file_to_remove,
                    "title": title,
                    "dataset_uuids_to_link": dataset_uuids_to_link,
                    "dataset_uuids_to_unlink": dataset_uuids_to_unlink,
                    "validation_message": validation_message,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityRetrieveResponse:
        """Retrieve a provenance entity by id.

        Entity types of Donor, Sample and Datasets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EntityRetrieveResponse,
            self._get(
                f"/entities/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EntityRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.DonorMetadata | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          description: Free text description of the donor

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_donor_id: A lab specific identifier for the donor.

          label: Lab provided, de-identified name for the donor

          metadata: Donor metadata as an array of UMLS codes and descriptions

          protocol_url: The protocols.io doi url pointing the protocol describing the donor selection,
              inclusion/exclusion criteria

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.SampleContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.SampleCreator] | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.SampleMetadata | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_access_level: One of the values: public, consortium.

          description: Free text description of the sample

          direct_ancestor_uuid: The uuid of source entity from which this new entity is derived from. Used on
              creation or edit to create an action and relationship to the ancestor. The
              direct ancestor must be a Donor or Sample. If the direct ancestor is a Donor,
              the sample must be of type organ.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_tissue_sample_id: Lab specific id for the sample.

          metadata: The sample specific metadata derived from the uploaded sample_metadata.tsv file.
              Returned as a json object.

          metadata_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          metadata_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          organ: Organ code specifier, only set if sample_category == organ. Valid values found
              in:
              [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)

          organ_other: The organ type provided by the user if "other" organ type is selected

          protocol_url: The protocols.io doi url pointing the protocol under wich the sample was
              obtained and/or prepared.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          rui_location: The sample location and orientation in the ancestor organ as specified in the
              RUI tool. Returned as a json object.

          sample_category: A code representing the type of specimen. Must be an organ, block, section, or
              suspension

          submission_id: The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.
              This id is generated at creation time which tracks the lab, donor, organ and
              sample hierarchy per the following:
              https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing

          visit: The visit id for the donor/patient when the sample was obtained.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        antibodies: Iterable[entity_update_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contacts: Iterable[entity_update_params.DatasetContact] | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DatasetCreator] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_update_params.DatasetFile] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          antibodies: A list of antibodies used in the assay that created the dataset

          calculated_metadata: Calculated metadata outputted from the processing pipeline.

          contacts: A list of the people who are the main contacts to get information about the
              entity.

          contains_human_genetic_sequences: True if the data contains any human genetic sequence information. Can only be
              set at CREATE/POST time

          creation_action: The associated action that represents the creation of that dataset

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_types: The data or assay types contained in this dataset as a json array of strings.
              Each is an assay code from
              [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).

          dbgap_sra_experiment_url: A URL linking the dataset to the associated uploaded data at dbGaP.

          dbgap_study_url: A URL linking the dataset to the particular study on dbGap it belongs to

          description: Free text description of the dataset

          error_message: An open text field that holds the last error message that arose from pipeline
              validation or analysis.

          files: A list of files associated with the dataset.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          ingest_metadata: Information associated with running the ingest and processing pipelines.

          intended_dataset_type: The dataset type of the intended datasets that will be uploaded as part of the
              Upload.

          intended_organ: The organ code representing the organ type that the data contained in the upload
              will be registered/associated with.

          metadata: Metadata associated with the ingested experimental data.

          previous_revision_uuid: The uuid of previous revision dataset. Can only be set at Create/POST time.

          previous_revision_uuids: The uuids of previous revision datasets. Can only be set at Create/POST time.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          retraction_reason: Information recorded about why a the dataset was retracted.

          status: One of: New|Processing|QA|Published|Error|Hold|Invalid

          sub_status: A sub-status provided to further define the status. The only current allowable
              value is "Retracted"

          thumbnail_file_to_add: Just a temporary file id. Provide as a json object with an temp_file_id like
              {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}

          thumbnail_file_to_remove: The thumbnail image file previously uploaded to delete. Provide as a string of
              the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"

          title: The dataset title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.DonorMetadata
        | entity_update_params.SampleMetadata
        | object
        | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        antibodies: Iterable[entity_update_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_update_params.DatasetFile] | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EntityUpdateResponse,
            self._put(
                f"/entities/{id}",
                body=maybe_transform(
                    {
                        "contacts": contacts,
                        "creators": creators,
                        "description": description,
                        "group_uuid": group_uuid,
                        "image_files_to_add": image_files_to_add,
                        "image_files_to_remove": image_files_to_remove,
                        "lab_donor_id": lab_donor_id,
                        "label": label,
                        "metadata": metadata,
                        "protocol_url": protocol_url,
                        "registered_doi": registered_doi,
                        "data_access_level": data_access_level,
                        "direct_ancestor_uuid": direct_ancestor_uuid,
                        "lab_tissue_sample_id": lab_tissue_sample_id,
                        "metadata_files_to_add": metadata_files_to_add,
                        "metadata_files_to_remove": metadata_files_to_remove,
                        "organ": organ,
                        "organ_other": organ_other,
                        "rui_location": rui_location,
                        "sample_category": sample_category,
                        "submission_id": submission_id,
                        "visit": visit,
                        "antibodies": antibodies,
                        "calculated_metadata": calculated_metadata,
                        "contains_human_genetic_sequences": contains_human_genetic_sequences,
                        "creation_action": creation_action,
                        "data_types": data_types,
                        "dbgap_sra_experiment_url": dbgap_sra_experiment_url,
                        "dbgap_study_url": dbgap_study_url,
                        "error_message": error_message,
                        "files": files,
                        "ingest_metadata": ingest_metadata,
                        "intended_dataset_type": intended_dataset_type,
                        "intended_organ": intended_organ,
                        "previous_revision_uuid": previous_revision_uuid,
                        "previous_revision_uuids": previous_revision_uuids,
                        "retraction_reason": retraction_reason,
                        "status": status,
                        "sub_status": sub_status,
                        "thumbnail_file_to_add": thumbnail_file_to_add,
                        "thumbnail_file_to_remove": thumbnail_file_to_remove,
                        "title": title,
                    },
                    entity_update_params.EntityUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EntityUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_multiple_samples(
        self,
        count: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateMultipleSamplesResponse:
        """Create multiple samples from the same source entity.

        'count' samples will be
        generated each with individual uuids, hubmap_ids and submission_ids.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not count:
            raise ValueError(f"Expected a non-empty value for `count` but received {count!r}")
        return self._post(
            f"/entities/multiple-samples/{count}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateMultipleSamplesResponse,
        )

    def is_instance_of(
        self,
        type: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instanceof:
        """
        Determines if the Entity with id is an instance of type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return self._get(
            f"/entities/{id}/instanceof/{type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instanceof,
        )

    def is_type_instance_of(
        self,
        type_b: str,
        *,
        type_a: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instanceof:
        """
        Determines if the Entity type type_a is an instance of type_b

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_a:
            raise ValueError(f"Expected a non-empty value for `type_a` but received {type_a!r}")
        if not type_b:
            raise ValueError(f"Expected a non-empty value for `type_b` but received {type_b!r}")
        return self._get(
            f"/entities/type/{type_a}/instanceof/{type_b}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instanceof,
        )

    def list_ancestor_organs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListAncestorOrgansResponse:
        """
        Retrievea list of ancestor organ(s) of a given uuid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/entities/{id}/ancestor-organs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListAncestorOrgansResponse,
        )

    def list_collections(
        self,
        id: str,
        *,
        property: Literal["uuid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListCollectionsResponse:
        """
        Get the list of all collections the Entity belongs to.

        Args:
          property: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property=uuid is provided, rather than entire dictionary representations of each
              node, only the list of matching uuid's will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/entities/{id}/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"property": property}, entity_list_collections_params.EntityListCollectionsParams
                ),
            ),
            cast_to=EntityListCollectionsResponse,
        )

    def list_siblings(
        self,
        id: str,
        *,
        include_old_revisions: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        property_key: Literal["uuid"] | NotGiven = NOT_GIVEN,
        status: Literal["new", "qa", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListSiblingsResponse:
        """Get the siblings list for an Entity.

        The siblings have the same direct ancestor.
        This list does not include all nodes whom have common ancestors, only the direct
        ancestor.

        Args:
          include_old_revisions: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', datasets that are have newer revisions will be included,
              otherwise by default they are not included.

          property_key: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property_key=uuid is provided, rather than entire dictionary representations of
              each node, only the list of matching uuid's will be returned

          status: A case insensitive string. Any value besides 'new', 'qa', and 'published' will
              raise an error. If a valid status is provided, only results matching that status
              (if they are datasets) will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/entities/{id}/siblings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_old_revisions": include_old_revisions,
                        "property_key": property_key,
                        "status": status,
                    },
                    entity_list_siblings_params.EntityListSiblingsParams,
                ),
            ),
            cast_to=EntityListSiblingsResponse,
        )

    def list_tuplets(
        self,
        id: str,
        *,
        property_key: Literal["uuid"] | NotGiven = NOT_GIVEN,
        status: Literal["new", "qa", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListTupletsResponse:
        """Get the tuplets list for an Entity.

        The tuplets have the same parent activity
        node.

        Args:
          property_key: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property_key=uuid is provided, rather than entire dictionary representations of
              each node, only the list of matching uuid's will be returned

          status: A case insensitive string. Any value besides 'new', 'qa', and 'published' will
              raise an error. If a valid status is provided, only results matching that status
              (if they are datasets) will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/entities/{id}/tuplets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "property_key": property_key,
                        "status": status,
                    },
                    entity_list_tuplets_params.EntityListTupletsParams,
                ),
            ),
            cast_to=EntityListTupletsResponse,
        )

    def list_uploads(
        self,
        id: str,
        *,
        property: Literal["uuid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListUploadsResponse:
        """
        Get the list of all uploads the Entity belongs to.

        Args:
          property: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property=uuid is provided, rather than entire dictionary representations of each
              node, only the list of matching uuid's will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/entities/{id}/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"property": property}, entity_list_uploads_params.EntityListUploadsParams),
            ),
            cast_to=EntityListUploadsResponse,
        )

    def retrieve_globus_url(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get the Globus URL to the given Dataset or Upload entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            f"/entities/{id}/globus-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def retrieve_provenance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get Provenance Data for Entity.

        This returns a PROV JSON compliant
        representation of the entity's provenance. Refer to this document for more
        information regarding
        [PROV JSON format](https://www.w3.org/Submission/2013/SUBM-prov-json-20130424/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/entities/{id}/provenance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncEntitiesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.DonorMetadata | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          description: Free text description of the donor

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_donor_id: A lab specific identifier for the donor.

          label: Lab provided, de-identified name for the donor

          metadata: Donor metadata as an array of UMLS codes and descriptions

          protocol_url: The protocols.io doi url pointing the protocol describing the donor selection,
              inclusion/exclusion criteria

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.SampleContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.SampleCreator] | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.SampleMetadata | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_access_level: One of the values: public, consortium.

          description: Free text description of the sample

          direct_ancestor_uuid: The uuid of source entity from which this new entity is derived from. Used on
              creation or edit to create an action and relationship to the ancestor. The
              direct ancestor must be a Donor or Sample. If the direct ancestor is a Donor,
              the sample must be of type organ.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_tissue_sample_id: Lab specific id for the sample.

          metadata: The sample specific metadata derived from the uploaded sample_metadata.tsv file.
              Returned as a json object.

          metadata_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          metadata_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          organ: Organ code specifier, only set if sample_category == organ. Valid values found
              in:
              [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)

          organ_other: The organ type provided by the user if "other" organ type is selected

          protocol_url: The protocols.io doi url pointing the protocol under wich the sample was
              obtained and/or prepared.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          rui_location: The sample location and orientation in the ancestor organ as specified in the
              RUI tool. Returned as a json object.

          sample_category: A code representing the type of specimen. Must be an organ, block, section, or
              suspension

          submission_id: The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.
              This id is generated at creation time which tracks the lab, donor, organ and
              sample hierarchy per the following:
              https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing

          visit: The visit id for the donor/patient when the sample was obtained.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        entity_type: str,
        *,
        antibodies: Iterable[entity_create_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contacts: Iterable[entity_create_params.DatasetContact] | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DatasetCreator] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_create_params.DatasetFile] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          antibodies: A list of antibodies used in the assay that created the dataset

          calculated_metadata: Calculated metadata outputted from the processing pipeline.

          contacts: A list of the people who are the main contacts to get information about the
              entity.

          contains_human_genetic_sequences: True if the data contains any human genetic sequence information. Can only be
              set at CREATE/POST time

          creation_action: The associated action that represents the creation of that dataset

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_types: The data or assay types contained in this dataset as a json array of strings.
              Each is an assay code from
              [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).

          dbgap_sra_experiment_url: A URL linking the dataset to the associated uploaded data at dbGaP.

          dbgap_study_url: A URL linking the dataset to the particular study on dbGap it belongs to

          description: Free text description of the dataset

          error_message: An open text field that holds the last error message that arose from pipeline
              validation or analysis.

          files: A list of files associated with the dataset.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          ingest_metadata: Information associated with running the ingest and processing pipelines.

          intended_dataset_type: The dataset type of the intended datasets that will be uploaded as part of the
              Upload.

          intended_organ: The organ code representing the organ type that the data contained in the upload
              will be registered/associated with.

          metadata: Metadata associated with the ingested experimental data.

          previous_revision_uuid: The uuid of previous revision dataset. Can only be set at Create/POST time.

          previous_revision_uuids: The uuids of previous revision datasets. Can only be set at Create/POST time.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          retraction_reason: Information recorded about why a the dataset was retracted.

          status: One of: New|Processing|QA|Published|Error|Hold|Invalid

          sub_status: A sub-status provided to further define the status. The only current allowable
              value is "Retracted"

          thumbnail_file_to_add: Just a temporary file id. Provide as a json object with an temp_file_id like
              {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}

          thumbnail_file_to_remove: The thumbnail image file previously uploaded to delete. Provide as a string of
              the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"

          title: The dataset title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        entity_type: str,
        *,
        dataset_uuids_to_link: List[str] | NotGiven = NOT_GIVEN,
        dataset_uuids_to_unlink: List[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        validation_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        """
        Create a new entity of the target type

        Args:
          dataset_uuids_to_link: List of datasets to add to the Upload. Provide as a json array of the dataset
              uuids like: ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          dataset_uuids_to_unlink: List of datasets to remove from a Upload. Provide as a json array of the dataset
              uuids like: ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          description: Free text description of the data being submitted.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          status: One of: New|Valid|Invalid|Error|Submitted

          title: Title of the datasets, a sentance or less

          validation_message: A message from the validataion tools describing what is invalid with the upload.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        entity_type: str,
        *,
        contacts: Iterable[entity_create_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_create_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_create_params.DonorMetadata
        | entity_create_params.SampleMetadata
        | object
        | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        antibodies: Iterable[entity_create_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_create_params.DatasetFile] | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"]
        | str
        | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        dataset_uuids_to_link: List[str] | NotGiven = NOT_GIVEN,
        dataset_uuids_to_unlink: List[str] | NotGiven = NOT_GIVEN,
        validation_message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateResponse:
        if not entity_type:
            raise ValueError(f"Expected a non-empty value for `entity_type` but received {entity_type!r}")
        return await self._post(
            f"/entities/new/{entity_type}",
            body=await async_maybe_transform(
                {
                    "contacts": contacts,
                    "creators": creators,
                    "description": description,
                    "group_uuid": group_uuid,
                    "image_files_to_add": image_files_to_add,
                    "image_files_to_remove": image_files_to_remove,
                    "lab_donor_id": lab_donor_id,
                    "label": label,
                    "metadata": metadata,
                    "protocol_url": protocol_url,
                    "registered_doi": registered_doi,
                    "data_access_level": data_access_level,
                    "direct_ancestor_uuid": direct_ancestor_uuid,
                    "lab_tissue_sample_id": lab_tissue_sample_id,
                    "metadata_files_to_add": metadata_files_to_add,
                    "metadata_files_to_remove": metadata_files_to_remove,
                    "organ": organ,
                    "organ_other": organ_other,
                    "rui_location": rui_location,
                    "sample_category": sample_category,
                    "submission_id": submission_id,
                    "visit": visit,
                    "antibodies": antibodies,
                    "calculated_metadata": calculated_metadata,
                    "contains_human_genetic_sequences": contains_human_genetic_sequences,
                    "creation_action": creation_action,
                    "data_types": data_types,
                    "dbgap_sra_experiment_url": dbgap_sra_experiment_url,
                    "dbgap_study_url": dbgap_study_url,
                    "error_message": error_message,
                    "files": files,
                    "ingest_metadata": ingest_metadata,
                    "intended_dataset_type": intended_dataset_type,
                    "intended_organ": intended_organ,
                    "previous_revision_uuid": previous_revision_uuid,
                    "previous_revision_uuids": previous_revision_uuids,
                    "retraction_reason": retraction_reason,
                    "status": status,
                    "sub_status": sub_status,
                    "thumbnail_file_to_add": thumbnail_file_to_add,
                    "thumbnail_file_to_remove": thumbnail_file_to_remove,
                    "title": title,
                    "dataset_uuids_to_link": dataset_uuids_to_link,
                    "dataset_uuids_to_unlink": dataset_uuids_to_unlink,
                    "validation_message": validation_message,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityRetrieveResponse:
        """Retrieve a provenance entity by id.

        Entity types of Donor, Sample and Datasets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EntityRetrieveResponse,
            await self._get(
                f"/entities/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EntityRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.DonorMetadata | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          description: Free text description of the donor

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_donor_id: A lab specific identifier for the donor.

          label: Lab provided, de-identified name for the donor

          metadata: Donor metadata as an array of UMLS codes and descriptions

          protocol_url: The protocols.io doi url pointing the protocol describing the donor selection,
              inclusion/exclusion criteria

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.SampleContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.SampleCreator] | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.SampleMetadata | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          contacts: A list of the people who are the main contacts to get information about the
              entity.

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_access_level: One of the values: public, consortium.

          description: Free text description of the sample

          direct_ancestor_uuid: The uuid of source entity from which this new entity is derived from. Used on
              creation or edit to create an action and relationship to the ancestor. The
              direct ancestor must be a Donor or Sample. If the direct ancestor is a Donor,
              the sample must be of type organ.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          image_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          image_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          lab_tissue_sample_id: Lab specific id for the sample.

          metadata: The sample specific metadata derived from the uploaded sample_metadata.tsv file.
              Returned as a json object.

          metadata_files_to_add: List of temporary file ids with an optional description. Provide as a json array
              with an temp_file_id and description attribute for each element like {"files":
              [{"temp_file_id":"dzevgd6xjs4d5grmcp4n","description":"This is image file
              one"},{"temp_file_id":"yrahjadfhadf","description":"This is image file two"}]}

          metadata_files_to_remove: List of image files previously uploaded to delete. Provide as a json array of
              the file_uuids of the file like:
              ["232934234234234234234270c0ea6c51d604a850558ef2247d0b4",
              "230948203482234234234a57bfe9c056d08a0f8e6cd612baa3bfa"]

          organ: Organ code specifier, only set if sample_category == organ. Valid values found
              in:
              [organ types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/organ_types.yaml)

          organ_other: The organ type provided by the user if "other" organ type is selected

          protocol_url: The protocols.io doi url pointing the protocol under wich the sample was
              obtained and/or prepared.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          rui_location: The sample location and orientation in the ancestor organ as specified in the
              RUI tool. Returned as a json object.

          sample_category: A code representing the type of specimen. Must be an organ, block, section, or
              suspension

          submission_id: The hubmap internal id with embedded semantic information e.g.: VAN0003-LK-1-10.
              This id is generated at creation time which tracks the lab, donor, organ and
              sample hierarchy per the following:
              https://docs.google.com/document/d/1DjHgmqWF1VA5-3mfzLFNfabbzmc8KLSG9xWx1DDLlzo/edit?usp=sharing

          visit: The visit id for the donor/patient when the sample was obtained.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        antibodies: Iterable[entity_update_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contacts: Iterable[entity_update_params.DatasetContact] | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DatasetCreator] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_update_params.DatasetFile] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        """
        Update the properties of a given Donor, Sample, Dataset or Upload

        Args:
          antibodies: A list of antibodies used in the assay that created the dataset

          calculated_metadata: Calculated metadata outputted from the processing pipeline.

          contacts: A list of the people who are the main contacts to get information about the
              entity.

          contains_human_genetic_sequences: True if the data contains any human genetic sequence information. Can only be
              set at CREATE/POST time

          creation_action: The associated action that represents the creation of that dataset

          creators: A list of the people who created the entity with full name, email, ORCID iD,
              institution, etc.. This is analogus to the author list on a publication.

          data_types: The data or assay types contained in this dataset as a json array of strings.
              Each is an assay code from
              [assay types](https://github.com/hubmapconsortium/search-api/blob/main/src/search-schema/data/definitions/enums/assay_types.yaml).

          dbgap_sra_experiment_url: A URL linking the dataset to the associated uploaded data at dbGaP.

          dbgap_study_url: A URL linking the dataset to the particular study on dbGap it belongs to

          description: Free text description of the dataset

          error_message: An open text field that holds the last error message that arose from pipeline
              validation or analysis.

          files: A list of files associated with the dataset.

          group_uuid: The uuid of globus group which the user who created this entity is a member of.
              This is required on Create/POST if the user creating the Donor is a member of
              more than one write group. This property cannot be set via PUT (only on
              Create/POST).

          ingest_metadata: Information associated with running the ingest and processing pipelines.

          intended_dataset_type: The dataset type of the intended datasets that will be uploaded as part of the
              Upload.

          intended_organ: The organ code representing the organ type that the data contained in the upload
              will be registered/associated with.

          metadata: Metadata associated with the ingested experimental data.

          previous_revision_uuid: The uuid of previous revision dataset. Can only be set at Create/POST time.

          previous_revision_uuids: The uuids of previous revision datasets. Can only be set at Create/POST time.

          registered_doi: The doi of a the registered entity. e.g. 10.35079/hbm289.pcbm.487. This is set
              during the publication process and currently available for certain Collections
              and Datasets.

          retraction_reason: Information recorded about why a the dataset was retracted.

          status: One of: New|Processing|QA|Published|Error|Hold|Invalid

          sub_status: A sub-status provided to further define the status. The only current allowable
              value is "Retracted"

          thumbnail_file_to_add: Just a temporary file id. Provide as a json object with an temp_file_id like
              {"temp_file_id":"dzevgd6xjs4d5grmcp4n"}

          thumbnail_file_to_remove: The thumbnail image file previously uploaded to delete. Provide as a string of
              the file_uuid like: "c35002f9c3d49f8b77e1e2cd4a01803d"

          title: The dataset title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        id: str,
        *,
        contacts: Iterable[entity_update_params.DonorContact] | NotGiven = NOT_GIVEN,
        creators: Iterable[entity_update_params.DonorCreator] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        image_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        image_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
        lab_donor_id: str | NotGiven = NOT_GIVEN,
        label: str | NotGiven = NOT_GIVEN,
        metadata: entity_update_params.DonorMetadata
        | entity_update_params.SampleMetadata
        | object
        | NotGiven = NOT_GIVEN,
        protocol_url: str | NotGiven = NOT_GIVEN,
        registered_doi: str | NotGiven = NOT_GIVEN,
        data_access_level: Literal["consortium", "public"] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuid: str | NotGiven = NOT_GIVEN,
        lab_tissue_sample_id: str | NotGiven = NOT_GIVEN,
        metadata_files_to_add: List[str] | NotGiven = NOT_GIVEN,
        metadata_files_to_remove: List[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        organ_other: str | NotGiven = NOT_GIVEN,
        rui_location: object | NotGiven = NOT_GIVEN,
        sample_category: Literal["organ", "block", "section", "suspension"] | NotGiven = NOT_GIVEN,
        submission_id: str | NotGiven = NOT_GIVEN,
        visit: str | NotGiven = NOT_GIVEN,
        antibodies: Iterable[entity_update_params.DatasetAntibody] | NotGiven = NOT_GIVEN,
        calculated_metadata: object | NotGiven = NOT_GIVEN,
        contains_human_genetic_sequences: bool | NotGiven = NOT_GIVEN,
        creation_action: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        dbgap_sra_experiment_url: str | NotGiven = NOT_GIVEN,
        dbgap_study_url: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        files: Iterable[entity_update_params.DatasetFile] | NotGiven = NOT_GIVEN,
        ingest_metadata: object | NotGiven = NOT_GIVEN,
        intended_dataset_type: str | NotGiven = NOT_GIVEN,
        intended_organ: str | NotGiven = NOT_GIVEN,
        previous_revision_uuid: str | NotGiven = NOT_GIVEN,
        previous_revision_uuids: List[str] | NotGiven = NOT_GIVEN,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        status: Literal["New", "Processing", "QA", "Published", "Error", "Hold", "Invalid"] | NotGiven = NOT_GIVEN,
        sub_status: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_add: str | NotGiven = NOT_GIVEN,
        thumbnail_file_to_remove: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityUpdateResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EntityUpdateResponse,
            await self._put(
                f"/entities/{id}",
                body=await async_maybe_transform(
                    {
                        "contacts": contacts,
                        "creators": creators,
                        "description": description,
                        "group_uuid": group_uuid,
                        "image_files_to_add": image_files_to_add,
                        "image_files_to_remove": image_files_to_remove,
                        "lab_donor_id": lab_donor_id,
                        "label": label,
                        "metadata": metadata,
                        "protocol_url": protocol_url,
                        "registered_doi": registered_doi,
                        "data_access_level": data_access_level,
                        "direct_ancestor_uuid": direct_ancestor_uuid,
                        "lab_tissue_sample_id": lab_tissue_sample_id,
                        "metadata_files_to_add": metadata_files_to_add,
                        "metadata_files_to_remove": metadata_files_to_remove,
                        "organ": organ,
                        "organ_other": organ_other,
                        "rui_location": rui_location,
                        "sample_category": sample_category,
                        "submission_id": submission_id,
                        "visit": visit,
                        "antibodies": antibodies,
                        "calculated_metadata": calculated_metadata,
                        "contains_human_genetic_sequences": contains_human_genetic_sequences,
                        "creation_action": creation_action,
                        "data_types": data_types,
                        "dbgap_sra_experiment_url": dbgap_sra_experiment_url,
                        "dbgap_study_url": dbgap_study_url,
                        "error_message": error_message,
                        "files": files,
                        "ingest_metadata": ingest_metadata,
                        "intended_dataset_type": intended_dataset_type,
                        "intended_organ": intended_organ,
                        "previous_revision_uuid": previous_revision_uuid,
                        "previous_revision_uuids": previous_revision_uuids,
                        "retraction_reason": retraction_reason,
                        "status": status,
                        "sub_status": sub_status,
                        "thumbnail_file_to_add": thumbnail_file_to_add,
                        "thumbnail_file_to_remove": thumbnail_file_to_remove,
                        "title": title,
                    },
                    entity_update_params.EntityUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EntityUpdateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_multiple_samples(
        self,
        count: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityCreateMultipleSamplesResponse:
        """Create multiple samples from the same source entity.

        'count' samples will be
        generated each with individual uuids, hubmap_ids and submission_ids.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not count:
            raise ValueError(f"Expected a non-empty value for `count` but received {count!r}")
        return await self._post(
            f"/entities/multiple-samples/{count}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateMultipleSamplesResponse,
        )

    async def is_instance_of(
        self,
        type: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instanceof:
        """
        Determines if the Entity with id is an instance of type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        return await self._get(
            f"/entities/{id}/instanceof/{type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instanceof,
        )

    async def is_type_instance_of(
        self,
        type_b: str,
        *,
        type_a: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Instanceof:
        """
        Determines if the Entity type type_a is an instance of type_b

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not type_a:
            raise ValueError(f"Expected a non-empty value for `type_a` but received {type_a!r}")
        if not type_b:
            raise ValueError(f"Expected a non-empty value for `type_b` but received {type_b!r}")
        return await self._get(
            f"/entities/type/{type_a}/instanceof/{type_b}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Instanceof,
        )

    async def list_ancestor_organs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListAncestorOrgansResponse:
        """
        Retrievea list of ancestor organ(s) of a given uuid

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/entities/{id}/ancestor-organs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListAncestorOrgansResponse,
        )

    async def list_collections(
        self,
        id: str,
        *,
        property: Literal["uuid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListCollectionsResponse:
        """
        Get the list of all collections the Entity belongs to.

        Args:
          property: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property=uuid is provided, rather than entire dictionary representations of each
              node, only the list of matching uuid's will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/entities/{id}/collections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"property": property}, entity_list_collections_params.EntityListCollectionsParams
                ),
            ),
            cast_to=EntityListCollectionsResponse,
        )

    async def list_siblings(
        self,
        id: str,
        *,
        include_old_revisions: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        property_key: Literal["uuid"] | NotGiven = NOT_GIVEN,
        status: Literal["new", "qa", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListSiblingsResponse:
        """Get the siblings list for an Entity.

        The siblings have the same direct ancestor.
        This list does not include all nodes whom have common ancestors, only the direct
        ancestor.

        Args:
          include_old_revisions: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', datasets that are have newer revisions will be included,
              otherwise by default they are not included.

          property_key: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property_key=uuid is provided, rather than entire dictionary representations of
              each node, only the list of matching uuid's will be returned

          status: A case insensitive string. Any value besides 'new', 'qa', and 'published' will
              raise an error. If a valid status is provided, only results matching that status
              (if they are datasets) will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/entities/{id}/siblings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_old_revisions": include_old_revisions,
                        "property_key": property_key,
                        "status": status,
                    },
                    entity_list_siblings_params.EntityListSiblingsParams,
                ),
            ),
            cast_to=EntityListSiblingsResponse,
        )

    async def list_tuplets(
        self,
        id: str,
        *,
        property_key: Literal["uuid"] | NotGiven = NOT_GIVEN,
        status: Literal["new", "qa", "published"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListTupletsResponse:
        """Get the tuplets list for an Entity.

        The tuplets have the same parent activity
        node.

        Args:
          property_key: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property_key=uuid is provided, rather than entire dictionary representations of
              each node, only the list of matching uuid's will be returned

          status: A case insensitive string. Any value besides 'new', 'qa', and 'published' will
              raise an error. If a valid status is provided, only results matching that status
              (if they are datasets) will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/entities/{id}/tuplets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "property_key": property_key,
                        "status": status,
                    },
                    entity_list_tuplets_params.EntityListTupletsParams,
                ),
            ),
            cast_to=EntityListTupletsResponse,
        )

    async def list_uploads(
        self,
        id: str,
        *,
        property: Literal["uuid"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListUploadsResponse:
        """
        Get the list of all uploads the Entity belongs to.

        Args:
          property: A case insensitive string. Any value besides 'uuid' will raise an error. If
              property=uuid is provided, rather than entire dictionary representations of each
              node, only the list of matching uuid's will be returned

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/entities/{id}/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"property": property}, entity_list_uploads_params.EntityListUploadsParams
                ),
            ),
            cast_to=EntityListUploadsResponse,
        )

    async def retrieve_globus_url(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Get the Globus URL to the given Dataset or Upload entity

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            f"/entities/{id}/globus-url",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def retrieve_provenance(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Get Provenance Data for Entity.

        This returns a PROV JSON compliant
        representation of the entity's provenance. Refer to this document for more
        information regarding
        [PROV JSON format](https://www.w3.org/Submission/2013/SUBM-prov-json-20130424/)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/entities/{id}/provenance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = to_raw_response_wrapper(
            entities.retrieve,
        )
        self.update = to_raw_response_wrapper(
            entities.update,
        )
        self.create_multiple_samples = to_raw_response_wrapper(
            entities.create_multiple_samples,
        )
        self.is_instance_of = to_raw_response_wrapper(
            entities.is_instance_of,
        )
        self.is_type_instance_of = to_raw_response_wrapper(
            entities.is_type_instance_of,
        )
        self.list_ancestor_organs = to_raw_response_wrapper(
            entities.list_ancestor_organs,
        )
        self.list_collections = to_raw_response_wrapper(
            entities.list_collections,
        )
        self.list_siblings = to_raw_response_wrapper(
            entities.list_siblings,
        )
        self.list_tuplets = to_raw_response_wrapper(
            entities.list_tuplets,
        )
        self.list_uploads = to_raw_response_wrapper(
            entities.list_uploads,
        )
        self.retrieve_globus_url = to_raw_response_wrapper(
            entities.retrieve_globus_url,
        )
        self.retrieve_provenance = to_raw_response_wrapper(
            entities.retrieve_provenance,
        )


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_raw_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            entities.update,
        )
        self.create_multiple_samples = async_to_raw_response_wrapper(
            entities.create_multiple_samples,
        )
        self.is_instance_of = async_to_raw_response_wrapper(
            entities.is_instance_of,
        )
        self.is_type_instance_of = async_to_raw_response_wrapper(
            entities.is_type_instance_of,
        )
        self.list_ancestor_organs = async_to_raw_response_wrapper(
            entities.list_ancestor_organs,
        )
        self.list_collections = async_to_raw_response_wrapper(
            entities.list_collections,
        )
        self.list_siblings = async_to_raw_response_wrapper(
            entities.list_siblings,
        )
        self.list_tuplets = async_to_raw_response_wrapper(
            entities.list_tuplets,
        )
        self.list_uploads = async_to_raw_response_wrapper(
            entities.list_uploads,
        )
        self.retrieve_globus_url = async_to_raw_response_wrapper(
            entities.retrieve_globus_url,
        )
        self.retrieve_provenance = async_to_raw_response_wrapper(
            entities.retrieve_provenance,
        )


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.create = to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            entities.update,
        )
        self.create_multiple_samples = to_streamed_response_wrapper(
            entities.create_multiple_samples,
        )
        self.is_instance_of = to_streamed_response_wrapper(
            entities.is_instance_of,
        )
        self.is_type_instance_of = to_streamed_response_wrapper(
            entities.is_type_instance_of,
        )
        self.list_ancestor_organs = to_streamed_response_wrapper(
            entities.list_ancestor_organs,
        )
        self.list_collections = to_streamed_response_wrapper(
            entities.list_collections,
        )
        self.list_siblings = to_streamed_response_wrapper(
            entities.list_siblings,
        )
        self.list_tuplets = to_streamed_response_wrapper(
            entities.list_tuplets,
        )
        self.list_uploads = to_streamed_response_wrapper(
            entities.list_uploads,
        )
        self.retrieve_globus_url = to_streamed_response_wrapper(
            entities.retrieve_globus_url,
        )
        self.retrieve_provenance = to_streamed_response_wrapper(
            entities.retrieve_provenance,
        )


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.create = async_to_streamed_response_wrapper(
            entities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            entities.update,
        )
        self.create_multiple_samples = async_to_streamed_response_wrapper(
            entities.create_multiple_samples,
        )
        self.is_instance_of = async_to_streamed_response_wrapper(
            entities.is_instance_of,
        )
        self.is_type_instance_of = async_to_streamed_response_wrapper(
            entities.is_type_instance_of,
        )
        self.list_ancestor_organs = async_to_streamed_response_wrapper(
            entities.list_ancestor_organs,
        )
        self.list_collections = async_to_streamed_response_wrapper(
            entities.list_collections,
        )
        self.list_siblings = async_to_streamed_response_wrapper(
            entities.list_siblings,
        )
        self.list_tuplets = async_to_streamed_response_wrapper(
            entities.list_tuplets,
        )
        self.list_uploads = async_to_streamed_response_wrapper(
            entities.list_uploads,
        )
        self.retrieve_globus_url = async_to_streamed_response_wrapper(
            entities.retrieve_globus_url,
        )
        self.retrieve_provenance = async_to_streamed_response_wrapper(
            entities.retrieve_provenance,
        )
