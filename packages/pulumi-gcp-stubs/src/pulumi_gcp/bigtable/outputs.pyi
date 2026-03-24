import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppProfileDataBoostIsolationReadOnly",
    "AppProfileSingleClusterRouting",
    "AppProfileStandardIsolation",
    "AuthorizedViewSubsetView",
    "AuthorizedViewSubsetViewFamilySubset",
    "GCPolicyMaxAge",
    "GCPolicyMaxVersion",
    "InstanceCluster",
    "InstanceClusterAutoscalingConfig",
    "InstanceIamBindingCondition",
    "InstanceIamMemberCondition",
    "SchemaBundleProtoSchema",
    "TableAutomatedBackupPolicy",
    "TableColumnFamily",
    "TableIamBindingCondition",
    "TableIamMemberCondition",
]

@pulumi.output_type
class AppProfileDataBoostIsolationReadOnly(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, compute_billing_owner: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeBillingOwner")
    def compute_billing_owner(self) -> _builtins.str: ...

@pulumi.output_type
class AppProfileSingleClusterRouting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_id: _builtins.str,
        allow_transactional_writes: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowTransactionalWrites")
    def allow_transactional_writes(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AppProfileStandardIsolation(dict):
    def __init__(__self__, *, priority: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.str: ...

@pulumi.output_type
class AuthorizedViewSubsetView(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        family_subsets: Optional[
            Sequence[outputs.AuthorizedViewSubsetViewFamilySubset]
        ] = ...,
        row_prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="familySubsets")
    def family_subsets(
        self,
    ) -> Optional[Sequence[outputs.AuthorizedViewSubsetViewFamilySubset]]: ...
    @_builtins.property
    @pulumi.getter(name="rowPrefixes")
    def row_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AuthorizedViewSubsetViewFamilySubset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        family_name: _builtins.str,
        qualifier_prefixes: Optional[Sequence[_builtins.str]] = ...,
        qualifiers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="familyName")
    def family_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="qualifierPrefixes")
    def qualifier_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def qualifiers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GCPolicyMaxAge(dict):
    def __init__(
        __self__,
        *,
        days: Optional[_builtins.int] = ...,
        duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""Deprecated in favor of duration""")
    def days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GCPolicyMaxVersion(dict):
    def __init__(__self__, *, number: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def number(self) -> _builtins.int: ...

@pulumi.output_type
class InstanceCluster(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cluster_id: _builtins.str,
        autoscaling_config: Optional[outputs.InstanceClusterAutoscalingConfig] = ...,
        kms_key_name: Optional[_builtins.str] = ...,
        node_scaling_factor: Optional[_builtins.str] = ...,
        num_nodes: Optional[_builtins.int] = ...,
        state: Optional[_builtins.str] = ...,
        storage_type: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(
        self,
    ) -> Optional[outputs.InstanceClusterAutoscalingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeScalingFactor")
    def node_scaling_factor(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class InstanceClusterAutoscalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cpu_target: _builtins.int,
        max_nodes: _builtins.int,
        min_nodes: _builtins.int,
        storage_target: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuTarget")
    def cpu_target(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxNodes")
    def max_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minNodes")
    def min_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageTarget")
    def storage_target(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceIamBindingCondition(dict):
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
class InstanceIamMemberCondition(dict):
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
class SchemaBundleProtoSchema(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, proto_descriptors: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="protoDescriptors")
    def proto_descriptors(self) -> _builtins.str: ...

@pulumi.output_type
class TableAutomatedBackupPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        frequency: Optional[_builtins.str] = ...,
        retention_period: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableColumnFamily(dict):
    def __init__(
        __self__, *, family: _builtins.str, type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TableIamBindingCondition(dict):
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
class TableIamMemberCondition(dict):
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
