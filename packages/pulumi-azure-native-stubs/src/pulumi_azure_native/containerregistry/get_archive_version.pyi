

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetArchiveVersionResult', 'AwaitableGetArchiveVersionResult', 'get_archive_version', 'get_archive_version_output']
@pulumi.output_type
class GetArchiveVersionResult:
    
    def __init__(__self__, archive_version_error_message=..., azure_api_version=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveVersionErrorMessage")
    def archive_version_error_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetArchiveVersionResult(GetArchiveVersionResult):
    def __await__(self): # -> Generator[Never, Any, GetArchiveVersionResult]:
        ...
    


def get_archive_version(archive_name: Optional[_builtins.str] = ..., archive_version_name: Optional[_builtins.str] = ..., package_type: Optional[_builtins.str] = ..., registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetArchiveVersionResult:
    
    ...

def get_archive_version_output(archive_name: Optional[pulumi.Input[_builtins.str]] = ..., archive_version_name: Optional[pulumi.Input[_builtins.str]] = ..., package_type: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetArchiveVersionResult]:
    
    ...

