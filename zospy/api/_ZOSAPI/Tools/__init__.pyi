"""
This file provides autocompletions for the ZOS-API and was automatically generated.
It should not be edited manually.
"""

from __future__ import annotations

from zospy.api._ZOSAPI.Analysis import IMessage
from zospy.api._ZOSAPI.Common import IVectorData
from zospy.api._ZOSAPI.SystemData import ZemaxSystemUnits
from zospy.api._ZOSAPI.Tools.General import (
    IComputeRMSSpotSize,
    ICreateArchive,
    IExportCAD,
    IHullTools,
    ILensCatalogs,
    IPointTools,
    IQuickAdjust,
    IQuickFocus,
    IRayAimingWizard,
    IRestoreArchive,
    IScale,
)
from zospy.api._ZOSAPI.Tools.Optimization import (
    IGlobalOptimization,
    IHammerOptimization,
    ILocalOptimization,
)
from zospy.api._ZOSAPI.Tools.RayTrace import (
    IBatchRayTrace,
    ILightningTrace,
    INSCRayTrace,
    IZRDReader,
)
from zospy.api._ZOSAPI.Tools.Tolerancing import (
    IQuickSensitivity,
    IToleranceDataViewer,
    ITolerancing,
)

from . import General, LMx, Optimization, RayTrace, Tolerancing

__all__ = (
    "General",
    "LMx",
    "Optimization",
    "RayTrace",
    "Tolerancing",
    "CriticalRayType",
    "HPCEnvironments",
    "HPCNodeSize",
    "HPCRunState",
    "IConvertToNSCGroup",
    "ICriticalRaysetGenerator",
    "IDesignLockdown",
    "IHPCSettings",
    "IHPCSettings",
    "IMaterialsCatalog",
    "IMFCalculator",
    "IOpticalSystemTools",
    "IOpticalSystemTools",
    "IShadedModelTriangleList",
    "IShadedModelTriangleList",
    "IShadedModelVisualizationExport",
    "ISystemTool",
    "ISystemTool",
    "MaterialFormulas",
    "MaterialStatuses",
    "RayPatternOption",
    "RunStatus",
    "VertexOrder",
)

class CriticalRayType:
    Chief = 0
    Marginal = 1
    Grid = 2
    Ring = 3
    Y_Fan = 4
    X_Fan = 5
    XY_Fan = 6
    List = 7

class HPCEnvironments:
    OnPremise = 0
    AWSKubernetes = 1
    AzureKubernetes = 2

class HPCNodeSize:
    Default = 0
    Tiny = 1
    Small = 2
    Medium = 3
    Large = 4
    XLarge = 5

class HPCRunState:
    NotRunning = 0
    Initializing = 1
    ClusterAllocating = 2
    UploadingData = 3
    Queued = 4
    RunStarting = 5
    WaitingForResults = 6
    Complete = 7

class IConvertToNSCGroup(ISystemTool):
    @property
    def ConvertFileToNSC(self) -> bool: ...
    @property
    def ConvertStopToNSCAperture(self) -> bool: ...
    @property
    def ConvertToGlobalCoordinates(self) -> bool: ...
    @property
    def CreateSourcesAndDetectors(self) -> bool: ...
    @property
    def FirstSurface(self) -> int: ...
    @property
    def IgnoreErrors(self) -> bool: ...
    @property
    def LastSurface(self) -> int: ...
    @property
    def OverfillFactor(self) -> float: ...
    @property
    def StopMechanicalHalfWidth(self) -> float: ...
    @property
    def StopObjectFace(self) -> int: ...
    @property
    def StopObjectNumber(self) -> int: ...
    @ConvertFileToNSC.setter
    def ConvertFileToNSC(self, value: bool) -> None: ...
    @ConvertStopToNSCAperture.setter
    def ConvertStopToNSCAperture(self, value: bool) -> None: ...
    @ConvertToGlobalCoordinates.setter
    def ConvertToGlobalCoordinates(self, value: bool) -> None: ...
    @CreateSourcesAndDetectors.setter
    def CreateSourcesAndDetectors(self, value: bool) -> None: ...
    @FirstSurface.setter
    def FirstSurface(self, value: int) -> None: ...
    @IgnoreErrors.setter
    def IgnoreErrors(self, value: bool) -> None: ...
    @LastSurface.setter
    def LastSurface(self, value: int) -> None: ...
    @OverfillFactor.setter
    def OverfillFactor(self, value: float) -> None: ...
    @StopMechanicalHalfWidth.setter
    def StopMechanicalHalfWidth(self, value: float) -> None: ...

class ICriticalRaysetGenerator(ISystemTool):
    @property
    def EffectiveInputDistance(self) -> float: ...
    @property
    def MinimumEfectiveInputDistance(self) -> float: ...
    @property
    def NumRays(self) -> int: ...
    @property
    def RayPattern(self) -> RayPatternOption: ...
    @property
    def RayScale(self) -> float: ...
    @property
    def UseAllFields(self) -> bool: ...
    @property
    def UseAllWavelengths(self) -> bool: ...
    @EffectiveInputDistance.setter
    def EffectiveInputDistance(self, value: float) -> None: ...
    @NumRays.setter
    def NumRays(self, value: int) -> None: ...
    @RayPattern.setter
    def RayPattern(self, value: RayPatternOption) -> None: ...
    @RayScale.setter
    def RayScale(self, value: float) -> None: ...
    @ReadRaysFromFilename.setter
    def ReadRaysFromFilename(self, value: str) -> None: ...
    @SaveCriticalRaysFilename.setter
    def SaveCriticalRaysFilename(self, value: str) -> None: ...
    @UseAllFields.setter
    def UseAllFields(self, value: bool) -> None: ...
    @UseAllWavelengths.setter
    def UseAllWavelengths(self, value: bool) -> None: ...

class IDesignLockdown(ISystemTool):
    @property
    def ConvertSDToMaxApertures(self) -> bool: ...
    @property
    def DecimalPrecision(self) -> int: ...
    @property
    def ExcludePickups(self) -> bool: ...
    @property
    def FixModelGlasses(self) -> bool: ...
    @property
    def UsePrecisionRounding(self) -> bool: ...
    @ConvertSDToMaxApertures.setter
    def ConvertSDToMaxApertures(self, value: bool) -> None: ...
    @DecimalPrecision.setter
    def DecimalPrecision(self, value: int) -> None: ...
    @ExcludePickups.setter
    def ExcludePickups(self, value: bool) -> None: ...
    @FixModelGlasses.setter
    def FixModelGlasses(self, value: bool) -> None: ...
    @UsePrecisionRounding.setter
    def UsePrecisionRounding(self, value: bool) -> None: ...

class IHPCSettings:
    @property
    def InstanceType(self) -> HPCNodeSize: ...
    @property
    def IsHPCConfigured(self) -> bool: ...
    @property
    def MaxNodeCount(self) -> int: ...
    @property
    def NodeCount(self) -> int: ...
    @property
    def ShutdownTimeTicks(self) -> int: ...
    @property
    def ThreadsPerTask(self) -> int: ...

class IMaterialsCatalog(ISystemTool):
    @property
    def AR(self) -> str: ...
    @property
    def CatalogComment(self) -> str: ...
    @property
    def Comment(self) -> str: ...
    @property
    def CR(self) -> str: ...
    @property
    def D0(self) -> float: ...
    @property
    def D1(self) -> float: ...
    @property
    def D2(self) -> float: ...
    @property
    def dPgF(self) -> float: ...
    @property
    def E0(self) -> float: ...
    @property
    def E1(self) -> float: ...
    @property
    def ExcludeSubstitution(self) -> bool: ...
    @property
    def FR(self) -> str: ...
    @property
    def IgnoreThermalExpansion(self) -> bool: ...
    @property
    def Ltk(self) -> float: ...
    @property
    def MaterialFormula(self) -> MaterialFormulas: ...
    @property
    def MaterialStatus(self) -> MaterialStatuses: ...
    @property
    def MaximumWavelength(self) -> float: ...
    @property
    def MeltFreq(self) -> str: ...
    @property
    def MetaMaterial(self) -> bool: ...
    @property
    def MinimumWavelength(self) -> float: ...
    @property
    def Nd(self) -> float: ...
    @property
    def NumberOfFitCoefficients(self) -> int: ...
    @property
    def p(self) -> float: ...
    @property
    def PR(self) -> str: ...
    @property
    def RelCost(self) -> str: ...
    @property
    def SelectedCatalog(self) -> str: ...
    @property
    def SelectedMaterial(self) -> str: ...
    @property
    def SR(self) -> str: ...
    @property
    def TCE(self) -> float: ...
    @property
    def Temp(self) -> float: ...
    @property
    def Vd(self) -> float: ...
    def GetAllCatalogs(self) -> list[str]: ...
    def GetAllMaterials(self) -> list[str]: ...
    def GetCoefficientName(self, coeff: int) -> str: ...
    def GetFitCoefficient(self, coeff: int) -> float: ...
    def SaveCatalog(self) -> bool: ...
    @AR.setter
    def AR(self, value: str) -> None: ...
    @CatalogComment.setter
    def CatalogComment(self, value: str) -> None: ...
    @Comment.setter
    def Comment(self, value: str) -> None: ...
    @CR.setter
    def CR(self, value: str) -> None: ...
    @D0.setter
    def D0(self, value: float) -> None: ...
    @D1.setter
    def D1(self, value: float) -> None: ...
    @D2.setter
    def D2(self, value: float) -> None: ...
    @dPgF.setter
    def dPgF(self, value: float) -> None: ...
    @E0.setter
    def E0(self, value: float) -> None: ...
    @E1.setter
    def E1(self, value: float) -> None: ...
    @ExcludeSubstitution.setter
    def ExcludeSubstitution(self, value: bool) -> None: ...
    @FR.setter
    def FR(self, value: str) -> None: ...
    @IgnoreThermalExpansion.setter
    def IgnoreThermalExpansion(self, value: bool) -> None: ...
    @Ltk.setter
    def Ltk(self, value: float) -> None: ...
    @MaterialFormula.setter
    def MaterialFormula(self, value: MaterialFormulas) -> None: ...
    @MaterialStatus.setter
    def MaterialStatus(self, value: MaterialStatuses) -> None: ...
    @MaximumWavelength.setter
    def MaximumWavelength(self, value: float) -> None: ...
    @MeltFreq.setter
    def MeltFreq(self, value: str) -> None: ...
    @MetaMaterial.setter
    def MetaMaterial(self, value: bool) -> None: ...
    @MinimumWavelength.setter
    def MinimumWavelength(self, value: float) -> None: ...
    @p.setter
    def p(self, value: float) -> None: ...
    @PR.setter
    def PR(self, value: str) -> None: ...
    @RelCost.setter
    def RelCost(self, value: str) -> None: ...
    @SelectedCatalog.setter
    def SelectedCatalog(self, value: str) -> None: ...
    @SelectedMaterial.setter
    def SelectedMaterial(self, value: str) -> None: ...
    @SR.setter
    def SR(self, value: str) -> None: ...
    @TCE.setter
    def TCE(self, value: float) -> None: ...
    @Temp.setter
    def Temp(self, value: float) -> None: ...
    def SetFitCoefficient(self, coeff: int, Value: float) -> None: ...

class IMFCalculator(ISystemTool):
    @property
    def MeritFunctionCalculation(self) -> float: ...

class IOpticalSystemTools:
    def CreateDoubleMatrix(self, Rows: int, Cols: int) -> list[list[float]]: ...
    def CreateDoubleVector(self, numElements: int) -> list[float]: ...
    @property
    def CurrentTool(self) -> ISystemTool: ...
    @property
    def IsRunning(self) -> bool: ...
    @property
    def LastError(self) -> IMessage: ...
    @property
    def Progress(self) -> int: ...
    @property
    def Status(self) -> str: ...
    def GetConversionFromSystemUnits(self, toUnits: ZemaxSystemUnits) -> float: ...
    def GetConversionToSystemUnits(self, fromUnits: ZemaxSystemUnits) -> float: ...
    def GetHPCSettingsCustom(self, nodeCount: int, instanceType: HPCNodeSize) -> IHPCSettings: ...
    def GetHPCSettingsFromPrefs(self) -> IHPCSettings: ...
    def GetHullTools(self) -> IHullTools: ...
    def GetPointTools(self) -> IPointTools: ...
    def OpenBatchRayTrace(self) -> IBatchRayTrace: ...
    def OpenConvertToNSCGroup(self) -> IConvertToNSCGroup: ...
    def OpenCreateZAR(self) -> ICreateArchive: ...
    def OpenCriticalRaysetGenerator(self) -> ICriticalRaysetGenerator: ...
    def OpenDesignLockdown(self) -> IDesignLockdown: ...
    def OpenExportCAD(self) -> IExportCAD: ...
    def OpenGlobalOptimization(self) -> IGlobalOptimization: ...
    def OpenGlobalOptimization_HPC(self, hpcSettings: IHPCSettings) -> IGlobalOptimization: ...
    def OpenHammerOptimization(self) -> IHammerOptimization: ...
    def OpenHammerOptimization_HPC(self, hpcSettings: IHPCSettings) -> IHammerOptimization: ...
    def OpenLensCatalogs(self) -> ILensCatalogs: ...
    def OpenLightningTrace(self) -> ILightningTrace: ...
    def OpenLocalOptimization(self) -> ILocalOptimization: ...
    def OpenMaterialsCatalog(self) -> IMaterialsCatalog: ...
    def OpenMeritFunctionCalculator(self) -> IMFCalculator: ...
    def OpenNSCRayTrace(self) -> INSCRayTrace: ...
    def OpenNSCRayTrace_HPC(self, hpcSettings: IHPCSettings) -> INSCRayTrace: ...
    def OpenQuickAdjust(self) -> IQuickAdjust: ...
    def OpenQuickFocus(self) -> IQuickFocus: ...
    def OpenQuickSensitivity(self) -> IQuickSensitivity: ...
    def OpenRayAimingWizard(self) -> IRayAimingWizard: ...
    def OpenRayDatabaseReader(self) -> IZRDReader: ...
    def OpenRestoreZAR(self) -> IRestoreArchive: ...
    def OpenRMSSpotRadiusCalculator(self) -> IComputeRMSSpotSize: ...
    def OpenScale(self) -> IScale: ...
    def OpenShadedModelVisualizationExport(self) -> IShadedModelVisualizationExport: ...
    def OpenToleranceDataViewer(self) -> IToleranceDataViewer: ...
    def OpenTolerancing(self) -> ITolerancing: ...
    def OpenTolerancing_HPC(self, hpcSettings: IHPCSettings) -> ITolerancing: ...
    def RemoveAllVariables(self) -> bool: ...
    def SetAllRadiiVariable(self) -> int: ...
    def SetAllThicknessesVariable(self) -> int: ...

class IShadedModelTriangleList:
    @property
    def NumberOfSurfaces(self) -> int: ...
    @property
    def NumberOfTriangles(self) -> int: ...
    @property
    def ObjectIndex(self) -> IVectorData: ...
    @property
    def SurfaceIndex(self) -> IVectorData: ...
    @property
    def TotalNumberOfObjects(self) -> int: ...
    @property
    def XCoords(self) -> IVectorData: ...
    @property
    def XNormals(self) -> IVectorData: ...
    @property
    def YCoords(self) -> IVectorData: ...
    @property
    def YNormals(self) -> IVectorData: ...
    @property
    def ZCoords(self) -> IVectorData: ...
    @property
    def ZNormals(self) -> IVectorData: ...
    def GetVertex(
        self, TriangleNumber: int, Vertex: VertexOrder
    ) -> tuple[bool, float, float, float, float, float, float, int, int]: ...
    def NumberOfObjects(self, Surface: int) -> list[int]: ...
    @ObjectIndex.setter
    def ObjectIndex(self, value: IVectorData) -> None: ...
    @SurfaceIndex.setter
    def SurfaceIndex(self, value: IVectorData) -> None: ...
    @XCoords.setter
    def XCoords(self, value: IVectorData) -> None: ...
    @XNormals.setter
    def XNormals(self, value: IVectorData) -> None: ...
    @YCoords.setter
    def YCoords(self, value: IVectorData) -> None: ...
    @YNormals.setter
    def YNormals(self, value: IVectorData) -> None: ...
    @ZCoords.setter
    def ZCoords(self, value: IVectorData) -> None: ...
    @ZNormals.setter
    def ZNormals(self, value: IVectorData) -> None: ...

class IShadedModelVisualizationExport(ISystemTool):
    @property
    def EndSurface(self) -> int: ...
    @property
    def Object(self) -> int: ...
    @property
    def StartSurface(self) -> int: ...
    def GetResults(self) -> IShadedModelTriangleList: ...
    @EndSurface.setter
    def EndSurface(self, value: int) -> None: ...
    @Object.setter
    def Object(self, value: int) -> None: ...
    @StartSurface.setter
    def StartSurface(self, value: int) -> None: ...

class ISystemTool:
    def Cancel(self) -> bool: ...
    def Close(self) -> bool: ...
    @property
    def CanCancel(self) -> bool: ...
    @property
    def ErrorMessage(self) -> str: ...
    @property
    def IsAsynchronous(self) -> bool: ...
    @property
    def IsFiniteDuration(self) -> bool: ...
    @property
    def IsRunning(self) -> bool: ...
    @property
    def IsValid(self) -> bool: ...
    @property
    def Progress(self) -> int: ...
    @property
    def Status(self) -> str: ...
    @property
    def Succeeded(self) -> bool: ...
    def Run(self) -> bool: ...
    def RunAndWaitForCompletion(self) -> bool: ...
    def RunAndWaitWithTimeout(self, timeOutSeconds: float) -> RunStatus: ...
    def WaitForCompletion(self) -> bool: ...
    def WaitWithTimeout(self, timeOutSeconds: float) -> RunStatus: ...

class MaterialFormulas:
    Schott = 1
    Sellmeier1 = 2
    Herzberger = 3
    Sellmeier2 = 4
    Conrady = 5
    Sellmeier3 = 6
    Handbook1 = 7
    Handbook2 = 8
    Sellmeier4 = 9
    Extended = 10
    Sellmeier5 = 11
    Extended2 = 12
    Extended3 = 13

class MaterialStatuses:
    Standard = 0
    Preferred = 1
    Obsolete = 2
    Special = 3
    Melt = 4

class RayPatternOption:
    XyFan = 0
    XFan = 1
    YFan = 2
    ChiefAndRing = 3
    List = 4
    Grid = 6
    ChiefAndMarginals = 8

class RunStatus:
    Completed = 0
    FailedToStart = 1
    TimedOut = 2
    InvalidTimeout = 3

class VertexOrder:
    First = 0
    Second = 1
    Third = 2