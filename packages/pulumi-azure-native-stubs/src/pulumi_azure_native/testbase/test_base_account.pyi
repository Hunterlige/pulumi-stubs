import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TestBaseAccountArgs", "TestBaseAccount"]

@pulumi.input_type
class TestBaseAccountArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[TestBaseAccountSKUArgs],
        identity: Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        restore: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[TestBaseAccountSKUArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[TestBaseAccountSKUArgs]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[SystemAssignedServiceIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def restore(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restore.setter
    def restore(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @test_base_account_name.setter
    def test_base_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:testbase:TestBaseAccount")
class TestBaseAccount(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity: Optional[
            pulumi.Input[
                Union[
                    SystemAssignedServiceIdentityArgs,
                    SystemAssignedServiceIdentityArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        restore: Optional[pulumi.Input[_builtins.bool]] = ...,
        sku: Optional[
            pulumi.Input[Union[TestBaseAccountSKUArgs, TestBaseAccountSKUArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TestBaseAccountArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> TestBaseAccount: ...
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.SystemAssignedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.TestBaseAccountSKUResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
