import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAuthorizedApplicationResult",
    "AwaitableGetAuthorizedApplicationResult",
    "get_authorized_application",
    "get_authorized_application_output",
]

@pulumi.output_type
class GetAuthorizedApplicationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
        system_data=...,
        type=...,
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
    @pulumi.getter
    def properties(self) -> outputs.AuthorizedApplicationPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAuthorizedApplicationResult(GetAuthorizedApplicationResult):
    def __await__(self): ...

def get_authorized_application(
    application_id: Optional[_builtins.str] = ...,
    provider_namespace: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAuthorizedApplicationResult: ...
def get_authorized_application_output(
    application_id: Optional[pulumi.Input[_builtins.str]] = ...,
    provider_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAuthorizedApplicationResult]: ...
