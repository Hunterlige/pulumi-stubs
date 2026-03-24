

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DnsManagedZoneIamBindingCondition', 'DnsManagedZoneIamMemberCondition', 'ManagedZoneCloudLoggingConfig', 'ManagedZoneDnssecConfig', 'ManagedZoneDnssecConfigDefaultKeySpec', 'ManagedZoneForwardingConfig', 'ManagedZoneForwardingConfigTargetNameServer', 'ManagedZonePeeringConfig', 'ManagedZonePeeringConfigTargetNetwork', 'ManagedZonePrivateVisibilityConfig', 'ManagedZonePrivateVisibilityConfigGkeCluster', 'ManagedZonePrivateVisibilityConfigNetwork', 'ManagedZoneServiceDirectoryConfig', 'ManagedZoneServiceDirectoryConfigNamespace', 'PolicyAlternativeNameServerConfig', 'PolicyAlternativeNameServerConfigTargetNameServer', 'PolicyDns64Config', 'PolicyDns64ConfigScope', 'PolicyNetwork', 'RecordSetRoutingPolicy', 'RecordSetRoutingPolicyGeo', 'RecordSetRoutingPolicyGeoHealthCheckedTargets', ..., 'RecordSetRoutingPolicyPrimaryBackup', 'RecordSetRoutingPolicyPrimaryBackupBackupGeo', ..., ..., 'RecordSetRoutingPolicyPrimaryBackupPrimary', ..., 'RecordSetRoutingPolicyWrr', 'RecordSetRoutingPolicyWrrHealthCheckedTargets', ..., 'ResponsePolicyGkeCluster', 'ResponsePolicyNetwork', 'ResponsePolicyRuleLocalData', 'ResponsePolicyRuleLocalDataLocalData', 'GetKeysKeySigningKeyResult', 'GetKeysKeySigningKeyDigestResult', 'GetKeysZoneSigningKeyResult', 'GetKeysZoneSigningKeyDigestResult', 'GetManagedZonesManagedZoneResult']
@pulumi.output_type
class DnsManagedZoneIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class DnsManagedZoneIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class ManagedZoneCloudLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_logging: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class ManagedZoneDnssecConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_key_specs: Optional[Sequence[outputs.ManagedZoneDnssecConfigDefaultKeySpec]] = ..., kind: Optional[_builtins.str] = ..., non_existence: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultKeySpecs")
    def default_key_specs(self) -> Optional[Sequence[outputs.ManagedZoneDnssecConfigDefaultKeySpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonExistence")
    def non_existence(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedZoneDnssecConfigDefaultKeySpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, algorithm: Optional[_builtins.str] = ..., key_length: Optional[_builtins.int] = ..., key_type: Optional[_builtins.str] = ..., kind: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyType")
    def key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedZoneForwardingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_name_servers: Sequence[outputs.ManagedZoneForwardingConfigTargetNameServer]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> Sequence[outputs.ManagedZoneForwardingConfigTargetNameServer]:
        
        ...
    


@pulumi.output_type
class ManagedZoneForwardingConfigTargetNameServer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., forwarding_path: Optional[_builtins.str] = ..., ipv4_address: Optional[_builtins.str] = ..., ipv6_address: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagedZonePeeringConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_network: outputs.ManagedZonePeeringConfigTargetNetwork) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNetwork")
    def target_network(self) -> outputs.ManagedZonePeeringConfigTargetNetwork:
        
        ...
    


@pulumi.output_type
class ManagedZonePeeringConfigTargetNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedZonePrivateVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gke_clusters: Optional[Sequence[outputs.ManagedZonePrivateVisibilityConfigGkeCluster]] = ..., networks: Optional[Sequence[outputs.ManagedZonePrivateVisibilityConfigNetwork]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[Sequence[outputs.ManagedZonePrivateVisibilityConfigGkeCluster]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Optional[Sequence[outputs.ManagedZonePrivateVisibilityConfigNetwork]]:
        
        ...
    


@pulumi.output_type
class ManagedZonePrivateVisibilityConfigGkeCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gke_cluster_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterName")
    def gke_cluster_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedZonePrivateVisibilityConfigNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ManagedZoneServiceDirectoryConfig(dict):
    def __init__(__self__, *, namespace: outputs.ManagedZoneServiceDirectoryConfigNamespace) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> outputs.ManagedZoneServiceDirectoryConfigNamespace:
        
        ...
    


@pulumi.output_type
class ManagedZoneServiceDirectoryConfigNamespace(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespace_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceUrl")
    def namespace_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyAlternativeNameServerConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_name_servers: Sequence[outputs.PolicyAlternativeNameServerConfigTargetNameServer]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNameServers")
    def target_name_servers(self) -> Sequence[outputs.PolicyAlternativeNameServerConfigTargetNameServer]:
        
        ...
    


@pulumi.output_type
class PolicyAlternativeNameServerConfigTargetNameServer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ipv4_address: _builtins.str, forwarding_path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingPath")
    def forwarding_path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyDns64Config(dict):
    def __init__(__self__, *, scope: outputs.PolicyDns64ConfigScope) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> outputs.PolicyDns64ConfigScope:
        
        ...
    


@pulumi.output_type
class PolicyDns64ConfigScope(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_queries: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueries")
    def all_queries(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PolicyNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_geo_fencing: Optional[_builtins.bool] = ..., geos: Optional[Sequence[outputs.RecordSetRoutingPolicyGeo]] = ..., health_check: Optional[_builtins.str] = ..., primary_backup: Optional[outputs.RecordSetRoutingPolicyPrimaryBackup] = ..., wrrs: Optional[Sequence[outputs.RecordSetRoutingPolicyWrr]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGeoFencing")
    def enable_geo_fencing(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def geos(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyGeo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryBackup")
    def primary_backup(self) -> Optional[outputs.RecordSetRoutingPolicyPrimaryBackup]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def wrrs(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyWrr]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyGeo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, health_checked_targets: Optional[outputs.RecordSetRoutingPolicyGeoHealthCheckedTargets] = ..., rrdatas: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[outputs.RecordSetRoutingPolicyGeoHealthCheckedTargets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyGeoHealthCheckedTargets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_endpoints: Optional[Sequence[_builtins.str]] = ..., internal_load_balancers: Optional[Sequence[outputs.RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancer]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancer]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyGeoHealthCheckedTargetsInternalLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: _builtins.str, ip_protocol: _builtins.str, network_url: _builtins.str, port: _builtins.str, project: _builtins.str, load_balancer_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, backup_geos: Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeo], primary: outputs.RecordSetRoutingPolicyPrimaryBackupPrimary, enable_geo_fencing_for_backups: Optional[_builtins.bool] = ..., trickle_ratio: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupGeos")
    def backup_geos(self) -> Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primary(self) -> outputs.RecordSetRoutingPolicyPrimaryBackupPrimary:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGeoFencingForBackups")
    def enable_geo_fencing_for_backups(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trickleRatio")
    def trickle_ratio(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, health_checked_targets: Optional[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargets] = ..., rrdatas: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_endpoints: Optional[Sequence[_builtins.str]] = ..., internal_load_balancers: Optional[Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancer]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancer]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackupBackupGeoHealthCheckedTargetsInternalLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: _builtins.str, ip_protocol: _builtins.str, network_url: _builtins.str, port: _builtins.str, project: _builtins.str, load_balancer_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackupPrimary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_endpoints: Optional[Sequence[_builtins.str]] = ..., internal_load_balancers: Optional[Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancer]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancer]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyPrimaryBackupPrimaryInternalLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: _builtins.str, ip_protocol: _builtins.str, network_url: _builtins.str, port: _builtins.str, project: _builtins.str, load_balancer_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyWrr(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, weight: _builtins.float, health_checked_targets: Optional[outputs.RecordSetRoutingPolicyWrrHealthCheckedTargets] = ..., rrdatas: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheckedTargets")
    def health_checked_targets(self) -> Optional[outputs.RecordSetRoutingPolicyWrrHealthCheckedTargets]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyWrrHealthCheckedTargets(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, external_endpoints: Optional[Sequence[_builtins.str]] = ..., internal_load_balancers: Optional[Sequence[outputs.RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancer]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalEndpoints")
    def external_endpoints(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="internalLoadBalancers")
    def internal_load_balancers(self) -> Optional[Sequence[outputs.RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancer]]:
        
        ...
    


@pulumi.output_type
class RecordSetRoutingPolicyWrrHealthCheckedTargetsInternalLoadBalancer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ip_address: _builtins.str, ip_protocol: _builtins.str, network_url: _builtins.str, port: _builtins.str, project: _builtins.str, load_balancer_type: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerType")
    def load_balancer_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ResponsePolicyGkeCluster(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gke_cluster_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusterName")
    def gke_cluster_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResponsePolicyNetwork(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, network_url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkUrl")
    def network_url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ResponsePolicyRuleLocalData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, local_datas: Sequence[outputs.ResponsePolicyRuleLocalDataLocalData]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDatas")
    def local_datas(self) -> Sequence[outputs.ResponsePolicyRuleLocalDataLocalData]:
        
        ...
    


@pulumi.output_type
class ResponsePolicyRuleLocalDataLocalData(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str, rrdatas: Optional[Sequence[_builtins.str]] = ..., ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rrdatas(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class GetKeysKeySigningKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, creation_time: _builtins.str, description: _builtins.str, digests: Sequence[outputs.GetKeysKeySigningKeyDigestResult], ds_record: _builtins.str, id: _builtins.str, is_active: _builtins.bool, key_length: _builtins.int, key_tag: _builtins.int, public_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digests(self) -> Sequence[outputs.GetKeysKeySigningKeyDigestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dsRecord")
    def ds_record(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetKeysKeySigningKeyDigestResult(dict):
    def __init__(__self__, *, digest: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetKeysZoneSigningKeyResult(dict):
    def __init__(__self__, *, algorithm: _builtins.str, creation_time: _builtins.str, description: _builtins.str, digests: Sequence[outputs.GetKeysZoneSigningKeyDigestResult], id: _builtins.str, is_active: _builtins.bool, key_length: _builtins.int, key_tag: _builtins.int, public_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digests(self) -> Sequence[outputs.GetKeysZoneSigningKeyDigestResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyLength")
    def key_length(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetKeysZoneSigningKeyDigestResult(dict):
    def __init__(__self__, *, digest: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digest(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetManagedZonesManagedZoneResult(dict):
    def __init__(__self__, *, description: _builtins.str, dns_name: _builtins.str, id: _builtins.str, managed_zone_id: _builtins.str, name_servers: Sequence[_builtins.str], visibility: _builtins.str, name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedZoneId")
    def managed_zone_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        
        ...
    


