import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PreferenceSetVirtualMachinePreferences", ..., ..., ..., ..., ..., ..., ...]

@pulumi.output_type
class PreferenceSetVirtualMachinePreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[_builtins.str] = ...,
        compute_engine_preferences: Optional[
            outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferences
        ] = ...,
        region_preferences: Optional[
            outputs.PreferenceSetVirtualMachinePreferencesRegionPreferences
        ] = ...,
        sizing_optimization_strategy: Optional[_builtins.str] = ...,
        sole_tenancy_preferences: Optional[
            outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences
        ] = ...,
        target_product: Optional[_builtins.str] = ...,
        vmware_engine_preferences: Optional[
            outputs.PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeEnginePreferences")
    def compute_engine_preferences(
        self,
    ) -> Optional[
        outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferences
    ]: ...
    @_builtins.property
    @pulumi.getter(name="regionPreferences")
    def region_preferences(
        self,
    ) -> Optional[outputs.PreferenceSetVirtualMachinePreferencesRegionPreferences]: ...
    @_builtins.property
    @pulumi.getter(name="sizingOptimizationStrategy")
    def sizing_optimization_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="soleTenancyPreferences")
    def sole_tenancy_preferences(
        self,
    ) -> Optional[
        outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetProduct")
    def target_product(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vmwareEnginePreferences")
    def vmware_engine_preferences(
        self,
    ) -> Optional[
        outputs.PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences
    ]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        license_type: Optional[_builtins.str] = ...,
        machine_preferences: Optional[
            outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machinePreferences")
    def machine_preferences(
        self,
    ) -> Optional[
        outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences
    ]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferences(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_machine_series: Optional[
            Sequence[
                outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMachineSeries")
    def allowed_machine_series(
        self,
    ) -> Optional[
        Sequence[
            outputs.PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries
        ]
    ]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeries(
    dict
):
    def __init__(__self__, *, code: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesRegionPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, preferred_regions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredRegions")
    def preferred_regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[_builtins.str] = ...,
        cpu_overcommit_ratio: Optional[_builtins.float] = ...,
        host_maintenance_policy: Optional[_builtins.str] = ...,
        node_types: Optional[
            Sequence[
                outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(
        self,
    ) -> Optional[
        Sequence[
            outputs.PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType
        ]
    ]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeType(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, node_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PreferenceSetVirtualMachinePreferencesVmwareEnginePreferences(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[_builtins.str] = ...,
        cpu_overcommit_ratio: Optional[_builtins.float] = ...,
        memory_overcommit_ratio: Optional[_builtins.float] = ...,
        storage_deduplication_compression_ratio: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="memoryOvercommitRatio")
    def memory_overcommit_ratio(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="storageDeduplicationCompressionRatio")
    def storage_deduplication_compression_ratio(self) -> Optional[_builtins.float]: ...
