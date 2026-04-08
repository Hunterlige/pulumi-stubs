import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetChangeDataCaptureResult",
    "AwaitableGetChangeDataCaptureResult",
    "get_change_data_capture",
    "get_change_data_capture_output",
]

@pulumi.output_type
class GetChangeDataCaptureResult:
    def __init__(
        __self__,
        allow_v_net_override=...,
        azure_api_version=...,
        description=...,
        etag=...,
        folder=...,
        id=...,
        name=...,
        policy=...,
        source_connections_info=...,
        status=...,
        target_connections_info=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowVNetOverride")
    def allow_v_net_override(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def folder(self) -> Optional[outputs.ChangeDataCaptureResponseFolder]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> outputs.MapperPolicyResponse: ...
    @_builtins.property
    @pulumi.getter(name="sourceConnectionsInfo")
    def source_connections_info(
        self,
    ) -> Sequence[outputs.MapperSourceConnectionsInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetConnectionsInfo")
    def target_connections_info(
        self,
    ) -> Sequence[outputs.MapperTargetConnectionsInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetChangeDataCaptureResult(GetChangeDataCaptureResult):
    def __await__(self): ...

def get_change_data_capture(
    change_data_capture_name: Optional[_builtins.str] = ...,
    factory_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetChangeDataCaptureResult: ...
def get_change_data_capture_output(
    change_data_capture_name: Optional[pulumi.Input[_builtins.str]] = ...,
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetChangeDataCaptureResult]: ...
