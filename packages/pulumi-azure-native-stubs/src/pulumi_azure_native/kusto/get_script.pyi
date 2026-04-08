import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetScriptResult",
    "AwaitableGetScriptResult",
    "get_script",
    "get_script_output",
]

@pulumi.output_type
class GetScriptResult:
    def __init__(
        __self__,
        azure_api_version=...,
        continue_on_errors=...,
        force_update_tag=...,
        id=...,
        name=...,
        principal_permissions_action=...,
        provisioning_state=...,
        script_level=...,
        script_url=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="continueOnErrors")
    def continue_on_errors(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalPermissionsAction")
    def principal_permissions_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scriptLevel")
    def script_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scriptUrl")
    def script_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetScriptResult(GetScriptResult):
    def __await__(self): ...

def get_script(
    cluster_name: Optional[_builtins.str] = ...,
    database_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    script_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetScriptResult: ...
def get_script_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    database_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    script_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetScriptResult]: ...
