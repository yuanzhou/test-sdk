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
from ..types.retrieve_child_retrieve_children_response import RetrieveChildRetrieveChildrenResponse

__all__ = ["RetrieveChildrenResource", "AsyncRetrieveChildrenResource"]


class RetrieveChildrenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveChildrenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return RetrieveChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveChildrenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return RetrieveChildrenResourceWithStreamingResponse(self)

    def retrieve_children(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveChildRetrieveChildrenResponse:
        """Get the list of children directly connected to an Entity.

        The children are the
        nodes one level below the current node. This list only returns the items one
        level below in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/children/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveChildRetrieveChildrenResponse,
        )


class AsyncRetrieveChildrenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveChildrenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveChildrenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveChildrenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return AsyncRetrieveChildrenResourceWithStreamingResponse(self)

    async def retrieve_children(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveChildRetrieveChildrenResponse:
        """Get the list of children directly connected to an Entity.

        The children are the
        nodes one level below the current node. This list only returns the items one
        level below in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/children/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveChildRetrieveChildrenResponse,
        )


class RetrieveChildrenResourceWithRawResponse:
    def __init__(self, retrieve_children: RetrieveChildrenResource) -> None:
        self._retrieve_children = retrieve_children

        self.retrieve_children = to_raw_response_wrapper(
            retrieve_children.retrieve_children,
        )


class AsyncRetrieveChildrenResourceWithRawResponse:
    def __init__(self, retrieve_children: AsyncRetrieveChildrenResource) -> None:
        self._retrieve_children = retrieve_children

        self.retrieve_children = async_to_raw_response_wrapper(
            retrieve_children.retrieve_children,
        )


class RetrieveChildrenResourceWithStreamingResponse:
    def __init__(self, retrieve_children: RetrieveChildrenResource) -> None:
        self._retrieve_children = retrieve_children

        self.retrieve_children = to_streamed_response_wrapper(
            retrieve_children.retrieve_children,
        )


class AsyncRetrieveChildrenResourceWithStreamingResponse:
    def __init__(self, retrieve_children: AsyncRetrieveChildrenResource) -> None:
        self._retrieve_children = retrieve_children

        self.retrieve_children = async_to_streamed_response_wrapper(
            retrieve_children.retrieve_children,
        )
