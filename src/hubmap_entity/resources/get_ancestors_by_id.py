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
from ..types.get_ancestors_by_id_get_ancestors_by_id_response import GetAncestorsByIDGetAncestorsByIDResponse

__all__ = ["GetAncestorsByIDResource", "AsyncGetAncestorsByIDResource"]


class GetAncestorsByIDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GetAncestorsByIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return GetAncestorsByIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetAncestorsByIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return GetAncestorsByIDResourceWithStreamingResponse(self)

    def get_ancestors_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetAncestorsByIDGetAncestorsByIDResponse:
        """Get the ancestor list for an Entity.

        The ancestors are the nodes connected
        "upstream" from the current node. This list traverses all the levels in the
        graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/ancestors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetAncestorsByIDGetAncestorsByIDResponse,
        )


class AsyncGetAncestorsByIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGetAncestorsByIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGetAncestorsByIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetAncestorsByIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return AsyncGetAncestorsByIDResourceWithStreamingResponse(self)

    async def get_ancestors_by_id(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetAncestorsByIDGetAncestorsByIDResponse:
        """Get the ancestor list for an Entity.

        The ancestors are the nodes connected
        "upstream" from the current node. This list traverses all the levels in the
        graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/ancestors/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetAncestorsByIDGetAncestorsByIDResponse,
        )


class GetAncestorsByIDResourceWithRawResponse:
    def __init__(self, get_ancestors_by_id: GetAncestorsByIDResource) -> None:
        self._get_ancestors_by_id = get_ancestors_by_id

        self.get_ancestors_by_id = to_raw_response_wrapper(
            get_ancestors_by_id.get_ancestors_by_id,
        )


class AsyncGetAncestorsByIDResourceWithRawResponse:
    def __init__(self, get_ancestors_by_id: AsyncGetAncestorsByIDResource) -> None:
        self._get_ancestors_by_id = get_ancestors_by_id

        self.get_ancestors_by_id = async_to_raw_response_wrapper(
            get_ancestors_by_id.get_ancestors_by_id,
        )


class GetAncestorsByIDResourceWithStreamingResponse:
    def __init__(self, get_ancestors_by_id: GetAncestorsByIDResource) -> None:
        self._get_ancestors_by_id = get_ancestors_by_id

        self.get_ancestors_by_id = to_streamed_response_wrapper(
            get_ancestors_by_id.get_ancestors_by_id,
        )


class AsyncGetAncestorsByIDResourceWithStreamingResponse:
    def __init__(self, get_ancestors_by_id: AsyncGetAncestorsByIDResource) -> None:
        self._get_ancestors_by_id = get_ancestors_by_id

        self.get_ancestors_by_id = async_to_streamed_response_wrapper(
            get_ancestors_by_id.get_ancestors_by_id,
        )
