import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountArgs", "Account"]

@pulumi.input_type
class AccountArgs:
    def __init__(
        __self__,
        *,
        email: pulumi.Input[_builtins.str],
        close_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_govcloud: Optional[pulumi.Input[_builtins.bool]] = ...,
        iam_user_access_to_billing: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="closeOnDeletion")
    def close_on_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @close_on_deletion.setter
    def close_on_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createGovcloud")
    def create_govcloud(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_govcloud.setter
    def create_govcloud(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="iamUserAccessToBilling")
    def iam_user_access_to_billing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_user_access_to_billing.setter
    def iam_user_access_to_billing(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _AccountState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        close_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_govcloud: Optional[pulumi.Input[_builtins.bool]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        govcloud_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_user_access_to_billing: Optional[pulumi.Input[_builtins.str]] = ...,
        joined_method: Optional[pulumi.Input[_builtins.str]] = ...,
        joined_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="closeOnDeletion")
    def close_on_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @close_on_deletion.setter
    def close_on_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createGovcloud")
    def create_govcloud(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_govcloud.setter
    def create_govcloud(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="govcloudId")
    def govcloud_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @govcloud_id.setter
    def govcloud_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iamUserAccessToBilling")
    def iam_user_access_to_billing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_user_access_to_billing.setter
    def iam_user_access_to_billing(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @joined_method.setter
    def joined_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @joined_timestamp.setter
    def joined_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:organizations/account:Account")
class Account(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        close_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_govcloud: Optional[pulumi.Input[_builtins.bool]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_user_access_to_billing: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        close_on_deletion: Optional[pulumi.Input[_builtins.bool]] = ...,
        create_govcloud: Optional[pulumi.Input[_builtins.bool]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        govcloud_id: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_user_access_to_billing: Optional[pulumi.Input[_builtins.str]] = ...,
        joined_method: Optional[pulumi.Input[_builtins.str]] = ...,
        joined_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Account: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="closeOnDeletion")
    def close_on_deletion(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createGovcloud")
    def create_govcloud(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="govcloudId")
    def govcloud_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iamUserAccessToBilling")
    def iam_user_access_to_billing(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""status is deprecated. Use state instead.""")
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
