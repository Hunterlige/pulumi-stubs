

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'list_manufacturing_data_service_available_versions', ...]
@pulumi.output_type
class ListManufacturingDataServiceAvailableVersionsResult:
    
    def __init__(__self__, versions=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def versions(self) -> Sequence[outputs.ApplicationVersionResponse]:
        
        ...
    


class AwaitableListManufacturingDataServiceAvailableVersionsResult(ListManufacturingDataServiceAvailableVersionsResult):
    def __await__(self): # -> Generator[Never, Any, ListManufacturingDataServiceAvailableVersionsResult]:
        ...
    


def list_manufacturing_data_service_available_versions(mds_resource_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListManufacturingDataServiceAvailableVersionsResult:
    
    ...

def list_manufacturing_data_service_available_versions_output(mds_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListManufacturingDataServiceAvailableVersionsResult]:
    
    ...

