

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GatewayDetailsResponse', 'IPv4FirewallRuleResponse', 'IPv4FirewallSettingsResponse', 'ResourceSkuResponse', 'ServerAdministratorsResponse']
@pulumi.output_type
class GatewayDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dmts_cluster_uri: _builtins.str, gateway_object_id: _builtins.str, gateway_resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dmtsClusterUri")
    def dmts_cluster_uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayObjectId")
    def gateway_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayResourceId")
    def gateway_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IPv4FirewallRuleResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, firewall_rule_name: Optional[_builtins.str] = ..., range_end: Optional[_builtins.str] = ..., range_start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRuleName")
    def firewall_rule_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeEnd")
    def range_end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rangeStart")
    def range_start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IPv4FirewallSettingsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_power_bi_service: Optional[_builtins.bool] = ..., firewall_rules: Optional[Sequence[outputs.IPv4FirewallRuleResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePowerBIService")
    def enable_power_bi_service(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[Sequence[outputs.IPv4FirewallRuleResponse]]:
        
        ...
    


@pulumi.output_type
class ResourceSkuResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, capacity: Optional[_builtins.int] = ..., tier: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerAdministratorsResponse(dict):
    
    def __init__(__self__, *, members: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


