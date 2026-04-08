import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOpenIdConnectProviderResult",
    "AwaitableGetOpenIdConnectProviderResult",
    "get_open_id_connect_provider",
    "get_open_id_connect_provider_output",
]

@pulumi.output_type
class GetOpenIdConnectProviderResult:
    def __init__(
        __self__,
        azure_api_version=...,
        client_id=...,
        client_secret=...,
        description=...,
        display_name=...,
        id=...,
        metadata_endpoint=...,
        name=...,
        type=...,
        use_in_api_documentation=...,
        use_in_test_console=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="metadataEndpoint")
    def metadata_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="useInApiDocumentation")
    def use_in_api_documentation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="useInTestConsole")
    def use_in_test_console(self) -> Optional[_builtins.bool]: ...

class AwaitableGetOpenIdConnectProviderResult(GetOpenIdConnectProviderResult):
    def __await__(self): ...

def get_open_id_connect_provider(
    opid: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOpenIdConnectProviderResult: ...
def get_open_id_connect_provider_output(
    opid: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOpenIdConnectProviderResult]: ...
