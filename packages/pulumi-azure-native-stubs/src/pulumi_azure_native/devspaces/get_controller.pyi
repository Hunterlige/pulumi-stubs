import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetControllerResult",
    "AwaitableGetControllerResult",
    "get_controller",
    "get_controller_output",
]

@pulumi.output_type
class GetControllerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        data_plane_fqdn=...,
        host_suffix=...,
        id=...,
        location=...,
        name=...,
        provisioning_state=...,
        sku=...,
        tags=...,
        target_container_host_api_server_fqdn=...,
        target_container_host_resource_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneFqdn")
    def data_plane_fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostSuffix")
    def host_suffix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="targetContainerHostApiServerFqdn")
    def target_container_host_api_server_fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetContainerHostResourceId")
    def target_container_host_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetControllerResult(GetControllerResult):
    def __await__(self): ...

def get_controller(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetControllerResult: ...
def get_controller_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetControllerResult]: ...
