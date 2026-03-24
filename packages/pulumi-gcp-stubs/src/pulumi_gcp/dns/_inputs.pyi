

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DnsManagedZoneIamBindingConditionArgs', 'DnsManagedZoneIamBindingConditionArgsDict', 'DnsManagedZoneIamMemberConditionArgs', 'DnsManagedZoneIamMemberConditionArgsDict', 'ManagedZoneCloudLoggingConfigArgs', 'ManagedZoneCloudLoggingConfigArgsDict', 'ManagedZoneDnssecConfigArgs', 'ManagedZoneDnssecConfigArgsDict', 'ManagedZoneDnssecConfigDefaultKeySpecArgs', 'ManagedZoneDnssecConfigDefaultKeySpecArgsDict', 'ManagedZoneForwardingConfigArgs', 'ManagedZoneForwardingConfigArgsDict', 'ManagedZoneForwardingConfigTargetNameServerArgs', ..., 'ManagedZonePeeringConfigArgs', 'ManagedZonePeeringConfigArgsDict', 'ManagedZonePeeringConfigTargetNetworkArgs', 'ManagedZonePeeringConfigTargetNetworkArgsDict', 'ManagedZonePrivateVisibilityConfigArgs', 'ManagedZonePrivateVisibilityConfigArgsDict', 'ManagedZonePrivateVisibilityConfigGkeClusterArgs', ..., 'ManagedZonePrivateVisibilityConfigNetworkArgs', 'ManagedZonePrivateVisibilityConfigNetworkArgsDict', 'ManagedZoneServiceDirectoryConfigArgs', 'ManagedZoneServiceDirectoryConfigArgsDict', 'ManagedZoneServiceDirectoryConfigNamespaceArgs', 'ManagedZoneServiceDirectoryConfigNamespaceArgsDict', 'PolicyAlternativeNameServerConfigArgs', 'PolicyAlternativeNameServerConfigArgsDict', ..., ..., 'PolicyDns64ConfigArgs', 'PolicyDns64ConfigArgsDict', 'PolicyDns64ConfigScopeArgs', 'PolicyDns64ConfigScopeArgsDict', 'PolicyNetworkArgs', 'PolicyNetworkArgsDict', 'RecordSetRoutingPolicyArgs', 'RecordSetRoutingPolicyArgsDict', 'RecordSetRoutingPolicyGeoArgs', 'RecordSetRoutingPolicyGeoArgsDict', 'RecordSetRoutingPolicyGeoHealthCheckedTargetsArgs', ..., ..., ..., 'RecordSetRoutingPolicyPrimaryBackupArgs', 'RecordSetRoutingPolicyPrimaryBackupArgsDict', 'RecordSetRoutingPolicyPrimaryBackupBackupGeoArgs', ..., ..., ..., ..., ..., 'RecordSetRoutingPolicyPrimaryBackupPrimaryArgs', 'RecordSetRoutingPolicyPrimaryBackupPrimaryArgsDict', ..., ..., 'RecordSetRoutingPolicyWrrArgs', 'RecordSetRoutingPolicyWrrArgsDict', 'RecordSetRoutingPolicyWrrHealthCheckedTargetsArgs', ..., ..., ..., 'ResponsePolicyGkeClusterArgs', 'ResponsePolicyGkeClusterArgsDict', 'ResponsePolicyNetworkArgs', 'ResponsePolicyNetworkArgsDict', 'ResponsePolicyRuleLocalDataArgs', 'ResponsePolicyRuleLocalDataArgsDict', 'ResponsePolicyRuleLocalDataLocalDataArgs', 'ResponsePolicyRuleLocalDataLocalDataArgsDict']
class DnsManagedZoneIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DnsManagedZoneIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DnsManagedZoneIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DnsManagedZoneIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedZoneCloudLoggingConfigArgsDict(TypedDict):
    enable_logging: pulumi.Input[_builtins.bool]


@pulumi.input_type
class ManagedZoneCloudLoggingConfigArgs:
    def __init__(__self__, *, enable_logging: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_logging.setter
    def enable_logging(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class ManagedZoneDnssecConfigArgsDict(TypedDict):
    default_key_specs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedZoneDnssecConfigDefaultKeySpecArgsDict]]]]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    non_existence: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedZoneDnssecConfigArgs:
    def __init__(__self__, *, default_key_specs: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZoneDnssecConfigDefaultKeySpecArgs]]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., non_existence: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeySpecs")
    def default_key_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZoneDnssecConfigDefaultKeySpecArgs]]]]:
        
        ...
    
    @default_key_specs.setter
    def default_key_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZoneDnssecConfigDefaultKeySpecArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonExistence")
    def non_existence(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @non_existence.setter
    def non_existence(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedZoneDnssecConfigDefaultKeySpecArgsDict(TypedDict):
    algorithm: NotRequired[pulumi.Input[_builtins.str]]
    key_length: NotRequired[pulumi.Input[_builtins.int]]
    key_type: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedZoneDnssecConfigDefaultKeySpecArgs:
    def __init__(__self__, *, algorithm: Optional[pulumi.Input[_builtins.str]] = ..., key_length: Optional[pulumi.Input[_builtins.int]] = ..., key_type: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @algorithm.setter
    def algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_length.setter
    def key_length(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_type.setter
    def key_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedZoneForwardingConfigArgsDict(TypedDict):
    target_name_servers: pulumi.Input[Sequence[pulumi.Input[ManagedZoneForwardingConfigTargetNameServerArgsDict]]]


@pulumi.input_type
class ManagedZoneForwardingConfigArgs:
    def __init__(__self__, *, target_name_servers: pulumi.Input[Sequence[pulumi.Input[ManagedZoneForwardingConfigTargetNameServerArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> pulumi.Input[Sequence[pulumi.Input[ManagedZoneForwardingConfigTargetNameServerArgs]]]:
        
        ...
    
    @target_name_servers.setter
    def target_name_servers(self, value: pulumi.Input[Sequence[pulumi.Input[ManagedZoneForwardingConfigTargetNameServerArgs]]]): # -> None:
        ...
    


class ManagedZoneForwardingConfigTargetNameServerArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_path: NotRequired[pulumi.Input[_builtins.str]]
    ipv4_address: NotRequired[pulumi.Input[_builtins.str]]
    ipv6_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagedZoneForwardingConfigTargetNameServerArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., forwarding_path: Optional[pulumi.Input[_builtins.str]] = ..., ipv4_address: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forwarding_path.setter
    def forwarding_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedZonePeeringConfigArgsDict(TypedDict):
    target_network: pulumi.Input[ManagedZonePeeringConfigTargetNetworkArgsDict]


@pulumi.input_type
class ManagedZonePeeringConfigArgs:
    def __init__(__self__, *, target_network: pulumi.Input[ManagedZonePeeringConfigTargetNetworkArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> pulumi.Input[ManagedZonePeeringConfigTargetNetworkArgs]:
        
        ...
    
    @target_network.setter
    def target_network(self, value: pulumi.Input[ManagedZonePeeringConfigTargetNetworkArgs]): # -> None:
        ...
    


class ManagedZonePeeringConfigTargetNetworkArgsDict(TypedDict):
    network_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagedZonePeeringConfigTargetNetworkArgs:
    def __init__(__self__, *, network_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedZonePrivateVisibilityConfigArgsDict(TypedDict):
    gke_clusters: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigGkeClusterArgsDict]]]]
    networks: NotRequired[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigNetworkArgsDict]]]]


@pulumi.input_type
class ManagedZonePrivateVisibilityConfigArgs:
    def __init__(__self__, *, gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigGkeClusterArgs]]]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigNetworkArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigGkeClusterArgs]]]]:
        
        ...
    
    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigGkeClusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ManagedZonePrivateVisibilityConfigNetworkArgs]]]]): # -> None:
        ...
    


class ManagedZonePrivateVisibilityConfigGkeClusterArgsDict(TypedDict):
    gke_cluster_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagedZonePrivateVisibilityConfigGkeClusterArgs:
    def __init__(__self__, *, gke_cluster_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterName")
    def gke_cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gke_cluster_name.setter
    def gke_cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedZonePrivateVisibilityConfigNetworkArgsDict(TypedDict):
    network_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagedZonePrivateVisibilityConfigNetworkArgs:
    def __init__(__self__, *, network_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagedZoneServiceDirectoryConfigArgsDict(TypedDict):
    namespace: pulumi.Input[ManagedZoneServiceDirectoryConfigNamespaceArgsDict]


@pulumi.input_type
class ManagedZoneServiceDirectoryConfigArgs:
    def __init__(__self__, *, namespace: pulumi.Input[ManagedZoneServiceDirectoryConfigNamespaceArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[ManagedZoneServiceDirectoryConfigNamespaceArgs]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: pulumi.Input[ManagedZoneServiceDirectoryConfigNamespaceArgs]): # -> None:
        ...
    


class ManagedZoneServiceDirectoryConfigNamespaceArgsDict(TypedDict):
    namespace_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagedZoneServiceDirectoryConfigNamespaceArgs:
    def __init__(__self__, *, namespace_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceUrl")
    def namespace_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_url.setter
    def namespace_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class PolicyAlternativeNameServerConfigArgsDict(TypedDict):
    target_name_servers: pulumi.Input[Sequence[pulumi.Input[PolicyAlternativeNameServerConfigTargetNameServerArgsDict]]]


@pulumi.input_type
class PolicyAlternativeNameServerConfigArgs:
    def __init__(__self__, *, target_name_servers: pulumi.Input[Sequence[pulumi.Input[PolicyAlternativeNameServerConfigTargetNameServerArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> pulumi.Input[Sequence[pulumi.Input[PolicyAlternativeNameServerConfigTargetNameServerArgs]]]:
        
        ...
    
    @target_name_servers.setter
    def target_name_servers(self, value: pulumi.Input[Sequence[pulumi.Input[PolicyAlternativeNameServerConfigTargetNameServerArgs]]]): # -> None:
        ...
    


class PolicyAlternativeNameServerConfigTargetNameServerArgsDict(TypedDict):
    ipv4_address: pulumi.Input[_builtins.str]
    forwarding_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class PolicyAlternativeNameServerConfigTargetNameServerArgs:
    def __init__(__self__, *, ipv4_address: pulumi.Input[_builtins.str], forwarding_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ipv4_address.setter
    def ipv4_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @forwarding_path.setter
    def forwarding_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PolicyDns64ConfigArgsDict(TypedDict):
    scope: pulumi.Input[PolicyDns64ConfigScopeArgsDict]


@pulumi.input_type
class PolicyDns64ConfigArgs:
    def __init__(__self__, *, scope: pulumi.Input[PolicyDns64ConfigScopeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[PolicyDns64ConfigScopeArgs]:
        
        ...
    
    @scope.setter
    def scope(self, value: pulumi.Input[PolicyDns64ConfigScopeArgs]): # -> None:
        ...
    


class PolicyDns64ConfigScopeArgsDict(TypedDict):
    all_queries: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class PolicyDns64ConfigScopeArgs:
    def __init__(__self__, *, all_queries: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueries")
    def all_queries(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @all_queries.setter
    def all_queries(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class PolicyNetworkArgsDict(TypedDict):
    network_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class PolicyNetworkArgs:
    def __init__(__self__, *, network_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RecordSetRoutingPolicyArgsDict(TypedDict):
    enable_geo_fencing: NotRequired[pulumi.Input[_builtins.bool]]
    geos: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoArgsDict]]]]
    health_check: NotRequired[pulumi.Input[_builtins.str]]
    primary_backup: NotRequired[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupArgsDict]]
    wrrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrArgsDict]]]]


@pulumi.input_type
class RecordSetRoutingPolicyArgs:
    def __init__(__self__, *, enable_geo_fencing: Optional[pulumi.Input[_builtins.bool]] = ..., geos: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoArgs]]]] = ..., health_check: Optional[pulumi.Input[_builtins.str]] = ..., primary_backup: Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupArgs]] = ..., wrrs: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGeoFencing")
    def enable_geo_fencing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_geo_fencing.setter
    def enable_geo_fencing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def geos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoArgs]]]]:
        
        ...
    
    @geos.setter
    def geos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryBackup")
    def primary_backup(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupArgs]]:
        
        ...
    
    @primary_backup.setter
    def primary_backup(self, value: Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def wrrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrArgs]]]]:
        
        ...
    
    @wrrs.setter
    def wrrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrArgs]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyGeoArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    health_checked_targets: NotRequired[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsArgsDict]]
    rrdatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RecordSetRoutingPolicyGeoArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], health_checked_targets: Optional[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsArgs]] = ..., rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsArgs]]:
        
        ...
    
    @health_checked_targets.setter
    def health_checked_targets(self, value: Optional[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @rrdatas.setter
    def rrdatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyGeoHealthCheckedTargetsArgsDict(TypedDict):
    external_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    internal_load_balancers: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgsDict]]]]


@pulumi.input_type
class RecordSetRoutingPolicyGeoHealthCheckedTargetsArgs:
    def __init__(__self__, *, external_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., internal_load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_endpoints.setter
    def external_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]]:
        
        ...
    
    @internal_load_balancers.setter
    def internal_load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]
    ip_protocol: pulumi.Input[_builtins.str]
    network_url: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.str]
    project: pulumi.Input[_builtins.str]
    load_balancer_type: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancerArgs:
    def __init__(__self__, *, ip_address: pulumi.Input[_builtins.str], ip_protocol: pulumi.Input[_builtins.str], network_url: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.str], project: pulumi.Input[_builtins.str], load_balancer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupArgsDict(TypedDict):
    backup_geos: pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoArgsDict]]]
    primary: pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryArgsDict]
    enable_geo_fencing_for_backups: NotRequired[pulumi.Input[_builtins.bool]]
    trickle_ratio: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupArgs:
    def __init__(__self__, *, backup_geos: pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoArgs]]], primary: pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryArgs], enable_geo_fencing_for_backups: Optional[pulumi.Input[_builtins.bool]] = ..., trickle_ratio: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupGeos")
    def backup_geos(self) -> pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoArgs]]]:
        
        ...
    
    @backup_geos.setter
    def backup_geos(self, value: pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryArgs]:
        
        ...
    
    @primary.setter
    def primary(self, value: pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGeoFencingForBackups")
    def enable_geo_fencing_for_backups(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_geo_fencing_for_backups.setter
    def enable_geo_fencing_for_backups(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trickleRatio")
    def trickle_ratio(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @trickle_ratio.setter
    def trickle_ratio(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupBackupGeoArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    health_checked_targets: NotRequired[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgsDict]]
    rrdatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeoArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], health_checked_targets: Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgs]] = ..., rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgs]]:
        
        ...
    
    @health_checked_targets.setter
    def health_checked_targets(self, value: Optional[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @rrdatas.setter
    def rrdatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgsDict(TypedDict):
    external_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    internal_load_balancers: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgsDict]]]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsArgs:
    def __init__(__self__, *, external_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., internal_load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_endpoints.setter
    def external_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]]:
        
        ...
    
    @internal_load_balancers.setter
    def internal_load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgs]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]
    ip_protocol: pulumi.Input[_builtins.str]
    network_url: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.str]
    project: pulumi.Input[_builtins.str]
    load_balancer_type: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancerArgs:
    def __init__(__self__, *, ip_address: pulumi.Input[_builtins.str], ip_protocol: pulumi.Input[_builtins.str], network_url: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.str], project: pulumi.Input[_builtins.str], load_balancer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupPrimaryArgsDict(TypedDict):
    external_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    internal_load_balancers: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgsDict]]]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupPrimaryArgs:
    def __init__(__self__, *, external_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., internal_load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_endpoints.setter
    def external_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgs]]]]:
        
        ...
    
    @internal_load_balancers.setter
    def internal_load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgs]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]
    ip_protocol: pulumi.Input[_builtins.str]
    network_url: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.str]
    project: pulumi.Input[_builtins.str]
    load_balancer_type: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancerArgs:
    def __init__(__self__, *, ip_address: pulumi.Input[_builtins.str], ip_protocol: pulumi.Input[_builtins.str], network_url: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.str], project: pulumi.Input[_builtins.str], load_balancer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RecordSetRoutingPolicyWrrArgsDict(TypedDict):
    weight: pulumi.Input[_builtins.float]
    health_checked_targets: NotRequired[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsArgsDict]]
    rrdatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RecordSetRoutingPolicyWrrArgs:
    def __init__(__self__, *, weight: pulumi.Input[_builtins.float], health_checked_targets: Optional[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsArgs]] = ..., rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsArgs]]:
        
        ...
    
    @health_checked_targets.setter
    def health_checked_targets(self, value: Optional[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @rrdatas.setter
    def rrdatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyWrrHealthCheckedTargetsArgsDict(TypedDict):
    external_endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    internal_load_balancers: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgsDict]]]]


@pulumi.input_type
class RecordSetRoutingPolicyWrrHealthCheckedTargetsArgs:
    def __init__(__self__, *, external_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., internal_load_balancers: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @external_endpoints.setter
    def external_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgs]]]]:
        
        ...
    
    @internal_load_balancers.setter
    def internal_load_balancers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgs]]]]): # -> None:
        ...
    


class RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgsDict(TypedDict):
    ip_address: pulumi.Input[_builtins.str]
    ip_protocol: pulumi.Input[_builtins.str]
    network_url: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.str]
    project: pulumi.Input[_builtins.str]
    load_balancer_type: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancerArgs:
    def __init__(__self__, *, ip_address: pulumi.Input[_builtins.str], ip_protocol: pulumi.Input[_builtins.str], network_url: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.str], project: pulumi.Input[_builtins.str], load_balancer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @load_balancer_type.setter
    def load_balancer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResponsePolicyGkeClusterArgsDict(TypedDict):
    gke_cluster_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResponsePolicyGkeClusterArgs:
    def __init__(__self__, *, gke_cluster_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterName")
    def gke_cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gke_cluster_name.setter
    def gke_cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponsePolicyNetworkArgsDict(TypedDict):
    network_url: pulumi.Input[_builtins.str]


@pulumi.input_type
class ResponsePolicyNetworkArgs:
    def __init__(__self__, *, network_url: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_url.setter
    def network_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ResponsePolicyRuleLocalDataArgsDict(TypedDict):
    local_datas: pulumi.Input[Sequence[pulumi.Input[ResponsePolicyRuleLocalDataLocalDataArgsDict]]]


@pulumi.input_type
class ResponsePolicyRuleLocalDataArgs:
    def __init__(__self__, *, local_datas: pulumi.Input[Sequence[pulumi.Input[ResponsePolicyRuleLocalDataLocalDataArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDatas")
    def local_datas(self) -> pulumi.Input[Sequence[pulumi.Input[ResponsePolicyRuleLocalDataLocalDataArgs]]]:
        
        ...
    
    @local_datas.setter
    def local_datas(self, value: pulumi.Input[Sequence[pulumi.Input[ResponsePolicyRuleLocalDataLocalDataArgs]]]): # -> None:
        ...
    


class ResponsePolicyRuleLocalDataLocalDataArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    rrdatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ttl: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ResponsePolicyRuleLocalDataLocalDataArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], rrdatas: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ttl: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @rrdatas.setter
    def rrdatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


