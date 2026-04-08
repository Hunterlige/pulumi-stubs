import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListWebAppPublishingCredentialsResult",
    "AwaitableListWebAppPublishingCredentialsResult",
    "list_web_app_publishing_credentials",
    "list_web_app_publishing_credentials_output",
]

@pulumi.output_type
class ListWebAppPublishingCredentialsResult:
    def __init__(
        __self__,
        id=...,
        kind=...,
        name=...,
        publishing_password=...,
        publishing_password_hash=...,
        publishing_password_hash_salt=...,
        publishing_user_name=...,
        scm_uri=...,
        type=...,
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
    @pulumi.getter(name="publishingPassword")
    def publishing_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishingPasswordHash")
    def publishing_password_hash(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishingPasswordHashSalt")
    def publishing_password_hash_salt(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publishingUserName")
    def publishing_user_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scmUri")
    def scm_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableListWebAppPublishingCredentialsResult(
    ListWebAppPublishingCredentialsResult
):
    def __await__(self): ...

def list_web_app_publishing_credentials(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListWebAppPublishingCredentialsResult: ...
def list_web_app_publishing_credentials_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListWebAppPublishingCredentialsResult]: ...
