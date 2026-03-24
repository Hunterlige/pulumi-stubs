

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
__all__ = ['WorkloadArgs', 'Workload']
@pulumi.input_type
class WorkloadArgs:
    def __init__(__self__, *, application_id: pulumi.Input[_builtins.str], discovered_workload: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], workload_id: pulumi.Input[_builtins.str], attributes: Optional[pulumi.Input[WorkloadAttributesArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredWorkload")
    def discovered_workload(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discovered_workload.setter
    def discovered_workload(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workload_id.setter
    def workload_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[WorkloadAttributesArgs]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[WorkloadAttributesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkloadState:
    def __init__(__self__, *, application_id: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[WorkloadAttributesArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovered_workload: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_id: Optional[pulumi.Input[_builtins.str]] = ..., workload_properties: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyArgs]]]] = ..., workload_references: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadReferenceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[pulumi.Input[WorkloadAttributesArgs]]:
        
        ...
    
    @attributes.setter
    def attributes(self, value: Optional[pulumi.Input[WorkloadAttributesArgs]]): # -> None:
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
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredWorkload")
    def discovered_workload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @discovered_workload.setter
    def discovered_workload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workload_id.setter
    def workload_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProperties")
    def workload_properties(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyArgs]]]]:
        
        ...
    
    @workload_properties.setter
    def workload_properties(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadReferences")
    def workload_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadReferenceArgs]]]]:
        
        ...
    
    @workload_references.setter
    def workload_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadReferenceArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apphub/workload:Workload")
class Workload(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Union[WorkloadAttributesArgs, WorkloadAttributesArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovered_workload: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., workload_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_id: Optional[pulumi.Input[_builtins.str]] = ..., attributes: Optional[pulumi.Input[Union[WorkloadAttributesArgs, WorkloadAttributesArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovered_workload: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., workload_id: Optional[pulumi.Input[_builtins.str]] = ..., workload_properties: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkloadWorkloadPropertyArgs, WorkloadWorkloadPropertyArgsDict]]]]] = ..., workload_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkloadWorkloadReferenceArgs, WorkloadWorkloadReferenceArgsDict]]]]] = ...) -> Workload:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[outputs.WorkloadAttributes]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredWorkload")
    def discovered_workload(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadId")
    def workload_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadProperties")
    def workload_properties(self) -> pulumi.Output[Sequence[outputs.WorkloadWorkloadProperty]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workloadReferences")
    def workload_references(self) -> pulumi.Output[Sequence[outputs.WorkloadWorkloadReference]]:
        
        ...
    


