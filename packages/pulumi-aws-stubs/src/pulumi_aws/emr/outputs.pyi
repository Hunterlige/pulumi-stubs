import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    "ClusterAutoTerminationPolicy",
    "ClusterBootstrapAction",
    "ClusterCoreInstanceFleet",
    "ClusterCoreInstanceFleetInstanceTypeConfig",
    ...,
    ...,
    "ClusterCoreInstanceFleetLaunchSpecifications",
    ...,
    ...,
    "ClusterCoreInstanceGroup",
    "ClusterCoreInstanceGroupEbsConfig",
    "ClusterEc2Attributes",
    "ClusterKerberosAttributes",
    "ClusterMasterInstanceFleet",
    "ClusterMasterInstanceFleetInstanceTypeConfig",
    ...,
    ...,
    "ClusterMasterInstanceFleetLaunchSpecifications",
    ...,
    ...,
    "ClusterMasterInstanceGroup",
    "ClusterMasterInstanceGroupEbsConfig",
    "ClusterPlacementGroupConfig",
    "ClusterStep",
    "ClusterStepHadoopJarStep",
    "InstanceFleetInstanceTypeConfig",
    "InstanceFleetInstanceTypeConfigConfiguration",
    "InstanceFleetInstanceTypeConfigEbsConfig",
    "InstanceFleetLaunchSpecifications",
    ...,
    "InstanceFleetLaunchSpecificationsSpotSpecification",
    "InstanceGroupEbsConfig",
    "ManagedScalingPolicyComputeLimit",
    "GetReleaseLabelsFiltersResult",
    ...,
]

@pulumi.output_type
class BlockPublicAccessConfigurationPermittedPublicSecurityGroupRuleRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_range: _builtins.int, min_range: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRange")
    def max_range(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minRange")
    def min_range(self) -> _builtins.int: ...

@pulumi.output_type
class ClusterAutoTerminationPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, idle_timeout: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterBootstrapAction(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        path: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterCoreInstanceFleet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        instance_type_configs: Optional[
            Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfig]
        ] = ...,
        launch_specifications: Optional[
            outputs.ClusterCoreInstanceFleetLaunchSpecifications
        ] = ...,
        name: Optional[_builtins.str] = ...,
        provisioned_on_demand_capacity: Optional[_builtins.int] = ...,
        provisioned_spot_capacity: Optional[_builtins.int] = ...,
        target_on_demand_capacity: Optional[_builtins.int] = ...,
        target_spot_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> Optional[outputs.ClusterCoreInstanceFleetLaunchSpecifications]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterCoreInstanceFleetInstanceTypeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        bid_price: Optional[_builtins.str] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[_builtins.float] = ...,
        configurations: Optional[
            Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfigConfiguration]
        ] = ...,
        ebs_configs: Optional[
            Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfigEbsConfig]
        ] = ...,
        weighted_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfigConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCoreInstanceFleetInstanceTypeConfigEbsConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterCoreInstanceFleetInstanceTypeConfigConfiguration(dict):
    def __init__(
        __self__,
        *,
        classification: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ClusterCoreInstanceFleetInstanceTypeConfigEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterCoreInstanceFleetLaunchSpecifications(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            Sequence[
                outputs.ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification
            ]
        ] = ...,
        spot_specifications: Optional[
            Sequence[
                outputs.ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification]
    ]: ...

@pulumi.output_type
class ClusterCoreInstanceFleetLaunchSpecificationsOnDemandSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allocation_strategy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterCoreInstanceFleetLaunchSpecificationsSpotSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: _builtins.str,
        timeout_action: _builtins.str,
        timeout_duration_minutes: _builtins.int,
        block_duration_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterCoreInstanceGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        autoscaling_policy: Optional[_builtins.str] = ...,
        bid_price: Optional[_builtins.str] = ...,
        ebs_configs: Optional[
            Sequence[outputs.ClusterCoreInstanceGroupEbsConfig]
        ] = ...,
        id: Optional[_builtins.str] = ...,
        instance_count: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingPolicy")
    def autoscaling_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterCoreInstanceGroupEbsConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCoreInstanceGroupEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterEc2Attributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_profile: _builtins.str,
        additional_master_security_groups: Optional[_builtins.str] = ...,
        additional_slave_security_groups: Optional[_builtins.str] = ...,
        emr_managed_master_security_group: Optional[_builtins.str] = ...,
        emr_managed_slave_security_group: Optional[_builtins.str] = ...,
        key_name: Optional[_builtins.str] = ...,
        service_access_security_group: Optional[_builtins.str] = ...,
        subnet_id: Optional[_builtins.str] = ...,
        subnet_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceProfile")
    def instance_profile(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalMasterSecurityGroups")
    def additional_master_security_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="additionalSlaveSecurityGroups")
    def additional_slave_security_groups(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emrManagedMasterSecurityGroup")
    def emr_managed_master_security_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emrManagedSlaveSecurityGroup")
    def emr_managed_slave_security_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccessSecurityGroup")
    def service_access_security_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterKerberosAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kdc_admin_password: _builtins.str,
        realm: _builtins.str,
        ad_domain_join_password: Optional[_builtins.str] = ...,
        ad_domain_join_user: Optional[_builtins.str] = ...,
        cross_realm_trust_principal_password: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kdcAdminPassword")
    def kdc_admin_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def realm(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="adDomainJoinPassword")
    def ad_domain_join_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="adDomainJoinUser")
    def ad_domain_join_user(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crossRealmTrustPrincipalPassword")
    def cross_realm_trust_principal_password(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMasterInstanceFleet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        instance_type_configs: Optional[
            Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfig]
        ] = ...,
        launch_specifications: Optional[
            outputs.ClusterMasterInstanceFleetLaunchSpecifications
        ] = ...,
        name: Optional[_builtins.str] = ...,
        provisioned_on_demand_capacity: Optional[_builtins.int] = ...,
        provisioned_spot_capacity: Optional[_builtins.int] = ...,
        target_on_demand_capacity: Optional[_builtins.int] = ...,
        target_spot_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypeConfigs")
    def instance_type_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="launchSpecifications")
    def launch_specifications(
        self,
    ) -> Optional[outputs.ClusterMasterInstanceFleetLaunchSpecifications]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedOnDemandCapacity")
    def provisioned_on_demand_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedSpotCapacity")
    def provisioned_spot_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetOnDemandCapacity")
    def target_on_demand_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetSpotCapacity")
    def target_spot_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMasterInstanceFleetInstanceTypeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        bid_price: Optional[_builtins.str] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[_builtins.float] = ...,
        configurations: Optional[
            Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfigConfiguration]
        ] = ...,
        ebs_configs: Optional[
            Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfigEbsConfig]
        ] = ...,
        weighted_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfigConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterMasterInstanceFleetInstanceTypeConfigEbsConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMasterInstanceFleetInstanceTypeConfigConfiguration(dict):
    def __init__(
        __self__,
        *,
        classification: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ClusterMasterInstanceFleetInstanceTypeConfigEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMasterInstanceFleetLaunchSpecifications(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            Sequence[
                outputs.ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification
            ]
        ] = ...,
        spot_specifications: Optional[
            Sequence[
                outputs.ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification
        ]
    ]: ...

@pulumi.output_type
class ClusterMasterInstanceFleetLaunchSpecificationsOnDemandSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allocation_strategy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterMasterInstanceFleetLaunchSpecificationsSpotSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: _builtins.str,
        timeout_action: _builtins.str,
        timeout_duration_minutes: _builtins.int,
        block_duration_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterMasterInstanceGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        bid_price: Optional[_builtins.str] = ...,
        ebs_configs: Optional[
            Sequence[outputs.ClusterMasterInstanceGroupEbsConfig]
        ] = ...,
        id: Optional[_builtins.str] = ...,
        instance_count: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterMasterInstanceGroupEbsConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterMasterInstanceGroupEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        throughput: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterPlacementGroupConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_role: _builtins.str,
        placement_strategy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementStrategy")
    def placement_strategy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_on_failure: _builtins.str,
        hadoop_jar_step: outputs.ClusterStepHadoopJarStep,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionOnFailure")
    def action_on_failure(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hadoopJarStep")
    def hadoop_jar_step(self) -> outputs.ClusterStepHadoopJarStep: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterStepHadoopJarStep(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        jar: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        main_class: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def jar(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="mainClass")
    def main_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class InstanceFleetInstanceTypeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        bid_price: Optional[_builtins.str] = ...,
        bid_price_as_percentage_of_on_demand_price: Optional[_builtins.float] = ...,
        configurations: Optional[
            Sequence[outputs.InstanceFleetInstanceTypeConfigConfiguration]
        ] = ...,
        ebs_configs: Optional[
            Sequence[outputs.InstanceFleetInstanceTypeConfigEbsConfig]
        ] = ...,
        weighted_capacity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bidPrice")
    def bid_price(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bidPriceAsPercentageOfOnDemandPrice")
    def bid_price_as_percentage_of_on_demand_price(
        self,
    ) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def configurations(
        self,
    ) -> Optional[Sequence[outputs.InstanceFleetInstanceTypeConfigConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="ebsConfigs")
    def ebs_configs(
        self,
    ) -> Optional[Sequence[outputs.InstanceFleetInstanceTypeConfigEbsConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceFleetInstanceTypeConfigConfiguration(dict):
    def __init__(
        __self__,
        *,
        classification: Optional[_builtins.str] = ...,
        properties: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def classification(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class InstanceFleetInstanceTypeConfigEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceFleetLaunchSpecifications(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        on_demand_specifications: Optional[
            Sequence[outputs.InstanceFleetLaunchSpecificationsOnDemandSpecification]
        ] = ...,
        spot_specifications: Optional[
            Sequence[outputs.InstanceFleetLaunchSpecificationsSpotSpecification]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onDemandSpecifications")
    def on_demand_specifications(
        self,
    ) -> Optional[
        Sequence[outputs.InstanceFleetLaunchSpecificationsOnDemandSpecification]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="spotSpecifications")
    def spot_specifications(
        self,
    ) -> Optional[
        Sequence[outputs.InstanceFleetLaunchSpecificationsSpotSpecification]
    ]: ...

@pulumi.output_type
class InstanceFleetLaunchSpecificationsOnDemandSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allocation_strategy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...

@pulumi.output_type
class InstanceFleetLaunchSpecificationsSpotSpecification(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allocation_strategy: _builtins.str,
        timeout_action: _builtins.str,
        timeout_duration_minutes: _builtins.int,
        block_duration_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutAction")
    def timeout_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutDurationMinutes")
    def timeout_duration_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="blockDurationMinutes")
    def block_duration_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class InstanceGroupEbsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        size: _builtins.int,
        type: _builtins.str,
        iops: Optional[_builtins.int] = ...,
        volumes_per_instance: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="volumesPerInstance")
    def volumes_per_instance(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ManagedScalingPolicyComputeLimit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_capacity_units: _builtins.int,
        minimum_capacity_units: _builtins.int,
        unit_type: _builtins.str,
        maximum_core_capacity_units: Optional[_builtins.int] = ...,
        maximum_ondemand_capacity_units: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumCapacityUnits")
    def maximum_capacity_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minimumCapacityUnits")
    def minimum_capacity_units(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="unitType")
    def unit_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maximumCoreCapacityUnits")
    def maximum_core_capacity_units(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumOndemandCapacityUnits")
    def maximum_ondemand_capacity_units(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetReleaseLabelsFiltersResult(dict):
    def __init__(
        __self__,
        *,
        application: Optional[_builtins.str] = ...,
        prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def application(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetSupportedInstanceTypesSupportedInstanceTypeResult(dict):
    def __init__(
        __self__,
        *,
        architecture: _builtins.str,
        ebs_optimized_available: _builtins.bool,
        ebs_optimized_by_default: _builtins.bool,
        ebs_storage_only: _builtins.bool,
        instance_family_id: _builtins.str,
        is64_bits_only: _builtins.bool,
        memory_gb: _builtins.float,
        number_of_disks: _builtins.int,
        storage_gb: _builtins.int,
        type: _builtins.str,
        vcpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptimizedAvailable")
    def ebs_optimized_available(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ebsOptimizedByDefault")
    def ebs_optimized_by_default(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ebsStorageOnly")
    def ebs_storage_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="instanceFamilyId")
    def instance_family_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="is64BitsOnly")
    def is64_bits_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="numberOfDisks")
    def number_of_disks(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageGb")
    def storage_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def vcpu(self) -> _builtins.int: ...
