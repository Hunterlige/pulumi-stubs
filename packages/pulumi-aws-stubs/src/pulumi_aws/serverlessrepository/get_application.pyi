import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApplicationResult",
    "AwaitableGetApplicationResult",
    "get_application",
    "get_application_output",
]

@pulumi.output_type
class GetApplicationResult:
    def __init__(
        __self__,
        application_id=...,
        id=...,
        name=...,
        region=...,
        required_capabilities=...,
        semantic_version=...,
        source_code_url=...,
        template_url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredCapabilities")
    def required_capabilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="semanticVersion")
    def semantic_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceCodeUrl")
    def source_code_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> _builtins.str: ...

class AwaitableGetApplicationResult(GetApplicationResult):
    def __await__(self): ...

def get_application(
    application_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    semantic_version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApplicationResult: ...
def get_application_output(
    application_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    semantic_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApplicationResult]: ...
