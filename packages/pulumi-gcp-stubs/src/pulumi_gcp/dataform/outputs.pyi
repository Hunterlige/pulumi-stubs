

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RepositoryGitRemoteSettings', 'RepositoryGitRemoteSettingsSshAuthenticationConfig', 'RepositoryIamBindingCondition', 'RepositoryIamMemberCondition', 'RepositoryReleaseConfigCodeCompilationConfig', ..., ..., 'RepositoryWorkflowConfigInvocationConfig', ..., ..., ..., 'RepositoryWorkspaceCompilationOverrides']
@pulumi.output_type
class RepositoryGitRemoteSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_branch: _builtins.str, url: _builtins.str, authentication_token_secret_version: Optional[_builtins.str] = ..., ssh_authentication_config: Optional[outputs.RepositoryGitRemoteSettingsSshAuthenticationConfig] = ..., token_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationTokenSecretVersion")
    def authentication_token_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sshAuthenticationConfig")
    def ssh_authentication_config(self) -> Optional[outputs.RepositoryGitRemoteSettingsSshAuthenticationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenStatus")
    def token_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryGitRemoteSettingsSshAuthenticationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, host_public_key: _builtins.str, user_private_key_secret_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPublicKey")
    def host_public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userPrivateKeySecretVersion")
    def user_private_key_secret_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RepositoryIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RepositoryIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RepositoryReleaseConfigCodeCompilationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, assertion_schema: Optional[_builtins.str] = ..., database_suffix: Optional[_builtins.str] = ..., default_database: Optional[_builtins.str] = ..., default_location: Optional[_builtins.str] = ..., default_schema: Optional[_builtins.str] = ..., schema_suffix: Optional[_builtins.str] = ..., table_prefix: Optional[_builtins.str] = ..., vars: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assertionSchema")
    def assertion_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseSuffix")
    def database_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatabase")
    def default_database(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSchema")
    def default_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaSuffix")
    def schema_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vars(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class RepositoryReleaseConfigRecentScheduledReleaseRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compilation_result: Optional[_builtins.str] = ..., error_statuses: Optional[Sequence[outputs.RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatus]] = ..., release_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="compilationResult")
    def compilation_result(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(self) -> Optional[Sequence[outputs.RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseTime")
    def release_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryReleaseConfigRecentScheduledReleaseRecordErrorStatus(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryWorkflowConfigInvocationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fully_refresh_incremental_tables_enabled: Optional[_builtins.bool] = ..., included_tags: Optional[Sequence[_builtins.str]] = ..., included_targets: Optional[Sequence[outputs.RepositoryWorkflowConfigInvocationConfigIncludedTarget]] = ..., service_account: Optional[_builtins.str] = ..., transitive_dependencies_included: Optional[_builtins.bool] = ..., transitive_dependents_included: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyRefreshIncrementalTablesEnabled")
    def fully_refresh_incremental_tables_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedTags")
    def included_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedTargets")
    def included_targets(self) -> Optional[Sequence[outputs.RepositoryWorkflowConfigInvocationConfigIncludedTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitiveDependenciesIncluded")
    def transitive_dependencies_included(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transitiveDependentsIncluded")
    def transitive_dependents_included(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class RepositoryWorkflowConfigInvocationConfigIncludedTarget(dict):
    def __init__(__self__, *, database: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., schema: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryWorkflowConfigRecentScheduledExecutionRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_statuses: Optional[Sequence[outputs.RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatus]] = ..., execution_time: Optional[_builtins.str] = ..., workflow_invocation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorStatuses")
    def error_statuses(self) -> Optional[Sequence[outputs.RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowInvocation")
    def workflow_invocation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryWorkflowConfigRecentScheduledExecutionRecordErrorStatus(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RepositoryWorkspaceCompilationOverrides(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_database: Optional[_builtins.str] = ..., schema_suffix: Optional[_builtins.str] = ..., table_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDatabase")
    def default_database(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaSuffix")
    def schema_suffix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


