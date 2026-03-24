

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBackupPlanAssociationResult', 'AwaitableGetBackupPlanAssociationResult', 'get_backup_plan_association', 'get_backup_plan_association_output']
@pulumi.output_type
class GetBackupPlanAssociationResult:
    
    def __init__(__self__, backup_plan=..., backup_plan_association_id=..., create_time=..., data_source=..., id=..., location=..., name=..., project=..., resource=..., resource_type=..., rules_config_infos=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociationId")
    def backup_plan_association_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> _builtins.str:
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
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesConfigInfos")
    def rules_config_infos(self) -> Sequence[outputs.GetBackupPlanAssociationRulesConfigInfoResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetBackupPlanAssociationResult(GetBackupPlanAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetBackupPlanAssociationResult]:
        ...
    


def get_backup_plan_association(backup_plan_association_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBackupPlanAssociationResult:
    
    ...

def get_backup_plan_association_output(backup_plan_association_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBackupPlanAssociationResult]:
    
    ...

