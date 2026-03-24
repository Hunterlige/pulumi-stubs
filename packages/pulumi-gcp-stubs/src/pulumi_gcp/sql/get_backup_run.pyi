

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackupRunResult', 'AwaitableGetBackupRunResult', 'get_backup_run', 'get_backup_run_output']
@pulumi.output_type
class GetBackupRunResult:
    
    def __init__(__self__, backup_id=..., id=..., instance=..., location=..., most_recent=..., project=..., start_time=..., status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    


class AwaitableGetBackupRunResult(GetBackupRunResult):
    def __await__(self): # -> Generator[Never, Any, GetBackupRunResult]:
        ...
    


def get_backup_run(backup_id: Optional[_builtins.int] = ..., instance: Optional[_builtins.str] = ..., most_recent: Optional[_builtins.bool] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackupRunResult:
    
    ...

def get_backup_run_output(backup_id: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackupRunResult]:
    
    ...

