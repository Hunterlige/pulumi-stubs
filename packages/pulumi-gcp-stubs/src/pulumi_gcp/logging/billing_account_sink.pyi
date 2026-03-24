import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BillingAccountSinkArgs", "BillingAccountSink"]

@pulumi.input_type
class BillingAccountSinkArgs:
    def __init__(
        __self__,
        *,
        billing_account: pulumi.Input[_builtins.str],
        destination: pulumi.Input[_builtins.str],
        bigquery_options: Optional[
            pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Input[_builtins.str]: ...
    @billing_account.setter
    def billing_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> Optional[pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]]: ...
    @bigquery_options.setter
    def bigquery_options(
        self, value: Optional[pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
    ]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BillingAccountSinkState:
    def __init__(
        __self__,
        *,
        bigquery_options: Optional[
            pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]
        ] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> Optional[pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]]: ...
    @bigquery_options.setter
    def bigquery_options(
        self, value: Optional[pulumi.Input[BillingAccountSinkBigqueryOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
    ]: ...
    @exclusions.setter
    def exclusions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BillingAccountSinkExclusionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @writer_identity.setter
    def writer_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:logging/billingAccountSink:BillingAccountSink")
class BillingAccountSink(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bigquery_options: Optional[
            pulumi.Input[
                Union[
                    BillingAccountSinkBigqueryOptionsArgs,
                    BillingAccountSinkBigqueryOptionsArgsDict,
                ]
            ]
        ] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BillingAccountSinkExclusionArgs,
                            BillingAccountSinkExclusionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BillingAccountSinkArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bigquery_options: Optional[
            pulumi.Input[
                Union[
                    BillingAccountSinkBigqueryOptionsArgs,
                    BillingAccountSinkBigqueryOptionsArgsDict,
                ]
            ]
        ] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclusions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BillingAccountSinkExclusionArgs,
                            BillingAccountSinkExclusionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        writer_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BillingAccountSink: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryOptions")
    def bigquery_options(
        self,
    ) -> pulumi.Output[outputs.BillingAccountSinkBigqueryOptions]: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def exclusions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BillingAccountSinkExclusion]]]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="writerIdentity")
    def writer_identity(self) -> pulumi.Output[_builtins.str]: ...
