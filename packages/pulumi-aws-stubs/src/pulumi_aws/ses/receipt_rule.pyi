import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReceiptRuleArgs", "ReceiptRule"]

@pulumi.input_type
class ReceiptRuleArgs:
    def __init__(
        __self__,
        *,
        rule_set_name: pulumi.Input[_builtins.str],
        add_header_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
        ] = ...,
        after: Optional[pulumi.Input[_builtins.str]] = ...,
        bounce_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]
        ] = ...,
        scan_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sns_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]
        ] = ...,
        stop_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]
        ] = ...,
        tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        workmail_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @rule_set_name.setter
    def rule_set_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addHeaderActions")
    def add_header_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
    ]: ...
    @add_header_actions.setter
    def add_header_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @after.setter
    def after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bounceActions")
    def bounce_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
    ]: ...
    @bounce_actions.setter
    def bounce_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaActions")
    def lambda_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
    ]: ...
    @lambda_actions.setter
    def lambda_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @recipients.setter
    def recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Actions")
    def s3_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]]: ...
    @s3_actions.setter
    def s3_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanEnabled")
    def scan_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @scan_enabled.setter
    def scan_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snsActions")
    def sns_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]]: ...
    @sns_actions.setter
    def sns_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stopActions")
    def stop_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]]: ...
    @stop_actions.setter
    def stop_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_policy.setter
    def tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workmailActions")
    def workmail_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
    ]: ...
    @workmail_actions.setter
    def workmail_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
        ],
    ): ...

@pulumi.input_type
class _ReceiptRuleState:
    def __init__(
        __self__,
        *,
        add_header_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
        ] = ...,
        after: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bounce_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]
        ] = ...,
        scan_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sns_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]
        ] = ...,
        stop_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]
        ] = ...,
        tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        workmail_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addHeaderActions")
    def add_header_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
    ]: ...
    @add_header_actions.setter
    def add_header_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleAddHeaderActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @after.setter
    def after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bounceActions")
    def bounce_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
    ]: ...
    @bounce_actions.setter
    def bounce_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleBounceActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaActions")
    def lambda_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
    ]: ...
    @lambda_actions.setter
    def lambda_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleLambdaActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def recipients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @recipients.setter
    def recipients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_set_name.setter
    def rule_set_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Actions")
    def s3_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]]: ...
    @s3_actions.setter
    def s3_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleS3ActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanEnabled")
    def scan_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @scan_enabled.setter
    def scan_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snsActions")
    def sns_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]]: ...
    @sns_actions.setter
    def sns_actions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleSnsActionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stopActions")
    def stop_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]]: ...
    @stop_actions.setter
    def stop_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleStopActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_policy.setter
    def tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workmailActions")
    def workmail_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
    ]: ...
    @workmail_actions.setter
    def workmail_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReceiptRuleWorkmailActionArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:ses/receiptRule:ReceiptRule")
class ReceiptRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        add_header_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleAddHeaderActionArgs,
                            ReceiptRuleAddHeaderActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        after: Optional[pulumi.Input[_builtins.str]] = ...,
        bounce_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleBounceActionArgs, ReceiptRuleBounceActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleLambdaActionArgs, ReceiptRuleLambdaActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleS3ActionArgs, ReceiptRuleS3ActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        scan_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sns_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleSnsActionArgs, ReceiptRuleSnsActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        stop_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleStopActionArgs, ReceiptRuleStopActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        workmail_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleWorkmailActionArgs,
                            ReceiptRuleWorkmailActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReceiptRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        add_header_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleAddHeaderActionArgs,
                            ReceiptRuleAddHeaderActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        after: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bounce_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleBounceActionArgs, ReceiptRuleBounceActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleLambdaActionArgs, ReceiptRuleLambdaActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        recipients: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleS3ActionArgs, ReceiptRuleS3ActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        scan_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        sns_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleSnsActionArgs, ReceiptRuleSnsActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        stop_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReceiptRuleStopActionArgs, ReceiptRuleStopActionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tls_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        workmail_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReceiptRuleWorkmailActionArgs,
                            ReceiptRuleWorkmailActionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> ReceiptRule: ...
    @_builtins.property
    @pulumi.getter(name="addHeaderActions")
    def add_header_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleAddHeaderAction]]]: ...
    @_builtins.property
    @pulumi.getter
    def after(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bounceActions")
    def bounce_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleBounceAction]]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaActions")
    def lambda_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleLambdaAction]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def recipients(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Actions")
    def s3_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleS3Action]]]: ...
    @_builtins.property
    @pulumi.getter(name="scanEnabled")
    def scan_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snsActions")
    def sns_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleSnsAction]]]: ...
    @_builtins.property
    @pulumi.getter(name="stopActions")
    def stop_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleStopAction]]]: ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workmailActions")
    def workmail_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReceiptRuleWorkmailAction]]]: ...
