"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import HuygensShowAsTypes, SampleSizes
from zospy.api._ZOSAPI.Analysis.Settings import (
    IAS_,
    HuygensPsfTypes,
    IAS_Field,
    IAS_Surface,
    IAS_Wavelength,
    PsfSpread,
    PsfTypes,
    Rotations,
)

__all__ = (
    "FftPsfType",
    "IAS_FftPsf",
    "IAS_FftPsfCrossSection",
    "IAS_FftPsfLineEdgeSpread",
    "IAS_HuygensPsf",
    "IAS_HuygensPsfCrossSection",
    "PsfRotation",
    "PsfSampling",
)

class FftPsfType:
    Linear = 0
    Log = 1
    Phase = 2
    Real = 3
    Imaginary = 4

class IAS_FftPsf(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def ImageDelta(self) -> float: ...
    @property
    def Normalize(self) -> bool: ...
    @property
    def OutputSize(self) -> PsfSampling: ...
    @property
    def Rotation(self) -> PsfRotation: ...
    @property
    def SampleSize(self) -> PsfSampling: ...
    @property
    def Surface(self) -> IAS_Surface: ...
    @property
    def Type(self) -> FftPsfType: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @ImageDelta.setter
    def ImageDelta(self, value: float) -> None: ...
    @Normalize.setter
    def Normalize(self, value: bool) -> None: ...
    @OutputSize.setter
    def OutputSize(self, value: PsfSampling) -> None: ...
    @Rotation.setter
    def Rotation(self, value: PsfRotation) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: PsfSampling) -> None: ...
    @Type.setter
    def Type(self, value: FftPsfType) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...

class IAS_FftPsfCrossSection(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def Normalize(self) -> bool: ...
    @property
    def PlotScale(self) -> float: ...
    @property
    def RowCol(self) -> int: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def Type(self) -> PsfTypes: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Normalize.setter
    def Normalize(self, value: bool) -> None: ...
    @PlotScale.setter
    def PlotScale(self, value: float) -> None: ...
    @RowCol.setter
    def RowCol(self, value: int) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @Type.setter
    def Type(self, value: PsfTypes) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...

class IAS_FftPsfLineEdgeSpread(IAS_):
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def PlotScale(self) -> float: ...
    @property
    def SampleSize(self) -> SampleSizes: ...
    @property
    def Spread(self) -> PsfSpread: ...
    @property
    def Type(self) -> PsfTypes: ...
    @property
    def UseCoherentPSF(self) -> bool: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @PlotScale.setter
    def PlotScale(self, value: float) -> None: ...
    @SampleSize.setter
    def SampleSize(self, value: SampleSizes) -> None: ...
    @Spread.setter
    def Spread(self, value: PsfSpread) -> None: ...
    @Type.setter
    def Type(self, value: PsfTypes) -> None: ...
    @UseCoherentPSF.setter
    def UseCoherentPSF(self, value: bool) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...

class IAS_HuygensPsf(IAS_):
    @property
    def Configuration(self) -> int: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def ImageDelta(self) -> float: ...
    @property
    def ImageSampleSize(self) -> SampleSizes: ...
    @property
    def Normalize(self) -> bool: ...
    @property
    def PupilSampleSize(self) -> SampleSizes: ...
    @property
    def Rotation(self) -> Rotations: ...
    @property
    def ShowAsType(self) -> HuygensShowAsTypes: ...
    @property
    def Type(self) -> HuygensPsfTypes: ...
    @property
    def UseCentroid(self) -> bool: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @ImageDelta.setter
    def ImageDelta(self, value: float) -> None: ...
    @ImageSampleSize.setter
    def ImageSampleSize(self, value: SampleSizes) -> None: ...
    @Normalize.setter
    def Normalize(self, value: bool) -> None: ...
    @PupilSampleSize.setter
    def PupilSampleSize(self, value: SampleSizes) -> None: ...
    @Rotation.setter
    def Rotation(self, value: Rotations) -> None: ...
    @ShowAsType.setter
    def ShowAsType(self, value: HuygensShowAsTypes) -> None: ...
    @Type.setter
    def Type(self, value: HuygensPsfTypes) -> None: ...
    @UseCentroid.setter
    def UseCentroid(self, value: bool) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...

class IAS_HuygensPsfCrossSection(IAS_):
    @property
    def Configuration(self) -> int: ...
    @property
    def Field(self) -> IAS_Field: ...
    @property
    def ImageDelta(self) -> float: ...
    @property
    def ImageSampleSize(self) -> SampleSizes: ...
    @property
    def Normalize(self) -> bool: ...
    @property
    def PupilSampleSize(self) -> SampleSizes: ...
    @property
    def RowCol(self) -> int: ...
    @property
    def Type(self) -> PsfTypes: ...
    @property
    def UseCentroid(self) -> bool: ...
    @property
    def UsePolarization(self) -> bool: ...
    @property
    def Wavelength(self) -> IAS_Wavelength: ...
    @Configuration.setter
    def Configuration(self, value: int) -> None: ...
    @ImageDelta.setter
    def ImageDelta(self, value: float) -> None: ...
    @ImageSampleSize.setter
    def ImageSampleSize(self, value: SampleSizes) -> None: ...
    @Normalize.setter
    def Normalize(self, value: bool) -> None: ...
    @PupilSampleSize.setter
    def PupilSampleSize(self, value: SampleSizes) -> None: ...
    @RowCol.setter
    def RowCol(self, value: int) -> None: ...
    @Type.setter
    def Type(self, value: PsfTypes) -> None: ...
    @UseCentroid.setter
    def UseCentroid(self, value: bool) -> None: ...
    @UsePolarization.setter
    def UsePolarization(self, value: bool) -> None: ...

class PsfRotation:
    CW0 = 0
    CW90 = 1
    CW180 = 2
    CW270 = 3

class PsfSampling:
    PsfS_32x32 = 1
    PsfS_64x64 = 2
    PsfS_128x128 = 3
    PsfS_256x256 = 4
    PsfS_512x512 = 5
    PsfS_1024x1024 = 6
    PsfS_2048x2048 = 7
    PsfS_4096x4096 = 8
    PsfS_8192x8192 = 9
    PsfS_16384x16384 = 10