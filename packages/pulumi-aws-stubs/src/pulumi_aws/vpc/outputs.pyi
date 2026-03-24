

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EndpointServicePrivateDnsVerificationTimeouts', 'RouteServerEndpointTimeouts', 'RouteServerPeerBgpOptions', 'RouteServerPeerTimeouts', 'RouteServerPropagationTimeouts', 'RouteServerTimeouts', 'RouteServerVpcAssociationTimeouts', 'SecurityGroupVpcAssociationTimeouts', 'GetEndpointAssociationsAssociationResult', 'GetEndpointAssociationsAssociationDnsEntryResult', ..., 'GetSecurityGroupRuleFilterResult', 'GetSecurityGroupRulesFilterResult']
@pulumi.output_type
class EndpointServicePrivateDnsVerificationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerEndpointTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerPeerBgpOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, peer_asn: _builtins.int, peer_liveness_detection: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peerLivenessDetection")
    def peer_liveness_detection(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerPeerTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerPropagationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RouteServerVpcAssociationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecurityGroupVpcAssociationTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetEndpointAssociationsAssociationResult(dict):
    def __init__(__self__, *, associated_resource_accessibility: _builtins.str, associated_resource_arn: _builtins.str, dns_entries: Sequence[outputs.GetEndpointAssociationsAssociationDnsEntryResult], id: _builtins.str, private_dns_entries: Sequence[outputs.GetEndpointAssociationsAssociationPrivateDnsEntryResult], resource_configuration_group_arn: _builtins.str, service_network_arn: _builtins.str, service_network_name: _builtins.str, tags: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResourceAccessibility")
    def associated_resource_accessibility(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedResourceArn")
    def associated_resource_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsEntries")
    def dns_entries(self) -> Sequence[outputs.GetEndpointAssociationsAssociationDnsEntryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateDnsEntries")
    def private_dns_entries(self) -> Sequence[outputs.GetEndpointAssociationsAssociationPrivateDnsEntryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationGroupArn")
    def resource_configuration_group_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkArn")
    def service_network_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkName")
    def service_network_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetEndpointAssociationsAssociationDnsEntryResult(dict):
    def __init__(__self__, *, dns_name: _builtins.str, hosted_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEndpointAssociationsAssociationPrivateDnsEntryResult(dict):
    def __init__(__self__, *, dns_name: _builtins.str, hosted_zone_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecurityGroupRuleFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSecurityGroupRulesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


