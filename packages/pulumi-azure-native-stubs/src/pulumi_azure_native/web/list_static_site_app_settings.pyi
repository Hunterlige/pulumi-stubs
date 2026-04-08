import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListStaticSiteAppSettingsResult",
    "AwaitableListStaticSiteAppSettingsResult",
    "list_static_site_app_settings",
    "list_static_site_app_settings_output",
]

@pulumi.output_type
class ListStaticSiteAppSettingsResult:
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

class AwaitableListStaticSiteAppSettingsResult(ListStaticSiteAppSettingsResult):
    def __await__(self): ...

def list_static_site_app_settings(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListStaticSiteAppSettingsResult: ...
def list_static_site_app_settings_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListStaticSiteAppSettingsResult]: ...
