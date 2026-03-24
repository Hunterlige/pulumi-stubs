

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ...]
@pulumi.input_type
class StaticSiteUserProvidedFunctionAppForStaticSiteBuildArgs:
    def __init__(__self__, *, environment_name: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], function_app_name: Optional[pulumi.Input[_builtins.str]] = ..., function_app_region: Optional[pulumi.Input[_builtins.str]] = ..., function_app_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., is_forced: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppName")
    def function_app_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_app_name.setter
    def function_app_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_app_region.setter
    def function_app_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_app_resource_id.setter
    def function_app_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isForced")
    def is_forced(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_forced.setter
    def is_forced(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class StaticSiteUserProvidedFunctionAppForStaticSiteBuild(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., function_app_name: Optional[pulumi.Input[_builtins.str]] = ..., function_app_region: Optional[pulumi.Input[_builtins.str]] = ..., function_app_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., is_forced: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StaticSiteUserProvidedFunctionAppForStaticSiteBuildArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> StaticSiteUserProvidedFunctionAppForStaticSiteBuild:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


