

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PrefixListAssociationArgs', 'PrefixListAssociation']
@pulumi.input_type
class PrefixListAssociationArgs:
    def __init__(__self__, *, core_network_id: pulumi.Input[_builtins.str], prefix_list_alias: pulumi.Input[_builtins.str], prefix_list_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListAlias")
    def prefix_list_alias(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix_list_alias.setter
    def prefix_list_alias(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListArn")
    def prefix_list_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @prefix_list_arn.setter
    def prefix_list_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _PrefixListAssociationState:
    def __init__(__self__, *, core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_alias: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @core_network_id.setter
    def core_network_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListAlias")
    def prefix_list_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_list_alias.setter
    def prefix_list_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListArn")
    def prefix_list_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prefix_list_arn.setter
    def prefix_list_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class PrefixListAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_alias: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PrefixListAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., core_network_id: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_alias: Optional[pulumi.Input[_builtins.str]] = ..., prefix_list_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> PrefixListAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListAlias")
    def prefix_list_alias(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixListArn")
    def prefix_list_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


