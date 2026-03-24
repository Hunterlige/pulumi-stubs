

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStaticSiteResult', 'AwaitableGetStaticSiteResult', 'get_static_site', 'get_static_site_output']
@pulumi.output_type
class GetStaticSiteResult:
    
    def __init__(__self__, allow_config_file_updates=..., azure_api_version=..., branch=..., build_properties=..., content_distribution_endpoint=..., custom_domains=..., database_connections=..., default_hostname=..., enterprise_grade_cdn_status=..., id=..., identity=..., key_vault_reference_identity=..., kind=..., linked_backends=..., location=..., name=..., private_endpoint_connections=..., provider=..., public_network_access=..., repository_token=..., repository_url=..., sku=..., staging_environment_policy=..., tags=..., template_properties=..., type=..., user_provided_function_apps=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowConfigFileUpdates")
    def allow_config_file_updates(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildProperties")
    def build_properties(self) -> Optional[outputs.StaticSiteBuildPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentDistributionEndpoint")
    def content_distribution_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseConnections")
    def database_connections(self) -> Sequence[outputs.DatabaseConnectionOverviewResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enterpriseGradeCdnStatus")
    def enterprise_grade_cdn_status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkedBackends")
    def linked_backends(self) -> Sequence[outputs.StaticSiteLinkedBackendResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence[outputs.ResponseMessageEnvelopeRemotePrivateEndpointConnectionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def provider(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryToken")
    def repository_token(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuDescriptionResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stagingEnvironmentPolicy")
    def staging_environment_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateProperties")
    def template_properties(self) -> Optional[outputs.StaticSiteTemplateOptionsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userProvidedFunctionApps")
    def user_provided_function_apps(self) -> Sequence[outputs.StaticSiteUserProvidedFunctionAppResponse]:
        
        ...
    


class AwaitableGetStaticSiteResult(GetStaticSiteResult):
    def __await__(self): # -> Generator[Never, Any, GetStaticSiteResult]:
        ...
    


def get_static_site(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStaticSiteResult:
    
    ...

def get_static_site_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStaticSiteResult]:
    
    ...

