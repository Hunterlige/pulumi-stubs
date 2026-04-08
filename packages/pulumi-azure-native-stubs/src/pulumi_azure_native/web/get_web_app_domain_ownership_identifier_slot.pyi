import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebAppDomainOwnershipIdentifierSlotResult",
    ...,
    "get_web_app_domain_ownership_identifier_slot",
    ...,
]

@pulumi.output_type
class GetWebAppDomainOwnershipIdentifierSlotResult:
    def __init__(
        __self__, azure_api_version=..., id=..., kind=..., name=..., type=..., value=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

class AwaitableGetWebAppDomainOwnershipIdentifierSlotResult(
    GetWebAppDomainOwnershipIdentifierSlotResult
):
    def __await__(self): ...

def get_web_app_domain_ownership_identifier_slot(
    domain_ownership_identifier_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    slot: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebAppDomainOwnershipIdentifierSlotResult: ...
def get_web_app_domain_ownership_identifier_slot_output(
    domain_ownership_identifier_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    slot: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebAppDomainOwnershipIdentifierSlotResult]: ...
