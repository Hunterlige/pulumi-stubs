

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetInstanceResult', 'AwaitableGetInstanceResult', 'get_instance', 'get_instance_output']
@pulumi.output_type
class GetInstanceResult:
    
    def __init__(__self__, autoscaling_configs=..., config=..., default_backup_schedule_type=..., display_name=..., edition=..., effective_labels=..., force_destroy=..., id=..., instance_type=..., labels=..., name=..., num_nodes=..., processing_units=..., project=..., pulumi_labels=..., state=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfigs")
    def autoscaling_configs(self) -> Sequence[outputs.GetInstanceAutoscalingConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBackupScheduleType")
    def default_backup_schedule_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    


class AwaitableGetInstanceResult(GetInstanceResult):
    def __await__(self): # -> Generator[Never, Any, GetInstanceResult]:
        ...
    


def get_instance(config: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetInstanceResult:
    
    ...

def get_instance_output(config: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., display_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetInstanceResult]:
    
    ...

