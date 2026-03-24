

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomKeyStoreArgs', 'CustomKeyStore']
@pulumi.input_type
class CustomKeyStoreArgs:
    def __init__(__self__, *, custom_key_store_name: pulumi.Input[_builtins.str], cloud_hsm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_type: Optional[pulumi.Input[_builtins.str]] = ..., key_store_password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trust_anchor_certificate: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_authentication_credential: Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]] = ..., xks_proxy_connectivity: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_path: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreName")
    def custom_key_store_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @custom_key_store_name.setter
    def custom_key_store_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudHsmClusterId")
    def cloud_hsm_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_hsm_cluster_id.setter
    def cloud_hsm_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreType")
    def custom_key_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_key_store_type.setter
    def custom_key_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorePassword")
    def key_store_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @key_store_password.setter
    def key_store_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchorCertificate")
    def trust_anchor_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @trust_anchor_certificate.setter
    def trust_anchor_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyAuthenticationCredential")
    def xks_proxy_authentication_credential(self) -> Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]]:
        ...
    
    @xks_proxy_authentication_credential.setter
    def xks_proxy_authentication_credential(self, value: Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyConnectivity")
    def xks_proxy_connectivity(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_connectivity.setter
    def xks_proxy_connectivity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriEndpoint")
    def xks_proxy_uri_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_uri_endpoint.setter
    def xks_proxy_uri_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriPath")
    def xks_proxy_uri_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_uri_path.setter
    def xks_proxy_uri_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyVpcEndpointServiceName")
    def xks_proxy_vpc_endpoint_service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_vpc_endpoint_service_name.setter
    def xks_proxy_vpc_endpoint_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _CustomKeyStoreState:
    def __init__(__self__, *, cloud_hsm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_type: Optional[pulumi.Input[_builtins.str]] = ..., key_store_password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trust_anchor_certificate: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_authentication_credential: Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]] = ..., xks_proxy_connectivity: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_path: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudHsmClusterId")
    def cloud_hsm_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_hsm_cluster_id.setter
    def cloud_hsm_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreName")
    def custom_key_store_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_key_store_name.setter
    def custom_key_store_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreType")
    def custom_key_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_key_store_type.setter
    def custom_key_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorePassword")
    def key_store_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @key_store_password.setter
    def key_store_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchorCertificate")
    def trust_anchor_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @trust_anchor_certificate.setter
    def trust_anchor_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyAuthenticationCredential")
    def xks_proxy_authentication_credential(self) -> Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]]:
        ...
    
    @xks_proxy_authentication_credential.setter
    def xks_proxy_authentication_credential(self, value: Optional[pulumi.Input[CustomKeyStoreXksProxyAuthenticationCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyConnectivity")
    def xks_proxy_connectivity(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_connectivity.setter
    def xks_proxy_connectivity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriEndpoint")
    def xks_proxy_uri_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_uri_endpoint.setter
    def xks_proxy_uri_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriPath")
    def xks_proxy_uri_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_uri_path.setter
    def xks_proxy_uri_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyVpcEndpointServiceName")
    def xks_proxy_vpc_endpoint_service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @xks_proxy_vpc_endpoint_service_name.setter
    def xks_proxy_vpc_endpoint_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:kms/customKeyStore:CustomKeyStore")
class CustomKeyStore(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cloud_hsm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_type: Optional[pulumi.Input[_builtins.str]] = ..., key_store_password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trust_anchor_certificate: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_authentication_credential: Optional[pulumi.Input[Union[CustomKeyStoreXksProxyAuthenticationCredentialArgs, CustomKeyStoreXksProxyAuthenticationCredentialArgsDict]]] = ..., xks_proxy_connectivity: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_path: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomKeyStoreArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cloud_hsm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_name: Optional[pulumi.Input[_builtins.str]] = ..., custom_key_store_type: Optional[pulumi.Input[_builtins.str]] = ..., key_store_password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., trust_anchor_certificate: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_authentication_credential: Optional[pulumi.Input[Union[CustomKeyStoreXksProxyAuthenticationCredentialArgs, CustomKeyStoreXksProxyAuthenticationCredentialArgsDict]]] = ..., xks_proxy_connectivity: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_uri_path: Optional[pulumi.Input[_builtins.str]] = ..., xks_proxy_vpc_endpoint_service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> CustomKeyStore:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudHsmClusterId")
    def cloud_hsm_cluster_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreName")
    def custom_key_store_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeyStoreType")
    def custom_key_store_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyStorePassword")
    def key_store_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustAnchorCertificate")
    def trust_anchor_certificate(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyAuthenticationCredential")
    def xks_proxy_authentication_credential(self) -> pulumi.Output[Optional[outputs.CustomKeyStoreXksProxyAuthenticationCredential]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyConnectivity")
    def xks_proxy_connectivity(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriEndpoint")
    def xks_proxy_uri_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyUriPath")
    def xks_proxy_uri_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="xksProxyVpcEndpointServiceName")
    def xks_proxy_vpc_endpoint_service_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    


