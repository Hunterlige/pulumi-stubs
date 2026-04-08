import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTestResultFileResult",
    "AwaitableGetTestResultFileResult",
    "get_test_result_file",
    "get_test_result_file_output",
]

@pulumi.output_type
class GetTestResultFileResult:
    def __init__(__self__, data=..., next_link=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...

class AwaitableGetTestResultFileResult(GetTestResultFileResult):
    def __await__(self): ...

def get_test_result_file(
    continuation_token: Optional[_builtins.str] = ...,
    download_as: Optional[_builtins.str] = ...,
    geo_location_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    test_successful_criteria: Optional[_builtins.bool] = ...,
    time_stamp: Optional[_builtins.int] = ...,
    web_test_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTestResultFileResult: ...
def get_test_result_file_output(
    continuation_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    download_as: Optional[pulumi.Input[_builtins.str]] = ...,
    geo_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    test_successful_criteria: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    time_stamp: Optional[pulumi.Input[_builtins.int]] = ...,
    web_test_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTestResultFileResult]: ...
