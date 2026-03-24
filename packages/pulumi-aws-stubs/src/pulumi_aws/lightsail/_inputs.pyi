

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateDomainValidationOptionArgs', 'CertificateDomainValidationOptionArgsDict', 'ContainerServiceDeploymentVersionContainerArgs', 'ContainerServiceDeploymentVersionContainerArgsDict', ..., ..., ..., ..., 'ContainerServicePrivateRegistryAccessArgs', 'ContainerServicePrivateRegistryAccessArgsDict', ..., ..., 'ContainerServicePublicDomainNamesArgs', 'ContainerServicePublicDomainNamesArgsDict', 'ContainerServicePublicDomainNamesCertificateArgs', ..., 'DistributionCacheBehaviorArgs', 'DistributionCacheBehaviorArgsDict', 'DistributionCacheBehaviorSettingsArgs', 'DistributionCacheBehaviorSettingsArgsDict', ..., ..., ..., ..., ..., ..., 'DistributionDefaultCacheBehaviorArgs', 'DistributionDefaultCacheBehaviorArgsDict', 'DistributionLocationArgs', 'DistributionLocationArgsDict', 'DistributionOriginArgs', 'DistributionOriginArgsDict', 'InstanceAddOnArgs', 'InstanceAddOnArgsDict', 'InstancePublicPortsPortInfoArgs', 'InstancePublicPortsPortInfoArgsDict', 'LbCertificateDomainValidationRecordArgs', 'LbCertificateDomainValidationRecordArgsDict']
class CertificateDomainValidationOptionArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CertificateDomainValidationOptionArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_name.setter
    def resource_record_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_type.setter
    def resource_record_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_record_value.setter
    def resource_record_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerServiceDeploymentVersionContainerArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    image: pulumi.Input[_builtins.str]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    environment: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ports: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ContainerServiceDeploymentVersionContainerArgs:
    def __init__(__self__, *, container_name: pulumi.Input[_builtins.str], image: pulumi.Input[_builtins.str], commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., environment: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ports: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ContainerServiceDeploymentVersionPublicEndpointArgsDict(TypedDict):
    container_name: pulumi.Input[_builtins.str]
    container_port: pulumi.Input[_builtins.int]
    health_check: pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgsDict]


@pulumi.input_type
class ContainerServiceDeploymentVersionPublicEndpointArgs:
    def __init__(__self__, *, container_name: pulumi.Input[_builtins.str], container_port: pulumi.Input[_builtins.int], health_check: pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @container_port.setter
    def container_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgs]:
        
        ...
    
    @health_check.setter
    def health_check(self, value: pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgs]): # -> None:
        ...
    


class ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgsDict(TypedDict):
    healthy_threshold: NotRequired[pulumi.Input[_builtins.int]]
    interval_seconds: NotRequired[pulumi.Input[_builtins.int]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    success_codes: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    unhealthy_threshold: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ContainerServiceDeploymentVersionPublicEndpointHealthCheckArgs:
    def __init__(__self__, *, healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., interval_seconds: Optional[pulumi.Input[_builtins.int]] = ..., path: Optional[pulumi.Input[_builtins.str]] = ..., success_codes: Optional[pulumi.Input[_builtins.str]] = ..., timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalSeconds")
    def interval_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval_seconds.setter
    def interval_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @success_codes.setter
    def success_codes(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ContainerServicePrivateRegistryAccessArgsDict(TypedDict):
    ecr_image_puller_role: NotRequired[pulumi.Input[ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgsDict]]


@pulumi.input_type
class ContainerServicePrivateRegistryAccessArgs:
    def __init__(__self__, *, ecr_image_puller_role: Optional[pulumi.Input[ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecrImagePullerRole")
    def ecr_image_puller_role(self) -> Optional[pulumi.Input[ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgs]]:
        
        ...
    
    @ecr_image_puller_role.setter
    def ecr_image_puller_role(self, value: Optional[pulumi.Input[ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgs]]): # -> None:
        ...
    


class ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgsDict(TypedDict):
    is_active: NotRequired[pulumi.Input[_builtins.bool]]
    principal_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContainerServicePrivateRegistryAccessEcrImagePullerRoleArgs:
    def __init__(__self__, *, is_active: Optional[pulumi.Input[_builtins.bool]] = ..., principal_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_arn.setter
    def principal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerServicePublicDomainNamesArgsDict(TypedDict):
    certificates: pulumi.Input[Sequence[pulumi.Input[ContainerServicePublicDomainNamesCertificateArgsDict]]]


@pulumi.input_type
class ContainerServicePublicDomainNamesArgs:
    def __init__(__self__, *, certificates: pulumi.Input[Sequence[pulumi.Input[ContainerServicePublicDomainNamesCertificateArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> pulumi.Input[Sequence[pulumi.Input[ContainerServicePublicDomainNamesCertificateArgs]]]:
        
        ...
    
    @certificates.setter
    def certificates(self, value: pulumi.Input[Sequence[pulumi.Input[ContainerServicePublicDomainNamesCertificateArgs]]]): # -> None:
        ...
    


class ContainerServicePublicDomainNamesCertificateArgsDict(TypedDict):
    certificate_name: pulumi.Input[_builtins.str]
    domain_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ContainerServicePublicDomainNamesCertificateArgs:
    def __init__(__self__, *, certificate_name: pulumi.Input[_builtins.str], domain_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @certificate_name.setter
    def certificate_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @domain_names.setter
    def domain_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class DistributionCacheBehaviorArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionCacheBehaviorArgs:
    def __init__(__self__, *, behavior: pulumi.Input[_builtins.str], path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionCacheBehaviorSettingsArgsDict(TypedDict):
    allowed_http_methods: NotRequired[pulumi.Input[_builtins.str]]
    cached_http_methods: NotRequired[pulumi.Input[_builtins.str]]
    default_ttl: NotRequired[pulumi.Input[_builtins.int]]
    forwarded_cookies: NotRequired[pulumi.Input[DistributionCacheBehaviorSettingsForwardedCookiesArgsDict]]
    forwarded_headers: NotRequired[pulumi.Input[DistributionCacheBehaviorSettingsForwardedHeadersArgsDict]]
    forwarded_query_strings: NotRequired[pulumi.Input[DistributionCacheBehaviorSettingsForwardedQueryStringsArgsDict]]
    maximum_ttl: NotRequired[pulumi.Input[_builtins.int]]
    minimum_ttl: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class DistributionCacheBehaviorSettingsArgs:
    def __init__(__self__, *, allowed_http_methods: Optional[pulumi.Input[_builtins.str]] = ..., cached_http_methods: Optional[pulumi.Input[_builtins.str]] = ..., default_ttl: Optional[pulumi.Input[_builtins.int]] = ..., forwarded_cookies: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedCookiesArgs]] = ..., forwarded_headers: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedHeadersArgs]] = ..., forwarded_query_strings: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedQueryStringsArgs]] = ..., maximum_ttl: Optional[pulumi.Input[_builtins.int]] = ..., minimum_ttl: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHttpMethods")
    def allowed_http_methods(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allowed_http_methods.setter
    def allowed_http_methods(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedHttpMethods")
    def cached_http_methods(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cached_http_methods.setter
    def cached_http_methods(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @default_ttl.setter
    def default_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedCookies")
    def forwarded_cookies(self) -> Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedCookiesArgs]]:
        
        ...
    
    @forwarded_cookies.setter
    def forwarded_cookies(self, value: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedCookiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedHeaders")
    def forwarded_headers(self) -> Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedHeadersArgs]]:
        
        ...
    
    @forwarded_headers.setter
    def forwarded_headers(self, value: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedHeadersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedQueryStrings")
    def forwarded_query_strings(self) -> Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedQueryStringsArgs]]:
        
        ...
    
    @forwarded_query_strings.setter
    def forwarded_query_strings(self, value: Optional[pulumi.Input[DistributionCacheBehaviorSettingsForwardedQueryStringsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumTtl")
    def maximum_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_ttl.setter
    def maximum_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @minimum_ttl.setter
    def minimum_ttl(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class DistributionCacheBehaviorSettingsForwardedCookiesArgsDict(TypedDict):
    cookies_allow_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    option: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionCacheBehaviorSettingsForwardedCookiesArgs:
    def __init__(__self__, *, cookies_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., option: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookiesAllowLists")
    def cookies_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cookies_allow_lists.setter
    def cookies_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @option.setter
    def option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionCacheBehaviorSettingsForwardedHeadersArgsDict(TypedDict):
    headers_allow_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    option: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionCacheBehaviorSettingsForwardedHeadersArgs:
    def __init__(__self__, *, headers_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., option: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersAllowLists")
    def headers_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @headers_allow_lists.setter
    def headers_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @option.setter
    def option(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DistributionCacheBehaviorSettingsForwardedQueryStringsArgsDict(TypedDict):
    option: NotRequired[pulumi.Input[_builtins.bool]]
    query_strings_allowed_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DistributionCacheBehaviorSettingsForwardedQueryStringsArgs:
    def __init__(__self__, *, option: Optional[pulumi.Input[_builtins.bool]] = ..., query_strings_allowed_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @option.setter
    def option(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsAllowedLists")
    def query_strings_allowed_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @query_strings_allowed_lists.setter
    def query_strings_allowed_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class DistributionDefaultCacheBehaviorArgsDict(TypedDict):
    behavior: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionDefaultCacheBehaviorArgs:
    def __init__(__self__, *, behavior: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @behavior.setter
    def behavior(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionLocationArgsDict(TypedDict):
    availability_zone: pulumi.Input[_builtins.str]
    region_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class DistributionLocationArgs:
    def __init__(__self__, *, availability_zone: pulumi.Input[_builtins.str], region_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DistributionOriginArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    region_name: pulumi.Input[_builtins.str]
    protocol_policy: NotRequired[pulumi.Input[_builtins.str]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DistributionOriginArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], region_name: pulumi.Input[_builtins.str], protocol_policy: Optional[pulumi.Input[_builtins.str]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region_name.setter
    def region_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolPolicy")
    def protocol_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_policy.setter
    def protocol_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class InstanceAddOnArgsDict(TypedDict):
    snapshot_time: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class InstanceAddOnArgs:
    def __init__(__self__, *, snapshot_time: pulumi.Input[_builtins.str], status: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @snapshot_time.setter
    def snapshot_time(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class InstancePublicPortsPortInfoArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]
    cidr_list_aliases: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ipv6_cidrs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class InstancePublicPortsPortInfoArgs:
    def __init__(__self__, *, from_port: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], to_port: pulumi.Input[_builtins.int], cidr_list_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ipv6_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrListAliases")
    def cidr_list_aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidr_list_aliases.setter
    def cidr_list_aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @cidrs.setter
    def cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Cidrs")
    def ipv6_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ipv6_cidrs.setter
    def ipv6_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class LbCertificateDomainValidationRecordArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_name: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_type: NotRequired[pulumi.Input[_builtins.str]]
    resource_record_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LbCertificateDomainValidationRecordArgs:
    def __init__(__self__, *, domain_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_record_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_record_name.setter
    def resource_record_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_record_type.setter
    def resource_record_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_record_value.setter
    def resource_record_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


