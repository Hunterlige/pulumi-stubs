

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityConnectorApplicationResult', 'AwaitableGetSecurityConnectorApplicationResult', 'get_security_connector_application', 'get_security_connector_application_output']
@pulumi.output_type
class GetSecurityConnectorApplicationResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., name=..., source_resource_type=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecurityConnectorApplicationResult(GetSecurityConnectorApplicationResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityConnectorApplicationResult]:
        ...
    


def get_security_connector_application(application_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., security_connector_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityConnectorApplicationResult:
    
    ...

def get_security_connector_application_output(application_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityConnectorApplicationResult]:
    
    ...

