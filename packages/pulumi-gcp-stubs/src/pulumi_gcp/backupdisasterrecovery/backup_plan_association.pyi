

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BackupPlanAssociationArgs', 'BackupPlanAssociation']
@pulumi.input_type
class BackupPlanAssociationArgs:
    def __init__(__self__, *, backup_plan: pulumi.Input[_builtins.str], backup_plan_association_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], resource: pulumi.Input[_builtins.str], resource_type: pulumi.Input[_builtins.str], project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_plan.setter
    def backup_plan(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociationId")
    def backup_plan_association_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @backup_plan_association_id.setter
    def backup_plan_association_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BackupPlanAssociationState:
    def __init__(__self__, *, backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., backup_plan_association_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., rules_config_infos: Optional[pulumi.Input[Sequence[pulumi.Input[BackupPlanAssociationRulesConfigInfoArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_plan.setter
    def backup_plan(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociationId")
    def backup_plan_association_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backup_plan_association_id.setter
    def backup_plan_association_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesConfigInfos")
    def rules_config_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackupPlanAssociationRulesConfigInfoArgs]]]]:
        
        ...
    
    @rules_config_infos.setter
    def rules_config_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BackupPlanAssociationRulesConfigInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class BackupPlanAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., backup_plan_association_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BackupPlanAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., backup_plan: Optional[pulumi.Input[_builtins.str]] = ..., backup_plan_association_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., data_source: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., resource: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., rules_config_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BackupPlanAssociationRulesConfigInfoArgs, BackupPlanAssociationRulesConfigInfoArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> BackupPlanAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlan")
    def backup_plan(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupPlanAssociationId")
    def backup_plan_association_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesConfigInfos")
    def rules_config_infos(self) -> pulumi.Output[Sequence[outputs.BackupPlanAssociationRulesConfigInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


