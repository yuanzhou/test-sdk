# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .shared.donor import Donor
from .shared.sample import Sample

__all__ = ["EntityCreateResponse", "EntityCreateResponseItem"]

EntityCreateResponseItem: TypeAlias = Union[Donor, Sample, "Dataset", "Upload"]

EntityCreateResponse: TypeAlias = List[EntityCreateResponseItem]

from .shared.upload import Upload
from .shared.dataset import Dataset
