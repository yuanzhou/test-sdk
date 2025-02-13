# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types import (
    DatasetBulkUpdateResponse,
    DatasetListDonorsResponse,
    DatasetListOrgansResponse,
    DatasetListSamplesResponse,
    DatasetListUnpublishedResponse,
    DatasetCreateComponentsResponse,
    DatasetRetrieveRevisionsResponse,
    DatasetRetrieveSankeyDataResponse,
    DatasetRetrieveProvMetadataResponse,
    DatasetRetrievePairedDatasetResponse,
)
from hubmap_entity.types.shared import Dataset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_bulk_update(self, client: HubmapEntity) -> None:
        dataset = client.datasets.bulk_update(
            body=[{}],
        )
        assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_bulk_update(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.bulk_update(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_bulk_update(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.bulk_update(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_components(self, client: HubmapEntity) -> None:
        dataset = client.datasets.create_components()
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_components_with_all_params(self, client: HubmapEntity) -> None:
        dataset = client.datasets.create_components(
            creation_action="creation_action",
            datasets=[
                {
                    "antibodies": [
                        {
                            "antibody_name": "antibody_name",
                            "channel_id": "channel_id",
                            "conjugated_cat_number": "conjugated_cat_number",
                            "conjugated_tag": "conjugated_tag",
                            "dilution": "dilution",
                            "lot_number": "lot_number",
                            "rr_id": "rr_id",
                            "uniprot_accession_number": "uniprot_accession_number",
                        }
                    ],
                    "calculated_metadata": {},
                    "contacts": [
                        {
                            "affiliation": "affiliation",
                            "first_name": "first_name",
                            "last_name": "last_name",
                            "middle_name_or_initial": "middle_name_or_initial",
                            "orcid_id": "orcid_id",
                        }
                    ],
                    "contains_human_genetic_sequences": True,
                    "creation_action": "creation_action",
                    "creators": [
                        {
                            "affiliation": "affiliation",
                            "first_name": "first_name",
                            "last_name": "last_name",
                            "middle_name_or_initial": "middle_name_or_initial",
                            "orcid_id": "orcid_id",
                        }
                    ],
                    "data_types": ["AF"],
                    "dbgap_sra_experiment_url": "dbgap_sra_experiment_url",
                    "dbgap_study_url": "dbgap_study_url",
                    "description": "description",
                    "error_message": "error_message",
                    "files": [
                        {
                            "description": "description",
                            "file_uuid": "file_uuid",
                            "filename": "filename",
                        }
                    ],
                    "group_uuid": "group_uuid",
                    "ingest_metadata": {},
                    "intended_dataset_type": "intended_dataset_type",
                    "intended_organ": "intended_organ",
                    "metadata": {},
                    "previous_revision_uuid": "previous_revision_uuid",
                    "previous_revision_uuids": ["string"],
                    "registered_doi": "registered_doi",
                    "retraction_reason": "retraction_reason",
                    "status": "New",
                    "sub_status": "sub_status",
                    "thumbnail_file_to_add": "thumbnail_file_to_add",
                    "thumbnail_file_to_remove": "thumbnail_file_to_remove",
                    "title": "title",
                    "dataset_link_abs_dir": "dataset_link_abs_dir",
                }
            ],
            direct_ancestor_uuids="direct_ancestor_uuids",
            group_uuid="group_uuid",
        )
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_components(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.create_components()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_components(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.create_components() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_donors(self, client: HubmapEntity) -> None:
        dataset = client.datasets.list_donors(
            "id",
        )
        assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_donors(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.list_donors(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_donors(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.list_donors(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_donors(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.list_donors(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_organs(self, client: HubmapEntity) -> None:
        dataset = client.datasets.list_organs(
            "id",
        )
        assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_organs(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.list_organs(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_organs(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.list_organs(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_organs(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.list_organs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_samples(self, client: HubmapEntity) -> None:
        dataset = client.datasets.list_samples(
            "id",
        )
        assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_samples(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.list_samples(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_samples(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.list_samples(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_samples(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.list_samples(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_unpublished(self, client: HubmapEntity) -> None:
        dataset = client.datasets.list_unpublished()
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_unpublished_with_all_params(self, client: HubmapEntity) -> None:
        dataset = client.datasets.list_unpublished(
            format="format",
        )
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_unpublished(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.list_unpublished()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_unpublished(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.list_unpublished() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retract(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retract(
            id="id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_method_retract_with_all_params(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retract(
            id="id",
            retraction_reason="retraction_reason",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retract(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retract(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retract(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retract(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retract(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retract(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_latest_revision(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_latest_revision(
            "id",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_latest_revision(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_latest_revision(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_latest_revision(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_latest_revision(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_latest_revision(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve_latest_revision(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_paired_dataset(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        )
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_paired_dataset_with_all_params(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
            search_depth=0,
        )
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_paired_dataset(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_paired_dataset(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_paired_dataset(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve_paired_dataset(
                id="",
                data_type="data_type",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_prov_metadata(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_prov_metadata(
            "id",
        )
        assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_prov_metadata(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_prov_metadata(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_prov_metadata(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_prov_metadata(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_prov_metadata(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve_prov_metadata(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_revision(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_revision(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_revision(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_revision(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_revision(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_revision(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_revision(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve_revision(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_revisions(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_revisions(
            id="id",
        )
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_revisions_with_all_params(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_revisions(
            id="id",
            include_dataset="true",
        )
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_revisions(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_revisions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_revisions(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_revisions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_revisions(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve_revisions(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_sankey_data(self, client: HubmapEntity) -> None:
        dataset = client.datasets.retrieve_sankey_data()
        assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_sankey_data(self, client: HubmapEntity) -> None:
        response = client.datasets.with_raw_response.retrieve_sankey_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_sankey_data(self, client: HubmapEntity) -> None:
        with client.datasets.with_streaming_response.retrieve_sankey_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.bulk_update(
            body=[{}],
        )
        assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.bulk_update(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.bulk_update(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetBulkUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_components(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.create_components()
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_components_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.create_components(
            creation_action="creation_action",
            datasets=[
                {
                    "antibodies": [
                        {
                            "antibody_name": "antibody_name",
                            "channel_id": "channel_id",
                            "conjugated_cat_number": "conjugated_cat_number",
                            "conjugated_tag": "conjugated_tag",
                            "dilution": "dilution",
                            "lot_number": "lot_number",
                            "rr_id": "rr_id",
                            "uniprot_accession_number": "uniprot_accession_number",
                        }
                    ],
                    "calculated_metadata": {},
                    "contacts": [
                        {
                            "affiliation": "affiliation",
                            "first_name": "first_name",
                            "last_name": "last_name",
                            "middle_name_or_initial": "middle_name_or_initial",
                            "orcid_id": "orcid_id",
                        }
                    ],
                    "contains_human_genetic_sequences": True,
                    "creation_action": "creation_action",
                    "creators": [
                        {
                            "affiliation": "affiliation",
                            "first_name": "first_name",
                            "last_name": "last_name",
                            "middle_name_or_initial": "middle_name_or_initial",
                            "orcid_id": "orcid_id",
                        }
                    ],
                    "data_types": ["AF"],
                    "dbgap_sra_experiment_url": "dbgap_sra_experiment_url",
                    "dbgap_study_url": "dbgap_study_url",
                    "description": "description",
                    "error_message": "error_message",
                    "files": [
                        {
                            "description": "description",
                            "file_uuid": "file_uuid",
                            "filename": "filename",
                        }
                    ],
                    "group_uuid": "group_uuid",
                    "ingest_metadata": {},
                    "intended_dataset_type": "intended_dataset_type",
                    "intended_organ": "intended_organ",
                    "metadata": {},
                    "previous_revision_uuid": "previous_revision_uuid",
                    "previous_revision_uuids": ["string"],
                    "registered_doi": "registered_doi",
                    "retraction_reason": "retraction_reason",
                    "status": "New",
                    "sub_status": "sub_status",
                    "thumbnail_file_to_add": "thumbnail_file_to_add",
                    "thumbnail_file_to_remove": "thumbnail_file_to_remove",
                    "title": "title",
                    "dataset_link_abs_dir": "dataset_link_abs_dir",
                }
            ],
            direct_ancestor_uuids="direct_ancestor_uuids",
            group_uuid="group_uuid",
        )
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_components(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.create_components()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_components(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.create_components() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetCreateComponentsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_donors(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.list_donors(
            "id",
        )
        assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_donors(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.list_donors(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_donors(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.list_donors(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListDonorsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_donors(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.list_donors(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_organs(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.list_organs(
            "id",
        )
        assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_organs(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.list_organs(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_organs(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.list_organs(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListOrgansResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_organs(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.list_organs(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_samples(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.list_samples(
            "id",
        )
        assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_samples(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.list_samples(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_samples(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.list_samples(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListSamplesResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_samples(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.list_samples(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_unpublished(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.list_unpublished()
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_unpublished_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.list_unpublished(
            format="format",
        )
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_unpublished(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.list_unpublished()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_unpublished(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.list_unpublished() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListUnpublishedResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retract(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retract(
            id="id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_retract_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retract(
            id="id",
            retraction_reason="retraction_reason",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retract(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retract(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retract(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retract(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retract(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retract(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_latest_revision(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_latest_revision(
            "id",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_latest_revision(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_latest_revision(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_latest_revision(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_latest_revision(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_latest_revision(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_latest_revision(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_paired_dataset(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        )
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_paired_dataset_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
            search_depth=0,
        )
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_paired_dataset(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_paired_dataset(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_paired_dataset(
            id="id",
            data_type="data_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrievePairedDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_paired_dataset(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_paired_dataset(
                id="",
                data_type="data_type",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_prov_metadata(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_prov_metadata(
            "id",
        )
        assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_prov_metadata(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_prov_metadata(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_prov_metadata(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_prov_metadata(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveProvMetadataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_prov_metadata(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_prov_metadata(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_revision(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_revision(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_revision(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_revision(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_revision(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_revision(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_revision(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_revision(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_revisions(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_revisions(
            id="id",
        )
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_revisions_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_revisions(
            id="id",
            include_dataset="true",
        )
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_revisions(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_revisions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_revisions(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_revisions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveRevisionsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_revisions(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_revisions(
                id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_sankey_data(self, async_client: AsyncHubmapEntity) -> None:
        dataset = await async_client.datasets.retrieve_sankey_data()
        assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_sankey_data(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_sankey_data()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_sankey_data(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_sankey_data() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveSankeyDataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
