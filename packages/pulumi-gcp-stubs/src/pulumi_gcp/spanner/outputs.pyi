import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupScheduleEncryptionConfig",
    "BackupScheduleFullBackupSpec",
    "BackupScheduleIncrementalBackupSpec",
    "BackupScheduleSpec",
    "BackupScheduleSpecCronSpec",
    "DatabaseEncryptionConfig",
    "DatabaseIAMBindingCondition",
    "DatabaseIAMMemberCondition",
    "InstanceAutoscalingConfig",
    ...,
    ...,
    ...,
    ...,
    "InstanceAutoscalingConfigAutoscalingLimits",
    "InstanceAutoscalingConfigAutoscalingTargets",
    "InstanceConfigReplica",
    "InstanceIAMBindingCondition",
    "InstanceIAMMemberCondition",
    "GetDatabaseEncryptionConfigResult",
    "GetInstanceAutoscalingConfigResult",
    ...,
    ...,
    ...,
    ...,
    "GetInstanceAutoscalingConfigAutoscalingLimitResult",
    ...,
]

@pulumi.output_type
class BackupScheduleEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: _builtins.str,
        kms_key_name: Optional[_builtins.str] = ...,
        kms_key_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNames")
    def kms_key_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class BackupScheduleFullBackupSpec(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class BackupScheduleIncrementalBackupSpec(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class BackupScheduleSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cron_spec: Optional[outputs.BackupScheduleSpecCronSpec] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronSpec")
    def cron_spec(self) -> Optional[outputs.BackupScheduleSpecCronSpec]: ...

@pulumi.output_type
class BackupScheduleSpecCronSpec(dict):
    def __init__(__self__, *, text: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabaseEncryptionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[_builtins.str] = ...,
        kms_key_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNames")
    def kms_key_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DatabaseIAMBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DatabaseIAMMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceAutoscalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        asymmetric_autoscaling_options: Optional[
            Sequence[outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOption]
        ] = ...,
        autoscaling_limits: Optional[
            outputs.InstanceAutoscalingConfigAutoscalingLimits
        ] = ...,
        autoscaling_targets: Optional[
            outputs.InstanceAutoscalingConfigAutoscalingTargets
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asymmetricAutoscalingOptions")
    def asymmetric_autoscaling_options(
        self,
    ) -> Optional[
        Sequence[outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOption]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> Optional[outputs.InstanceAutoscalingConfigAutoscalingLimits]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingTargets")
    def autoscaling_targets(
        self,
    ) -> Optional[outputs.InstanceAutoscalingConfigAutoscalingTargets]: ...

@pulumi.output_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        overrides: outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrides,
        replica_selection: outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelection,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrides: ...
    @_builtins.property
    @pulumi.getter(name="replicaSelection")
    def replica_selection(
        self,
    ) -> (
        outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelection
    ): ...

@pulumi.output_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrides(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        autoscaling_limits: outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimits,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> outputs.InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimits: ...

@pulumi.output_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimits(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_nodes: _builtins.int, min_nodes: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> _builtins.int: ...

@pulumi.output_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelection(dict):
    def __init__(__self__, *, location: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceAutoscalingConfigAutoscalingLimits(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_nodes: Optional[_builtins.int] = ...,
        max_processing_units: Optional[_builtins.int] = ...,
        min_nodes: Optional[_builtins.int] = ...,
        min_processing_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxProcessingUnits")
    def max_processing_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="minProcessingUnits")
    def min_processing_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceAutoscalingConfigAutoscalingTargets(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        high_priority_cpu_utilization_percent: Optional[_builtins.int] = ...,
        storage_utilization_percent: Optional[_builtins.int] = ...,
        total_cpu_utilization_percent: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="highPriorityCpuUtilizationPercent")
    def high_priority_cpu_utilization_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageUtilizationPercent")
    def storage_utilization_percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="totalCpuUtilizationPercent")
    def total_cpu_utilization_percent(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceConfigReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_leader_location: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLeaderLocation")
    def default_leader_location(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIAMBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceIAMMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetDatabaseEncryptionConfigResult(dict):
    def __init__(
        __self__, *, kms_key_name: _builtins.str, kms_key_names: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNames")
    def kms_key_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigResult(dict):
    def __init__(
        __self__,
        *,
        asymmetric_autoscaling_options: Sequence[
            outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionResult
        ],
        autoscaling_limits: Sequence[
            outputs.GetInstanceAutoscalingConfigAutoscalingLimitResult
        ],
        autoscaling_targets: Sequence[
            outputs.GetInstanceAutoscalingConfigAutoscalingTargetResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asymmetricAutoscalingOptions")
    def asymmetric_autoscaling_options(
        self,
    ) -> Sequence[
        outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> Sequence[outputs.GetInstanceAutoscalingConfigAutoscalingLimitResult]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingTargets")
    def autoscaling_targets(
        self,
    ) -> Sequence[outputs.GetInstanceAutoscalingConfigAutoscalingTargetResult]: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionResult(dict):
    def __init__(
        __self__,
        *,
        overrides: Sequence[
            outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideResult
        ],
        replica_selections: Sequence[
            outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> Sequence[
        outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="replicaSelections")
    def replica_selections(
        self,
    ) -> Sequence[
        outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionResult
    ]: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideResult(dict):
    def __init__(
        __self__,
        *,
        autoscaling_limits: Sequence[
            outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideAutoscalingLimitResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> Sequence[
        outputs.GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideAutoscalingLimitResult
    ]: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionOverrideAutoscalingLimitResult(
    dict
):
    def __init__(
        __self__, *, max_nodes: _builtins.int, min_nodes: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionResult(
    dict
):
    def __init__(__self__, *, location: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAutoscalingLimitResult(dict):
    def __init__(
        __self__,
        *,
        max_nodes: _builtins.int,
        max_processing_units: _builtins.int,
        min_nodes: _builtins.int,
        min_processing_units: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxProcessingUnits")
    def max_processing_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minProcessingUnits")
    def min_processing_units(self) -> _builtins.int: ...

@pulumi.output_type
class GetInstanceAutoscalingConfigAutoscalingTargetResult(dict):
    def __init__(
        __self__,
        *,
        high_priority_cpu_utilization_percent: _builtins.int,
        storage_utilization_percent: _builtins.int,
        total_cpu_utilization_percent: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="highPriorityCpuUtilizationPercent")
    def high_priority_cpu_utilization_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageUtilizationPercent")
    def storage_utilization_percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="totalCpuUtilizationPercent")
    def total_cpu_utilization_percent(self) -> _builtins.int: ...
