import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BackupScheduleEncryptionConfigArgs",
    "BackupScheduleEncryptionConfigArgsDict",
    "BackupScheduleFullBackupSpecArgs",
    "BackupScheduleFullBackupSpecArgsDict",
    "BackupScheduleIncrementalBackupSpecArgs",
    "BackupScheduleIncrementalBackupSpecArgsDict",
    "BackupScheduleSpecArgs",
    "BackupScheduleSpecArgsDict",
    "BackupScheduleSpecCronSpecArgs",
    "BackupScheduleSpecCronSpecArgsDict",
    "DatabaseEncryptionConfigArgs",
    "DatabaseEncryptionConfigArgsDict",
    "DatabaseIAMBindingConditionArgs",
    "DatabaseIAMBindingConditionArgsDict",
    "DatabaseIAMMemberConditionArgs",
    "DatabaseIAMMemberConditionArgsDict",
    "InstanceAutoscalingConfigArgs",
    "InstanceAutoscalingConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "InstanceAutoscalingConfigAutoscalingLimitsArgs",
    "InstanceAutoscalingConfigAutoscalingLimitsArgsDict",
    "InstanceAutoscalingConfigAutoscalingTargetsArgs",
    ...,
    "InstanceConfigReplicaArgs",
    "InstanceConfigReplicaArgsDict",
    "InstanceIAMBindingConditionArgs",
    "InstanceIAMBindingConditionArgsDict",
    "InstanceIAMMemberConditionArgs",
    "InstanceIAMMemberConditionArgsDict",
]

class BackupScheduleEncryptionConfigArgsDict(TypedDict):
    encryption_type: pulumi.Input[_builtins.str]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class BackupScheduleEncryptionConfigArgs:
    def __init__(
        __self__,
        *,
        encryption_type: pulumi.Input[_builtins.str],
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNames")
    def kms_key_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kms_key_names.setter
    def kms_key_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class BackupScheduleFullBackupSpecArgsDict(TypedDict): ...

@pulumi.input_type
class BackupScheduleFullBackupSpecArgs:
    def __init__(__self__) -> None: ...

class BackupScheduleIncrementalBackupSpecArgsDict(TypedDict): ...

@pulumi.input_type
class BackupScheduleIncrementalBackupSpecArgs:
    def __init__(__self__) -> None: ...

class BackupScheduleSpecArgsDict(TypedDict):
    cron_spec: NotRequired[pulumi.Input[BackupScheduleSpecCronSpecArgsDict]]
    ...

@pulumi.input_type
class BackupScheduleSpecArgs:
    def __init__(
        __self__,
        *,
        cron_spec: Optional[pulumi.Input[BackupScheduleSpecCronSpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cronSpec")
    def cron_spec(self) -> Optional[pulumi.Input[BackupScheduleSpecCronSpecArgs]]: ...
    @cron_spec.setter
    def cron_spec(
        self, value: Optional[pulumi.Input[BackupScheduleSpecCronSpecArgs]]
    ): ...

class BackupScheduleSpecCronSpecArgsDict(TypedDict):
    text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class BackupScheduleSpecCronSpecArgs:
    def __init__(
        __self__, *, text: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatabaseEncryptionConfigArgsDict(TypedDict):
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DatabaseEncryptionConfigArgs:
    def __init__(
        __self__,
        *,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyNames")
    def kms_key_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @kms_key_names.setter
    def kms_key_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DatabaseIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatabaseIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DatabaseIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DatabaseIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceAutoscalingConfigArgsDict(TypedDict):
    asymmetric_autoscaling_options: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgsDict
                ]
            ]
        ]
    ]
    autoscaling_limits: NotRequired[
        pulumi.Input[InstanceAutoscalingConfigAutoscalingLimitsArgsDict]
    ]
    autoscaling_targets: NotRequired[
        pulumi.Input[InstanceAutoscalingConfigAutoscalingTargetsArgsDict]
    ]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigArgs:
    def __init__(
        __self__,
        *,
        asymmetric_autoscaling_options: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgs
                    ]
                ]
            ]
        ] = ...,
        autoscaling_limits: Optional[
            pulumi.Input[InstanceAutoscalingConfigAutoscalingLimitsArgs]
        ] = ...,
        autoscaling_targets: Optional[
            pulumi.Input[InstanceAutoscalingConfigAutoscalingTargetsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asymmetricAutoscalingOptions")
    def asymmetric_autoscaling_options(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgs]
            ]
        ]
    ]: ...
    @asymmetric_autoscaling_options.setter
    def asymmetric_autoscaling_options(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> Optional[pulumi.Input[InstanceAutoscalingConfigAutoscalingLimitsArgs]]: ...
    @autoscaling_limits.setter
    def autoscaling_limits(
        self,
        value: Optional[pulumi.Input[InstanceAutoscalingConfigAutoscalingLimitsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingTargets")
    def autoscaling_targets(
        self,
    ) -> Optional[pulumi.Input[InstanceAutoscalingConfigAutoscalingTargetsArgs]]: ...
    @autoscaling_targets.setter
    def autoscaling_targets(
        self,
        value: Optional[pulumi.Input[InstanceAutoscalingConfigAutoscalingTargetsArgs]],
    ): ...

class InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgsDict(TypedDict):
    overrides: pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgsDict
    ]
    replica_selection: pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgsDict
    ]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionArgs:
    def __init__(
        __self__,
        *,
        overrides: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgs
        ],
        replica_selection: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def overrides(
        self,
    ) -> pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgs
    ]: ...
    @overrides.setter
    def overrides(
        self,
        value: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaSelection")
    def replica_selection(
        self,
    ) -> pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgs
    ]: ...
    @replica_selection.setter
    def replica_selection(
        self,
        value: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgs
        ],
    ): ...

class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgsDict(TypedDict):
    autoscaling_limits: pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgsDict
    ]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesArgs:
    def __init__(
        __self__,
        *,
        autoscaling_limits: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingLimits")
    def autoscaling_limits(
        self,
    ) -> pulumi.Input[
        InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgs
    ]: ...
    @autoscaling_limits.setter
    def autoscaling_limits(
        self,
        value: pulumi.Input[
            InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgs
        ],
    ): ...

class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgsDict(
    TypedDict
):
    max_nodes: pulumi.Input[_builtins.int]
    min_nodes: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionOverridesAutoscalingLimitsArgs:
    def __init__(
        __self__,
        *,
        max_nodes: pulumi.Input[_builtins.int],
        min_nodes: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> pulumi.Input[_builtins.int]: ...
    @max_nodes.setter
    def max_nodes(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> pulumi.Input[_builtins.int]: ...
    @min_nodes.setter
    def min_nodes(self, value: pulumi.Input[_builtins.int]): ...

class InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgsDict(
    TypedDict
):
    location: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAsymmetricAutoscalingOptionReplicaSelectionArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...

class InstanceAutoscalingConfigAutoscalingLimitsArgsDict(TypedDict):
    max_nodes: NotRequired[pulumi.Input[_builtins.int]]
    max_processing_units: NotRequired[pulumi.Input[_builtins.int]]
    min_nodes: NotRequired[pulumi.Input[_builtins.int]]
    min_processing_units: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAutoscalingLimitsArgs:
    def __init__(
        __self__,
        *,
        max_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        max_processing_units: Optional[pulumi.Input[_builtins.int]] = ...,
        min_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        min_processing_units: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_nodes.setter
    def max_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxProcessingUnits")
    def max_processing_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_processing_units.setter
    def max_processing_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_nodes.setter
    def min_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minProcessingUnits")
    def min_processing_units(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_processing_units.setter
    def min_processing_units(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceAutoscalingConfigAutoscalingTargetsArgsDict(TypedDict):
    high_priority_cpu_utilization_percent: NotRequired[pulumi.Input[_builtins.int]]
    storage_utilization_percent: NotRequired[pulumi.Input[_builtins.int]]
    total_cpu_utilization_percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceAutoscalingConfigAutoscalingTargetsArgs:
    def __init__(
        __self__,
        *,
        high_priority_cpu_utilization_percent: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        storage_utilization_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        total_cpu_utilization_percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="highPriorityCpuUtilizationPercent")
    def high_priority_cpu_utilization_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @high_priority_cpu_utilization_percent.setter
    def high_priority_cpu_utilization_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageUtilizationPercent")
    def storage_utilization_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_utilization_percent.setter
    def storage_utilization_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="totalCpuUtilizationPercent")
    def total_cpu_utilization_percent(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_cpu_utilization_percent.setter
    def total_cpu_utilization_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class InstanceConfigReplicaArgsDict(TypedDict):
    default_leader_location: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceConfigReplicaArgs:
    def __init__(
        __self__,
        *,
        default_leader_location: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLeaderLocation")
    def default_leader_location(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_leader_location.setter
    def default_leader_location(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceIAMBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIAMBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceIAMMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceIAMMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
