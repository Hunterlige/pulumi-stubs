

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAppServicePlanServerFarmInstanceDetailsResult', ..., 'list_app_service_plan_server_farm_instance_details', ...]
@pulumi.output_type
class ListAppServicePlanServerFarmInstanceDetailsResult:
    
    def __init__(__self__, instance_count=..., instances=..., server_farm_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[Sequence[outputs.ServerFarmInstanceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverFarmName")
    def server_farm_name(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListAppServicePlanServerFarmInstanceDetailsResult(ListAppServicePlanServerFarmInstanceDetailsResult):
    def __await__(self): # -> Generator[Never, Any, ListAppServicePlanServerFarmInstanceDetailsResult]:
        ...
    


def list_app_service_plan_server_farm_instance_details(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAppServicePlanServerFarmInstanceDetailsResult:
    
    ...

def list_app_service_plan_server_farm_instance_details_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAppServicePlanServerFarmInstanceDetailsResult]:
    
    ...

