import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVMwareCollectorResult",
    "AwaitableGetVMwareCollectorResult",
    "get_v_mware_collector",
    "get_v_mware_collector_output",
]

@pulumi.output_type
class GetVMwareCollectorResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        name=...,
        properties=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.CollectorPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetVMwareCollectorResult(GetVMwareCollectorResult):
    def __await__(self): ...

def get_v_mware_collector(
    project_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vm_ware_collector_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVMwareCollectorResult: ...
def get_v_mware_collector_output(
    project_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vm_ware_collector_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVMwareCollectorResult]: ...
