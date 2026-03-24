

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CertificateDomainValidationOption', 'ContainerServiceDeploymentVersionContainer', 'ContainerServiceDeploymentVersionPublicEndpoint', ..., 'ContainerServicePrivateRegistryAccess', ..., 'ContainerServicePublicDomainNames', 'ContainerServicePublicDomainNamesCertificate', 'DistributionCacheBehavior', 'DistributionCacheBehaviorSettings', 'DistributionCacheBehaviorSettingsForwardedCookies', 'DistributionCacheBehaviorSettingsForwardedHeaders', ..., 'DistributionDefaultCacheBehavior', 'DistributionLocation', 'DistributionOrigin', 'InstanceAddOn', 'InstancePublicPortsPortInfo', 'LbCertificateDomainValidationRecord']
@pulumi.output_type
class CertificateDomainValidationOption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., resource_record_name: Optional[_builtins.str] = ..., resource_record_type: Optional[_builtins.str] = ..., resource_record_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerServiceDeploymentVersionContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_name: _builtins.str, image: _builtins.str, commands: Optional[Sequence[_builtins.str]] = ..., environment: Optional[Mapping[str, _builtins.str]] = ..., ports: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ContainerServiceDeploymentVersionPublicEndpoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, container_name: _builtins.str, container_port: _builtins.int, health_check: outputs.ContainerServiceDeploymentVersionPublicEndpointHealthCheck) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> outputs.ContainerServiceDeploymentVersionPublicEndpointHealthCheck:
        
        ...
    


@pulumi.output_type
class ContainerServiceDeploymentVersionPublicEndpointHealthCheck(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, healthy_threshold: Optional[_builtins.int] = ..., interval_seconds: Optional[_builtins.int] = ..., path: Optional[_builtins.str] = ..., success_codes: Optional[_builtins.str] = ..., timeout_seconds: Optional[_builtins.int] = ..., unhealthy_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intervalSeconds")
    def interval_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ContainerServicePrivateRegistryAccess(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ecr_image_puller_role: Optional[outputs.ContainerServicePrivateRegistryAccessEcrImagePullerRole] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ecrImagePullerRole")
    def ecr_image_puller_role(self) -> Optional[outputs.ContainerServicePrivateRegistryAccessEcrImagePullerRole]:
        
        ...
    


@pulumi.output_type
class ContainerServicePrivateRegistryAccessEcrImagePullerRole(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_active: Optional[_builtins.bool] = ..., principal_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ContainerServicePublicDomainNames(dict):
    def __init__(__self__, *, certificates: Sequence[outputs.ContainerServicePublicDomainNamesCertificate]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Sequence[outputs.ContainerServicePublicDomainNamesCertificate]:
        
        ...
    


@pulumi.output_type
class ContainerServicePublicDomainNamesCertificate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, certificate_name: _builtins.str, domain_names: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DistributionCacheBehavior(dict):
    def __init__(__self__, *, behavior: _builtins.str, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DistributionCacheBehaviorSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_http_methods: Optional[_builtins.str] = ..., cached_http_methods: Optional[_builtins.str] = ..., default_ttl: Optional[_builtins.int] = ..., forwarded_cookies: Optional[outputs.DistributionCacheBehaviorSettingsForwardedCookies] = ..., forwarded_headers: Optional[outputs.DistributionCacheBehaviorSettingsForwardedHeaders] = ..., forwarded_query_strings: Optional[outputs.DistributionCacheBehaviorSettingsForwardedQueryStrings] = ..., maximum_ttl: Optional[_builtins.int] = ..., minimum_ttl: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedHttpMethods")
    def allowed_http_methods(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cachedHttpMethods")
    def cached_http_methods(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultTtl")
    def default_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedCookies")
    def forwarded_cookies(self) -> Optional[outputs.DistributionCacheBehaviorSettingsForwardedCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedHeaders")
    def forwarded_headers(self) -> Optional[outputs.DistributionCacheBehaviorSettingsForwardedHeaders]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedQueryStrings")
    def forwarded_query_strings(self) -> Optional[outputs.DistributionCacheBehaviorSettingsForwardedQueryStrings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumTtl")
    def maximum_ttl(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumTtl")
    def minimum_ttl(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class DistributionCacheBehaviorSettingsForwardedCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cookies_allow_lists: Optional[Sequence[_builtins.str]] = ..., option: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cookiesAllowLists")
    def cookies_allow_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DistributionCacheBehaviorSettingsForwardedHeaders(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, headers_allow_lists: Optional[Sequence[_builtins.str]] = ..., option: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headersAllowLists")
    def headers_allow_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DistributionCacheBehaviorSettingsForwardedQueryStrings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, option: Optional[_builtins.bool] = ..., query_strings_allowed_lists: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def option(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryStringsAllowedLists")
    def query_strings_allowed_lists(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class DistributionDefaultCacheBehavior(dict):
    def __init__(__self__, *, behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DistributionLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, availability_zone: _builtins.str, region_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class DistributionOrigin(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, region_name: _builtins.str, protocol_policy: Optional[_builtins.str] = ..., resource_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regionName")
    def region_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolPolicy")
    def protocol_policy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InstanceAddOn(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, snapshot_time: _builtins.str, status: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InstancePublicPortsPortInfo(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, from_port: _builtins.int, protocol: _builtins.str, to_port: _builtins.int, cidr_list_aliases: Optional[Sequence[_builtins.str]] = ..., cidrs: Optional[Sequence[_builtins.str]] = ..., ipv6_cidrs: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrListAliases")
    def cidr_list_aliases(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Cidrs")
    def ipv6_cidrs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class LbCertificateDomainValidationRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., resource_record_name: Optional[_builtins.str] = ..., resource_record_type: Optional[_builtins.str] = ..., resource_record_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordName")
    def resource_record_name(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordType")
    def resource_record_type(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRecordValue")
    def resource_record_value(self) -> Optional[_builtins.str]:
        ...
    


