

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntityAnalyticsResult', 'AwaitableGetEntityAnalyticsResult', 'get_entity_analytics', 'get_entity_analytics_output']
@pulumi.output_type
class GetEntityAnalyticsResult:
    
    def __init__(__self__, azure_api_version=..., entity_providers=..., etag=..., id=..., kind=..., name=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityProviders")
    def entity_providers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEntityAnalyticsResult(GetEntityAnalyticsResult):
    def __await__(self): # -> Generator[Never, Any, GetEntityAnalyticsResult]:
        ...
    


def get_entity_analytics(resource_group_name: Optional[_builtins.str] = ..., settings_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntityAnalyticsResult:
    
    ...

def get_entity_analytics_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., settings_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntityAnalyticsResult]:
    
    ...

