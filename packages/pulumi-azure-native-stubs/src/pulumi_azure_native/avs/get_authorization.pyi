import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAuthorizationResult",
    "AwaitableGetAuthorizationResult",
    "get_authorization",
    "get_authorization_output",
]

@pulumi.output_type
class GetAuthorizationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        express_route_authorization_id=...,
        express_route_authorization_key=...,
        express_route_id=...,
        id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteAuthorizationId")
    def express_route_authorization_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteAuthorizationKey")
    def express_route_authorization_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAuthorizationResult(GetAuthorizationResult):
    def __await__(self): ...

def get_authorization(
    authorization_name: Optional[_builtins.str] = ...,
    private_cloud_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAuthorizationResult: ...
def get_authorization_output(
    authorization_name: Optional[pulumi.Input[_builtins.str]] = ...,
    private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAuthorizationResult]: ...
