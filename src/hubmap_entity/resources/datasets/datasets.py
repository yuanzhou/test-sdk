# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    dataset_retract_params,
    dataset_list_unpublished_params,
    dataset_create_components_params,
    dataset_retrieve_revisions_params,
    dataset_retrieve_paired_dataset_params,
    dataset_retrieve_multi_revisions_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .prov_info import (
    ProvInfoResource,
    AsyncProvInfoResource,
    ProvInfoResourceWithRawResponse,
    AsyncProvInfoResourceWithRawResponse,
    ProvInfoResourceWithStreamingResponse,
    AsyncProvInfoResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.dataset import Dataset as SharedDataset
from ...types.shared_params.dataset import Dataset as SharedParamsDataset
from ...types.dataset_bulk_update_response import DatasetBulkUpdateResponse
from ...types.dataset_list_donors_response import DatasetListDonorsResponse
from ...types.dataset_list_organs_response import DatasetListOrgansResponse
from ...types.dataset_list_samples_response import DatasetListSamplesResponse
from ...types.dataset_list_unpublished_response import DatasetListUnpublishedResponse
from ...types.dataset_create_components_response import DatasetCreateComponentsResponse
from ...types.dataset_retrieve_revisions_response import DatasetRetrieveRevisionsResponse
from ...types.dataset_retrieve_sankey_data_response import DatasetRetrieveSankeyDataResponse
from ...types.dataset_retrieve_prov_metadata_response import DatasetRetrieveProvMetadataResponse
from ...types.dataset_retrieve_paired_dataset_response import DatasetRetrievePairedDatasetResponse
from ...types.dataset_retrieve_multi_revisions_response import DatasetRetrieveMultiRevisionsResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def prov_info(self) -> ProvInfoResource:
        return ProvInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def bulk_update(
        self,
        *,
        body: Iterable[SharedParamsDataset],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetBulkUpdateResponse:
        """Bulk updating of entity type dataset.

        it's only limited to the fields::
        assigned_to_group_name, ingest_task, status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/datasets",
            body=maybe_transform(body, Iterable[SharedParamsDataset]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetBulkUpdateResponse,
        )

    def create_components(
        self,
        *,
        creation_action: str | NotGiven = NOT_GIVEN,
        datasets: Iterable[dataset_create_components_params.Dataset] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuids: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateComponentsResponse:
        """
        Create multiple component datasets from a single Multi-Assay ancestor

        Args:
          creation_action: the action event that will describe the activity node. Allowed valuese are
              "Multi-Assay Split"

          direct_ancestor_uuids: the uuid for the parent multi assay dataset

          group_uuid: the group uuid for the new component datasets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/datasets/components",
            body=maybe_transform(
                {
                    "creation_action": creation_action,
                    "datasets": datasets,
                    "direct_ancestor_uuids": direct_ancestor_uuids,
                    "group_uuid": group_uuid,
                },
                dataset_create_components_params.DatasetCreateComponentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateComponentsResponse,
        )

    def list_donors(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListDonorsResponse:
        """
        Retrieve a list of all of the donors that are associated with the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/donors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListDonorsResponse,
        )

    def list_organs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListOrgansResponse:
        """
        Retrieve a list of all of the smples that are organs that are associated with
        the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/organs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListOrgansResponse,
        )

    def list_samples(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListSamplesResponse:
        """
        Retrieve a list of all of the samples that are not organs that are associated
        with the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/samples",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListSamplesResponse,
        )

    def list_unpublished(
        self,
        *,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListUnpublishedResponse:
        """
        returns information about all unpublished datasets in json or tsv format.
        Defaults to json

        Args:
          format: The desired return format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/datasets/unpublished",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, dataset_list_unpublished_params.DatasetListUnpublishedParams),
            ),
            cast_to=DatasetListUnpublishedResponse,
        )

    def retract(
        self,
        id: str,
        *,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retracts a dataset after it has been published.

        Requires a json body with a
        single field {retraction_reason: string}. The dataset for the given id is
        modified to include this new retraction_reason field and sets the dataset
        property sub_status to Retracted. The complete modified dataset is returned.
        Requires that the dataset being retracted has already been published
        (dataset.status == Published. Requires a user token with membership in the
        HuBMAP-Data-Admin group otherwise then a 403 will be returned.

        Args:
          retraction_reason: Free text describing why the dataset was retracted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/datasets/{id}/retract",
            body=maybe_transform({"retraction_reason": retraction_reason}, dataset_retract_params.DatasetRetractParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_latest_revision(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedDataset:
        """Retrive the latest (newest) revision of a given Dataset.

        Public/Consortium
        access rules apply - if no token/consortium access then must be for a public
        dataset and the returned Dataset must be the latest public version. If the given
        dataset itself is the latest revision, meaning it has no next revisions, this
        dataset gets returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/latest-revision",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedDataset,
        )

    def retrieve_multi_revisions(
        self,
        id: str,
        *,
        include_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveMultiRevisionsResponse:
        """
        Retrieve a list of all multi revisions of a dataset from the id of any dataset
        in the chain. E.g: If there are 5 revisions, and the id for revision 4 is given,
        a list of revisions 1-5 will be returned in reverse order (newest first).
        Non-public access is only required to retrieve information on non-published
        datasets. Output will be a list of dictionaries. Each dictionary contains the
        dataset revision number and its list of uuids. Optionally, the full dataset can
        be included for each.

        Args:
          include_dataset: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', the full dataset for each revision will be included in the
              response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/multi-revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_dataset": include_dataset},
                    dataset_retrieve_multi_revisions_params.DatasetRetrieveMultiRevisionsParams,
                ),
            ),
            cast_to=DatasetRetrieveMultiRevisionsResponse,
        )

    def retrieve_paired_dataset(
        self,
        id: str,
        *,
        data_type: str,
        search_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrievePairedDatasetResponse:
        """
        Retrieve uuids for associated dataset of given data_type which shares a sample
        ancestor of given dataset id

        Args:
          data_type: The desired data_type to be searched for

          search_depth: The maximum number of generations of datasets beneath the sample to search for
              the paired dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/paired-dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "data_type": data_type,
                        "search_depth": search_depth,
                    },
                    dataset_retrieve_paired_dataset_params.DatasetRetrievePairedDatasetParams,
                ),
            ),
            cast_to=DatasetRetrievePairedDatasetResponse,
        )

    def retrieve_prov_metadata(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveProvMetadataResponse:
        """
        Returns full provenance metadata for a Dataset, which can be used when
        publishing the Dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/prov-metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveProvMetadataResponse,
        )

    def retrieve_revision(
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
        """Retrive the calculated revision number of a Dataset.

        The calculated revision is
        number is based on the [:REVISION_OF] relationships to the oldest dataset in a
        revision chain. Where the oldest dataset = 1 and each newer version is
        incremented by one (1, 2, 3 ...). Public/Consortium access rules apply, if is
        for a non-public dataset and no token or a token without membership in
        HuBMAP-Read group is sent with the request then a 403 response should be
        returned.

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
            f"/datasets/{id}/revision",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_revisions(
        self,
        id: str,
        *,
        include_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveRevisionsResponse:
        """
        From a given ID of a versioned dataset, retrieve a list of every dataset in the
        chain ordered from most recent to oldest. The revision number, as well as the
        dataset uuid will be included. An optional parameter ?include_dataset=true will
        include the full dataset for each revision as well. Public/Consortium access
        rules apply, if is for a non-public dataset and no token or a token without
        membership in HuBMAP-Read group is sent with the request then a 403 response
        should be returned. If the given id is published, but later revisions are not
        and the user is not in HuBMAP-Read group, only published revisions will be
        returned. The field next_revision_uuid will not be returned if the next revision
        is unpublished

        Args:
          include_dataset: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', the full dataset for each revision will be included in the
              response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_dataset": include_dataset},
                    dataset_retrieve_revisions_params.DatasetRetrieveRevisionsParams,
                ),
            ),
            cast_to=DatasetRetrieveRevisionsResponse,
        )

    def retrieve_sankey_data(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveSankeyDataResponse:
        """
        Retrieves the information needed to generate the sankey on software-docs as a
        json.
        """
        return self._get(
            "/datasets/sankey_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveSankeyDataResponse,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def prov_info(self) -> AsyncProvInfoResource:
        return AsyncProvInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def bulk_update(
        self,
        *,
        body: Iterable[SharedParamsDataset],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetBulkUpdateResponse:
        """Bulk updating of entity type dataset.

        it's only limited to the fields::
        assigned_to_group_name, ingest_task, status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/datasets",
            body=await async_maybe_transform(body, Iterable[SharedParamsDataset]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetBulkUpdateResponse,
        )

    async def create_components(
        self,
        *,
        creation_action: str | NotGiven = NOT_GIVEN,
        datasets: Iterable[dataset_create_components_params.Dataset] | NotGiven = NOT_GIVEN,
        direct_ancestor_uuids: str | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetCreateComponentsResponse:
        """
        Create multiple component datasets from a single Multi-Assay ancestor

        Args:
          creation_action: the action event that will describe the activity node. Allowed valuese are
              "Multi-Assay Split"

          direct_ancestor_uuids: the uuid for the parent multi assay dataset

          group_uuid: the group uuid for the new component datasets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/datasets/components",
            body=await async_maybe_transform(
                {
                    "creation_action": creation_action,
                    "datasets": datasets,
                    "direct_ancestor_uuids": direct_ancestor_uuids,
                    "group_uuid": group_uuid,
                },
                dataset_create_components_params.DatasetCreateComponentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCreateComponentsResponse,
        )

    async def list_donors(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListDonorsResponse:
        """
        Retrieve a list of all of the donors that are associated with the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/donors",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListDonorsResponse,
        )

    async def list_organs(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListOrgansResponse:
        """
        Retrieve a list of all of the smples that are organs that are associated with
        the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/organs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListOrgansResponse,
        )

    async def list_samples(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListSamplesResponse:
        """
        Retrieve a list of all of the samples that are not organs that are associated
        with the dataset id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/samples",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListSamplesResponse,
        )

    async def list_unpublished(
        self,
        *,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListUnpublishedResponse:
        """
        returns information about all unpublished datasets in json or tsv format.
        Defaults to json

        Args:
          format: The desired return format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/datasets/unpublished",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, dataset_list_unpublished_params.DatasetListUnpublishedParams
                ),
            ),
            cast_to=DatasetListUnpublishedResponse,
        )

    async def retract(
        self,
        id: str,
        *,
        retraction_reason: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Retracts a dataset after it has been published.

        Requires a json body with a
        single field {retraction_reason: string}. The dataset for the given id is
        modified to include this new retraction_reason field and sets the dataset
        property sub_status to Retracted. The complete modified dataset is returned.
        Requires that the dataset being retracted has already been published
        (dataset.status == Published. Requires a user token with membership in the
        HuBMAP-Data-Admin group otherwise then a 403 will be returned.

        Args:
          retraction_reason: Free text describing why the dataset was retracted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/datasets/{id}/retract",
            body=await async_maybe_transform(
                {"retraction_reason": retraction_reason}, dataset_retract_params.DatasetRetractParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_latest_revision(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SharedDataset:
        """Retrive the latest (newest) revision of a given Dataset.

        Public/Consortium
        access rules apply - if no token/consortium access then must be for a public
        dataset and the returned Dataset must be the latest public version. If the given
        dataset itself is the latest revision, meaning it has no next revisions, this
        dataset gets returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/latest-revision",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedDataset,
        )

    async def retrieve_multi_revisions(
        self,
        id: str,
        *,
        include_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveMultiRevisionsResponse:
        """
        Retrieve a list of all multi revisions of a dataset from the id of any dataset
        in the chain. E.g: If there are 5 revisions, and the id for revision 4 is given,
        a list of revisions 1-5 will be returned in reverse order (newest first).
        Non-public access is only required to retrieve information on non-published
        datasets. Output will be a list of dictionaries. Each dictionary contains the
        dataset revision number and its list of uuids. Optionally, the full dataset can
        be included for each.

        Args:
          include_dataset: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', the full dataset for each revision will be included in the
              response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/multi-revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_dataset": include_dataset},
                    dataset_retrieve_multi_revisions_params.DatasetRetrieveMultiRevisionsParams,
                ),
            ),
            cast_to=DatasetRetrieveMultiRevisionsResponse,
        )

    async def retrieve_paired_dataset(
        self,
        id: str,
        *,
        data_type: str,
        search_depth: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrievePairedDatasetResponse:
        """
        Retrieve uuids for associated dataset of given data_type which shares a sample
        ancestor of given dataset id

        Args:
          data_type: The desired data_type to be searched for

          search_depth: The maximum number of generations of datasets beneath the sample to search for
              the paired dataset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/paired-dataset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "data_type": data_type,
                        "search_depth": search_depth,
                    },
                    dataset_retrieve_paired_dataset_params.DatasetRetrievePairedDatasetParams,
                ),
            ),
            cast_to=DatasetRetrievePairedDatasetResponse,
        )

    async def retrieve_prov_metadata(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveProvMetadataResponse:
        """
        Returns full provenance metadata for a Dataset, which can be used when
        publishing the Dataset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/prov-metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveProvMetadataResponse,
        )

    async def retrieve_revision(
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
        """Retrive the calculated revision number of a Dataset.

        The calculated revision is
        number is based on the [:REVISION_OF] relationships to the oldest dataset in a
        revision chain. Where the oldest dataset = 1 and each newer version is
        incremented by one (1, 2, 3 ...). Public/Consortium access rules apply, if is
        for a non-public dataset and no token or a token without membership in
        HuBMAP-Read group is sent with the request then a 403 response should be
        returned.

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
            f"/datasets/{id}/revision",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_revisions(
        self,
        id: str,
        *,
        include_dataset: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveRevisionsResponse:
        """
        From a given ID of a versioned dataset, retrieve a list of every dataset in the
        chain ordered from most recent to oldest. The revision number, as well as the
        dataset uuid will be included. An optional parameter ?include_dataset=true will
        include the full dataset for each revision as well. Public/Consortium access
        rules apply, if is for a non-public dataset and no token or a token without
        membership in HuBMAP-Read group is sent with the request then a 403 response
        should be returned. If the given id is published, but later revisions are not
        and the user is not in HuBMAP-Read group, only published revisions will be
        returned. The field next_revision_uuid will not be returned if the next revision
        is unpublished

        Args:
          include_dataset: A case insensitive string. Any value besides true will have no effect. If the
              string is 'true', the full dataset for each revision will be included in the
              response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_dataset": include_dataset},
                    dataset_retrieve_revisions_params.DatasetRetrieveRevisionsParams,
                ),
            ),
            cast_to=DatasetRetrieveRevisionsResponse,
        )

    async def retrieve_sankey_data(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveSankeyDataResponse:
        """
        Retrieves the information needed to generate the sankey on software-docs as a
        json.
        """
        return await self._get(
            "/datasets/sankey_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetRetrieveSankeyDataResponse,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.bulk_update = to_raw_response_wrapper(
            datasets.bulk_update,
        )
        self.create_components = to_raw_response_wrapper(
            datasets.create_components,
        )
        self.list_donors = to_raw_response_wrapper(
            datasets.list_donors,
        )
        self.list_organs = to_raw_response_wrapper(
            datasets.list_organs,
        )
        self.list_samples = to_raw_response_wrapper(
            datasets.list_samples,
        )
        self.list_unpublished = to_raw_response_wrapper(
            datasets.list_unpublished,
        )
        self.retract = to_raw_response_wrapper(
            datasets.retract,
        )
        self.retrieve_latest_revision = to_raw_response_wrapper(
            datasets.retrieve_latest_revision,
        )
        self.retrieve_multi_revisions = to_raw_response_wrapper(
            datasets.retrieve_multi_revisions,
        )
        self.retrieve_paired_dataset = to_raw_response_wrapper(
            datasets.retrieve_paired_dataset,
        )
        self.retrieve_prov_metadata = to_raw_response_wrapper(
            datasets.retrieve_prov_metadata,
        )
        self.retrieve_revision = to_raw_response_wrapper(
            datasets.retrieve_revision,
        )
        self.retrieve_revisions = to_raw_response_wrapper(
            datasets.retrieve_revisions,
        )
        self.retrieve_sankey_data = to_raw_response_wrapper(
            datasets.retrieve_sankey_data,
        )

    @cached_property
    def prov_info(self) -> ProvInfoResourceWithRawResponse:
        return ProvInfoResourceWithRawResponse(self._datasets.prov_info)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.bulk_update = async_to_raw_response_wrapper(
            datasets.bulk_update,
        )
        self.create_components = async_to_raw_response_wrapper(
            datasets.create_components,
        )
        self.list_donors = async_to_raw_response_wrapper(
            datasets.list_donors,
        )
        self.list_organs = async_to_raw_response_wrapper(
            datasets.list_organs,
        )
        self.list_samples = async_to_raw_response_wrapper(
            datasets.list_samples,
        )
        self.list_unpublished = async_to_raw_response_wrapper(
            datasets.list_unpublished,
        )
        self.retract = async_to_raw_response_wrapper(
            datasets.retract,
        )
        self.retrieve_latest_revision = async_to_raw_response_wrapper(
            datasets.retrieve_latest_revision,
        )
        self.retrieve_multi_revisions = async_to_raw_response_wrapper(
            datasets.retrieve_multi_revisions,
        )
        self.retrieve_paired_dataset = async_to_raw_response_wrapper(
            datasets.retrieve_paired_dataset,
        )
        self.retrieve_prov_metadata = async_to_raw_response_wrapper(
            datasets.retrieve_prov_metadata,
        )
        self.retrieve_revision = async_to_raw_response_wrapper(
            datasets.retrieve_revision,
        )
        self.retrieve_revisions = async_to_raw_response_wrapper(
            datasets.retrieve_revisions,
        )
        self.retrieve_sankey_data = async_to_raw_response_wrapper(
            datasets.retrieve_sankey_data,
        )

    @cached_property
    def prov_info(self) -> AsyncProvInfoResourceWithRawResponse:
        return AsyncProvInfoResourceWithRawResponse(self._datasets.prov_info)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.bulk_update = to_streamed_response_wrapper(
            datasets.bulk_update,
        )
        self.create_components = to_streamed_response_wrapper(
            datasets.create_components,
        )
        self.list_donors = to_streamed_response_wrapper(
            datasets.list_donors,
        )
        self.list_organs = to_streamed_response_wrapper(
            datasets.list_organs,
        )
        self.list_samples = to_streamed_response_wrapper(
            datasets.list_samples,
        )
        self.list_unpublished = to_streamed_response_wrapper(
            datasets.list_unpublished,
        )
        self.retract = to_streamed_response_wrapper(
            datasets.retract,
        )
        self.retrieve_latest_revision = to_streamed_response_wrapper(
            datasets.retrieve_latest_revision,
        )
        self.retrieve_multi_revisions = to_streamed_response_wrapper(
            datasets.retrieve_multi_revisions,
        )
        self.retrieve_paired_dataset = to_streamed_response_wrapper(
            datasets.retrieve_paired_dataset,
        )
        self.retrieve_prov_metadata = to_streamed_response_wrapper(
            datasets.retrieve_prov_metadata,
        )
        self.retrieve_revision = to_streamed_response_wrapper(
            datasets.retrieve_revision,
        )
        self.retrieve_revisions = to_streamed_response_wrapper(
            datasets.retrieve_revisions,
        )
        self.retrieve_sankey_data = to_streamed_response_wrapper(
            datasets.retrieve_sankey_data,
        )

    @cached_property
    def prov_info(self) -> ProvInfoResourceWithStreamingResponse:
        return ProvInfoResourceWithStreamingResponse(self._datasets.prov_info)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.bulk_update = async_to_streamed_response_wrapper(
            datasets.bulk_update,
        )
        self.create_components = async_to_streamed_response_wrapper(
            datasets.create_components,
        )
        self.list_donors = async_to_streamed_response_wrapper(
            datasets.list_donors,
        )
        self.list_organs = async_to_streamed_response_wrapper(
            datasets.list_organs,
        )
        self.list_samples = async_to_streamed_response_wrapper(
            datasets.list_samples,
        )
        self.list_unpublished = async_to_streamed_response_wrapper(
            datasets.list_unpublished,
        )
        self.retract = async_to_streamed_response_wrapper(
            datasets.retract,
        )
        self.retrieve_latest_revision = async_to_streamed_response_wrapper(
            datasets.retrieve_latest_revision,
        )
        self.retrieve_multi_revisions = async_to_streamed_response_wrapper(
            datasets.retrieve_multi_revisions,
        )
        self.retrieve_paired_dataset = async_to_streamed_response_wrapper(
            datasets.retrieve_paired_dataset,
        )
        self.retrieve_prov_metadata = async_to_streamed_response_wrapper(
            datasets.retrieve_prov_metadata,
        )
        self.retrieve_revision = async_to_streamed_response_wrapper(
            datasets.retrieve_revision,
        )
        self.retrieve_revisions = async_to_streamed_response_wrapper(
            datasets.retrieve_revisions,
        )
        self.retrieve_sankey_data = async_to_streamed_response_wrapper(
            datasets.retrieve_sankey_data,
        )

    @cached_property
    def prov_info(self) -> AsyncProvInfoResourceWithStreamingResponse:
        return AsyncProvInfoResourceWithStreamingResponse(self._datasets.prov_info)
