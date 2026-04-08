import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBuildServiceResourceUploadUrlResult",
    "AwaitableGetBuildServiceResourceUploadUrlResult",
    "get_build_service_resource_upload_url",
    "get_build_service_resource_upload_url_output",
]

@pulumi.output_type
class GetBuildServiceResourceUploadUrlResult:
    def __init__(__self__, relative_path=..., upload_url=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="uploadUrl")
    def upload_url(self) -> Optional[_builtins.str]: ...

class AwaitableGetBuildServiceResourceUploadUrlResult(
    GetBuildServiceResourceUploadUrlResult
):
    def __await__(self): ...

def get_build_service_resource_upload_url(
    build_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBuildServiceResourceUploadUrlResult: ...
def get_build_service_resource_upload_url_output(
    build_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBuildServiceResourceUploadUrlResult]: ...
