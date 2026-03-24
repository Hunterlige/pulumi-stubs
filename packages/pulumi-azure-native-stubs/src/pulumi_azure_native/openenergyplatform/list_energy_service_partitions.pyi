

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListEnergyServicePartitionsResult', 'AwaitableListEnergyServicePartitionsResult', 'list_energy_service_partitions', 'list_energy_service_partitions_output']
@pulumi.output_type
class ListEnergyServicePartitionsResult:
    
    def __init__(__self__, data_partition_info=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPartitionInfo")
    def data_partition_info(self) -> Optional[Sequence[outputs.DataPartitionPropertiesResponse]]:
        
        ...
    


class AwaitableListEnergyServicePartitionsResult(ListEnergyServicePartitionsResult):
    def __await__(self): # -> Generator[Never, Any, ListEnergyServicePartitionsResult]:
        ...
    


def list_energy_service_partitions(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListEnergyServicePartitionsResult:
    
    ...

def list_energy_service_partitions_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListEnergyServicePartitionsResult]:
    
    ...

