import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFunctionUrlResult",
    "AwaitableGetFunctionUrlResult",
    "get_function_url",
    "get_function_url_output",
]

@pulumi.output_type
class GetFunctionUrlResult:
    def __init__(
        __self__,
        authorization_type=...,
        cors=...,
        creation_time=...,
        function_arn=...,
        function_name=...,
        function_url=...,
        id=...,
        invoke_mode=...,
        last_modified_time=...,
        qualifier=...,
        region=...,
        url_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cors(self) -> Sequence[outputs.GetFunctionUrlCorResult]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="functionUrl")
    def function_url(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="invokeMode")
    def invoke_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="urlId")
    def url_id(self) -> _builtins.str: ...

class AwaitableGetFunctionUrlResult(GetFunctionUrlResult):
    def __await__(self): ...

def get_function_url(
    function_name: Optional[_builtins.str] = ...,
    qualifier: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFunctionUrlResult: ...
def get_function_url_output(
    function_name: Optional[pulumi.Input[_builtins.str]] = ...,
    qualifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFunctionUrlResult]: ...
