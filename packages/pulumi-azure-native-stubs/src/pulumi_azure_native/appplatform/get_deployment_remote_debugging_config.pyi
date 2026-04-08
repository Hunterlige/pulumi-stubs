import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDeploymentRemoteDebuggingConfigResult",
    "AwaitableGetDeploymentRemoteDebuggingConfigResult",
    "get_deployment_remote_debugging_config",
    "get_deployment_remote_debugging_config_output",
]

@pulumi.output_type
class GetDeploymentRemoteDebuggingConfigResult:
    def __init__(__self__, enabled=..., port=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

class AwaitableGetDeploymentRemoteDebuggingConfigResult(
    GetDeploymentRemoteDebuggingConfigResult
):
    def __await__(self): ...

def get_deployment_remote_debugging_config(
    app_name: Optional[_builtins.str] = ...,
    deployment_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDeploymentRemoteDebuggingConfigResult: ...
def get_deployment_remote_debugging_config_output(
    app_name: Optional[pulumi.Input[_builtins.str]] = ...,
    deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDeploymentRemoteDebuggingConfigResult]: ...
