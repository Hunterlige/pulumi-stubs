import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLinkerResult",
    "AwaitableGetLinkerResult",
    "get_linker",
    "get_linker_output",
]

@pulumi.output_type
class GetLinkerResult:
    def __init__(
        __self__,
        auth_info=...,
        azure_api_version=...,
        client_type=...,
        configuration_info=...,
        id=...,
        name=...,
        provisioning_state=...,
        public_network_solution=...,
        scope=...,
        secret_store=...,
        system_data=...,
        target_service=...,
        type=...,
        v_net_solution=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[outputs.ConfigurationInfoResponse]: ...
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
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(
        self,
    ) -> Optional[outputs.PublicNetworkSolutionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[outputs.SecretStoreResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter(name="targetService")
    def target_service(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> Optional[outputs.VNetSolutionResponse]: ...

class AwaitableGetLinkerResult(GetLinkerResult):
    def __await__(self): ...

def get_linker(
    linker_name: Optional[_builtins.str] = ...,
    resource_uri: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLinkerResult: ...
def get_linker_output(
    linker_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLinkerResult]: ...
