# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.shared_params.upload import Upload
from ..types.update_uploads_bulk_update_uploads_bulk_response import UpdateUploadsBulkUpdateUploadsBulkResponse

__all__ = ["UpdateUploadsBulkResource", "AsyncUpdateUploadsBulkResource"]


class UpdateUploadsBulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpdateUploadsBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return UpdateUploadsBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpdateUploadsBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return UpdateUploadsBulkResourceWithStreamingResponse(self)

    def update_uploads_bulk(
        self,
        *,
        body: Iterable[Upload],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateUploadsBulkUpdateUploadsBulkResponse:
        """Bulk updating of entity type upload.

        it's only limited to the fields::
        assigned_to_group_name, ingest_task, status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/uploads",
            body=maybe_transform(body, Iterable[Upload]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUploadsBulkUpdateUploadsBulkResponse,
        )


class AsyncUpdateUploadsBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpdateUploadsBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpdateUploadsBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpdateUploadsBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncUpdateUploadsBulkResourceWithStreamingResponse(self)

    async def update_uploads_bulk(
        self,
        *,
        body: Iterable[Upload],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateUploadsBulkUpdateUploadsBulkResponse:
        """Bulk updating of entity type upload.

        it's only limited to the fields::
        assigned_to_group_name, ingest_task, status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/uploads",
            body=await async_maybe_transform(body, Iterable[Upload]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUploadsBulkUpdateUploadsBulkResponse,
        )


class UpdateUploadsBulkResourceWithRawResponse:
    def __init__(self, update_uploads_bulk: UpdateUploadsBulkResource) -> None:
        self._update_uploads_bulk = update_uploads_bulk

        self.update_uploads_bulk = to_raw_response_wrapper(
            update_uploads_bulk.update_uploads_bulk,
        )


class AsyncUpdateUploadsBulkResourceWithRawResponse:
    def __init__(self, update_uploads_bulk: AsyncUpdateUploadsBulkResource) -> None:
        self._update_uploads_bulk = update_uploads_bulk

        self.update_uploads_bulk = async_to_raw_response_wrapper(
            update_uploads_bulk.update_uploads_bulk,
        )


class UpdateUploadsBulkResourceWithStreamingResponse:
    def __init__(self, update_uploads_bulk: UpdateUploadsBulkResource) -> None:
        self._update_uploads_bulk = update_uploads_bulk

        self.update_uploads_bulk = to_streamed_response_wrapper(
            update_uploads_bulk.update_uploads_bulk,
        )


class AsyncUpdateUploadsBulkResourceWithStreamingResponse:
    def __init__(self, update_uploads_bulk: AsyncUpdateUploadsBulkResource) -> None:
        self._update_uploads_bulk = update_uploads_bulk

        self.update_uploads_bulk = async_to_streamed_response_wrapper(
            update_uploads_bulk.update_uploads_bulk,
        )
