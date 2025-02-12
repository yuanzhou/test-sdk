# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types import RetrieveParentRetrieveParentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieveParents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_parents(self, client: HubmapEntity) -> None:
        retrieve_parent = client.retrieve_parents.retrieve_parents(
            "id",
        )
        assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_parents(self, client: HubmapEntity) -> None:
        response = client.retrieve_parents.with_raw_response.retrieve_parents(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve_parent = response.parse()
        assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_parents(self, client: HubmapEntity) -> None:
        with client.retrieve_parents.with_streaming_response.retrieve_parents(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve_parent = response.parse()
            assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_parents(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.retrieve_parents.with_raw_response.retrieve_parents(
                "",
            )


class TestAsyncRetrieveParents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_parents(self, async_client: AsyncHubmapEntity) -> None:
        retrieve_parent = await async_client.retrieve_parents.retrieve_parents(
            "id",
        )
        assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_parents(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.retrieve_parents.with_raw_response.retrieve_parents(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieve_parent = await response.parse()
        assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_parents(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.retrieve_parents.with_streaming_response.retrieve_parents(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieve_parent = await response.parse()
            assert_matches_type(RetrieveParentRetrieveParentsResponse, retrieve_parent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_parents(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.retrieve_parents.with_raw_response.retrieve_parents(
                "",
            )
