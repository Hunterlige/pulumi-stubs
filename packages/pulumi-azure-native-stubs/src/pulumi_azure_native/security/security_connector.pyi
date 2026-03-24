

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityConnectorArgs', 'SecurityConnector']
@pulumi.input_type
class SecurityConnectorArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], environment_data: Optional[pulumi.Input[Union[AwsEnvironmentDataArgs, AzureDevOpsScopeEnvironmentDataArgs, DockerHubEnvironmentDataArgs, GcpProjectEnvironmentDataArgs, GithubScopeEnvironmentDataArgs, GitlabScopeEnvironmentDataArgs, JFrogEnvironmentDataArgs]]] = ..., environment_name: Optional[pulumi.Input[Union[_builtins.str, CloudName]]] = ..., hierarchy_identifier: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., offerings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CspmMonitorAwsOfferingArgs, CspmMonitorAzureDevOpsOfferingArgs, CspmMonitorDockerHubOfferingArgs, CspmMonitorGcpOfferingArgs, CspmMonitorGitLabOfferingArgs, CspmMonitorGithubOfferingArgs, CspmMonitorJFrogOfferingArgs, DefenderCspmAwsOfferingArgs, DefenderCspmDockerHubOfferingArgs, DefenderCspmGcpOfferingArgs, DefenderCspmJFrogOfferingArgs, DefenderFoDatabasesAwsOfferingArgs, DefenderForContainersAwsOfferingArgs, DefenderForContainersDockerHubOfferingArgs, DefenderForContainersGcpOfferingArgs, DefenderForContainersJFrogOfferingArgs, DefenderForDatabasesGcpOfferingArgs, DefenderForServersAwsOfferingArgs, DefenderForServersGcpOfferingArgs]]]]] = ..., security_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentData")
    def environment_data(self) -> Optional[pulumi.Input[Union[AwsEnvironmentDataArgs, AzureDevOpsScopeEnvironmentDataArgs, DockerHubEnvironmentDataArgs, GcpProjectEnvironmentDataArgs, GithubScopeEnvironmentDataArgs, GitlabScopeEnvironmentDataArgs, JFrogEnvironmentDataArgs]]]:
        
        ...
    
    @environment_data.setter
    def environment_data(self, value: Optional[pulumi.Input[Union[AwsEnvironmentDataArgs, AzureDevOpsScopeEnvironmentDataArgs, DockerHubEnvironmentDataArgs, GcpProjectEnvironmentDataArgs, GithubScopeEnvironmentDataArgs, GitlabScopeEnvironmentDataArgs, JFrogEnvironmentDataArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[Union[_builtins.str, CloudName]]]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[Union[_builtins.str, CloudName]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyIdentifier")
    def hierarchy_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hierarchy_identifier.setter
    def hierarchy_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def offerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[CspmMonitorAwsOfferingArgs, CspmMonitorAzureDevOpsOfferingArgs, CspmMonitorDockerHubOfferingArgs, CspmMonitorGcpOfferingArgs, CspmMonitorGitLabOfferingArgs, CspmMonitorGithubOfferingArgs, CspmMonitorJFrogOfferingArgs, DefenderCspmAwsOfferingArgs, DefenderCspmDockerHubOfferingArgs, DefenderCspmGcpOfferingArgs, DefenderCspmJFrogOfferingArgs, DefenderFoDatabasesAwsOfferingArgs, DefenderForContainersAwsOfferingArgs, DefenderForContainersDockerHubOfferingArgs, DefenderForContainersGcpOfferingArgs, DefenderForContainersJFrogOfferingArgs, DefenderForDatabasesGcpOfferingArgs, DefenderForServersAwsOfferingArgs, DefenderForServersGcpOfferingArgs]]]]]:
        
        ...
    
    @offerings.setter
    def offerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CspmMonitorAwsOfferingArgs, CspmMonitorAzureDevOpsOfferingArgs, CspmMonitorDockerHubOfferingArgs, CspmMonitorGcpOfferingArgs, CspmMonitorGitLabOfferingArgs, CspmMonitorGithubOfferingArgs, CspmMonitorJFrogOfferingArgs, DefenderCspmAwsOfferingArgs, DefenderCspmDockerHubOfferingArgs, DefenderCspmGcpOfferingArgs, DefenderCspmJFrogOfferingArgs, DefenderFoDatabasesAwsOfferingArgs, DefenderForContainersAwsOfferingArgs, DefenderForContainersDockerHubOfferingArgs, DefenderForContainersGcpOfferingArgs, DefenderForContainersJFrogOfferingArgs, DefenderForDatabasesGcpOfferingArgs, DefenderForServersAwsOfferingArgs, DefenderForServersGcpOfferingArgs]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityConnectorName")
    def security_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_connector_name.setter
    def security_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:SecurityConnector")
class SecurityConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., environment_data: Optional[pulumi.Input[Union[Union[AwsEnvironmentDataArgs, AwsEnvironmentDataArgsDict], Union[AzureDevOpsScopeEnvironmentDataArgs, AzureDevOpsScopeEnvironmentDataArgsDict], Union[DockerHubEnvironmentDataArgs, DockerHubEnvironmentDataArgsDict], Union[GcpProjectEnvironmentDataArgs, GcpProjectEnvironmentDataArgsDict], Union[GithubScopeEnvironmentDataArgs, GithubScopeEnvironmentDataArgsDict], Union[GitlabScopeEnvironmentDataArgs, GitlabScopeEnvironmentDataArgsDict], Union[JFrogEnvironmentDataArgs, JFrogEnvironmentDataArgsDict]]]] = ..., environment_name: Optional[pulumi.Input[Union[_builtins.str, CloudName]]] = ..., hierarchy_identifier: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., offerings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union[CspmMonitorAwsOfferingArgs, CspmMonitorAwsOfferingArgsDict], Union[CspmMonitorAzureDevOpsOfferingArgs, CspmMonitorAzureDevOpsOfferingArgsDict], Union[CspmMonitorDockerHubOfferingArgs, CspmMonitorDockerHubOfferingArgsDict], Union[CspmMonitorGcpOfferingArgs, CspmMonitorGcpOfferingArgsDict], Union[CspmMonitorGitLabOfferingArgs, CspmMonitorGitLabOfferingArgsDict], Union[CspmMonitorGithubOfferingArgs, CspmMonitorGithubOfferingArgsDict], Union[CspmMonitorJFrogOfferingArgs, CspmMonitorJFrogOfferingArgsDict], Union[DefenderCspmAwsOfferingArgs, DefenderCspmAwsOfferingArgsDict], Union[DefenderCspmDockerHubOfferingArgs, DefenderCspmDockerHubOfferingArgsDict], Union[DefenderCspmGcpOfferingArgs, DefenderCspmGcpOfferingArgsDict], Union[DefenderCspmJFrogOfferingArgs, DefenderCspmJFrogOfferingArgsDict], Union[DefenderFoDatabasesAwsOfferingArgs, DefenderFoDatabasesAwsOfferingArgsDict], Union[DefenderForContainersAwsOfferingArgs, DefenderForContainersAwsOfferingArgsDict], Union[DefenderForContainersDockerHubOfferingArgs, DefenderForContainersDockerHubOfferingArgsDict], Union[DefenderForContainersGcpOfferingArgs, DefenderForContainersGcpOfferingArgsDict], Union[DefenderForContainersJFrogOfferingArgs, DefenderForContainersJFrogOfferingArgsDict], Union[DefenderForDatabasesGcpOfferingArgs, DefenderForDatabasesGcpOfferingArgsDict], Union[DefenderForServersAwsOfferingArgs, DefenderForServersAwsOfferingArgsDict], Union[DefenderForServersGcpOfferingArgs, DefenderForServersGcpOfferingArgsDict]]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., security_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SecurityConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SecurityConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentData")
    def environment_data(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyIdentifier")
    def hierarchy_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hierarchyIdentifierTrialEndDate")
    def hierarchy_identifier_trial_end_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def offerings(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


