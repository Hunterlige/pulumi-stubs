import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["QueryLoggingConfigurationArgs", "QueryLoggingConfiguration"]

@pulumi.input_type
class QueryLoggingConfigurationArgs:
    def __init__(
        __self__,
        *,
        destinations: pulumi.Input[
            Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]
        ],
        workspace_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _QueryLoggingConfigurationState:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[QueryLoggingConfigurationDestinationArgs]]
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
    ) -> Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[QueryLoggingConfigurationTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class QueryLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            QueryLoggingConfigurationDestinationArgs,
                            QueryLoggingConfigurationDestinationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    QueryLoggingConfigurationTimeoutsArgs,
                    QueryLoggingConfigurationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: QueryLoggingConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            QueryLoggingConfigurationDestinationArgs,
                            QueryLoggingConfigurationDestinationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    QueryLoggingConfigurationTimeoutsArgs,
                    QueryLoggingConfigurationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> QueryLoggingConfiguration: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Output[Sequence[outputs.QueryLoggingConfigurationDestination]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.QueryLoggingConfigurationTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[_builtins.str]: ...
