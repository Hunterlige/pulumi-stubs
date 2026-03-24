

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProjectServiceAccountResult', 'AwaitableGetProjectServiceAccountResult', 'get_project_service_account', 'get_project_service_account_output']
@pulumi.output_type
class GetProjectServiceAccountResult:
    
    def __init__(__self__, account_email=..., id=..., name=..., project_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountEmail")
    def account_email(self) -> _builtins.str:
        
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
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        ...
    


class AwaitableGetProjectServiceAccountResult(GetProjectServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetProjectServiceAccountResult]:
        ...
    


def get_project_service_account(project_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProjectServiceAccountResult:
    
    ...

def get_project_service_account_output(project_id: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProjectServiceAccountResult]:
    
    ...

