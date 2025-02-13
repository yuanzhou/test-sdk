# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types.datasets import ProvInfoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProvInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: HubmapEntity) -> None:
        prov_info = client.datasets.prov_info.retrieve(
            id="id",
        )
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HubmapEntity) -> None:
        prov_info = client.datasets.prov_info.retrieve(
            id="id",
            format="json",
        )
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: HubmapEntity) -> None:
        response = client.datasets.prov_info.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prov_info = response.parse()
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: HubmapEntity) -> None:
        with client.datasets.prov_info.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prov_info = response.parse()
            assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.prov_info.with_raw_response.retrieve(
                id="",
            )


class TestAsyncProvInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubmapEntity) -> None:
        prov_info = await async_client.datasets.prov_info.retrieve(
            id="id",
        )
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHubmapEntity) -> None:
        prov_info = await async_client.datasets.prov_info.retrieve(
            id="id",
            format="json",
        )
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.datasets.prov_info.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prov_info = await response.parse()
        assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.datasets.prov_info.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prov_info = await response.parse()
            assert_matches_type(ProvInfoRetrieveResponse, prov_info, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.prov_info.with_raw_response.retrieve(
                id="",
            )
