

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
__all__ = ['RecordsExclusiveArgs', 'RecordsExclusive']
@pulumi.input_type
class RecordsExclusiveArgs:
    def __init__(__self__, *, zone_id: pulumi.Input[_builtins.str], resource_record_sets: Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]] = ..., timeouts: Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @zone_id.setter
    def zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordSets")
    def resource_record_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]]:
        
        ...
    
    @resource_record_sets.setter
    def resource_record_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RecordsExclusiveState:
    def __init__(__self__, *, resource_record_sets: Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]] = ..., timeouts: Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]] = ..., zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordSets")
    def resource_record_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]]:
        
        ...
    
    @resource_record_sets.setter
    def resource_record_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecordsExclusiveResourceRecordSetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[RecordsExclusiveTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53/recordsExclusive:RecordsExclusive")
class RecordsExclusive(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., resource_record_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RecordsExclusiveResourceRecordSetArgs, RecordsExclusiveResourceRecordSetArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[RecordsExclusiveTimeoutsArgs, RecordsExclusiveTimeoutsArgsDict]]] = ..., zone_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RecordsExclusiveArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., resource_record_sets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RecordsExclusiveResourceRecordSetArgs, RecordsExclusiveResourceRecordSetArgsDict]]]]] = ..., timeouts: Optional[pulumi.Input[Union[RecordsExclusiveTimeoutsArgs, RecordsExclusiveTimeoutsArgsDict]]] = ..., zone_id: Optional[pulumi.Input[_builtins.str]] = ...) -> RecordsExclusive:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordSets")
    def resource_record_sets(self) -> pulumi.Output[Optional[Sequence[outputs.RecordsExclusiveResourceRecordSet]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.RecordsExclusiveTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


