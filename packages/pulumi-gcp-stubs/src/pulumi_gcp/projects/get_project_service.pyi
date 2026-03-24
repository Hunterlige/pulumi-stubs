

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectServiceResult', 'AwaitableGetProjectServiceResult', 'get_project_service', 'get_project_service_output']
@pulumi.output_type
class GetProjectServiceResult:
    
    def __init__(__self__, check_if_service_has_usage_on_destroy=..., disable_dependent_services=..., disable_on_destroy=..., id=..., project=..., service=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIfServiceHasUsageOnDestroy")
    def check_if_service_has_usage_on_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDependentServices")
    def disable_dependent_services(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableOnDestroy")
    def disable_on_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        ...
    


class AwaitableGetProjectServiceResult(GetProjectServiceResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectServiceResult]:
        ...
    


def get_project_service(project: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectServiceResult:
    
    ...

def get_project_service_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectServiceResult]:
    
    ...

