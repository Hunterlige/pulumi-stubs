import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RepositoryGitRemoteSettingsArgs",
    "RepositoryGitRemoteSettingsArgsDict",
    ...,
    ...,
    "RepositoryIamBindingConditionArgs",
    "RepositoryIamBindingConditionArgsDict",
    "RepositoryIamMemberConditionArgs",
    "RepositoryIamMemberConditionArgsDict",
    "RepositoryReleaseConfigCodeCompilationConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "RepositoryWorkflowConfigInvocationConfigArgs",
    "RepositoryWorkflowConfigInvocationConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "RepositoryWorkspaceCompilationOverridesArgs",
    "RepositoryWorkspaceCompilationOverridesArgsDict",
]

class RepositoryGitRemoteSettingsArgsDict(TypedDict):
    default_branch: pulumi.Input[_builtins.str]
    url: pulumi.Input[_builtins.str]
    authentication_token_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    ssh_authentication_config: NotRequired[
        pulumi.Input[RepositoryGitRemoteSettingsSshAuthenticationConfigArgsDict]
    ]
    token_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryGitRemoteSettingsArgs:
    def __init__(
        __self__,
        *,
        default_branch: pulumi.Input[_builtins.str],
        url: pulumi.Input[_builtins.str],
        authentication_token_secret_version: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        ssh_authentication_config: Optional[
            pulumi.Input[RepositoryGitRemoteSettingsSshAuthenticationConfigArgs]
        ] = ...,
        token_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> pulumi.Input[_builtins.str]: ...
    @default_branch.setter
    def default_branch(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationTokenSecretVersion")
    def authentication_token_secret_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_token_secret_version.setter
    def authentication_token_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sshAuthenticationConfig")
    def ssh_authentication_config(
        self,
    ) -> Optional[
        pulumi.Input[RepositoryGitRemoteSettingsSshAuthenticationConfigArgs]
    ]: ...
    @ssh_authentication_config.setter
    def ssh_authentication_config(
        self,
        value: Optional[
            pulumi.Input[RepositoryGitRemoteSettingsSshAuthenticationConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenStatus")
    def token_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_status.setter
    def token_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryGitRemoteSettingsSshAuthenticationConfigArgsDict(TypedDict):
    host_public_key: pulumi.Input[_builtins.str]
    user_private_key_secret_version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class RepositoryGitRemoteSettingsSshAuthenticationConfigArgs:
    def __init__(
        __self__,
        *,
        host_public_key: pulumi.Input[_builtins.str],
        user_private_key_secret_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPublicKey")
    def host_public_key(self) -> pulumi.Input[_builtins.str]: ...
    @host_public_key.setter
    def host_public_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPrivateKeySecretVersion")
    def user_private_key_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @user_private_key_secret_version.setter
    def user_private_key_secret_version(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryReleaseConfigCodeCompilationConfigArgsDict(TypedDict):
    assertion_schema: NotRequired[pulumi.Input[_builtins.str]]
    database_suffix: NotRequired[pulumi.Input[_builtins.str]]
    default_database: NotRequired[pulumi.Input[_builtins.str]]
    default_location: NotRequired[pulumi.Input[_builtins.str]]
    default_schema: NotRequired[pulumi.Input[_builtins.str]]
    schema_suffix: NotRequired[pulumi.Input[_builtins.str]]
    table_prefix: NotRequired[pulumi.Input[_builtins.str]]
    vars: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class RepositoryReleaseConfigCodeCompilationConfigArgs:
    def __init__(
        __self__,
        *,
        assertion_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        database_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        default_database: Optional[pulumi.Input[_builtins.str]] = ...,
        default_location: Optional[pulumi.Input[_builtins.str]] = ...,
        default_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        table_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        vars: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assertionSchema")
    def assertion_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assertion_schema.setter
    def assertion_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseSuffix")
    def database_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_suffix.setter
    def database_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultDatabase")
    def default_database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_database.setter
    def default_database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_location.setter
    def default_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultSchema")
    def default_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_schema.setter
    def default_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaSuffix")
    def schema_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_suffix.setter
    def schema_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_prefix.setter
    def table_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def vars(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @vars.setter
    def vars(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class RepositoryReleaseConfigRecentScheduledReleaseRecordArgsDict(TypedDict):
    compilation_result: NotRequired[pulumi.Input[_builtins.str]]
    error_statuses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgsDict
                ]
            ]
        ]
    ]
    release_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryReleaseConfigRecentScheduledReleaseRecordArgs:
    def __init__(
        __self__,
        *,
        compilation_result: Optional[pulumi.Input[_builtins.str]] = ...,
        error_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgs
                    ]
                ]
            ]
        ] = ...,
        release_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compilationResult")
    def compilation_result(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compilation_result.setter
    def compilation_result(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgs
                ]
            ]
        ]
    ]: ...
    @error_statuses.setter
    def error_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_time.setter
    def release_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatusArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryWorkflowConfigInvocationConfigArgsDict(TypedDict):
    fully_refresh_incremental_tables_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    included_tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    included_targets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryWorkflowConfigInvocationConfigIncludedTargetArgsDict
                ]
            ]
        ]
    ]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    transitive_dependencies_included: NotRequired[pulumi.Input[_builtins.bool]]
    transitive_dependents_included: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class RepositoryWorkflowConfigInvocationConfigArgs:
    def __init__(
        __self__,
        *,
        fully_refresh_incremental_tables_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        included_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigInvocationConfigIncludedTargetArgs
                    ]
                ]
            ]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        transitive_dependencies_included: Optional[pulumi.Input[_builtins.bool]] = ...,
        transitive_dependents_included: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullyRefreshIncrementalTablesEnabled")
    def fully_refresh_incremental_tables_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fully_refresh_incremental_tables_enabled.setter
    def fully_refresh_incremental_tables_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedTags")
    def included_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_tags.setter
    def included_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedTargets")
    def included_targets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryWorkflowConfigInvocationConfigIncludedTargetArgs]
            ]
        ]
    ]: ...
    @included_targets.setter
    def included_targets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigInvocationConfigIncludedTargetArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitiveDependenciesIncluded")
    def transitive_dependencies_included(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @transitive_dependencies_included.setter
    def transitive_dependencies_included(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitiveDependentsIncluded")
    def transitive_dependents_included(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @transitive_dependents_included.setter
    def transitive_dependents_included(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class RepositoryWorkflowConfigInvocationConfigIncludedTargetArgsDict(TypedDict):
    database: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schema: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryWorkflowConfigInvocationConfigIncludedTargetArgs:
    def __init__(
        __self__,
        *,
        database: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryWorkflowConfigRecentScheduledExecutionRecordArgsDict(TypedDict):
    error_statuses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgsDict
                ]
            ]
        ]
    ]
    execution_time: NotRequired[pulumi.Input[_builtins.str]]
    workflow_invocation: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryWorkflowConfigRecentScheduledExecutionRecordArgs:
    def __init__(
        __self__,
        *,
        error_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgs
                    ]
                ]
            ]
        ] = ...,
        execution_time: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_invocation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgs
                ]
            ]
        ]
    ]: ...
    @error_statuses.setter
    def error_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_time.setter
    def execution_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workflowInvocation")
    def workflow_invocation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workflow_invocation.setter
    def workflow_invocation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatusArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryWorkspaceCompilationOverridesArgsDict(TypedDict):
    default_database: NotRequired[pulumi.Input[_builtins.str]]
    schema_suffix: NotRequired[pulumi.Input[_builtins.str]]
    table_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RepositoryWorkspaceCompilationOverridesArgs:
    def __init__(
        __self__,
        *,
        default_database: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_suffix: Optional[pulumi.Input[_builtins.str]] = ...,
        table_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultDatabase")
    def default_database(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_database.setter
    def default_database(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaSuffix")
    def schema_suffix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_suffix.setter
    def schema_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_prefix.setter
    def table_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
