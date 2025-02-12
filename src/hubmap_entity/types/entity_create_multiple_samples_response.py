# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntityCreateMultipleSamplesResponse", "EntityCreateMultipleSamplesResponseItem"]


class EntityCreateMultipleSamplesResponseItem(BaseModel):
    hubmap_id: Optional[str] = None

    submission_id: Optional[str] = None

    uuid: Optional[str] = None


EntityCreateMultipleSamplesResponse: TypeAlias = List[EntityCreateMultipleSamplesResponseItem]
