

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
__all__ = ['GroupQuotaArgs', 'GroupQuota']
@pulumi.input_type
class GroupQuotaArgs:
    def __init__(__self__, *, management_group_id: pulumi.Input[_builtins.str], group_quota_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[GroupQuotasEntityPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupQuotaName")
    def group_quota_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_quota_name.setter
    def group_quota_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[GroupQuotasEntityPropertiesArgs]]:
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[GroupQuotasEntityPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:quota:GroupQuota")
class GroupQuota(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., group_quota_name: Optional[pulumi.Input[_builtins.str]] = ..., management_group_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[GroupQuotasEntityPropertiesArgs, GroupQuotasEntityPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GroupQuotaArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> GroupQuota:
        
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
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.GroupQuotasEntityResponseProperties]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


