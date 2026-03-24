

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackupPlanAssociationsResult', 'AwaitableGetBackupPlanAssociationsResult', 'get_backup_plan_associations', 'get_backup_plan_associations_output']
@pulumi.output_type
class GetBackupPlanAssociationsResult:
    
    def __init__(__self__, associations=..., id=..., location=..., project=..., resource_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def associations(self) -> Sequence[outputs.GetBackupPlanAssociationsAssociationResult]:
        
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
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    @_utilities.deprecated(...)
    def resource_type(self) -> Optional[_builtins.str]:
        ...
    


class AwaitableGetBackupPlanAssociationsResult(GetBackupPlanAssociationsResult):
    def __await__(self): # -> Generator[Never, Any, GetBackupPlanAssociationsResult]:
        ...
    


def get_backup_plan_associations(location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackupPlanAssociationsResult:
    
    ...

def get_backup_plan_associations_output(location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackupPlanAssociationsResult]:
    
    ...

