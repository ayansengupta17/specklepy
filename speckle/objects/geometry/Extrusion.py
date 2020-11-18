# generated by datamodel-codegen:
#   filename:  Extrusion.json
#   timestamp: 2020-11-18T11:56:14+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Base(BaseModel):
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Point(BaseModel):
    value: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Extrusion(BaseModel):
    length: Optional[Optional[float]] = None
    capped: Optional[Optional[bool]] = None
    profile: Optional[Base] = None
    pathStart: Optional[Point] = None
    pathEnd: Optional[Point] = None
    pathCurve: Optional[Base] = None
    pathTangent: Optional[Base] = None
    profiles: Optional[List[Base]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None