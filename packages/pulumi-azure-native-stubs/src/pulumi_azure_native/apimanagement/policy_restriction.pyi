

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyRestrictionArgs', 'PolicyRestriction']
@pulumi.input_type
class PolicyRestrictionArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], policy_restriction_id: Optional[pulumi.Input[_builtins.str]] = ..., require_base: Optional[pulumi.Input[Union[_builtins.str, PolicyRestrictionRequireBase]]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRestrictionId")
    def policy_restriction_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_restriction_id.setter
    def policy_restriction_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireBase")
    def require_base(self) -> Optional[pulumi.Input[Union[_builtins.str, PolicyRestrictionRequireBase]]]:
        
        ...
    
    @require_base.setter
    def require_base(self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyRestrictionRequireBase]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apimanagement:PolicyRestriction")
class PolicyRestriction(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., policy_restriction_id: Optional[pulumi.Input[_builtins.str]] = ..., require_base: Optional[pulumi.Input[Union[_builtins.str, PolicyRestrictionRequireBase]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyRestrictionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> PolicyRestriction:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requireBase")
    def require_base(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


