

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationGroupArgs', 'ApplicationGroup']
@pulumi.input_type
class ApplicationGroupArgs:
    def __init__(__self__, *, client_app_group_identifier: pulumi.Input[_builtins.str], namespace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], application_group_name: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., policies: Optional[pulumi.Input[Sequence[pulumi.Input[ThrottlingPolicyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAppGroupIdentifier")
    def client_app_group_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_app_group_identifier.setter
    def client_app_group_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationGroupName")
    def application_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_group_name.setter
    def application_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ThrottlingPolicyArgs]]]]:
        
        ...
    
    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ThrottlingPolicyArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:eventhub:ApplicationGroup")
class ApplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_group_name: Optional[pulumi.Input[_builtins.str]] = ..., client_app_group_identifier: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ThrottlingPolicyArgs, ThrottlingPolicyArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ApplicationGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ApplicationGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAppGroupIdentifier")
    def client_app_group_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence[outputs.ThrottlingPolicyResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


