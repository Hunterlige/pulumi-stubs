

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StaticSiteArgs', 'StaticSite']
@pulumi.input_type
class StaticSiteArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], allow_config_file_updates: Optional[pulumi.Input[_builtins.bool]] = ..., branch: Optional[pulumi.Input[_builtins.str]] = ..., build_properties: Optional[pulumi.Input[StaticSiteBuildPropertiesArgs]] = ..., enterprise_grade_cdn_status: Optional[pulumi.Input[Union[_builtins.str, EnterpriseGradeCdnStatus]]] = ..., identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provider: Optional[pulumi.Input[_builtins.str]] = ..., public_network_access: Optional[pulumi.Input[_builtins.str]] = ..., repository_token: Optional[pulumi.Input[_builtins.str]] = ..., repository_url: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[SkuDescriptionArgs]] = ..., staging_environment_policy: Optional[pulumi.Input[StagingEnvironmentPolicy]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_properties: Optional[pulumi.Input[StaticSiteTemplateOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowConfigFileUpdates")
    def allow_config_file_updates(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_config_file_updates.setter
    def allow_config_file_updates(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildProperties")
    def build_properties(self) -> Optional[pulumi.Input[StaticSiteBuildPropertiesArgs]]:
        
        ...
    
    @build_properties.setter
    def build_properties(self, value: Optional[pulumi.Input[StaticSiteBuildPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseGradeCdnStatus")
    def enterprise_grade_cdn_status(self) -> Optional[pulumi.Input[Union[_builtins.str, EnterpriseGradeCdnStatus]]]:
        
        ...
    
    @enterprise_grade_cdn_status.setter
    def enterprise_grade_cdn_status(self, value: Optional[pulumi.Input[Union[_builtins.str, EnterpriseGradeCdnStatus]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]:
        
        ...
    
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provider.setter
    def provider(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryToken")
    def repository_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_token.setter
    def repository_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_url.setter
    def repository_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuDescriptionArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuDescriptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingEnvironmentPolicy")
    def staging_environment_policy(self) -> Optional[pulumi.Input[StagingEnvironmentPolicy]]:
        
        ...
    
    @staging_environment_policy.setter
    def staging_environment_policy(self, value: Optional[pulumi.Input[StagingEnvironmentPolicy]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateProperties")
    def template_properties(self) -> Optional[pulumi.Input[StaticSiteTemplateOptionsArgs]]:
        
        ...
    
    @template_properties.setter
    def template_properties(self, value: Optional[pulumi.Input[StaticSiteTemplateOptionsArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:StaticSite")
class StaticSite(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_config_file_updates: Optional[pulumi.Input[_builtins.bool]] = ..., branch: Optional[pulumi.Input[_builtins.str]] = ..., build_properties: Optional[pulumi.Input[Union[StaticSiteBuildPropertiesArgs, StaticSiteBuildPropertiesArgsDict]]] = ..., enterprise_grade_cdn_status: Optional[pulumi.Input[Union[_builtins.str, EnterpriseGradeCdnStatus]]] = ..., identity: Optional[pulumi.Input[Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., provider: Optional[pulumi.Input[_builtins.str]] = ..., public_network_access: Optional[pulumi.Input[_builtins.str]] = ..., repository_token: Optional[pulumi.Input[_builtins.str]] = ..., repository_url: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[SkuDescriptionArgs, SkuDescriptionArgsDict]]] = ..., staging_environment_policy: Optional[pulumi.Input[StagingEnvironmentPolicy]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., template_properties: Optional[pulumi.Input[Union[StaticSiteTemplateOptionsArgs, StaticSiteTemplateOptionsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StaticSiteArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> StaticSite:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowConfigFileUpdates")
    def allow_config_file_updates(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildProperties")
    def build_properties(self) -> pulumi.Output[Optional[outputs.StaticSiteBuildPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDistributionEndpoint")
    def content_distribution_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseConnections")
    def database_connections(self) -> pulumi.Output[Sequence[outputs.DatabaseConnectionOverviewResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseGradeCdnStatus")
    def enterprise_grade_cdn_status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedBackends")
    def linked_backends(self) -> pulumi.Output[Sequence[outputs.StaticSiteLinkedBackendResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence[outputs.ResponseMessageEnvelopeRemotePrivateEndpointConnectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryToken")
    def repository_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuDescriptionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingEnvironmentPolicy")
    def staging_environment_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateProperties")
    def template_properties(self) -> pulumi.Output[Optional[outputs.StaticSiteTemplateOptionsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userProvidedFunctionApps")
    def user_provided_function_apps(self) -> pulumi.Output[Sequence[outputs.StaticSiteUserProvidedFunctionAppResponse]]:
        
        ...
    


