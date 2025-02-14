# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types import GetAncestorsByIDGetAncestorsByIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGetAncestorsByID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_ancestors_by_id(self, client: HubmapEntity) -> None:
        get_ancestors_by_id = client.get_ancestors_by_id.get_ancestors_by_id(
            "id",
        )
        assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_ancestors_by_id(self, client: HubmapEntity) -> None:
        response = client.get_ancestors_by_id.with_raw_response.get_ancestors_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_ancestors_by_id = response.parse()
        assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_ancestors_by_id(self, client: HubmapEntity) -> None:
        with client.get_ancestors_by_id.with_streaming_response.get_ancestors_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_ancestors_by_id = response.parse()
            assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_ancestors_by_id(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.get_ancestors_by_id.with_raw_response.get_ancestors_by_id(
                "",
            )


class TestAsyncGetAncestorsByID:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_ancestors_by_id(self, async_client: AsyncHubmapEntity) -> None:
        get_ancestors_by_id = await async_client.get_ancestors_by_id.get_ancestors_by_id(
            "id",
        )
        assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_ancestors_by_id(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.get_ancestors_by_id.with_raw_response.get_ancestors_by_id(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        get_ancestors_by_id = await response.parse()
        assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_ancestors_by_id(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.get_ancestors_by_id.with_streaming_response.get_ancestors_by_id(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            get_ancestors_by_id = await response.parse()
            assert_matches_type(GetAncestorsByIDGetAncestorsByIDResponse, get_ancestors_by_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_ancestors_by_id(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.get_ancestors_by_id.with_raw_response.get_ancestors_by_id(
                "",
            )
