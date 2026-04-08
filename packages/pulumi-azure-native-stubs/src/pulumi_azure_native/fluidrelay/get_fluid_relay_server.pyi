import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFluidRelayServerResult",
    "AwaitableGetFluidRelayServerResult",
    "get_fluid_relay_server",
    "get_fluid_relay_server_output",
]

@pulumi.output_type
class GetFluidRelayServerResult:
    def __init__(
        __self__,
        azure_api_version=...,
        encryption=...,
        fluid_relay_endpoints=...,
        frs_tenant_id=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        provisioning_state=...,
        storagesku=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fluidRelayEndpoints")
    def fluid_relay_endpoints(self) -> outputs.FluidRelayEndpointsResponse: ...
    @_builtins.property
    @pulumi.getter(name="frsTenantId")
    def frs_tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.IdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def storagesku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFluidRelayServerResult(GetFluidRelayServerResult):
    def __await__(self): ...

def get_fluid_relay_server(
    fluid_relay_server_name: Optional[_builtins.str] = ...,
    resource_group: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFluidRelayServerResult: ...
def get_fluid_relay_server_output(
    fluid_relay_server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFluidRelayServerResult]: ...
