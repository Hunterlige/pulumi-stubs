import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ResourceSetResource",
    "ResourceSetResourceDnsTargetResource",
    "ResourceSetResourceDnsTargetResourceTargetResource",
    ...,
    ...,
]

@pulumi.output_type
class ResourceSetResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_id: Optional[_builtins.str] = ...,
        dns_target_resource: Optional[
            outputs.ResourceSetResourceDnsTargetResource
        ] = ...,
        readiness_scopes: Optional[Sequence[_builtins.str]] = ...,
        resource_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsTargetResource")
    def dns_target_resource(
        self,
    ) -> Optional[outputs.ResourceSetResourceDnsTargetResource]: ...
    @_builtins.property
    @pulumi.getter(name="readinessScopes")
    def readiness_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceSetResourceDnsTargetResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        hosted_zone_arn: Optional[_builtins.str] = ...,
        record_set_id: Optional[_builtins.str] = ...,
        record_type: Optional[_builtins.str] = ...,
        target_resource: Optional[
            outputs.ResourceSetResourceDnsTargetResourceTargetResource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostedZoneArn")
    def hosted_zone_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordType")
    def record_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetResource")
    def target_resource(
        self,
    ) -> Optional[outputs.ResourceSetResourceDnsTargetResourceTargetResource]: ...

@pulumi.output_type
class ResourceSetResourceDnsTargetResourceTargetResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        nlb_resource: Optional[
            outputs.ResourceSetResourceDnsTargetResourceTargetResourceNlbResource
        ] = ...,
        r53_resource: Optional[
            outputs.ResourceSetResourceDnsTargetResourceTargetResourceR53Resource
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nlbResource")
    def nlb_resource(
        self,
    ) -> Optional[
        outputs.ResourceSetResourceDnsTargetResourceTargetResourceNlbResource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="r53Resource")
    def r53_resource(
        self,
    ) -> Optional[
        outputs.ResourceSetResourceDnsTargetResourceTargetResourceR53Resource
    ]: ...

@pulumi.output_type
class ResourceSetResourceDnsTargetResourceTargetResourceNlbResource(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceSetResourceDnsTargetResourceTargetResourceR53Resource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: Optional[_builtins.str] = ...,
        record_set_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recordSetId")
    def record_set_id(self) -> Optional[_builtins.str]: ...
