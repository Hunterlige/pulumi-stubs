

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UnitArgs', 'Unit']
@pulumi.input_type
class UnitArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], unit_id: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., maintenance: Optional[pulumi.Input[UnitMaintenanceArgs]] = ..., management_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., tenant: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitId")
    def unit_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @unit_id.setter
    def unit_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def maintenance(self) -> Optional[pulumi.Input[UnitMaintenanceArgs]]:
        
        ...
    
    @maintenance.setter
    def maintenance(self, value: Optional[pulumi.Input[UnitMaintenanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementMode")
    def management_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management_mode.setter
    def management_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tenant(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit_kind.setter
    def unit_kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UnitState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[UnitConditionArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependencyArgs]]]] = ..., dependents: Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependentArgs]]]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input_variables: Optional[pulumi.Input[Sequence[pulumi.Input[UnitInputVariableArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance: Optional[pulumi.Input[UnitMaintenanceArgs]] = ..., management_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ongoing_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., output_variables: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOutputVariableArgs]]]] = ..., pending_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., system_cleanup_at: Optional[pulumi.Input[_builtins.str]] = ..., system_managed_state: Optional[pulumi.Input[_builtins.str]] = ..., tenant: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., unit_id: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitConditionArgs]]]]:
        
        ...
    
    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitConditionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependencyArgs]]]]:
        
        ...
    
    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependencyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependentArgs]]]]:
        
        ...
    
    @dependents.setter
    def dependents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitDependentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitInputVariableArgs]]]]:
        
        ...
    
    @input_variables.setter
    def input_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitInputVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def maintenance(self) -> Optional[pulumi.Input[UnitMaintenanceArgs]]:
        
        ...
    
    @maintenance.setter
    def maintenance(self, value: Optional[pulumi.Input[UnitMaintenanceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementMode")
    def management_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @management_mode.setter
    def management_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ongoingOperations")
    def ongoing_operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ongoing_operations.setter
    def ongoing_operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariables")
    def output_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitOutputVariableArgs]]]]:
        
        ...
    
    @output_variables.setter
    def output_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitOutputVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingOperations")
    def pending_operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pending_operations.setter
    def pending_operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @release.setter
    def release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledOperations")
    def scheduled_operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scheduled_operations.setter
    def scheduled_operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemCleanupAt")
    def system_cleanup_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_cleanup_at.setter
    def system_cleanup_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemManagedState")
    def system_managed_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @system_managed_state.setter
    def system_managed_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant.setter
    def tenant(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitId")
    def unit_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit_id.setter
    def unit_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit_kind.setter
    def unit_kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:saasruntime/unit:Unit")
class Unit(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance: Optional[pulumi.Input[Union[UnitMaintenanceArgs, UnitMaintenanceArgsDict]]] = ..., management_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., tenant: Optional[pulumi.Input[_builtins.str]] = ..., unit_id: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UnitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitConditionArgs, UnitConditionArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitDependencyArgs, UnitDependencyArgsDict]]]]] = ..., dependents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitDependentArgs, UnitDependentArgsDict]]]]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., input_variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitInputVariableArgs, UnitInputVariableArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., maintenance: Optional[pulumi.Input[Union[UnitMaintenanceArgs, UnitMaintenanceArgsDict]]] = ..., management_mode: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., ongoing_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., output_variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitOutputVariableArgs, UnitOutputVariableArgsDict]]]]] = ..., pending_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., release: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_operations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., system_cleanup_at: Optional[pulumi.Input[_builtins.str]] = ..., system_managed_state: Optional[pulumi.Input[_builtins.str]] = ..., tenant: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., unit_id: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Unit:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.UnitCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> pulumi.Output[Sequence[outputs.UnitDependency]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependents(self) -> pulumi.Output[Sequence[outputs.UnitDependent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(self) -> pulumi.Output[Sequence[outputs.UnitInputVariable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def maintenance(self) -> pulumi.Output[Optional[outputs.UnitMaintenance]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementMode")
    def management_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ongoingOperations")
    def ongoing_operations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariables")
    def output_variables(self) -> pulumi.Output[Sequence[outputs.UnitOutputVariable]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingOperations")
    def pending_operations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def release(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledOperations")
    def scheduled_operations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemCleanupAt")
    def system_cleanup_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemManagedState")
    def system_managed_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitId")
    def unit_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


