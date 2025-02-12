# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from hubmap_entity import HubmapEntity, AsyncHubmapEntity
from hubmap_entity.types import (
    UpdateUploadsBulkUpdateUploadsBulkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpdateUploadsBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_uploads_bulk(self, client: HubmapEntity) -> None:
        update_uploads_bulk = client.update_uploads_bulk.update_uploads_bulk(
            body=[{}],
        )
        assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_uploads_bulk(self, client: HubmapEntity) -> None:
        response = client.update_uploads_bulk.with_raw_response.update_uploads_bulk(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update_uploads_bulk = response.parse()
        assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_uploads_bulk(self, client: HubmapEntity) -> None:
        with client.update_uploads_bulk.with_streaming_response.update_uploads_bulk(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update_uploads_bulk = response.parse()
            assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUpdateUploadsBulk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_uploads_bulk(self, async_client: AsyncHubmapEntity) -> None:
        update_uploads_bulk = await async_client.update_uploads_bulk.update_uploads_bulk(
            body=[{}],
        )
        assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_uploads_bulk(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.update_uploads_bulk.with_raw_response.update_uploads_bulk(
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update_uploads_bulk = await response.parse()
        assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_uploads_bulk(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.update_uploads_bulk.with_streaming_response.update_uploads_bulk(
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update_uploads_bulk = await response.parse()
            assert_matches_type(UpdateUploadsBulkUpdateUploadsBulkResponse, update_uploads_bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
