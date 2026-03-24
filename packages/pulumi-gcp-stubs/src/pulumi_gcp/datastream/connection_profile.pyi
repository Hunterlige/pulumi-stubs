import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
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
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        bigquery_profile: Optional[
            pulumi.Input[ConnectionProfileBigqueryProfileArgs]
        ] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        forward_ssh_connectivity: Optional[
            pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]
        ] = ...,
        gcs_profile: Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        mongodb_profile: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileArgs]
        ] = ...,
        mysql_profile: Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]] = ...,
        oracle_profile: Optional[
            pulumi.Input[ConnectionProfileOracleProfileArgs]
        ] = ...,
        postgresql_profile: Optional[
            pulumi.Input[ConnectionProfilePostgresqlProfileArgs]
        ] = ...,
        private_connectivity: Optional[
            pulumi.Input[ConnectionProfilePrivateConnectivityArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        salesforce_profile: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileArgs]
        ] = ...,
        spanner_profile: Optional[
            pulumi.Input[ConnectionProfileSpannerProfileArgs]
        ] = ...,
        sql_server_profile: Optional[
            pulumi.Input[ConnectionProfileSqlServerProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @connection_profile_id.setter
    def connection_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryProfile")
    def bigquery_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileBigqueryProfileArgs]]: ...
    @bigquery_profile.setter
    def bigquery_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileBigqueryProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="forwardSshConnectivity")
    def forward_ssh_connectivity(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]]: ...
    @forward_ssh_connectivity.setter
    def forward_ssh_connectivity(
        self, value: Optional[pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsProfile")
    def gcs_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]]: ...
    @gcs_profile.setter
    def gcs_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]]
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
    @pulumi.getter(name="mongodbProfile")
    def mongodb_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMongodbProfileArgs]]: ...
    @mongodb_profile.setter
    def mongodb_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileMongodbProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlProfile")
    def mysql_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]]: ...
    @mysql_profile.setter
    def mysql_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="oracleProfile")
    def oracle_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileOracleProfileArgs]]: ...
    @oracle_profile.setter
    def oracle_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileOracleProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlProfile")
    def postgresql_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfilePostgresqlProfileArgs]]: ...
    @postgresql_profile.setter
    def postgresql_profile(
        self, value: Optional[pulumi.Input[ConnectionProfilePostgresqlProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateConnectivity")
    def private_connectivity(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfilePrivateConnectivityArgs]]: ...
    @private_connectivity.setter
    def private_connectivity(
        self, value: Optional[pulumi.Input[ConnectionProfilePrivateConnectivityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="salesforceProfile")
    def salesforce_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSalesforceProfileArgs]]: ...
    @salesforce_profile.setter
    def salesforce_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSalesforceProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerProfile")
    def spanner_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSpannerProfileArgs]]: ...
    @spanner_profile.setter
    def spanner_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSpannerProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerProfile")
    def sql_server_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSqlServerProfileArgs]]: ...
    @sql_server_profile.setter
    def sql_server_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSqlServerProfileArgs]]
    ): ...

@pulumi.input_type
class _ConnectionProfileState:
    def __init__(
        __self__,
        *,
        bigquery_profile: Optional[
            pulumi.Input[ConnectionProfileBigqueryProfileArgs]
        ] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        forward_ssh_connectivity: Optional[
            pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]
        ] = ...,
        gcs_profile: Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_profile: Optional[
            pulumi.Input[ConnectionProfileMongodbProfileArgs]
        ] = ...,
        mysql_profile: Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oracle_profile: Optional[
            pulumi.Input[ConnectionProfileOracleProfileArgs]
        ] = ...,
        postgresql_profile: Optional[
            pulumi.Input[ConnectionProfilePostgresqlProfileArgs]
        ] = ...,
        private_connectivity: Optional[
            pulumi.Input[ConnectionProfilePrivateConnectivityArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        salesforce_profile: Optional[
            pulumi.Input[ConnectionProfileSalesforceProfileArgs]
        ] = ...,
        spanner_profile: Optional[
            pulumi.Input[ConnectionProfileSpannerProfileArgs]
        ] = ...,
        sql_server_profile: Optional[
            pulumi.Input[ConnectionProfileSqlServerProfileArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryProfile")
    def bigquery_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileBigqueryProfileArgs]]: ...
    @bigquery_profile.setter
    def bigquery_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileBigqueryProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_profile_id.setter
    def connection_profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter(name="forwardSshConnectivity")
    def forward_ssh_connectivity(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]]: ...
    @forward_ssh_connectivity.setter
    def forward_ssh_connectivity(
        self, value: Optional[pulumi.Input[ConnectionProfileForwardSshConnectivityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcsProfile")
    def gcs_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]]: ...
    @gcs_profile.setter
    def gcs_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileGcsProfileArgs]]
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
    @pulumi.getter(name="mongodbProfile")
    def mongodb_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMongodbProfileArgs]]: ...
    @mongodb_profile.setter
    def mongodb_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileMongodbProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mysqlProfile")
    def mysql_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]]: ...
    @mysql_profile.setter
    def mysql_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileMysqlProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oracleProfile")
    def oracle_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileOracleProfileArgs]]: ...
    @oracle_profile.setter
    def oracle_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileOracleProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="postgresqlProfile")
    def postgresql_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfilePostgresqlProfileArgs]]: ...
    @postgresql_profile.setter
    def postgresql_profile(
        self, value: Optional[pulumi.Input[ConnectionProfilePostgresqlProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateConnectivity")
    def private_connectivity(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfilePrivateConnectivityArgs]]: ...
    @private_connectivity.setter
    def private_connectivity(
        self, value: Optional[pulumi.Input[ConnectionProfilePrivateConnectivityArgs]]
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
    @pulumi.getter(name="salesforceProfile")
    def salesforce_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSalesforceProfileArgs]]: ...
    @salesforce_profile.setter
    def salesforce_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSalesforceProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="spannerProfile")
    def spanner_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSpannerProfileArgs]]: ...
    @spanner_profile.setter
    def spanner_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSpannerProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sqlServerProfile")
    def sql_server_profile(
        self,
    ) -> Optional[pulumi.Input[ConnectionProfileSqlServerProfileArgs]]: ...
    @sql_server_profile.setter
    def sql_server_profile(
        self, value: Optional[pulumi.Input[ConnectionProfileSqlServerProfileArgs]]
    ): ...

@pulumi.type_token("gcp:datastream/connectionProfile:ConnectionProfile")
class ConnectionProfile(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bigquery_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileBigqueryProfileArgs,
                    ConnectionProfileBigqueryProfileArgsDict,
                ]
            ]
        ] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        forward_ssh_connectivity: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileForwardSshConnectivityArgs,
                    ConnectionProfileForwardSshConnectivityArgsDict,
                ]
            ]
        ] = ...,
        gcs_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileGcsProfileArgs, ConnectionProfileGcsProfileArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileMongodbProfileArgs,
                    ConnectionProfileMongodbProfileArgsDict,
                ]
            ]
        ] = ...,
        mysql_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileMysqlProfileArgs,
                    ConnectionProfileMysqlProfileArgsDict,
                ]
            ]
        ] = ...,
        oracle_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileOracleProfileArgs,
                    ConnectionProfileOracleProfileArgsDict,
                ]
            ]
        ] = ...,
        postgresql_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePostgresqlProfileArgs,
                    ConnectionProfilePostgresqlProfileArgsDict,
                ]
            ]
        ] = ...,
        private_connectivity: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePrivateConnectivityArgs,
                    ConnectionProfilePrivateConnectivityArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        salesforce_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSalesforceProfileArgs,
                    ConnectionProfileSalesforceProfileArgsDict,
                ]
            ]
        ] = ...,
        spanner_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSpannerProfileArgs,
                    ConnectionProfileSpannerProfileArgsDict,
                ]
            ]
        ] = ...,
        sql_server_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSqlServerProfileArgs,
                    ConnectionProfileSqlServerProfileArgsDict,
                ]
            ]
        ] = ...,
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
        bigquery_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileBigqueryProfileArgs,
                    ConnectionProfileBigqueryProfileArgsDict,
                ]
            ]
        ] = ...,
        connection_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        forward_ssh_connectivity: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileForwardSshConnectivityArgs,
                    ConnectionProfileForwardSshConnectivityArgsDict,
                ]
            ]
        ] = ...,
        gcs_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileGcsProfileArgs, ConnectionProfileGcsProfileArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mongodb_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileMongodbProfileArgs,
                    ConnectionProfileMongodbProfileArgsDict,
                ]
            ]
        ] = ...,
        mysql_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileMysqlProfileArgs,
                    ConnectionProfileMysqlProfileArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        oracle_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileOracleProfileArgs,
                    ConnectionProfileOracleProfileArgsDict,
                ]
            ]
        ] = ...,
        postgresql_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePostgresqlProfileArgs,
                    ConnectionProfilePostgresqlProfileArgsDict,
                ]
            ]
        ] = ...,
        private_connectivity: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfilePrivateConnectivityArgs,
                    ConnectionProfilePrivateConnectivityArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        salesforce_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSalesforceProfileArgs,
                    ConnectionProfileSalesforceProfileArgsDict,
                ]
            ]
        ] = ...,
        spanner_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSpannerProfileArgs,
                    ConnectionProfileSpannerProfileArgsDict,
                ]
            ]
        ] = ...,
        sql_server_profile: Optional[
            pulumi.Input[
                Union[
                    ConnectionProfileSqlServerProfileArgs,
                    ConnectionProfileSqlServerProfileArgsDict,
                ]
            ]
        ] = ...,
    ) -> ConnectionProfile: ...
    @_builtins.property
    @pulumi.getter(name="bigqueryProfile")
    def bigquery_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileBigqueryProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionProfileId")
    def connection_profile_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forwardSshConnectivity")
    def forward_ssh_connectivity(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileForwardSshConnectivity]]: ...
    @_builtins.property
    @pulumi.getter(name="gcsProfile")
    def gcs_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileGcsProfile]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mongodbProfile")
    def mongodb_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileMongodbProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="mysqlProfile")
    def mysql_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileMysqlProfile]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oracleProfile")
    def oracle_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileOracleProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="postgresqlProfile")
    def postgresql_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfilePostgresqlProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="privateConnectivity")
    def private_connectivity(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfilePrivateConnectivity]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="salesforceProfile")
    def salesforce_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileSalesforceProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="spannerProfile")
    def spanner_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileSpannerProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServerProfile")
    def sql_server_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.ConnectionProfileSqlServerProfile]]: ...
