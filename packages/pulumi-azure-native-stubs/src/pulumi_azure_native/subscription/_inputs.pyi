import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PutAliasRequestAdditionalPropertiesArgs",
    "PutAliasRequestAdditionalPropertiesArgsDict",
    "PutAliasRequestPropertiesArgs",
    "PutAliasRequestPropertiesArgsDict",
    "TargetDirectoryRequestPropertiesArgs",
    "TargetDirectoryRequestPropertiesArgsDict",
]

class PutAliasRequestAdditionalPropertiesArgsDict(TypedDict):
    management_group_id: NotRequired[pulumi.Input[_builtins.str]]
    subscription_owner_id: NotRequired[pulumi.Input[_builtins.str]]
    subscription_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PutAliasRequestAdditionalPropertiesArgs:
    def __init__(
        __self__,
        *,
        management_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @management_group_id.setter
    def management_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionOwnerId")
    def subscription_owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_owner_id.setter
    def subscription_owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionTenantId")
    def subscription_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_tenant_id.setter
    def subscription_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class PutAliasRequestPropertiesArgsDict(TypedDict):
    additional_properties: NotRequired[
        pulumi.Input[PutAliasRequestAdditionalPropertiesArgsDict]
    ]
    billing_scope: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    reseller_id: NotRequired[pulumi.Input[_builtins.str]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]
    workload: NotRequired[pulumi.Input[Union[_builtins.str, Workload]]]

@pulumi.input_type
class PutAliasRequestPropertiesArgs:
    def __init__(
        __self__,
        *,
        additional_properties: Optional[
            pulumi.Input[PutAliasRequestAdditionalPropertiesArgs]
        ] = ...,
        billing_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        reseller_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workload: Optional[pulumi.Input[Union[_builtins.str, Workload]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(
        self,
    ) -> Optional[pulumi.Input[PutAliasRequestAdditionalPropertiesArgs]]: ...
    @additional_properties.setter
    def additional_properties(
        self, value: Optional[pulumi.Input[PutAliasRequestAdditionalPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingScope")
    def billing_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_scope.setter
    def billing_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resellerId")
    def reseller_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reseller_id.setter
    def reseller_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workload(self) -> Optional[pulumi.Input[Union[_builtins.str, Workload]]]: ...
    @workload.setter
    def workload(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Workload]]]
    ): ...

class TargetDirectoryRequestPropertiesArgsDict(TypedDict):
    destination_owner_id: NotRequired[pulumi.Input[_builtins.str]]
    destination_tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetDirectoryRequestPropertiesArgs:
    def __init__(
        __self__,
        *,
        destination_owner_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationOwnerId")
    def destination_owner_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_owner_id.setter
    def destination_owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationTenantId")
    def destination_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_tenant_id.setter
    def destination_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
