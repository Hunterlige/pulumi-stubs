

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionArgs', 'Connection']
@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *, network: pulumi.Input[_builtins.str], reserved_peering_ranges: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], service: pulumi.Input[_builtins.str], deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., update_on_creation_fail: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedPeeringRanges")
    def reserved_peering_ranges(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @reserved_peering_ranges.setter
    def reserved_peering_ranges(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateOnCreationFail")
    def update_on_creation_fail(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @update_on_creation_fail.setter
    def update_on_creation_fail(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *, deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., peering: Optional[pulumi.Input[_builtins.str]] = ..., reserved_peering_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., update_on_creation_fail: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def peering(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering.setter
    def peering(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedPeeringRanges")
    def reserved_peering_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reserved_peering_ranges.setter
    def reserved_peering_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateOnCreationFail")
    def update_on_creation_fail(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @update_on_creation_fail.setter
    def update_on_creation_fail(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("gcp:servicenetworking/connection:Connection")
class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., reserved_peering_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., update_on_creation_fail: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., peering: Optional[pulumi.Input[_builtins.str]] = ..., reserved_peering_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., update_on_creation_fail: Optional[pulumi.Input[_builtins.bool]] = ...) -> Connection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def peering(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservedPeeringRanges")
    def reserved_peering_ranges(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateOnCreationFail")
    def update_on_creation_fail(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


