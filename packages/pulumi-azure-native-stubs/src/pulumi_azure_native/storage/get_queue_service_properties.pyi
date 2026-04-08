import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetQueueServicePropertiesResult",
    "AwaitableGetQueueServicePropertiesResult",
    "get_queue_service_properties",
    "get_queue_service_properties_output",
]

@pulumi.output_type
class GetQueueServicePropertiesResult:
    def __init__(
        __self__, azure_api_version=..., cors=..., id=..., name=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Optional[outputs.CorsRulesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetQueueServicePropertiesResult(GetQueueServicePropertiesResult):
    def __await__(self): ...

def get_queue_service_properties(
    account_name: Optional[_builtins.str] = ...,
    queue_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQueueServicePropertiesResult: ...
def get_queue_service_properties_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    queue_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQueueServicePropertiesResult]: ...
