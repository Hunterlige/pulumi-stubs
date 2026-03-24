

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkInterfacePermissionArgs', 'NetworkInterfacePermission']
@pulumi.input_type
class NetworkInterfacePermissionArgs:
    def __init__(__self__, *, aws_account_id: pulumi.Input[_builtins.str], network_interface_id: pulumi.Input[_builtins.str], permission: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkInterfacePermissionState:
    def __init__(__self__, *, aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_permission_id: Optional[pulumi.Input[_builtins.str]] = ..., permission: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfacePermissionId")
    def network_interface_permission_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_permission_id.setter
    def network_interface_permission_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[NetworkInterfacePermissionTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class NetworkInterfacePermission(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., permission: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[NetworkInterfacePermissionTimeoutsArgs, NetworkInterfacePermissionTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkInterfacePermissionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_permission_id: Optional[pulumi.Input[_builtins.str]] = ..., permission: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[NetworkInterfacePermissionTimeoutsArgs, NetworkInterfacePermissionTimeoutsArgsDict]]] = ...) -> NetworkInterfacePermission:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfacePermissionId")
    def network_interface_permission_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.NetworkInterfacePermissionTimeouts]]:
        ...
    


