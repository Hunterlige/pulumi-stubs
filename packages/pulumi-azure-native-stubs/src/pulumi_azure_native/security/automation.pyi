import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AutomationArgs", "Automation"]

@pulumi.input_type
class AutomationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AutomationActionEventHubArgs,
                            AutomationActionLogicAppArgs,
                            AutomationActionWorkspaceArgs,
                        ]
                    ]
                ]
            ]
        ] = ...,
        automation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationScopeArgs]]]
        ] = ...,
        sources: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationSourceArgs]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    Union[
                        AutomationActionEventHubArgs,
                        AutomationActionLogicAppArgs,
                        AutomationActionWorkspaceArgs,
                    ]
                ]
            ]
        ]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AutomationActionEventHubArgs,
                            AutomationActionLogicAppArgs,
                            AutomationActionWorkspaceArgs,
                        ]
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="automationName")
    def automation_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @automation_name.setter
    def automation_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutomationScopeArgs]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationScopeArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutomationSourceArgs]]]]: ...
    @sources.setter
    def sources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AutomationSourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:security:Automation")
class Automation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            Union[
                                AutomationActionEventHubArgs,
                                AutomationActionEventHubArgsDict,
                            ],
                            Union[
                                AutomationActionLogicAppArgs,
                                AutomationActionLogicAppArgsDict,
                            ],
                            Union[
                                AutomationActionWorkspaceArgs,
                                AutomationActionWorkspaceArgsDict,
                            ],
                        ]
                    ]
                ]
            ]
        ] = ...,
        automation_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[AutomationScopeArgs, AutomationScopeArgsDict]]
                ]
            ]
        ] = ...,
        sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[AutomationSourceArgs, AutomationSourceArgsDict]]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AutomationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Automation: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence[Any]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AutomationScopeResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AutomationSourceResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
