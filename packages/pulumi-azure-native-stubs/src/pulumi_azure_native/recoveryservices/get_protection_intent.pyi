import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetProtectionIntentResult",
    "AwaitableGetProtectionIntentResult",
    "get_protection_intent",
    "get_protection_intent_output",
]

@pulumi.output_type
class GetProtectionIntentResult:
    def __init__(
        __self__,
        azure_api_version=...,
        e_tag=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[_builtins.str]: ...
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
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetProtectionIntentResult(GetProtectionIntentResult):
    def __await__(self): ...

def get_protection_intent(
    fabric_name: Optional[_builtins.str] = ...,
    intent_object_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    vault_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetProtectionIntentResult: ...
def get_protection_intent_output(
    fabric_name: Optional[pulumi.Input[_builtins.str]] = ...,
    intent_object_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetProtectionIntentResult]: ...
