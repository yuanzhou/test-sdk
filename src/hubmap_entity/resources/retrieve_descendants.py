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
from ..types.retrieve_descendant_retrieve_descendants_response import RetrieveDescendantRetrieveDescendantsResponse

__all__ = ["RetrieveDescendantsResource", "AsyncRetrieveDescendantsResource"]


class RetrieveDescendantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrieveDescendantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return RetrieveDescendantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieveDescendantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return RetrieveDescendantsResourceWithStreamingResponse(self)

    def retrieve_descendants(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveDescendantRetrieveDescendantsResponse:
        """Get the descendant list for an Entity.

        The descendants are the nodes
        "downstream" from the current node. This list traverses all the levels in the
        graph. Returns all descendants as an array of Entities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/descendants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveDescendantRetrieveDescendantsResponse,
        )


class AsyncRetrieveDescendantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrieveDescendantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieveDescendantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieveDescendantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubmap-entity-python#with_streaming_response
        """
        return AsyncRetrieveDescendantsResourceWithStreamingResponse(self)

    async def retrieve_descendants(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveDescendantRetrieveDescendantsResponse:
        """Get the descendant list for an Entity.

        The descendants are the nodes
        "downstream" from the current node. This list traverses all the levels in the
        graph. Returns all descendants as an array of Entities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/descendants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveDescendantRetrieveDescendantsResponse,
        )


class RetrieveDescendantsResourceWithRawResponse:
    def __init__(self, retrieve_descendants: RetrieveDescendantsResource) -> None:
        self._retrieve_descendants = retrieve_descendants

        self.retrieve_descendants = to_raw_response_wrapper(
            retrieve_descendants.retrieve_descendants,
        )


class AsyncRetrieveDescendantsResourceWithRawResponse:
    def __init__(self, retrieve_descendants: AsyncRetrieveDescendantsResource) -> None:
        self._retrieve_descendants = retrieve_descendants

        self.retrieve_descendants = async_to_raw_response_wrapper(
            retrieve_descendants.retrieve_descendants,
        )


class RetrieveDescendantsResourceWithStreamingResponse:
    def __init__(self, retrieve_descendants: RetrieveDescendantsResource) -> None:
        self._retrieve_descendants = retrieve_descendants

        self.retrieve_descendants = to_streamed_response_wrapper(
            retrieve_descendants.retrieve_descendants,
        )


class AsyncRetrieveDescendantsResourceWithStreamingResponse:
    def __init__(self, retrieve_descendants: AsyncRetrieveDescendantsResource) -> None:
        self._retrieve_descendants = retrieve_descendants

        self.retrieve_descendants = async_to_streamed_response_wrapper(
            retrieve_descendants.retrieve_descendants,
        )
