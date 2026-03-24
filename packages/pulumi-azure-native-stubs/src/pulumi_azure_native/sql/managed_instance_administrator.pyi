

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedInstanceAdministratorArgs', 'ManagedInstanceAdministrator']
@pulumi.input_type
class ManagedInstanceAdministratorArgs:
    def __init__(__self__, *, administrator_type: pulumi.Input[Union[_builtins.str, ManagedInstanceAdministratorType]], login: pulumi.Input[_builtins.str], managed_instance_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], sid: pulumi.Input[_builtins.str], administrator_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Input[Union[_builtins.str, ManagedInstanceAdministratorType]]:
        
        ...
    
    @administrator_type.setter
    def administrator_type(self, value: pulumi.Input[Union[_builtins.str, ManagedInstanceAdministratorType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @login.setter
    def login(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sid(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sid.setter
    def sid(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorName")
    def administrator_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @administrator_name.setter
    def administrator_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:ManagedInstanceAdministrator")
class ManagedInstanceAdministrator(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., administrator_name: Optional[pulumi.Input[_builtins.str]] = ..., administrator_type: Optional[pulumi.Input[Union[_builtins.str, ManagedInstanceAdministratorType]]] = ..., login: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sid: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedInstanceAdministratorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ManagedInstanceAdministrator:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


