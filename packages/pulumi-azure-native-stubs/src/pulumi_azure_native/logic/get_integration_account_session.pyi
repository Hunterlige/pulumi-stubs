

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIntegrationAccountSessionResult', 'AwaitableGetIntegrationAccountSessionResult', 'get_integration_account_session', 'get_integration_account_session_output']
@pulumi.output_type
class GetIntegrationAccountSessionResult:
    
    def __init__(__self__, azure_api_version=..., changed_time=..., content=..., created_time=..., id=..., location=..., name=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIntegrationAccountSessionResult(GetIntegrationAccountSessionResult):
    def __await__(self): # -> Generator[Never, Any, GetIntegrationAccountSessionResult]:
        ...
    


def get_integration_account_session(integration_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., session_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIntegrationAccountSessionResult:
    
    ...

def get_integration_account_session_output(integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., session_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIntegrationAccountSessionResult]:
    
    ...

