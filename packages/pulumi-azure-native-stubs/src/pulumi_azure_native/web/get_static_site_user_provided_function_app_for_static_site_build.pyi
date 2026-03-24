

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult:
    
    def __init__(__self__, azure_api_version=..., created_on=..., function_app_region=..., function_app_resource_id=..., id=..., kind=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppRegion")
    def function_app_region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAppResourceId")
    def function_app_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult(GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult):
    def __await__(self): # -> Generator[Never, Any, GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult]:
        ...
    


def get_static_site_user_provided_function_app_for_static_site_build(environment_name: Optional[_builtins.str] = ..., function_app_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult:
    
    ...

def get_static_site_user_provided_function_app_for_static_site_build_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., function_app_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStaticSiteUserProvidedFunctionAppForStaticSiteBuildResult]:
    
    ...

