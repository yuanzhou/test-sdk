# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["DatasetRetrieveRevisionsResponse"]


class DatasetRetrieveRevisionsResponse(BaseModel):
    dataset: Optional["Dataset"] = None

    revision_number: Optional[int] = None
    """The number in the revision chain of this dataset where 1 is the oldest revision"""

    uuid: Optional[str] = None
    """The uuid of a dataset"""


from .shared.dataset import Dataset

if PYDANTIC_V2:
    DatasetRetrieveRevisionsResponse.model_rebuild()
else:
    DatasetRetrieveRevisionsResponse.update_forward_refs()  # type: ignore
