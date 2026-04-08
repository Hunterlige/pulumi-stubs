import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListStaticSiteBuildFunctionAppSettingsResult",
    ...,
    "list_static_site_build_function_app_settings",
    ...,
]

@pulumi.output_type
class ListStaticSiteBuildFunctionAppSettingsResult:
    def __init__(
        __self__, id=..., kind=..., name=..., properties=..., type=...
    ) -> None: ...
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
    def properties(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListStaticSiteBuildFunctionAppSettingsResult(
    ListStaticSiteBuildFunctionAppSettingsResult
):
    def __await__(self): ...

def list_static_site_build_function_app_settings(
    environment_name: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListStaticSiteBuildFunctionAppSettingsResult: ...
def list_static_site_build_function_app_settings_output(
    environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListStaticSiteBuildFunctionAppSettingsResult]: ...
