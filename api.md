# Shared Types

```python
from hubmap_entity.types import Dataset, Donor, Sample, Upload
```

# Entities

Types:

```python
from hubmap_entity.types import (
    Instanceof,
    EntityCreateResponse,
    EntityRetrieveResponse,
    EntityUpdateResponse,
    EntityCreateMultipleSamplesResponse,
    EntityListAncestorOrgansResponse,
    EntityListCollectionsResponse,
    EntityListSiblingsResponse,
    EntityListTupletsResponse,
    EntityListUploadsResponse,
    EntityRetrieveGlobusURLResponse,
)
```

Methods:

- <code title="post /entities/new/{entity_type}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">create</a>(entity_type, \*\*<a href="src/hubmap_entity/types/entity_create_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_create_response.py">EntityCreateResponse</a></code>
- <code title="get /entities/{id}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">retrieve</a>(id) -> <a href="./src/hubmap_entity/types/entity_retrieve_response.py">EntityRetrieveResponse</a></code>
- <code title="put /entities/{id}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">update</a>(id, \*\*<a href="src/hubmap_entity/types/entity_update_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_update_response.py">EntityUpdateResponse</a></code>
- <code title="post /entities/multiple-samples/{count}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">create_multiple_samples</a>(count) -> <a href="./src/hubmap_entity/types/entity_create_multiple_samples_response.py">EntityCreateMultipleSamplesResponse</a></code>
- <code title="get /entities/{id}/instanceof/{type}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">is_instance_of</a>(type, \*, id) -> <a href="./src/hubmap_entity/types/instanceof.py">Instanceof</a></code>
- <code title="get /entities/type/{type_a}/instanceof/{type_b}">client.entities.<a href="./src/hubmap_entity/resources/entities.py">is_type_instance_of</a>(type_b, \*, type_a) -> <a href="./src/hubmap_entity/types/instanceof.py">Instanceof</a></code>
- <code title="get /entities/{id}/ancestor-organs">client.entities.<a href="./src/hubmap_entity/resources/entities.py">list_ancestor_organs</a>(id) -> <a href="./src/hubmap_entity/types/entity_list_ancestor_organs_response.py">EntityListAncestorOrgansResponse</a></code>
- <code title="get /entities/{id}/collections">client.entities.<a href="./src/hubmap_entity/resources/entities.py">list_collections</a>(id, \*\*<a href="src/hubmap_entity/types/entity_list_collections_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_list_collections_response.py">EntityListCollectionsResponse</a></code>
- <code title="get /entities/{id}/siblings">client.entities.<a href="./src/hubmap_entity/resources/entities.py">list_siblings</a>(id, \*\*<a href="src/hubmap_entity/types/entity_list_siblings_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_list_siblings_response.py">EntityListSiblingsResponse</a></code>
- <code title="get /entities/{id}/tuplets">client.entities.<a href="./src/hubmap_entity/resources/entities.py">list_tuplets</a>(id, \*\*<a href="src/hubmap_entity/types/entity_list_tuplets_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_list_tuplets_response.py">EntityListTupletsResponse</a></code>
- <code title="get /entities/{id}/uploads">client.entities.<a href="./src/hubmap_entity/resources/entities.py">list_uploads</a>(id, \*\*<a href="src/hubmap_entity/types/entity_list_uploads_params.py">params</a>) -> <a href="./src/hubmap_entity/types/entity_list_uploads_response.py">EntityListUploadsResponse</a></code>
- <code title="get /entities/{id}/globus-url">client.entities.<a href="./src/hubmap_entity/resources/entities.py">retrieve_globus_url</a>(id) -> str</code>
- <code title="get /entities/{id}/provenance">client.entities.<a href="./src/hubmap_entity/resources/entities.py">retrieve_provenance</a>(id) -> None</code>

# ListEntityTypes

Types:

```python
from hubmap_entity.types import ListEntityTypeListEntityTypesResponse
```

Methods:

- <code title="get /entity-types">client.list_entity_types.<a href="./src/hubmap_entity/resources/list_entity_types.py">list_entity_types</a>() -> <a href="./src/hubmap_entity/types/list_entity_type_list_entity_types_response.py">ListEntityTypeListEntityTypesResponse</a></code>

# RetrieveAncestors

Types:

```python
from hubmap_entity.types import RetrieveAncestorRetrieveAncestorsResponse
```

Methods:

- <code title="get /ancestors/{id}">client.retrieve_ancestors.<a href="./src/hubmap_entity/resources/retrieve_ancestors.py">retrieve_ancestors</a>(id) -> <a href="./src/hubmap_entity/types/retrieve_ancestor_retrieve_ancestors_response.py">RetrieveAncestorRetrieveAncestorsResponse</a></code>

# RetrieveDescendants

Types:

```python
from hubmap_entity.types import RetrieveDescendantRetrieveDescendantsResponse
```

Methods:

- <code title="get /descendants/{id}">client.retrieve_descendants.<a href="./src/hubmap_entity/resources/retrieve_descendants.py">retrieve_descendants</a>(id) -> <a href="./src/hubmap_entity/types/retrieve_descendant_retrieve_descendants_response.py">RetrieveDescendantRetrieveDescendantsResponse</a></code>

# RetrieveParents

Types:

```python
from hubmap_entity.types import RetrieveParentRetrieveParentsResponse
```

Methods:

- <code title="get /parents/{id}">client.retrieve_parents.<a href="./src/hubmap_entity/resources/retrieve_parents.py">retrieve_parents</a>(id) -> <a href="./src/hubmap_entity/types/retrieve_parent_retrieve_parents_response.py">RetrieveParentRetrieveParentsResponse</a></code>

# RetrieveChildren

Types:

```python
from hubmap_entity.types import RetrieveChildRetrieveChildrenResponse
```

Methods:

- <code title="get /children/{id}">client.retrieve_children.<a href="./src/hubmap_entity/resources/retrieve_children.py">retrieve_children</a>(id) -> <a href="./src/hubmap_entity/types/retrieve_child_retrieve_children_response.py">RetrieveChildRetrieveChildrenResponse</a></code>

# RedirectDoi

Methods:

- <code title="get /doi/redirect/{id}">client.redirect_doi.<a href="./src/hubmap_entity/resources/redirect_doi.py">redirect_doi</a>(id) -> None</code>

# UpdateUploadsBulk

Types:

```python
from hubmap_entity.types import UpdateUploadsBulkUpdateUploadsBulkResponse
```

Methods:

- <code title="put /uploads">client.update_uploads_bulk.<a href="./src/hubmap_entity/resources/update_uploads_bulk.py">update_uploads_bulk</a>(\*\*<a href="src/hubmap_entity/types/update_uploads_bulk_update_uploads_bulk_params.py">params</a>) -> <a href="./src/hubmap_entity/types/update_uploads_bulk_update_uploads_bulk_response.py">UpdateUploadsBulkUpdateUploadsBulkResponse</a></code>

# RetrieveSamplesProvenanceInfo

Types:

```python
from hubmap_entity.types import RetrieveSamplesProvenanceInfoRetrieveSamplesProvenanceInfoResponse
```

Methods:

- <code title="get /samples/prov-info">client.retrieve_samples_provenance_info.<a href="./src/hubmap_entity/resources/retrieve_samples_provenance_info.py">retrieve_samples_provenance_info</a>(\*\*<a href="src/hubmap_entity/types/retrieve_samples_provenance_info_retrieve_samples_provenance_info_params.py">params</a>) -> <a href="./src/hubmap_entity/types/retrieve_samples_provenance_info_retrieve_samples_provenance_info_response.py">RetrieveSamplesProvenanceInfoRetrieveSamplesProvenanceInfoResponse</a></code>

# Datasets

Types:

```python
from hubmap_entity.types import (
    DatasetBulkUpdateResponse,
    DatasetCreateComponentsResponse,
    DatasetListDonorsResponse,
    DatasetListOrgansResponse,
    DatasetListSamplesResponse,
    DatasetListUnpublishedResponse,
    DatasetRetrieveMultiRevisionsResponse,
    DatasetRetrievePairedDatasetResponse,
    DatasetRetrieveProvMetadataResponse,
    DatasetRetrieveRevisionsResponse,
    DatasetRetrieveSankeyDataResponse,
)
```

Methods:

- <code title="put /datasets">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">bulk_update</a>(\*\*<a href="src/hubmap_entity/types/dataset_bulk_update_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_bulk_update_response.py">DatasetBulkUpdateResponse</a></code>
- <code title="post /datasets/components">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">create_components</a>(\*\*<a href="src/hubmap_entity/types/dataset_create_components_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_create_components_response.py">DatasetCreateComponentsResponse</a></code>
- <code title="get /datasets/{id}/donors">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">list_donors</a>(id) -> <a href="./src/hubmap_entity/types/dataset_list_donors_response.py">DatasetListDonorsResponse</a></code>
- <code title="get /datasets/{id}/organs">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">list_organs</a>(id) -> <a href="./src/hubmap_entity/types/dataset_list_organs_response.py">DatasetListOrgansResponse</a></code>
- <code title="get /datasets/{id}/samples">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">list_samples</a>(id) -> <a href="./src/hubmap_entity/types/dataset_list_samples_response.py">DatasetListSamplesResponse</a></code>
- <code title="get /datasets/unpublished">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">list_unpublished</a>(\*\*<a href="src/hubmap_entity/types/dataset_list_unpublished_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_list_unpublished_response.py">DatasetListUnpublishedResponse</a></code>
- <code title="put /datasets/{id}/retract">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retract</a>(id, \*\*<a href="src/hubmap_entity/types/dataset_retract_params.py">params</a>) -> None</code>
- <code title="get /datasets/{id}/latest-revision">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_latest_revision</a>(id) -> <a href="./src/hubmap_entity/types/shared/dataset.py">Dataset</a></code>
- <code title="get /datasets/{id}/multi-revisions">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_multi_revisions</a>(id, \*\*<a href="src/hubmap_entity/types/dataset_retrieve_multi_revisions_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_retrieve_multi_revisions_response.py">DatasetRetrieveMultiRevisionsResponse</a></code>
- <code title="get /datasets/{id}/paired-dataset">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_paired_dataset</a>(id, \*\*<a href="src/hubmap_entity/types/dataset_retrieve_paired_dataset_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_retrieve_paired_dataset_response.py">DatasetRetrievePairedDatasetResponse</a></code>
- <code title="get /datasets/{id}/prov-metadata">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_prov_metadata</a>(id) -> <a href="./src/hubmap_entity/types/dataset_retrieve_prov_metadata_response.py">DatasetRetrieveProvMetadataResponse</a></code>
- <code title="get /datasets/{id}/revision">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_revision</a>(id) -> None</code>
- <code title="get /datasets/{id}/revisions">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_revisions</a>(id, \*\*<a href="src/hubmap_entity/types/dataset_retrieve_revisions_params.py">params</a>) -> <a href="./src/hubmap_entity/types/dataset_retrieve_revisions_response.py">DatasetRetrieveRevisionsResponse</a></code>
- <code title="get /datasets/sankey_data">client.datasets.<a href="./src/hubmap_entity/resources/datasets/datasets.py">retrieve_sankey_data</a>() -> <a href="./src/hubmap_entity/types/dataset_retrieve_sankey_data_response.py">DatasetRetrieveSankeyDataResponse</a></code>

## ProvInfo

Types:

```python
from hubmap_entity.types.datasets import ProvInfoRetrieveResponse, ProvInfoListAllResponse
```

Methods:

- <code title="get /datasets/{id}/prov-info">client.datasets.prov_info.<a href="./src/hubmap_entity/resources/datasets/prov_info.py">retrieve</a>(id, \*\*<a href="src/hubmap_entity/types/datasets/prov_info_retrieve_params.py">params</a>) -> <a href="./src/hubmap_entity/types/datasets/prov_info_retrieve_response.py">ProvInfoRetrieveResponse</a></code>
- <code title="get /datasets/prov-info">client.datasets.prov_info.<a href="./src/hubmap_entity/resources/datasets/prov_info.py">list_all</a>(\*\*<a href="src/hubmap_entity/types/datasets/prov_info_list_all_params.py">params</a>) -> <a href="./src/hubmap_entity/types/datasets/prov_info_list_all_response.py">ProvInfoListAllResponse</a></code>
