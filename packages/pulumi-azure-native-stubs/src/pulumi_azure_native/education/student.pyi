import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StudentArgs", "Student"]

@pulumi.input_type
class StudentArgs:
    def __init__(
        __self__,
        *,
        billing_account_name: pulumi.Input[_builtins.str],
        billing_profile_name: pulumi.Input[_builtins.str],
        budget: pulumi.Input[AmountArgs],
        email: pulumi.Input[_builtins.str],
        expiration_date: pulumi.Input[_builtins.str],
        first_name: pulumi.Input[_builtins.str],
        invoice_section_name: pulumi.Input[_builtins.str],
        last_name: pulumi.Input[_builtins.str],
        role: pulumi.Input[Union[_builtins.str, StudentRole]],
        student_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_invite_last_sent_date: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccountName")
    def billing_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account_name.setter
    def billing_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="billingProfileName")
    def billing_profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @billing_profile_name.setter
    def billing_profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def budget(self) -> pulumi.Input[AmountArgs]: ...
    @budget.setter
    def budget(self, value: pulumi.Input[AmountArgs]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]: ...
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Input[_builtins.str]: ...
    @expiration_date.setter
    def expiration_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[_builtins.str]: ...
    @first_name.setter
    def first_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="invoiceSectionName")
    def invoice_section_name(self) -> pulumi.Input[_builtins.str]: ...
    @invoice_section_name.setter
    def invoice_section_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[_builtins.str]: ...
    @last_name.setter
    def last_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[Union[_builtins.str, StudentRole]]: ...
    @role.setter
    def role(self, value: pulumi.Input[Union[_builtins.str, StudentRole]]): ...
    @_builtins.property
    @pulumi.getter(name="studentAlias")
    def student_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @student_alias.setter
    def student_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionAlias")
    def subscription_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_alias.setter
    def subscription_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionInviteLastSentDate")
    def subscription_invite_last_sent_date(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_invite_last_sent_date.setter
    def subscription_invite_last_sent_date(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:education:Student")
class Student(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        billing_profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        budget: Optional[pulumi.Input[Union[AmountArgs, AmountArgsDict]]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        expiration_date: Optional[pulumi.Input[_builtins.str]] = ...,
        first_name: Optional[pulumi.Input[_builtins.str]] = ...,
        invoice_section_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_name: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[Union[_builtins.str, StudentRole]]] = ...,
        student_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_invite_last_sent_date: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StudentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Student: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def budget(self) -> pulumi.Output[outputs.AmountResponse]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveDate")
    def effective_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionAlias")
    def subscription_alias(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionInviteLastSentDate")
    def subscription_invite_last_sent_date(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
