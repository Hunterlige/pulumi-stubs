

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEndpointResult', 'AwaitableGetEndpointResult', 'get_endpoint', 'get_endpoint_output']
@pulumi.output_type
class GetEndpointResult:
    
    def __init__(__self__, azure_api_version=..., content_types_to_compress=..., custom_domains=..., default_origin_group=..., delivery_policy=..., geo_filters=..., host_name=..., id=..., is_compression_enabled=..., is_http_allowed=..., is_https_allowed=..., location=..., name=..., optimization_type=..., origin_groups=..., origin_host_header=..., origin_path=..., origins=..., probe_path=..., provisioning_state=..., query_string_caching_behavior=..., resource_state=..., system_data=..., tags=..., type=..., url_signing_keys=..., web_application_firewall_policy_link=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentTypesToCompress")
    def content_types_to_compress(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Sequence[outputs.DeepCreatedCustomDomainResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOriginGroup")
    def default_origin_group(self) -> Optional[outputs.ResourceReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deliveryPolicy")
    def delivery_policy(self) -> Optional[outputs.EndpointPropertiesUpdateParametersDeliveryPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoFilters")
    def geo_filters(self) -> Optional[Sequence[outputs.GeoFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isCompressionEnabled")
    def is_compression_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHttpAllowed")
    def is_http_allowed(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHttpsAllowed")
    def is_https_allowed(self) -> Optional[_builtins.bool]:
        
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
    @pulumi.getter(name="optimizationType")
    def optimization_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originGroups")
    def origin_groups(self) -> Optional[Sequence[outputs.DeepCreatedOriginGroupResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def origins(self) -> Sequence[outputs.DeepCreatedOriginResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="probePath")
    def probe_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="urlSigningKeys")
    def url_signing_keys(self) -> Optional[Sequence[outputs.UrlSigningKeyResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webApplicationFirewallPolicyLink")
    def web_application_firewall_policy_link(self) -> Optional[outputs.EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLinkResponse]:
        
        ...
    


class AwaitableGetEndpointResult(GetEndpointResult):
    def __await__(self): # -> Generator[Never, Any, GetEndpointResult]:
        ...
    


def get_endpoint(endpoint_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEndpointResult:
    
    ...

def get_endpoint_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEndpointResult]:
    
    ...

