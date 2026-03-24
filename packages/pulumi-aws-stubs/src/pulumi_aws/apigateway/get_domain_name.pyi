import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDomainNameResult",
    "AwaitableGetDomainNameResult",
    "get_domain_name",
    "get_domain_name_output",
]

@pulumi.output_type
class GetDomainNameResult:
    def __init__(
        __self__,
        arn=...,
        certificate_arn=...,
        certificate_name=...,
        certificate_upload_date=...,
        cloudfront_domain_name=...,
        cloudfront_zone_id=...,
        domain_name=...,
        domain_name_id=...,
        endpoint_access_mode=...,
        endpoint_configurations=...,
        id=...,
        policy=...,
        region=...,
        regional_certificate_arn=...,
        regional_certificate_name=...,
        regional_domain_name=...,
        regional_zone_id=...,
        security_policy=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateUploadDate")
    def certificate_upload_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontDomainName")
    def cloudfront_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontZoneId")
    def cloudfront_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointAccessMode")
    def endpoint_access_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointConfigurations")
    def endpoint_configurations(
        self,
    ) -> Sequence[outputs.GetDomainNameEndpointConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateName")
    def regional_certificate_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="regionalZoneId")
    def regional_zone_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetDomainNameResult(GetDomainNameResult):
    def __await__(self): ...

def get_domain_name(
    domain_name: Optional[_builtins.str] = ...,
    domain_name_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDomainNameResult: ...
def get_domain_name_output(
    domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    domain_name_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDomainNameResult]: ...
