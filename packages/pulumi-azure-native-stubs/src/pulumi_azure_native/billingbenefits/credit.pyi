import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CreditArgs", "Credit"]

@pulumi.input_type
class CreditArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        billing_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        breakdown: Optional[
            pulumi.Input[Sequence[pulumi.Input[CreditBreakdownItemArgs]]]
        ] = ...,
        credit: Optional[pulumi.Input[CommitmentArgs]] = ...,
        credit_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_at: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[PlanArgs]] = ...,
        policies: Optional[pulumi.Input[CreditPoliciesArgs]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        start_at: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, CreditStatus]]] = ...,
        system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account_resource_id.setter
    def billing_account_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def breakdown(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CreditBreakdownItemArgs]]]]: ...
    @breakdown.setter
    def breakdown(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CreditBreakdownItemArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def credit(self) -> Optional[pulumi.Input[CommitmentArgs]]: ...
    @credit.setter
    def credit(self, value: Optional[pulumi.Input[CommitmentArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="creditName")
    def credit_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @credit_name.setter
    def credit_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_at.setter
    def end_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input[PlanArgs]]: ...
    @plan.setter
    def plan(self, value: Optional[pulumi.Input[PlanArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[CreditPoliciesArgs]]: ...
    @policies.setter
    def policies(self, value: Optional[pulumi.Input[CreditPoliciesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_at.setter
    def start_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, CreditStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CreditStatus]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @system_id.setter
    def system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:billingbenefits:Credit")
class Credit(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        breakdown: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CreditBreakdownItemArgs, CreditBreakdownItemArgsDict]
                    ]
                ]
            ]
        ] = ...,
        credit: Optional[pulumi.Input[Union[CommitmentArgs, CommitmentArgsDict]]] = ...,
        credit_name: Optional[pulumi.Input[_builtins.str]] = ...,
        end_at: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        plan: Optional[pulumi.Input[Union[PlanArgs, PlanArgsDict]]] = ...,
        policies: Optional[
            pulumi.Input[Union[CreditPoliciesArgs, CreditPoliciesArgsDict]]
        ] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        start_at: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, CreditStatus]]] = ...,
        system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CreditArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Credit: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="billingProfileResourceId")
    def billing_profile_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def breakdown(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CreditBreakdownItemResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def credit(self) -> pulumi.Output[Optional[outputs.CommitmentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional[outputs.PlanResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[outputs.CreditPoliciesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Output[Optional[outputs.CreditReasonResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
