# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .shared.donor import Donor
from .shared.sample import Sample

__all__ = ["EntityUpdateResponse"]

EntityUpdateResponse: TypeAlias = Union[Donor, Sample, "Dataset"]

from .shared.dataset import Dataset
