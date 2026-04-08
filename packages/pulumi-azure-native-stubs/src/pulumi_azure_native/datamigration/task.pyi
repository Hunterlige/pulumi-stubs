import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TaskArgs", "Task"]

@pulumi.input_type
class TaskArgs:
    def __init__(
        __self__,
        *,
        group_name: pulumi.Input[_builtins.str],
        project_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        properties: Optional[
            pulumi.Input[
                Union[
                    ConnectToMongoDbTaskPropertiesArgs,
                    ConnectToSourceMySqlTaskPropertiesArgs,
                    ConnectToSourceOracleSyncTaskPropertiesArgs,
                    ConnectToSourcePostgreSqlSyncTaskPropertiesArgs,
                    ConnectToSourceSqlServerSyncTaskPropertiesArgs,
                    ConnectToSourceSqlServerTaskPropertiesArgs,
                    ConnectToTargetAzureDbForMySqlTaskPropertiesArgs,
                    ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    ConnectToTargetSqlDbTaskPropertiesArgs,
                    ConnectToTargetSqlMISyncTaskPropertiesArgs,
                    ConnectToTargetSqlMITaskPropertiesArgs,
                    ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs,
                    GetTdeCertificatesSqlTaskPropertiesArgs,
                    GetUserTablesMySqlTaskPropertiesArgs,
                    GetUserTablesOracleTaskPropertiesArgs,
                    GetUserTablesPostgreSqlTaskPropertiesArgs,
                    GetUserTablesSqlSyncTaskPropertiesArgs,
                    GetUserTablesSqlTaskPropertiesArgs,
                    MigrateMongoDbTaskPropertiesArgs,
                    MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgs,
                    MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs,
                    MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    MigrateSqlServerSqlDbSyncTaskPropertiesArgs,
                    MigrateSqlServerSqlDbTaskPropertiesArgs,
                    MigrateSqlServerSqlMISyncTaskPropertiesArgs,
                    MigrateSqlServerSqlMITaskPropertiesArgs,
                    MigrateSsisTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs,
                    ValidateMongoDbTaskPropertiesArgs,
                    ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                ]
            ]
        ] = ...,
        task_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]: ...
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[_builtins.str]: ...
    @project_name.setter
    def project_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Union[
                ConnectToMongoDbTaskPropertiesArgs,
                ConnectToSourceMySqlTaskPropertiesArgs,
                ConnectToSourceOracleSyncTaskPropertiesArgs,
                ConnectToSourcePostgreSqlSyncTaskPropertiesArgs,
                ConnectToSourceSqlServerSyncTaskPropertiesArgs,
                ConnectToSourceSqlServerTaskPropertiesArgs,
                ConnectToTargetAzureDbForMySqlTaskPropertiesArgs,
                ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                ConnectToTargetSqlDbTaskPropertiesArgs,
                ConnectToTargetSqlMISyncTaskPropertiesArgs,
                ConnectToTargetSqlMITaskPropertiesArgs,
                ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs,
                GetTdeCertificatesSqlTaskPropertiesArgs,
                GetUserTablesMySqlTaskPropertiesArgs,
                GetUserTablesOracleTaskPropertiesArgs,
                GetUserTablesPostgreSqlTaskPropertiesArgs,
                GetUserTablesSqlSyncTaskPropertiesArgs,
                GetUserTablesSqlTaskPropertiesArgs,
                MigrateMongoDbTaskPropertiesArgs,
                MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgs,
                MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs,
                MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                MigrateSqlServerSqlDbSyncTaskPropertiesArgs,
                MigrateSqlServerSqlDbTaskPropertiesArgs,
                MigrateSqlServerSqlMISyncTaskPropertiesArgs,
                MigrateSqlServerSqlMITaskPropertiesArgs,
                MigrateSsisTaskPropertiesArgs,
                ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgs,
                ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgs,
                ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs,
                ValidateMongoDbTaskPropertiesArgs,
                ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
            ]
        ]
    ]: ...
    @properties.setter
    def properties(
        self,
        value: Optional[
            pulumi.Input[
                Union[
                    ConnectToMongoDbTaskPropertiesArgs,
                    ConnectToSourceMySqlTaskPropertiesArgs,
                    ConnectToSourceOracleSyncTaskPropertiesArgs,
                    ConnectToSourcePostgreSqlSyncTaskPropertiesArgs,
                    ConnectToSourceSqlServerSyncTaskPropertiesArgs,
                    ConnectToSourceSqlServerTaskPropertiesArgs,
                    ConnectToTargetAzureDbForMySqlTaskPropertiesArgs,
                    ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    ConnectToTargetSqlDbTaskPropertiesArgs,
                    ConnectToTargetSqlMISyncTaskPropertiesArgs,
                    ConnectToTargetSqlMITaskPropertiesArgs,
                    ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs,
                    GetTdeCertificatesSqlTaskPropertiesArgs,
                    GetUserTablesMySqlTaskPropertiesArgs,
                    GetUserTablesOracleTaskPropertiesArgs,
                    GetUserTablesPostgreSqlTaskPropertiesArgs,
                    GetUserTablesSqlSyncTaskPropertiesArgs,
                    GetUserTablesSqlTaskPropertiesArgs,
                    MigrateMongoDbTaskPropertiesArgs,
                    MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgs,
                    MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs,
                    MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                    MigrateSqlServerSqlDbSyncTaskPropertiesArgs,
                    MigrateSqlServerSqlDbTaskPropertiesArgs,
                    MigrateSqlServerSqlMISyncTaskPropertiesArgs,
                    MigrateSqlServerSqlMITaskPropertiesArgs,
                    MigrateSsisTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgs,
                    ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs,
                    ValidateMongoDbTaskPropertiesArgs,
                    ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="taskName")
    def task_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_name.setter
    def task_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:datamigration:Task")
class Task(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    Union[
                        ConnectToMongoDbTaskPropertiesArgs,
                        ConnectToMongoDbTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToSourceMySqlTaskPropertiesArgs,
                        ConnectToSourceMySqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToSourceOracleSyncTaskPropertiesArgs,
                        ConnectToSourceOracleSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToSourcePostgreSqlSyncTaskPropertiesArgs,
                        ConnectToSourcePostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToSourceSqlServerSyncTaskPropertiesArgs,
                        ConnectToSourceSqlServerSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToSourceSqlServerTaskPropertiesArgs,
                        ConnectToSourceSqlServerTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetAzureDbForMySqlTaskPropertiesArgs,
                        ConnectToTargetAzureDbForMySqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                        ConnectToTargetAzureDbForPostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                        ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetSqlDbTaskPropertiesArgs,
                        ConnectToTargetSqlDbTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetSqlMISyncTaskPropertiesArgs,
                        ConnectToTargetSqlMISyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetSqlMITaskPropertiesArgs,
                        ConnectToTargetSqlMITaskPropertiesArgsDict,
                    ],
                    Union[
                        ConnectToTargetSqlSqlDbSyncTaskPropertiesArgs,
                        ConnectToTargetSqlSqlDbSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetTdeCertificatesSqlTaskPropertiesArgs,
                        GetTdeCertificatesSqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetUserTablesMySqlTaskPropertiesArgs,
                        GetUserTablesMySqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetUserTablesOracleTaskPropertiesArgs,
                        GetUserTablesOracleTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetUserTablesPostgreSqlTaskPropertiesArgs,
                        GetUserTablesPostgreSqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetUserTablesSqlSyncTaskPropertiesArgs,
                        GetUserTablesSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        GetUserTablesSqlTaskPropertiesArgs,
                        GetUserTablesSqlTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateMongoDbTaskPropertiesArgs,
                        MigrateMongoDbTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgs,
                        MigrateMySqlAzureDbForMySqlOfflineTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgs,
                        MigrateMySqlAzureDbForMySqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                        MigrateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                        MigratePostgreSqlAzureDbForPostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateSqlServerSqlDbSyncTaskPropertiesArgs,
                        MigrateSqlServerSqlDbSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateSqlServerSqlDbTaskPropertiesArgs,
                        MigrateSqlServerSqlDbTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateSqlServerSqlMISyncTaskPropertiesArgs,
                        MigrateSqlServerSqlMISyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateSqlServerSqlMITaskPropertiesArgs,
                        MigrateSqlServerSqlMITaskPropertiesArgsDict,
                    ],
                    Union[
                        MigrateSsisTaskPropertiesArgs, MigrateSsisTaskPropertiesArgsDict
                    ],
                    Union[
                        ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgs,
                        ValidateMigrationInputSqlServerSqlDbSyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgs,
                        ValidateMigrationInputSqlServerSqlMISyncTaskPropertiesArgsDict,
                    ],
                    Union[
                        ValidateMigrationInputSqlServerSqlMITaskPropertiesArgs,
                        ValidateMigrationInputSqlServerSqlMITaskPropertiesArgsDict,
                    ],
                    Union[
                        ValidateMongoDbTaskPropertiesArgs,
                        ValidateMongoDbTaskPropertiesArgsDict,
                    ],
                    Union[
                        ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgs,
                        ValidateOracleAzureDbForPostgreSqlSyncTaskPropertiesArgsDict,
                    ],
                ]
            ]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        task_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TaskArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Task: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
