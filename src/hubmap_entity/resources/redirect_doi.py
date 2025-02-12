# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["RedirectDoiResource", "AsyncRedirectDoiResource"]


class RedirectDoiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedirectDoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return RedirectDoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedirectDoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return RedirectDoiResourceWithStreamingResponse(self)

    def redirect_doi(
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
        """
        Redirect a request from a doi service

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
            f"/doi/redirect/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRedirectDoiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedirectDoiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRedirectDoiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedirectDoiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return AsyncRedirectDoiResourceWithStreamingResponse(self)

    async def redirect_doi(
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
        """
        Redirect a request from a doi service

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
            f"/doi/redirect/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RedirectDoiResourceWithRawResponse:
    def __init__(self, redirect_doi: RedirectDoiResource) -> None:
        self._redirect_doi = redirect_doi

        self.redirect_doi = to_raw_response_wrapper(
            redirect_doi.redirect_doi,
        )


class AsyncRedirectDoiResourceWithRawResponse:
    def __init__(self, redirect_doi: AsyncRedirectDoiResource) -> None:
        self._redirect_doi = redirect_doi

        self.redirect_doi = async_to_raw_response_wrapper(
            redirect_doi.redirect_doi,
        )


class RedirectDoiResourceWithStreamingResponse:
    def __init__(self, redirect_doi: RedirectDoiResource) -> None:
        self._redirect_doi = redirect_doi

        self.redirect_doi = to_streamed_response_wrapper(
            redirect_doi.redirect_doi,
        )


class AsyncRedirectDoiResourceWithStreamingResponse:
    def __init__(self, redirect_doi: AsyncRedirectDoiResource) -> None:
        self._redirect_doi = redirect_doi

        self.redirect_doi = async_to_streamed_response_wrapper(
            redirect_doi.redirect_doi,
        )
