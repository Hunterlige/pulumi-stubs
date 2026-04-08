import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TargetArgs", "Target"]

@pulumi.input_type
class TargetArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        watcher_name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[
                Union[
                    SqlDbElasticPoolTargetPropertiesArgs,
                    SqlDbSingleDatabaseTargetPropertiesArgs,
                    SqlMiTargetPropertiesArgs,
                    SqlVmTargetPropertiesArgs,
                ]
            ]
        ] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="watcherName")
    def watcher_name(self) -> pulumi.Input[_builtins.str]: ...
    @watcher_name.setter
    def watcher_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                SqlDbElasticPoolTargetPropertiesArgs,
                SqlDbSingleDatabaseTargetPropertiesArgs,
                SqlMiTargetPropertiesArgs,
                SqlVmTargetPropertiesArgs,
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    SqlDbElasticPoolTargetPropertiesArgs,
                    SqlDbSingleDatabaseTargetPropertiesArgs,
                    SqlMiTargetPropertiesArgs,
                    SqlVmTargetPropertiesArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetName")
    def target_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_name.setter
    def target_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:databasewatcher:Target")
class Target(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[
                        SqlDbElasticPoolTargetPropertiesArgs,
                        SqlDbElasticPoolTargetPropertiesArgsDict,
                    ],
                    Union[
                        SqlDbSingleDatabaseTargetPropertiesArgs,
                        SqlDbSingleDatabaseTargetPropertiesArgsDict,
                    ],
                    Union[SqlMiTargetPropertiesArgs, SqlMiTargetPropertiesArgsDict],
                    Union[SqlVmTargetPropertiesArgs, SqlVmTargetPropertiesArgsDict],
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_name: Optional[pulumi.Input[_builtins.str]] = ...,
        watcher_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TargetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Target: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
