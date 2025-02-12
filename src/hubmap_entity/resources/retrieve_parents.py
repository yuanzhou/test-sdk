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
from ..types.retrieve_parent_retrieve_parents_response import RetrieveParentRetrieveParentsResponse

__all__ = ["RetrieveParentsResource", "AsyncRetrieveParentsResource"]


class RetrieveParentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveParentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveParentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveParentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return RetrieveParentsResourceWithStreamingResponse(self)

    def retrieve_parents(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveParentRetrieveParentsResponse:
        """Get the immediate parent list for an Entity.

        The parents are the nodes connected
        one level "upstream" from the current node. This list only goes to the next
        higher level in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/parents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveParentRetrieveParentsResponse,
        )


class AsyncRetrieveParentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveParentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveParentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveParentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncRetrieveParentsResourceWithStreamingResponse(self)

    async def retrieve_parents(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveParentRetrieveParentsResponse:
        """Get the immediate parent list for an Entity.

        The parents are the nodes connected
        one level "upstream" from the current node. This list only goes to the next
        higher level in the graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/parents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveParentRetrieveParentsResponse,
        )


class RetrieveParentsResourceWithRawResponse:
    def __init__(self, retrieve_parents: RetrieveParentsResource) -> None:
        self._retrieve_parents = retrieve_parents

        self.retrieve_parents = to_raw_response_wrapper(
            retrieve_parents.retrieve_parents,
        )


class AsyncRetrieveParentsResourceWithRawResponse:
    def __init__(self, retrieve_parents: AsyncRetrieveParentsResource) -> None:
        self._retrieve_parents = retrieve_parents

        self.retrieve_parents = async_to_raw_response_wrapper(
            retrieve_parents.retrieve_parents,
        )


class RetrieveParentsResourceWithStreamingResponse:
    def __init__(self, retrieve_parents: RetrieveParentsResource) -> None:
        self._retrieve_parents = retrieve_parents

        self.retrieve_parents = to_streamed_response_wrapper(
            retrieve_parents.retrieve_parents,
        )


class AsyncRetrieveParentsResourceWithStreamingResponse:
    def __init__(self, retrieve_parents: AsyncRetrieveParentsResource) -> None:
        self._retrieve_parents = retrieve_parents

        self.retrieve_parents = async_to_streamed_response_wrapper(
            retrieve_parents.retrieve_parents,
        )
