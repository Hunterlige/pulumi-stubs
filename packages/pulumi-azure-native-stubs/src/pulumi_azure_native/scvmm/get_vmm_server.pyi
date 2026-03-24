

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVmmServerResult', 'AwaitableGetVmmServerResult', 'get_vmm_server', 'get_vmm_server_output']
@pulumi.output_type
class GetVmmServerResult:
    
    def __init__(__self__, azure_api_version=..., connection_status=..., credentials=..., error_message=..., extended_location=..., fqdn=..., id=..., location=..., name=..., port=..., provisioning_state=..., system_data=..., tags=..., type=..., uuid=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.VMMServerPropertiesResponseCredentials]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVmmServerResult(GetVmmServerResult):
    def __await__(self): # -> Generator[Never, Any, GetVmmServerResult]:
        ...
    


def get_vmm_server(resource_group_name: Optional[_builtins.str] = ..., vmm_server_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVmmServerResult:
    
    ...

def get_vmm_server_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vmm_server_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVmmServerResult]:
    
    ...

