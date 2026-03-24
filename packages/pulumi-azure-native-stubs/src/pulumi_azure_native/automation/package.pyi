

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PackageArgs', 'Package']
@pulumi.input_type
class PackageArgs:
    def __init__(__self__, *, automation_account_name: pulumi.Input[_builtins.str], content_link: pulumi.Input[ContentLinkArgs], resource_group_name: pulumi.Input[_builtins.str], runtime_environment_name: pulumi.Input[_builtins.str], all_of: Optional[pulumi.Input[TrackedResourceArgs]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Input[ContentLinkArgs]:
        
        ...
    
    @content_link.setter
    def content_link(self, value: pulumi.Input[ContentLinkArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeEnvironmentName")
    def runtime_environment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime_environment_name.setter
    def runtime_environment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[pulumi.Input[TrackedResourceArgs]]:
        
        ...
    
    @all_of.setter
    def all_of(self, value: Optional[pulumi.Input[TrackedResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_name.setter
    def package_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:automation:Package")
class Package(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., all_of: Optional[pulumi.Input[Union[TrackedResourceArgs, TrackedResourceArgsDict]]] = ..., automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., content_link: Optional[pulumi.Input[Union[ContentLinkArgs, ContentLinkArgsDict]]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., runtime_environment_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PackageArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Package:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allOf")
    def all_of(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Output[Optional[outputs.ContentLinkResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def error(self) -> pulumi.Output[Optional[outputs.PackageErrorInfoResponse]]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


