import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationGroupResult",
    "AwaitableGetApplicationGroupResult",
    "get_application_group",
    "get_application_group_output",
]

@pulumi.output_type
class GetApplicationGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        client_app_group_identifier=...,
        id=...,
        is_enabled=...,
        location=...,
        name=...,
        policies=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientAppGroupIdentifier")
    def client_app_group_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[Sequence[outputs.ThrottlingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetApplicationGroupResult(GetApplicationGroupResult):
    def __await__(self): ...

def get_application_group(
    application_group_name: Optional[_builtins.str] = ...,
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationGroupResult: ...
def get_application_group_output(
    application_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationGroupResult]: ...
