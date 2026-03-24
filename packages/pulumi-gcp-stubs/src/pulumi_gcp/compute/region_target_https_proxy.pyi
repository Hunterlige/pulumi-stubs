

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionTargetHttpsProxyArgs', 'RegionTargetHttpsProxy']
@pulumi.input_type
class RegionTargetHttpsProxyArgs:
    def __init__(__self__, *, url_map: pulumi.Input[_builtins.str], certificate_manager_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., http_keep_alive_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ..., ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @url_map.setter
    def url_map(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateManagerCertificates")
    def certificate_manager_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @certificate_manager_certificates.setter
    def certificate_manager_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpKeepAliveTimeoutSec")
    def http_keep_alive_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_keep_alive_timeout_sec.setter
    def http_keep_alive_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_tls_policy.setter
    def server_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionTargetHttpsProxyState:
    def __init__(__self__, *, certificate_manager_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., http_keep_alive_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_id: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ..., ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., url_map: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateManagerCertificates")
    def certificate_manager_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @certificate_manager_certificates.setter
    def certificate_manager_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpKeepAliveTimeoutSec")
    def http_keep_alive_timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @http_keep_alive_timeout_sec.setter
    def http_keep_alive_timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @proxy_id.setter
    def proxy_id(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_tls_policy.setter
    def server_tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_policy.setter
    def ssl_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url_map.setter
    def url_map(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RegionTargetHttpsProxy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., certificate_manager_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., http_keep_alive_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ..., ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., url_map: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionTargetHttpsProxyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., certificate_manager_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., http_keep_alive_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., proxy_id: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_tls_policy: Optional[pulumi.Input[_builtins.str]] = ..., ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_policy: Optional[pulumi.Input[_builtins.str]] = ..., url_map: Optional[pulumi.Input[_builtins.str]] = ...) -> RegionTargetHttpsProxy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateManagerCertificates")
    def certificate_manager_certificates(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpKeepAliveTimeoutSec")
    def http_keep_alive_timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslPolicy")
    def ssl_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlMap")
    def url_map(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


