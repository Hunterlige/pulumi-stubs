import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackendResult",
    "AwaitableGetBackendResult",
    "get_backend",
    "get_backend_output",
]

@pulumi.output_type
class GetBackendResult:
    def __init__(
        __self__,
        azure_api_version=...,
        circuit_breaker=...,
        credentials=...,
        description=...,
        id=...,
        name=...,
        pool=...,
        properties=...,
        protocol=...,
        proxy=...,
        resource_id=...,
        title=...,
        tls=...,
        type=...,
        url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreaker")
    def circuit_breaker(self) -> Optional[outputs.BackendCircuitBreakerResponse]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.BackendCredentialsContractResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[outputs.BackendBaseParametersResponsePool]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.BackendPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[outputs.BackendProxyContractResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[outputs.BackendTlsPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

class AwaitableGetBackendResult(GetBackendResult):
    def __await__(self): ...

def get_backend(
    backend_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackendResult: ...
def get_backend_output(
    backend_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackendResult]: ...
