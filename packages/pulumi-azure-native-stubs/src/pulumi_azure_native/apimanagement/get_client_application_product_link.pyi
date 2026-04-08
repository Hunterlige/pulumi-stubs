import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClientApplicationProductLinkResult",
    "AwaitableGetClientApplicationProductLinkResult",
    "get_client_application_product_link",
    "get_client_application_product_link_output",
]

@pulumi.output_type
class GetClientApplicationProductLinkResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., product_id=..., type=...
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
    @pulumi.getter(name="productId")
    def product_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetClientApplicationProductLinkResult(
    GetClientApplicationProductLinkResult
):
    def __await__(self): ...

def get_client_application_product_link(
    client_application_id: Optional[_builtins.str] = ...,
    client_application_product_link_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClientApplicationProductLinkResult: ...
def get_client_application_product_link_output(
    client_application_id: Optional[pulumi.Input[_builtins.str]] = ...,
    client_application_product_link_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClientApplicationProductLinkResult]: ...
