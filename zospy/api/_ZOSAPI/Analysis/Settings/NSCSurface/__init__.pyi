"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import (
    BestFitSphereOptions,
    SampleSizes_Pow2Plus1_X,
    SurfaceSagData,
)
from zospy.api._ZOSAPI.Analysis.Settings import IAS_, IAS_Surface

__all__ = ("IAS_NSCSurfaceSag", "NSCSagRemoveOptions", "NSCSagShowAs")

class IAS_NSCSurfaceSag(IAS_):
    @property
    def BestFitSphereOption(self) -> BestFitSphereOptions: ...
    @property
    def BFSReverseDirection(self) -> bool: ...
    @property
    def ContourFormat(self) -> str: ...
    @property
    def Data(self) -> SurfaceSagData: ...
    @property
    def Decenter_X(self) -> float: ...
    @property
    def Decenter_Y(self) -> float: ...
    @property
    def FaceNumber(self) -> int: ...
    @property
    def KeepObjectTilts(self) -> bool: ...
    @property
    def KeepZRD(self) -> bool: ...
    @property
    def ObjectNumber(self) -> int: ...
    @property
    def Offset(self) -> float: ...
    @property
    def ProbeRayOffset(self) -> float: ...
    @property
    def RemoveOption(self) -> NSCSagRemoveOptions: ...
    @property
    def Rotation(self) -> float: ...
    @property
    def Sampling(self) -> SampleSizes_Pow2Plus1_X: ...
    @property
    def ShowAs(self) -> NSCSagShowAs: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Width(self) -> float: ...
    @property
    def ZRDFilename(self) -> str: ...
    @BestFitSphereOption.setter
    def BestFitSphereOption(self, value: BestFitSphereOptions) -> None: ...
    @BFSReverseDirection.setter
    def BFSReverseDirection(self, value: bool) -> None: ...
    @ContourFormat.setter
    def ContourFormat(self, value: str) -> None: ...
    @Data.setter
    def Data(self, value: SurfaceSagData) -> None: ...
    @Decenter_X.setter
    def Decenter_X(self, value: float) -> None: ...
    @Decenter_Y.setter
    def Decenter_Y(self, value: float) -> None: ...
    @FaceNumber.setter
    def FaceNumber(self, value: int) -> None: ...
    @KeepObjectTilts.setter
    def KeepObjectTilts(self, value: bool) -> None: ...
    @KeepZRD.setter
    def KeepZRD(self, value: bool) -> None: ...
    @ObjectNumber.setter
    def ObjectNumber(self, value: int) -> None: ...
    @Offset.setter
    def Offset(self, value: float) -> None: ...
    @ProbeRayOffset.setter
    def ProbeRayOffset(self, value: float) -> None: ...
    @RemoveOption.setter
    def RemoveOption(self, value: NSCSagRemoveOptions) -> None: ...
    @Rotation.setter
    def Rotation(self, value: float) -> None: ...
    @Sampling.setter
    def Sampling(self, value: SampleSizes_Pow2Plus1_X) -> None: ...
    @ShowAs.setter
    def ShowAs(self, value: NSCSagShowAs) -> None: ...
    @Width.setter
    def Width(self, value: float) -> None: ...
    @ZRDFilename.setter
    def ZRDFilename(self, value: str) -> None: ...

class NSCSagRemoveOptions:
    # None = 0
    BaseROC = 1
    BestFitSphere = 2
    AverageSag = 3
    MinimumSag = 4

class NSCSagShowAs:
    Surface = 0
    Contour = 1
    GreyScale = 2
    InverseGreyScale = 3
    FalseColor = 4
    InverseFalseColor = 5
    X_CrossSection = 6
    Y_CrossSection = 7