import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["V2modelsBotVersionArgs", "V2modelsBotVersion"]

@pulumi.input_type
class V2modelsBotVersionArgs:
    def __init__(
        __self__,
        *,
        bot_id: pulumi.Input[_builtins.str],
        locale_specification: pulumi.Input[
            Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
        ],
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[_builtins.str]: ...
    @bot_id.setter
    def bot_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localeSpecification")
    def locale_specification(
        self,
    ) -> pulumi.Input[
        Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
    ]: ...
    @locale_specification.setter
    def locale_specification(
        self,
        value: pulumi.Input[
            Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _V2modelsBotVersionState:
    def __init__(
        __self__,
        *,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_specification: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_id.setter
    def bot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localeSpecification")
    def locale_specification(
        self,
    ) -> Optional[
        pulumi.Input[
            Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
        ]
    ]: ...
    @locale_specification.setter
    def locale_specification(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[V2modelsBotVersionLocaleSpecificationArgs]]
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
    def timeouts(self) -> Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[V2modelsBotVersionTimeoutsArgs]]
    ): ...

@pulumi.type_token("aws:lex/v2modelsBotVersion:V2modelsBotVersion")
class V2modelsBotVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_specification: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            V2modelsBotVersionLocaleSpecificationArgs,
                            V2modelsBotVersionLocaleSpecificationArgsDict,
                        ]
                    ],
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    V2modelsBotVersionTimeoutsArgs, V2modelsBotVersionTimeoutsArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: V2modelsBotVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_specification: Optional[
            pulumi.Input[
                Mapping[
                    str,
                    pulumi.Input[
                        Union[
                            V2modelsBotVersionLocaleSpecificationArgs,
                            V2modelsBotVersionLocaleSpecificationArgsDict,
                        ]
                    ],
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    V2modelsBotVersionTimeoutsArgs, V2modelsBotVersionTimeoutsArgsDict
                ]
            ]
        ] = ...,
    ) -> V2modelsBotVersion: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localeSpecification")
    def locale_specification(
        self,
    ) -> pulumi.Output[Mapping[str, outputs.V2modelsBotVersionLocaleSpecification]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsBotVersionTimeouts]]: ...
