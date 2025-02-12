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
from ..types.retrieve_ancestor_retrieve_ancestors_response import RetrieveAncestorRetrieveAncestorsResponse

__all__ = ["RetrieveAncestorsResource", "AsyncRetrieveAncestorsResource"]


class RetrieveAncestorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveAncestorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveAncestorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveAncestorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return RetrieveAncestorsResourceWithStreamingResponse(self)

    def retrieve_ancestors(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveAncestorRetrieveAncestorsResponse:
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
            cast_to=RetrieveAncestorRetrieveAncestorsResponse,
        )


class AsyncRetrieveAncestorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveAncestorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveAncestorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveAncestorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncRetrieveAncestorsResourceWithStreamingResponse(self)

    async def retrieve_ancestors(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveAncestorRetrieveAncestorsResponse:
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
            cast_to=RetrieveAncestorRetrieveAncestorsResponse,
        )


class RetrieveAncestorsResourceWithRawResponse:
    def __init__(self, retrieve_ancestors: RetrieveAncestorsResource) -> None:
        self._retrieve_ancestors = retrieve_ancestors

        self.retrieve_ancestors = to_raw_response_wrapper(
            retrieve_ancestors.retrieve_ancestors,
        )


class AsyncRetrieveAncestorsResourceWithRawResponse:
    def __init__(self, retrieve_ancestors: AsyncRetrieveAncestorsResource) -> None:
        self._retrieve_ancestors = retrieve_ancestors

        self.retrieve_ancestors = async_to_raw_response_wrapper(
            retrieve_ancestors.retrieve_ancestors,
        )


class RetrieveAncestorsResourceWithStreamingResponse:
    def __init__(self, retrieve_ancestors: RetrieveAncestorsResource) -> None:
        self._retrieve_ancestors = retrieve_ancestors

        self.retrieve_ancestors = to_streamed_response_wrapper(
            retrieve_ancestors.retrieve_ancestors,
        )


class AsyncRetrieveAncestorsResourceWithStreamingResponse:
    def __init__(self, retrieve_ancestors: AsyncRetrieveAncestorsResource) -> None:
        self._retrieve_ancestors = retrieve_ancestors

        self.retrieve_ancestors = async_to_streamed_response_wrapper(
            retrieve_ancestors.retrieve_ancestors,
        )
