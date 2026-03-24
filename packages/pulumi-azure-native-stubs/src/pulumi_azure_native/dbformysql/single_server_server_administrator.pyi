

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SingleServerServerAdministratorArgs', 'SingleServerServerAdministrator']
@pulumi.input_type
class SingleServerServerAdministratorArgs:
    def __init__(__self__, *, administrator_type: pulumi.Input[Union[_builtins.str, AdministratorType]], login: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], sid: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Input[Union[_builtins.str, AdministratorType]]:
        
        ...
    
    @administrator_type.setter
    def administrator_type(self, value: pulumi.Input[Union[_builtins.str, AdministratorType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @login.setter
    def login(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sid(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sid.setter
    def sid(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.type_token(...)
class SingleServerServerAdministrator(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., administrator_type: Optional[pulumi.Input[Union[_builtins.str, AdministratorType]]] = ..., login: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., sid: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SingleServerServerAdministratorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SingleServerServerAdministrator:
        
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
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


