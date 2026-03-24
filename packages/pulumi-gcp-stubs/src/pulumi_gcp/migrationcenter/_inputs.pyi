import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PreferenceSetVirtualMachinePreferencesArgs",
    "PreferenceSetVirtualMachinePreferencesArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

class PreferenceSetVirtualMachinePreferencesArgsDict(TypedDict):
    commitment_plan: NotRequired[pulumi.Input[_builtins.str]]
    compute_engine_preferences: NotRequired[
        pulumi.Input[
            PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgsDict
        ]
    ]
    region_preferences: NotRequired[
        pulumi.Input[PreferenceSetVirtualMachinePreferencesRegionPreferencesArgsDict]
    ]
    sizing_optimization_strategy: NotRequired[pulumi.Input[_builtins.str]]
    sole_tenancy_preferences: NotRequired[
        pulumi.Input[
            PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgsDict
        ]
    ]
    target_product: NotRequired[pulumi.Input[_builtins.str]]
    vmware_engine_preferences: NotRequired[
        pulumi.Input[
            PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesArgs:
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_engine_preferences: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgs
            ]
        ] = ...,
        region_preferences: Optional[
            pulumi.Input[PreferenceSetVirtualMachinePreferencesRegionPreferencesArgs]
        ] = ...,
        sizing_optimization_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        sole_tenancy_preferences: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgs
            ]
        ] = ...,
        target_product: Optional[pulumi.Input[_builtins.str]] = ...,
        vmware_engine_preferences: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_plan.setter
    def commitment_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeEnginePreferences")
    def compute_engine_preferences(
        self,
    ) -> Optional[
        pulumi.Input[PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgs]
    ]: ...
    @compute_engine_preferences.setter
    def compute_engine_preferences(
        self,
        value: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionPreferences")
    def region_preferences(
        self,
    ) -> Optional[
        pulumi.Input[PreferenceSetVirtualMachinePreferencesRegionPreferencesArgs]
    ]: ...
    @region_preferences.setter
    def region_preferences(
        self,
        value: Optional[
            pulumi.Input[PreferenceSetVirtualMachinePreferencesRegionPreferencesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sizingOptimizationStrategy")
    def sizing_optimization_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sizing_optimization_strategy.setter
    def sizing_optimization_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="soleTenancyPreferences")
    def sole_tenancy_preferences(
        self,
    ) -> Optional[
        pulumi.Input[PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgs]
    ]: ...
    @sole_tenancy_preferences.setter
    def sole_tenancy_preferences(
        self,
        value: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetProduct")
    def target_product(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_product.setter
    def target_product(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vmwareEnginePreferences")
    def vmware_engine_preferences(
        self,
    ) -> Optional[
        pulumi.Input[PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgs]
    ]: ...
    @vmware_engine_preferences.setter
    def vmware_engine_preferences(
        self,
        value: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgs
            ]
        ],
    ): ...

class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgsDict(TypedDict):
    license_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_preferences: NotRequired[
        pulumi.Input[
            PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesArgs:
    def __init__(
        __self__,
        *,
        license_type: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_preferences: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @license_type.setter
    def license_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machinePreferences")
    def machine_preferences(
        self,
    ) -> Optional[
        pulumi.Input[
            PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgs
        ]
    ]: ...
    @machine_preferences.setter
    def machine_preferences(
        self,
        value: Optional[
            pulumi.Input[
                PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgs
            ]
        ],
    ): ...

class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgsDict(
    TypedDict
):
    allowed_machine_series: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesArgs:
    def __init__(
        __self__,
        *,
        allowed_machine_series: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedMachineSeries")
    def allowed_machine_series(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgs
                ]
            ]
        ]
    ]: ...
    @allowed_machine_series.setter
    def allowed_machine_series(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesComputeEnginePreferencesMachinePreferencesAllowedMachineSeriesArgs:
    def __init__(
        __self__, *, code: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreferenceSetVirtualMachinePreferencesRegionPreferencesArgsDict(TypedDict):
    preferred_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesRegionPreferencesArgs:
    def __init__(
        __self__,
        *,
        preferred_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preferredRegions")
    def preferred_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_regions.setter
    def preferred_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgsDict(TypedDict):
    commitment_plan: NotRequired[pulumi.Input[_builtins.str]]
    cpu_overcommit_ratio: NotRequired[pulumi.Input[_builtins.float]]
    host_maintenance_policy: NotRequired[pulumi.Input[_builtins.str]]
    node_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesArgs:
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_overcommit_ratio: Optional[pulumi.Input[_builtins.float]] = ...,
        host_maintenance_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        node_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_plan.setter
    def commitment_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu_overcommit_ratio.setter
    def cpu_overcommit_ratio(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="hostMaintenancePolicy")
    def host_maintenance_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_maintenance_policy.setter
    def host_maintenance_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeTypes")
    def node_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgs
                ]
            ]
        ]
    ]: ...
    @node_types.setter
    def node_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgsDict(
    TypedDict
):
    node_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesSoleTenancyPreferencesNodeTypeArgs:
    def __init__(
        __self__, *, node_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgsDict(TypedDict):
    commitment_plan: NotRequired[pulumi.Input[_builtins.str]]
    cpu_overcommit_ratio: NotRequired[pulumi.Input[_builtins.float]]
    memory_overcommit_ratio: NotRequired[pulumi.Input[_builtins.float]]
    storage_deduplication_compression_ratio: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class PreferenceSetVirtualMachinePreferencesVmwareEnginePreferencesArgs:
    def __init__(
        __self__,
        *,
        commitment_plan: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu_overcommit_ratio: Optional[pulumi.Input[_builtins.float]] = ...,
        memory_overcommit_ratio: Optional[pulumi.Input[_builtins.float]] = ...,
        storage_deduplication_compression_ratio: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commitmentPlan")
    def commitment_plan(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commitment_plan.setter
    def commitment_plan(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitRatio")
    def cpu_overcommit_ratio(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu_overcommit_ratio.setter
    def cpu_overcommit_ratio(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryOvercommitRatio")
    def memory_overcommit_ratio(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_overcommit_ratio.setter
    def memory_overcommit_ratio(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageDeduplicationCompressionRatio")
    def storage_deduplication_compression_ratio(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @storage_deduplication_compression_ratio.setter
    def storage_deduplication_compression_ratio(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
