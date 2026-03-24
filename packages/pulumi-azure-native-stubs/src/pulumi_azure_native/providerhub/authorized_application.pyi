

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizedApplicationArgs', 'AuthorizedApplication']
@pulumi.input_type
class AuthorizedApplicationArgs:
    def __init__(__self__, *, provider_namespace: pulumi.Input[_builtins.str], application_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[AuthorizedApplicationPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="providerNamespace")
    def provider_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @provider_namespace.setter
    def provider_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[AuthorizedApplicationPropertiesArgs]]:
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[AuthorizedApplicationPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:providerhub:AuthorizedApplication")
class AuthorizedApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[AuthorizedApplicationPropertiesArgs, AuthorizedApplicationPropertiesArgsDict]]] = ..., provider_namespace: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AuthorizedApplicationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> AuthorizedApplication:
        
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
    def properties(self) -> pulumi.Output[outputs.AuthorizedApplicationPropertiesResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


