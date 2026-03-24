import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CustomerManagedPolicyAttachmentArgs", "CustomerManagedPolicyAttachment"]

@pulumi.input_type
class CustomerManagedPolicyAttachmentArgs:
    def __init__(
        __self__,
        *,
        customer_managed_policy_reference: pulumi.Input[
            CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs
        ],
        instance_arn: pulumi.Input[_builtins.str],
        permission_set_arn: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(
        self,
    ) -> pulumi.Input[
        CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs
    ]: ...
    @customer_managed_policy_reference.setter
    def customer_managed_policy_reference(
        self,
        value: pulumi.Input[
            CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[_builtins.str]: ...
    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Input[_builtins.str]: ...
    @permission_set_arn.setter
    def permission_set_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CustomerManagedPolicyAttachmentState:
    def __init__(
        __self__,
        *,
        customer_managed_policy_reference: Optional[
            pulumi.Input[
                CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(
        self,
    ) -> Optional[
        pulumi.Input[CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs]
    ]: ...
    @customer_managed_policy_reference.setter
    def customer_managed_policy_reference(
        self,
        value: Optional[
            pulumi.Input[
                CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission_set_arn.setter
    def permission_set_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class CustomerManagedPolicyAttachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_managed_policy_reference: Optional[
            pulumi.Input[
                Union[
                    CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs,
                    CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgsDict,
                ]
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomerManagedPolicyAttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_managed_policy_reference: Optional[
            pulumi.Input[
                Union[
                    CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgs,
                    CustomerManagedPolicyAttachmentCustomerManagedPolicyReferenceArgsDict,
                ]
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CustomerManagedPolicyAttachment: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReference")
    def customer_managed_policy_reference(
        self,
    ) -> pulumi.Output[
        outputs.CustomerManagedPolicyAttachmentCustomerManagedPolicyReference
    ]: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
