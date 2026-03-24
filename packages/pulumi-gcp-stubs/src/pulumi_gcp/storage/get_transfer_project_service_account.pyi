

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTransferProjectServiceAccountResult', 'AwaitableGetTransferProjectServiceAccountResult', 'get_transfer_project_service_account', 'get_transfer_project_service_account_output']
@pulumi.output_type
class GetTransferProjectServiceAccountResult:
    
    def __init__(__self__, email=..., id=..., member=..., project=..., subject_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subjectId")
    def subject_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetTransferProjectServiceAccountResult(GetTransferProjectServiceAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetTransferProjectServiceAccountResult]:
        ...
    


def get_transfer_project_service_account(project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTransferProjectServiceAccountResult:
    
    ...

def get_transfer_project_service_account_output(project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTransferProjectServiceAccountResult]:
    
    ...

