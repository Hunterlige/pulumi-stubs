import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["QuicksetupConfigurationManagerArgs", "QuicksetupConfigurationManager"]

@pulumi.input_type
class QuicksetupConfigurationManagerArgs:
    def __init__(
        __self__,
        *,
        configuration_definition: pulumi.Input[
            QuicksetupConfigurationManagerConfigurationDefinitionArgs
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationDefinition")
    def configuration_definition(
        self,
    ) -> pulumi.Input[QuicksetupConfigurationManagerConfigurationDefinitionArgs]: ...
    @configuration_definition.setter
    def configuration_definition(
        self,
        value: pulumi.Input[QuicksetupConfigurationManagerConfigurationDefinitionArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _QuicksetupConfigurationManagerState:
    def __init__(
        __self__,
        *,
        configuration_definition: Optional[
            pulumi.Input[QuicksetupConfigurationManagerConfigurationDefinitionArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status_summaries: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[QuicksetupConfigurationManagerStatusSummaryArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationDefinition")
    def configuration_definition(
        self,
    ) -> Optional[
        pulumi.Input[QuicksetupConfigurationManagerConfigurationDefinitionArgs]
    ]: ...
    @configuration_definition.setter
    def configuration_definition(
        self,
        value: Optional[
            pulumi.Input[QuicksetupConfigurationManagerConfigurationDefinitionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managerArn")
    def manager_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manager_arn.setter
    def manager_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusSummaries")
    def status_summaries(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[QuicksetupConfigurationManagerStatusSummaryArgs]]
        ]
    ]: ...
    @status_summaries.setter
    def status_summaries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[QuicksetupConfigurationManagerStatusSummaryArgs]]
            ]
        ],
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
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[QuicksetupConfigurationManagerTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class QuicksetupConfigurationManager(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_definition: Optional[
            pulumi.Input[
                Union[
                    QuicksetupConfigurationManagerConfigurationDefinitionArgs,
                    QuicksetupConfigurationManagerConfigurationDefinitionArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    QuicksetupConfigurationManagerTimeoutsArgs,
                    QuicksetupConfigurationManagerTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: QuicksetupConfigurationManagerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration_definition: Optional[
            pulumi.Input[
                Union[
                    QuicksetupConfigurationManagerConfigurationDefinitionArgs,
                    QuicksetupConfigurationManagerConfigurationDefinitionArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        manager_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status_summaries: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            QuicksetupConfigurationManagerStatusSummaryArgs,
                            QuicksetupConfigurationManagerStatusSummaryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    QuicksetupConfigurationManagerTimeoutsArgs,
                    QuicksetupConfigurationManagerTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> QuicksetupConfigurationManager: ...
    @_builtins.property
    @pulumi.getter(name="configurationDefinition")
    def configuration_definition(
        self,
    ) -> pulumi.Output[
        outputs.QuicksetupConfigurationManagerConfigurationDefinition
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managerArn")
    def manager_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusSummaries")
    def status_summaries(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.QuicksetupConfigurationManagerStatusSummary]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.QuicksetupConfigurationManagerTimeouts]]: ...
