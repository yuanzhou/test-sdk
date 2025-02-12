# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_entity_type_list_entity_types_response import ListEntityTypeListEntityTypesResponse

__all__ = ["ListEntityTypesResource", "AsyncListEntityTypesResource"]


class ListEntityTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ListEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return ListEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return ListEntityTypesResourceWithStreamingResponse(self)

    def list_entity_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEntityTypeListEntityTypesResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEntityTypeListEntityTypesResponse,
        )


class AsyncListEntityTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncListEntityTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncListEntityTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListEntityTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return AsyncListEntityTypesResourceWithStreamingResponse(self)

    async def list_entity_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEntityTypeListEntityTypesResponse:
        """Get a list of all the available entity types defined in the schema yaml"""
        return await self._get(
            "/entity-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEntityTypeListEntityTypesResponse,
        )


class ListEntityTypesResourceWithRawResponse:
    def __init__(self, list_entity_types: ListEntityTypesResource) -> None:
        self._list_entity_types = list_entity_types

        self.list_entity_types = to_raw_response_wrapper(
            list_entity_types.list_entity_types,
        )


class AsyncListEntityTypesResourceWithRawResponse:
    def __init__(self, list_entity_types: AsyncListEntityTypesResource) -> None:
        self._list_entity_types = list_entity_types

        self.list_entity_types = async_to_raw_response_wrapper(
            list_entity_types.list_entity_types,
        )


class ListEntityTypesResourceWithStreamingResponse:
    def __init__(self, list_entity_types: ListEntityTypesResource) -> None:
        self._list_entity_types = list_entity_types

        self.list_entity_types = to_streamed_response_wrapper(
            list_entity_types.list_entity_types,
        )


class AsyncListEntityTypesResourceWithStreamingResponse:
    def __init__(self, list_entity_types: AsyncListEntityTypesResource) -> None:
        self._list_entity_types = list_entity_types

        self.list_entity_types = async_to_streamed_response_wrapper(
            list_entity_types.list_entity_types,
        )
