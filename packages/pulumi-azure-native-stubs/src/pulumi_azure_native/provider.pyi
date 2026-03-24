

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProviderArgs', 'Provider']
@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *, auxiliary_tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_certificate_password: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_path: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., disable_instance_discovery: Optional[pulumi.Input[_builtins.bool]] = ..., disable_pulumi_partner_id: Optional[pulumi.Input[_builtins.bool]] = ..., environment: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata_host: Optional[pulumi.Input[_builtins.str]] = ..., msi_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., oidc_request_token: Optional[pulumi.Input[_builtins.str]] = ..., oidc_request_url: Optional[pulumi.Input[_builtins.str]] = ..., oidc_token: Optional[pulumi.Input[_builtins.str]] = ..., oidc_token_file_path: Optional[pulumi.Input[_builtins.str]] = ..., partner_id: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., use_default_azure_credential: Optional[pulumi.Input[_builtins.bool]] = ..., use_msi: Optional[pulumi.Input[_builtins.bool]] = ..., use_oidc: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auxiliaryTenantIds")
    def auxiliary_tenant_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @auxiliary_tenant_ids.setter
    def auxiliary_tenant_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificatePassword")
    def client_certificate_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_password.setter
    def client_certificate_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificatePath")
    def client_certificate_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_certificate_path.setter
    def client_certificate_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableInstanceDiscovery")
    def disable_instance_discovery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_instance_discovery.setter
    def disable_instance_discovery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disablePulumiPartnerId")
    def disable_pulumi_partner_id(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_pulumi_partner_id.setter
    def disable_pulumi_partner_id(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataHost")
    def metadata_host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_host.setter
    def metadata_host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="msiEndpoint")
    def msi_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @msi_endpoint.setter
    def msi_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcRequestToken")
    def oidc_request_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oidc_request_token.setter
    def oidc_request_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcRequestUrl")
    def oidc_request_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oidc_request_url.setter
    def oidc_request_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oidc_token.setter
    def oidc_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oidcTokenFilePath")
    def oidc_token_file_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oidc_token_file_path.setter
    def oidc_token_file_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partner_id.setter
    def partner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDefaultAzureCredential")
    def use_default_azure_credential(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_default_azure_credential.setter
    def use_default_azure_credential(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useMsi")
    def use_msi(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_msi.setter
    def use_msi(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useOidc")
    def use_oidc(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_oidc.setter
    def use_oidc(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("pulumi:providers:azure-native")
class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auxiliary_tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., client_certificate_password: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_path: Optional[pulumi.Input[_builtins.str]] = ..., client_id: Optional[pulumi.Input[_builtins.str]] = ..., client_secret: Optional[pulumi.Input[_builtins.str]] = ..., disable_instance_discovery: Optional[pulumi.Input[_builtins.bool]] = ..., disable_pulumi_partner_id: Optional[pulumi.Input[_builtins.bool]] = ..., environment: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata_host: Optional[pulumi.Input[_builtins.str]] = ..., msi_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., oidc_request_token: Optional[pulumi.Input[_builtins.str]] = ..., oidc_request_url: Optional[pulumi.Input[_builtins.str]] = ..., oidc_token: Optional[pulumi.Input[_builtins.str]] = ..., oidc_token_file_path: Optional[pulumi.Input[_builtins.str]] = ..., partner_id: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., use_default_azure_credential: Optional[pulumi.Input[_builtins.bool]] = ..., use_msi: Optional[pulumi.Input[_builtins.bool]] = ..., use_oidc: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ProviderArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    


