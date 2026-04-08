import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServiceResult",
    "AwaitableGetServiceResult",
    "get_service",
    "get_service_output",
]

@pulumi.output_type
class GetServiceResult:
    def __init__(
        __self__,
        admin_domain_name=...,
        azure_api_version=...,
        billing_domain_name=...,
        etag=...,
        id=...,
        location=...,
        name=...,
        notes=...,
        quantity=...,
        start_date=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminDomainName")
    def admin_domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="billingDomainName")
    def billing_domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetServiceResult(GetServiceResult):
    def __await__(self): ...

def get_service(
    device_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServiceResult: ...
def get_service_output(
    device_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServiceResult]: ...
