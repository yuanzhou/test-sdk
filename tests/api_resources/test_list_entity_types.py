# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types import ListEntityTypeListEntityTypesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestListEntityTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_entity_types(self, client: HubmapEntity) -> None:
        list_entity_type = client.list_entity_types.list_entity_types()
        assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_entity_types(self, client: HubmapEntity) -> None:
        response = client.list_entity_types.with_raw_response.list_entity_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_entity_type = response.parse()
        assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_entity_types(self, client: HubmapEntity) -> None:
        with client.list_entity_types.with_streaming_response.list_entity_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_entity_type = response.parse()
            assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncListEntityTypes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_entity_types(self, async_client: AsyncHubmapEntity) -> None:
        list_entity_type = await async_client.list_entity_types.list_entity_types()
        assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_entity_types(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.list_entity_types.with_raw_response.list_entity_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_entity_type = await response.parse()
        assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_entity_types(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.list_entity_types.with_streaming_response.list_entity_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_entity_type = await response.parse()
            assert_matches_type(ListEntityTypeListEntityTypesResponse, list_entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True
