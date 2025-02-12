# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.datasets import prov_info_list_all_params, prov_info_retrieve_params
from ...types.datasets.prov_info_list_all_response import ProvInfoListAllResponse
from ...types.datasets.prov_info_retrieve_response import ProvInfoRetrieveResponse

__all__ = ["ProvInfoResource", "AsyncProvInfoResource"]


class ProvInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return ProvInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return ProvInfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        format: Literal["json", "tsv"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvInfoRetrieveResponse:
        """
        returns aLL provenance information for a single dataset in a default table/tsv
        format or optionally a json format when an optional ?format=json parameter is
        provided

        Args:
          format: A case insensitive string. Any value besides 'json' will have no effect. If the
              string is 'json', provenance info will be returned as a json. Otherwise, it will
              be returned as a tsv file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/datasets/{id}/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, prov_info_retrieve_params.ProvInfoRetrieveParams),
            ),
            cast_to=ProvInfoRetrieveResponse,
        )

    def list_all(
        self,
        *,
        dataset_status: Literal["qa", "new", "published"] | NotGiven = NOT_GIVEN,
        format: Literal["json", "tsv"] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        has_rui_info: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        organ: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvInfoListAllResponse:
        """
        returns ALL provenance information for ALL datasets in a default table/tsv
        format or optionally a json format when an optional ?format=json parameter is
        provided

        Args:
          dataset_status: Case insensitive string indicating the current status of a dataset

          format: A case insensitive string. Any value besides 'json' will have no effect. If the
              string is 'json', provenance info will be returned as a json. Otherwise, it will
              be returned as a tsv file

          group_uuid: The uuid of the group

          has_rui_info: A case insensitive string. Any value besides true or false will cause a 400
              exception.

          organ: Case insensitive string for 2 character organ code. Values must be present on
              organ yaml or a 400 exception is raised

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/datasets/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_status": dataset_status,
                        "format": format,
                        "group_uuid": group_uuid,
                        "has_rui_info": has_rui_info,
                        "organ": organ,
                    },
                    prov_info_list_all_params.ProvInfoListAllParams,
                ),
            ),
            cast_to=ProvInfoListAllResponse,
        )


class AsyncProvInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/yuanzhou/test-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProvInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/yuanzhou/test-sdk#with_streaming_response
        """
        return AsyncProvInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        format: Literal["json", "tsv"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvInfoRetrieveResponse:
        """
        returns aLL provenance information for a single dataset in a default table/tsv
        format or optionally a json format when an optional ?format=json parameter is
        provided

        Args:
          format: A case insensitive string. Any value besides 'json' will have no effect. If the
              string is 'json', provenance info will be returned as a json. Otherwise, it will
              be returned as a tsv file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/datasets/{id}/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, prov_info_retrieve_params.ProvInfoRetrieveParams),
            ),
            cast_to=ProvInfoRetrieveResponse,
        )

    async def list_all(
        self,
        *,
        dataset_status: Literal["qa", "new", "published"] | NotGiven = NOT_GIVEN,
        format: Literal["json", "tsv"] | NotGiven = NOT_GIVEN,
        group_uuid: str | NotGiven = NOT_GIVEN,
        has_rui_info: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        organ: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProvInfoListAllResponse:
        """
        returns ALL provenance information for ALL datasets in a default table/tsv
        format or optionally a json format when an optional ?format=json parameter is
        provided

        Args:
          dataset_status: Case insensitive string indicating the current status of a dataset

          format: A case insensitive string. Any value besides 'json' will have no effect. If the
              string is 'json', provenance info will be returned as a json. Otherwise, it will
              be returned as a tsv file

          group_uuid: The uuid of the group

          has_rui_info: A case insensitive string. Any value besides true or false will cause a 400
              exception.

          organ: Case insensitive string for 2 character organ code. Values must be present on
              organ yaml or a 400 exception is raised

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/datasets/prov-info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_status": dataset_status,
                        "format": format,
                        "group_uuid": group_uuid,
                        "has_rui_info": has_rui_info,
                        "organ": organ,
                    },
                    prov_info_list_all_params.ProvInfoListAllParams,
                ),
            ),
            cast_to=ProvInfoListAllResponse,
        )


class ProvInfoResourceWithRawResponse:
    def __init__(self, prov_info: ProvInfoResource) -> None:
        self._prov_info = prov_info

        self.retrieve = to_raw_response_wrapper(
            prov_info.retrieve,
        )
        self.list_all = to_raw_response_wrapper(
            prov_info.list_all,
        )


class AsyncProvInfoResourceWithRawResponse:
    def __init__(self, prov_info: AsyncProvInfoResource) -> None:
        self._prov_info = prov_info

        self.retrieve = async_to_raw_response_wrapper(
            prov_info.retrieve,
        )
        self.list_all = async_to_raw_response_wrapper(
            prov_info.list_all,
        )


class ProvInfoResourceWithStreamingResponse:
    def __init__(self, prov_info: ProvInfoResource) -> None:
        self._prov_info = prov_info

        self.retrieve = to_streamed_response_wrapper(
            prov_info.retrieve,
        )
        self.list_all = to_streamed_response_wrapper(
            prov_info.list_all,
        )


class AsyncProvInfoResourceWithStreamingResponse:
    def __init__(self, prov_info: AsyncProvInfoResource) -> None:
        self._prov_info = prov_info

        self.retrieve = async_to_streamed_response_wrapper(
            prov_info.retrieve,
        )
        self.list_all = async_to_streamed_response_wrapper(
            prov_info.list_all,
        )
