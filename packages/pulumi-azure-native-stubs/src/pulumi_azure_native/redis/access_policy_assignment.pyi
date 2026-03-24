

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPolicyAssignmentArgs', 'AccessPolicyAssignment']
@pulumi.input_type
class AccessPolicyAssignmentArgs:
    def __init__(__self__, *, access_policy_name: pulumi.Input[_builtins.str], cache_name: pulumi.Input[_builtins.str], object_id: pulumi.Input[_builtins.str], object_id_alias: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], access_policy_assignment_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_policy_name.setter
    def access_policy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheName")
    def cache_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cache_name.setter
    def cache_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_id.setter
    def object_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectIdAlias")
    def object_id_alias(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @object_id_alias.setter
    def object_id_alias(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyAssignmentName")
    def access_policy_assignment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_policy_assignment_name.setter
    def access_policy_assignment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:redis:AccessPolicyAssignment")
class AccessPolicyAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_policy_assignment_name: Optional[pulumi.Input[_builtins.str]] = ..., access_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., cache_name: Optional[pulumi.Input[_builtins.str]] = ..., object_id: Optional[pulumi.Input[_builtins.str]] = ..., object_id_alias: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessPolicyAssignmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AccessPolicyAssignment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectIdAlias")
    def object_id_alias(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


