# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubmap_entity import HubmapEntity, AsyncHubmapEntity

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedirectDoi:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_method_redirect_doi(self, client: HubmapEntity) -> None:
        redirect_doi = client.redirect_doi.redirect_doi(
            "id",
        )
        assert redirect_doi is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_raw_response_redirect_doi(self, client: HubmapEntity) -> None:
        response = client.redirect_doi.with_raw_response.redirect_doi(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redirect_doi = response.parse()
        assert redirect_doi is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_streaming_response_redirect_doi(self, client: HubmapEntity) -> None:
        with client.redirect_doi.with_streaming_response.redirect_doi(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redirect_doi = response.parse()
            assert redirect_doi is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    def test_path_params_redirect_doi(self, client: HubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.redirect_doi.with_raw_response.redirect_doi(
                "",
            )


class TestAsyncRedirectDoi:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_method_redirect_doi(self, async_client: AsyncHubmapEntity) -> None:
        redirect_doi = await async_client.redirect_doi.redirect_doi(
            "id",
        )
        assert redirect_doi is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_raw_response_redirect_doi(self, async_client: AsyncHubmapEntity) -> None:
        response = await async_client.redirect_doi.with_raw_response.redirect_doi(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        redirect_doi = await response.parse()
        assert redirect_doi is None

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_streaming_response_redirect_doi(self, async_client: AsyncHubmapEntity) -> None:
        async with async_client.redirect_doi.with_streaming_response.redirect_doi(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            redirect_doi = await response.parse()
            assert redirect_doi is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't properly handle redirects")
    @parametrize
    async def test_path_params_redirect_doi(self, async_client: AsyncHubmapEntity) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.redirect_doi.with_raw_response.redirect_doi(
                "",
            )
