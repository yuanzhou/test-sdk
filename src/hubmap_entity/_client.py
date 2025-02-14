# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    entities,
    redirect_doi,
    retrieve_parents,
    list_entity_types,
    retrieve_children,
    retrieve_ancestors,
    update_uploads_bulk,
    retrieve_descendants,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.datasets import datasets

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HubmapEntity",
    "AsyncHubmapEntity",
    "Client",
    "AsyncClient",
]


class HubmapEntity(SyncAPIClient):
    entities: entities.EntitiesResource
    list_entity_types: list_entity_types.ListEntityTypesResource
    retrieve_ancestors: retrieve_ancestors.RetrieveAncestorsResource
    retrieve_descendants: retrieve_descendants.RetrieveDescendantsResource
    retrieve_parents: retrieve_parents.RetrieveParentsResource
    retrieve_children: retrieve_children.RetrieveChildrenResource
    redirect_doi: redirect_doi.RedirectDoiResource
    update_uploads_bulk: update_uploads_bulk.UpdateUploadsBulkResource
    datasets: datasets.DatasetsResource
    with_raw_response: HubmapEntityWithRawResponse
    with_streaming_response: HubmapEntityWithStreamedResponse

    # client options
    bearer_token: str | None
    api_base_url: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        api_base_url: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous hubmap-entity client instance."""
        self.bearer_token = bearer_token

        self.api_base_url = api_base_url

        if base_url is None:
            base_url = os.environ.get("HUBMAP_ENTITY_BASE_URL")
        if base_url is None:
            base_url = f"https://entity.api.hubmapconsortium.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.entities = entities.EntitiesResource(self)
        self.list_entity_types = list_entity_types.ListEntityTypesResource(self)
        self.retrieve_ancestors = retrieve_ancestors.RetrieveAncestorsResource(self)
        self.retrieve_descendants = retrieve_descendants.RetrieveDescendantsResource(self)
        self.retrieve_parents = retrieve_parents.RetrieveParentsResource(self)
        self.retrieve_children = retrieve_children.RetrieveChildrenResource(self)
        self.redirect_doi = redirect_doi.RedirectDoiResource(self)
        self.update_uploads_bulk = update_uploads_bulk.UpdateUploadsBulkResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.with_raw_response = HubmapEntityWithRawResponse(self)
        self.with_streaming_response = HubmapEntityWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        api_base_url: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            api_base_url=api_base_url or self.api_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHubmapEntity(AsyncAPIClient):
    entities: entities.AsyncEntitiesResource
    list_entity_types: list_entity_types.AsyncListEntityTypesResource
    retrieve_ancestors: retrieve_ancestors.AsyncRetrieveAncestorsResource
    retrieve_descendants: retrieve_descendants.AsyncRetrieveDescendantsResource
    retrieve_parents: retrieve_parents.AsyncRetrieveParentsResource
    retrieve_children: retrieve_children.AsyncRetrieveChildrenResource
    redirect_doi: redirect_doi.AsyncRedirectDoiResource
    update_uploads_bulk: update_uploads_bulk.AsyncUpdateUploadsBulkResource
    datasets: datasets.AsyncDatasetsResource
    with_raw_response: AsyncHubmapEntityWithRawResponse
    with_streaming_response: AsyncHubmapEntityWithStreamedResponse

    # client options
    bearer_token: str | None
    api_base_url: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        api_base_url: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async hubmap-entity client instance."""
        self.bearer_token = bearer_token

        self.api_base_url = api_base_url

        if base_url is None:
            base_url = os.environ.get("HUBMAP_ENTITY_BASE_URL")
        if base_url is None:
            base_url = f"https://entity.api.hubmapconsortium.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.entities = entities.AsyncEntitiesResource(self)
        self.list_entity_types = list_entity_types.AsyncListEntityTypesResource(self)
        self.retrieve_ancestors = retrieve_ancestors.AsyncRetrieveAncestorsResource(self)
        self.retrieve_descendants = retrieve_descendants.AsyncRetrieveDescendantsResource(self)
        self.retrieve_parents = retrieve_parents.AsyncRetrieveParentsResource(self)
        self.retrieve_children = retrieve_children.AsyncRetrieveChildrenResource(self)
        self.redirect_doi = redirect_doi.AsyncRedirectDoiResource(self)
        self.update_uploads_bulk = update_uploads_bulk.AsyncUpdateUploadsBulkResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.with_raw_response = AsyncHubmapEntityWithRawResponse(self)
        self.with_streaming_response = AsyncHubmapEntityWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        if bearer_token is None:
            return {}
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.bearer_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the bearer_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        api_base_url: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            api_base_url=api_base_url or self.api_base_url,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HubmapEntityWithRawResponse:
    def __init__(self, client: HubmapEntity) -> None:
        self.entities = entities.EntitiesResourceWithRawResponse(client.entities)
        self.list_entity_types = list_entity_types.ListEntityTypesResourceWithRawResponse(client.list_entity_types)
        self.retrieve_ancestors = retrieve_ancestors.RetrieveAncestorsResourceWithRawResponse(client.retrieve_ancestors)
        self.retrieve_descendants = retrieve_descendants.RetrieveDescendantsResourceWithRawResponse(
            client.retrieve_descendants
        )
        self.retrieve_parents = retrieve_parents.RetrieveParentsResourceWithRawResponse(client.retrieve_parents)
        self.retrieve_children = retrieve_children.RetrieveChildrenResourceWithRawResponse(client.retrieve_children)
        self.redirect_doi = redirect_doi.RedirectDoiResourceWithRawResponse(client.redirect_doi)
        self.update_uploads_bulk = update_uploads_bulk.UpdateUploadsBulkResourceWithRawResponse(
            client.update_uploads_bulk
        )
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)


class AsyncHubmapEntityWithRawResponse:
    def __init__(self, client: AsyncHubmapEntity) -> None:
        self.entities = entities.AsyncEntitiesResourceWithRawResponse(client.entities)
        self.list_entity_types = list_entity_types.AsyncListEntityTypesResourceWithRawResponse(client.list_entity_types)
        self.retrieve_ancestors = retrieve_ancestors.AsyncRetrieveAncestorsResourceWithRawResponse(
            client.retrieve_ancestors
        )
        self.retrieve_descendants = retrieve_descendants.AsyncRetrieveDescendantsResourceWithRawResponse(
            client.retrieve_descendants
        )
        self.retrieve_parents = retrieve_parents.AsyncRetrieveParentsResourceWithRawResponse(client.retrieve_parents)
        self.retrieve_children = retrieve_children.AsyncRetrieveChildrenResourceWithRawResponse(
            client.retrieve_children
        )
        self.redirect_doi = redirect_doi.AsyncRedirectDoiResourceWithRawResponse(client.redirect_doi)
        self.update_uploads_bulk = update_uploads_bulk.AsyncUpdateUploadsBulkResourceWithRawResponse(
            client.update_uploads_bulk
        )
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)


class HubmapEntityWithStreamedResponse:
    def __init__(self, client: HubmapEntity) -> None:
        self.entities = entities.EntitiesResourceWithStreamingResponse(client.entities)
        self.list_entity_types = list_entity_types.ListEntityTypesResourceWithStreamingResponse(
            client.list_entity_types
        )
        self.retrieve_ancestors = retrieve_ancestors.RetrieveAncestorsResourceWithStreamingResponse(
            client.retrieve_ancestors
        )
        self.retrieve_descendants = retrieve_descendants.RetrieveDescendantsResourceWithStreamingResponse(
            client.retrieve_descendants
        )
        self.retrieve_parents = retrieve_parents.RetrieveParentsResourceWithStreamingResponse(client.retrieve_parents)
        self.retrieve_children = retrieve_children.RetrieveChildrenResourceWithStreamingResponse(
            client.retrieve_children
        )
        self.redirect_doi = redirect_doi.RedirectDoiResourceWithStreamingResponse(client.redirect_doi)
        self.update_uploads_bulk = update_uploads_bulk.UpdateUploadsBulkResourceWithStreamingResponse(
            client.update_uploads_bulk
        )
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)


class AsyncHubmapEntityWithStreamedResponse:
    def __init__(self, client: AsyncHubmapEntity) -> None:
        self.entities = entities.AsyncEntitiesResourceWithStreamingResponse(client.entities)
        self.list_entity_types = list_entity_types.AsyncListEntityTypesResourceWithStreamingResponse(
            client.list_entity_types
        )
        self.retrieve_ancestors = retrieve_ancestors.AsyncRetrieveAncestorsResourceWithStreamingResponse(
            client.retrieve_ancestors
        )
        self.retrieve_descendants = retrieve_descendants.AsyncRetrieveDescendantsResourceWithStreamingResponse(
            client.retrieve_descendants
        )
        self.retrieve_parents = retrieve_parents.AsyncRetrieveParentsResourceWithStreamingResponse(
            client.retrieve_parents
        )
        self.retrieve_children = retrieve_children.AsyncRetrieveChildrenResourceWithStreamingResponse(
            client.retrieve_children
        )
        self.redirect_doi = redirect_doi.AsyncRedirectDoiResourceWithStreamingResponse(client.redirect_doi)
        self.update_uploads_bulk = update_uploads_bulk.AsyncUpdateUploadsBulkResourceWithStreamingResponse(
            client.update_uploads_bulk
        )
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)


Client = HubmapEntity

AsyncClient = AsyncHubmapEntity
