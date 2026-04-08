import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppProfileDataBoostIsolationReadOnlyArgs",
    "AppProfileDataBoostIsolationReadOnlyArgsDict",
    "AppProfileSingleClusterRoutingArgs",
    "AppProfileSingleClusterRoutingArgsDict",
    "AppProfileStandardIsolationArgs",
    "AppProfileStandardIsolationArgsDict",
    "AuthorizedViewSubsetViewArgs",
    "AuthorizedViewSubsetViewArgsDict",
    "AuthorizedViewSubsetViewFamilySubsetArgs",
    "AuthorizedViewSubsetViewFamilySubsetArgsDict",
    "GCPolicyMaxAgeArgs",
    "GCPolicyMaxAgeArgsDict",
    "GCPolicyMaxVersionArgs",
    "GCPolicyMaxVersionArgsDict",
    "InstanceClusterArgs",
    "InstanceClusterArgsDict",
    "InstanceClusterAutoscalingConfigArgs",
    "InstanceClusterAutoscalingConfigArgsDict",
    "InstanceIamBindingConditionArgs",
    "InstanceIamBindingConditionArgsDict",
    "InstanceIamMemberConditionArgs",
    "InstanceIamMemberConditionArgsDict",
    "SchemaBundleProtoSchemaArgs",
    "SchemaBundleProtoSchemaArgsDict",
    "TableAutomatedBackupPolicyArgs",
    "TableAutomatedBackupPolicyArgsDict",
    "TableColumnFamilyArgs",
    "TableColumnFamilyArgsDict",
    "TableIamBindingConditionArgs",
    "TableIamBindingConditionArgsDict",
    "TableIamMemberConditionArgs",
    "TableIamMemberConditionArgsDict",
]

class AppProfileDataBoostIsolationReadOnlyArgsDict(TypedDict):
    compute_billing_owner: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppProfileDataBoostIsolationReadOnlyArgs:
    def __init__(
        __self__, *, compute_billing_owner: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeBillingOwner")
    def compute_billing_owner(self) -> pulumi.Input[_builtins.str]: ...
    @compute_billing_owner.setter
    def compute_billing_owner(self, value: pulumi.Input[_builtins.str]): ...

class AppProfileSingleClusterRoutingArgsDict(TypedDict):
    cluster_id: pulumi.Input[_builtins.str]
    allow_transactional_writes: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class AppProfileSingleClusterRoutingArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        allow_transactional_writes: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowTransactionalWrites")
    def allow_transactional_writes(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_transactional_writes.setter
    def allow_transactional_writes(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AppProfileStandardIsolationArgsDict(TypedDict):
    priority: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppProfileStandardIsolationArgs:
    def __init__(__self__, *, priority: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.str]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.str]): ...

class AuthorizedViewSubsetViewArgsDict(TypedDict):
    family_subsets: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AuthorizedViewSubsetViewFamilySubsetArgsDict]]
        ]
    ]
    row_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AuthorizedViewSubsetViewArgs:
    def __init__(
        __self__,
        *,
        family_subsets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AuthorizedViewSubsetViewFamilySubsetArgs]]
            ]
        ] = ...,
        row_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="familySubsets")
    def family_subsets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AuthorizedViewSubsetViewFamilySubsetArgs]]]
    ]: ...
    @family_subsets.setter
    def family_subsets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AuthorizedViewSubsetViewFamilySubsetArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rowPrefixes")
    def row_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @row_prefixes.setter
    def row_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AuthorizedViewSubsetViewFamilySubsetArgsDict(TypedDict):
    family_name: pulumi.Input[_builtins.str]
    qualifier_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    qualifiers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class AuthorizedViewSubsetViewFamilySubsetArgs:
    def __init__(
        __self__,
        *,
        family_name: pulumi.Input[_builtins.str],
        qualifier_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        qualifiers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> pulumi.Input[_builtins.str]: ...
    @family_name.setter
    def family_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="qualifierPrefixes")
    def qualifier_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @qualifier_prefixes.setter
    def qualifier_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def qualifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @qualifiers.setter
    def qualifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class GCPolicyMaxAgeArgsDict(TypedDict):
    days: NotRequired[pulumi.Input[_builtins.int]]
    duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GCPolicyMaxAgeArgs:
    def __init__(
        __self__,
        *,
        days: Optional[pulumi.Input[_builtins.int]] = ...,
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Deprecated in favor of duration""")
    def days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @days.setter
    def days(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GCPolicyMaxVersionArgsDict(TypedDict):
    number: pulumi.Input[_builtins.int]

@pulumi.input_type
class GCPolicyMaxVersionArgs:
    def __init__(__self__, *, number: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def number(self) -> pulumi.Input[_builtins.int]: ...
    @number.setter
    def number(self, value: pulumi.Input[_builtins.int]): ...

class InstanceClusterArgsDict(TypedDict):
    cluster_id: pulumi.Input[_builtins.str]
    autoscaling_config: NotRequired[
        pulumi.Input[InstanceClusterAutoscalingConfigArgsDict]
    ]
    kms_key_name: NotRequired[pulumi.Input[_builtins.str]]
    node_scaling_factor: NotRequired[pulumi.Input[_builtins.str]]
    num_nodes: NotRequired[pulumi.Input[_builtins.int]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    storage_type: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceClusterArgs:
    def __init__(
        __self__,
        *,
        cluster_id: pulumi.Input[_builtins.str],
        autoscaling_config: Optional[
            pulumi.Input[InstanceClusterAutoscalingConfigArgs]
        ] = ...,
        kms_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_scaling_factor: Optional[pulumi.Input[_builtins.str]] = ...,
        num_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_type: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> Optional[pulumi.Input[InstanceClusterAutoscalingConfigArgs]]: ...
    @autoscaling_config.setter
    def autoscaling_config(
        self, value: Optional[pulumi.Input[InstanceClusterAutoscalingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeScalingFactor")
    def node_scaling_factor(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_scaling_factor.setter
    def node_scaling_factor(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceClusterAutoscalingConfigArgsDict(TypedDict):
    cpu_target: pulumi.Input[_builtins.int]
    max_nodes: pulumi.Input[_builtins.int]
    min_nodes: pulumi.Input[_builtins.int]
    storage_target: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class InstanceClusterAutoscalingConfigArgs:
    def __init__(
        __self__,
        *,
        cpu_target: pulumi.Input[_builtins.int],
        max_nodes: pulumi.Input[_builtins.int],
        min_nodes: pulumi.Input[_builtins.int],
        storage_target: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuTarget")
    def cpu_target(self) -> pulumi.Input[_builtins.int]: ...
    @cpu_target.setter
    def cpu_target(self, value: pulumi.Input[_builtins.int]): ...
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
    @_builtins.property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_target.setter
    def storage_target(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceIamBindingConditionArgs:
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

class InstanceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InstanceIamMemberConditionArgs:
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

class SchemaBundleProtoSchemaArgsDict(TypedDict):
    proto_descriptors: pulumi.Input[_builtins.str]

@pulumi.input_type
class SchemaBundleProtoSchemaArgs:
    def __init__(
        __self__, *, proto_descriptors: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protoDescriptors")
    def proto_descriptors(self) -> pulumi.Input[_builtins.str]: ...
    @proto_descriptors.setter
    def proto_descriptors(self, value: pulumi.Input[_builtins.str]): ...

class TableAutomatedBackupPolicyArgsDict(TypedDict):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    retention_period: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableAutomatedBackupPolicyArgs:
    def __init__(
        __self__,
        *,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        retention_period: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retention_period.setter
    def retention_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableColumnFamilyArgsDict(TypedDict):
    family: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableColumnFamilyArgs:
    def __init__(
        __self__,
        *,
        family: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Input[_builtins.str]: ...
    @family.setter
    def family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableIamBindingConditionArgs:
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

class TableIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TableIamMemberConditionArgs:
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
