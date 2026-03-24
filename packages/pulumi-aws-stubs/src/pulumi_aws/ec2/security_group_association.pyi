

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityGroupAssociationArgs', 'SecurityGroupAssociation']
@pulumi.input_type
class SecurityGroupAssociationArgs:
    def __init__(__self__, *, security_group_id: pulumi.Input[_builtins.str], vpc_endpoint_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., replace_default_association: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDefaultAssociation")
    def replace_default_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_default_association.setter
    def replace_default_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _SecurityGroupAssociationState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., replace_default_association: Optional[pulumi.Input[_builtins.bool]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDefaultAssociation")
    def replace_default_association(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @replace_default_association.setter
    def replace_default_association(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SecurityGroupAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_default_association: Optional[pulumi.Input[_builtins.bool]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityGroupAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replace_default_association: Optional[pulumi.Input[_builtins.bool]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...) -> SecurityGroupAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDefaultAssociation")
    def replace_default_association(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


