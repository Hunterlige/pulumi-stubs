import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLogicAppResult",
    "AwaitableGetLogicAppResult",
    "get_logic_app",
    "get_logic_app_output",
]

@pulumi.output_type
class GetLogicAppResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., system_data=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetLogicAppResult(GetLogicAppResult):
    def __await__(self): ...

def get_logic_app(
    container_app_name: Optional[_builtins.str] = ...,
    logic_app_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLogicAppResult: ...
def get_logic_app_output(
    container_app_name: Optional[pulumi.Input[_builtins.str]] = ...,
    logic_app_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLogicAppResult]: ...
