import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConnectionProfileArgs", "ConnectionProfile"]

@pulumi.input_type
class ConnectionProfileArgs:
    def __init__(
        __self__,
        *,
        connection_profile_id: pulumi.Input[_builtins.str],
        alloydb: Optional[pulumi.Input[ConnectionProfileAlloydbArgs]] = ...,
        cloudsql: Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mysql: Optional[pulumi.Input[ConnectionProfileMysqlArgs]] = ...,
        oracle: Optional[pulumi.Input[ConnectionProfileOracleArgs]] = ...,
        postgresql: Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_profile_id.setter
    def connection_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def alloydb(self) -> Optional[pulumi.Input[ConnectionProfileAlloydbArgs]]: ...
    @alloydb.setter
    def alloydb(self, value: Optional[pulumi.Input[ConnectionProfileAlloydbArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudsql(self) -> Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]]: ...
    @cloudsql.setter
    def cloudsql(
        self, value: Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mysql(self) -> Optional[pulumi.Input[ConnectionProfileMysqlArgs]]: ...
    @mysql.setter
    def mysql(self, value: Optional[pulumi.Input[ConnectionProfileMysqlArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def oracle(self) -> Optional[pulumi.Input[ConnectionProfileOracleArgs]]: ...
    @oracle.setter
    def oracle(self, value: Optional[pulumi.Input[ConnectionProfileOracleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def postgresql(self) -> Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]]: ...
    @postgresql.setter
    def postgresql(
        self, value: Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ConnectionProfileState:
    def __init__(
        __self__,
        *,
        alloydb: Optional[pulumi.Input[ConnectionProfileAlloydbArgs]] = ...,
        cloudsql: Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dbprovider: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionProfileErrorArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mysql: Optional[pulumi.Input[ConnectionProfileMysqlArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oracle: Optional[pulumi.Input[ConnectionProfileOracleArgs]] = ...,
        postgresql: Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alloydb(self) -> Optional[pulumi.Input[ConnectionProfileAlloydbArgs]]: ...
    @alloydb.setter
    def alloydb(self, value: Optional[pulumi.Input[ConnectionProfileAlloydbArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def cloudsql(self) -> Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]]: ...
    @cloudsql.setter
    def cloudsql(
        self, value: Optional[pulumi.Input[ConnectionProfileCloudsqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_profile_id.setter
    def connection_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dbprovider(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dbprovider.setter
    def dbprovider(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectionProfileErrorArgs]]]]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionProfileErrorArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mysql(self) -> Optional[pulumi.Input[ConnectionProfileMysqlArgs]]: ...
    @mysql.setter
    def mysql(self, value: Optional[pulumi.Input[ConnectionProfileMysqlArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def oracle(self) -> Optional[pulumi.Input[ConnectionProfileOracleArgs]]: ...
    @oracle.setter
    def oracle(self, value: Optional[pulumi.Input[ConnectionProfileOracleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def postgresql(self) -> Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]]: ...
    @postgresql.setter
    def postgresql(
        self, value: Optional[pulumi.Input[ConnectionProfilePostgresqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ConnectionProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alloydb: Optional[
            pulumi.Input[
                Union[ConnectionProfileAlloydbArgs, ConnectionProfileAlloydbArgsDict]
            ]
        ] = ...,
        cloudsql: Optional[
            pulumi.Input[
                Union[ConnectionProfileCloudsqlArgs, ConnectionProfileCloudsqlArgsDict]
            ]
        ] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mysql: Optional[
            pulumi.Input[
                Union[ConnectionProfileMysqlArgs, ConnectionProfileMysqlArgsDict]
            ]
        ] = ...,
        oracle: Optional[
            pulumi.Input[
                Union[ConnectionProfileOracleArgs, ConnectionProfileOracleArgsDict]
            ]
        ] = ...,
        postgresql: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePostgresqlArgs, ConnectionProfilePostgresqlArgsDict
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
        args: ConnectionProfileArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alloydb: Optional[
            pulumi.Input[
                Union[ConnectionProfileAlloydbArgs, ConnectionProfileAlloydbArgsDict]
            ]
        ] = ...,
        cloudsql: Optional[
            pulumi.Input[
                Union[ConnectionProfileCloudsqlArgs, ConnectionProfileCloudsqlArgsDict]
            ]
        ] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dbprovider: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ConnectionProfileErrorArgs, ConnectionProfileErrorArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mysql: Optional[
            pulumi.Input[
                Union[ConnectionProfileMysqlArgs, ConnectionProfileMysqlArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oracle: Optional[
            pulumi.Input[
                Union[ConnectionProfileOracleArgs, ConnectionProfileOracleArgsDict]
            ]
        ] = ...,
        postgresql: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePostgresqlArgs, ConnectionProfilePostgresqlArgsDict
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ConnectionProfile: ...
    @_builtins.property
    @pulumi.getter
    def alloydb(self) -> pulumi.Output[Optional[outputs.ConnectionProfileAlloydb]]: ...
    @_builtins.property
    @pulumi.getter
    def cloudsql(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileCloudsql]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dbprovider(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.ConnectionProfileError]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def mysql(self) -> pulumi.Output[Optional[outputs.ConnectionProfileMysql]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def oracle(self) -> pulumi.Output[Optional[outputs.ConnectionProfileOracle]]: ...
    @_builtins.property
    @pulumi.getter
    def postgresql(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfilePostgresql]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
