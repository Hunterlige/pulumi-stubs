import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupQuotaSubscriptionArgs", "GroupQuotaSubscription"]

@pulumi.input_type
class GroupQuotaSubscriptionArgs:
    def __init__(
        __self__,
        *,
        group_quota_name: pulumi.Input[_builtins.str],
        management_group_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupQuotaName")
    def group_quota_name(self) -> pulumi.Input[_builtins.str]: ...
    @group_quota_name.setter
    def group_quota_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[_builtins.str]: ...
    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.type_token("azure-native:quota:GroupQuotaSubscription")
class GroupQuotaSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group_quota_name: Optional[pulumi.Input[_builtins.str]] = ...,
        management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GroupQuotaSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> GroupQuotaSubscription: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.GroupQuotaSubscriptionIdResponseProperties]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
