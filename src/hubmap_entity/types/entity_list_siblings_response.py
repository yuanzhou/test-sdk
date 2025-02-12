# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .shared.sample import Sample

__all__ = ["EntityListSiblingsResponse", "EntityListSiblingsResponseItem"]

EntityListSiblingsResponseItem: TypeAlias = Union[Sample, "Dataset"]

EntityListSiblingsResponse: TypeAlias = List[EntityListSiblingsResponseItem]

from .shared.dataset import Dataset
