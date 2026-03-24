import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CustomerManagedPolicyAttachmentsExclusiveArgs",
    "CustomerManagedPolicyAttachmentsExclusive",
]

@pulumi.input_type
class CustomerManagedPolicyAttachmentsExclusiveArgs:
    def __init__(
        __self__,
        *,
        instance_arn: pulumi.Input[_builtins.str],
        permission_set_arn: pulumi.Input[_builtins.str],
        customer_managed_policy_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
        ] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                ]
            ]
        ]
    ]: ...
    @customer_managed_policy_references.setter
    def customer_managed_policy_references(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[
        pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
    ]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
        ],
    ): ...

@pulumi.input_type
class _CustomerManagedPolicyAttachmentsExclusiveState:
    def __init__(
        __self__,
        *,
        customer_managed_policy_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                    ]
                ]
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                ]
            ]
        ]
    ]: ...
    @customer_managed_policy_references.setter
    def customer_managed_policy_references(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs
                    ]
                ]
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
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[
        pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
    ]: ...
    @timeouts.setter
    def timeouts(
        self,
        value: Optional[
            pulumi.Input[CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs]
        ],
    ): ...

@pulumi.type_token(...)
class CustomerManagedPolicyAttachmentsExclusive(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_managed_policy_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs,
                            CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs,
                    CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CustomerManagedPolicyAttachmentsExclusiveArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer_managed_policy_references: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgs,
                            CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgs,
                    CustomerManagedPolicyAttachmentsExclusiveTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> CustomerManagedPolicyAttachmentsExclusive: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> pulumi.Output[
        Optional[
            Sequence[
                outputs.CustomerManagedPolicyAttachmentsExclusiveCustomerManagedPolicyReference
            ]
        ]
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
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[
        Optional[outputs.CustomerManagedPolicyAttachmentsExclusiveTimeouts]
    ]: ...
