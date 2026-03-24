import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApplicationUrlDispatchRulesArgs", "ApplicationUrlDispatchRules"]

@pulumi.input_type
class ApplicationUrlDispatchRulesArgs:
    def __init__(
        __self__,
        *,
        dispatch_rules: pulumi.Input[
            Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
        ],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dispatchRules")
    def dispatch_rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
    ]: ...
    @dispatch_rules.setter
    def dispatch_rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ApplicationUrlDispatchRulesState:
    def __init__(
        __self__,
        *,
        dispatch_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dispatchRules")
    def dispatch_rules(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
        ]
    ]: ...
    @dispatch_rules.setter
    def dispatch_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationUrlDispatchRulesDispatchRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ApplicationUrlDispatchRules(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dispatch_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationUrlDispatchRulesDispatchRuleArgs,
                            ApplicationUrlDispatchRulesDispatchRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApplicationUrlDispatchRulesArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        dispatch_rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationUrlDispatchRulesDispatchRuleArgs,
                            ApplicationUrlDispatchRulesDispatchRuleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ApplicationUrlDispatchRules: ...
    @_builtins.property
    @pulumi.getter(name="dispatchRules")
    def dispatch_rules(
        self,
    ) -> pulumi.Output[Sequence[outputs.ApplicationUrlDispatchRulesDispatchRule]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
