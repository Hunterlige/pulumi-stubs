import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWebAppSitePushSettingsResult",
    "AwaitableListWebAppSitePushSettingsResult",
    "list_web_app_site_push_settings",
    "list_web_app_site_push_settings_output",
]

@pulumi.output_type
class ListWebAppSitePushSettingsResult:
    def __init__(
        __self__,
        dynamic_tags_json=...,
        id=...,
        is_push_enabled=...,
        kind=...,
        name=...,
        tag_whitelist_json=...,
        tags_requiring_auth=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dynamicTagsJson")
    def dynamic_tags_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isPushEnabled")
    def is_push_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagWhitelistJson")
    def tag_whitelist_json(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagsRequiringAuth")
    def tags_requiring_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListWebAppSitePushSettingsResult(ListWebAppSitePushSettingsResult):
    def __await__(self): ...

def list_web_app_site_push_settings(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWebAppSitePushSettingsResult: ...
def list_web_app_site_push_settings_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWebAppSitePushSettingsResult]: ...
