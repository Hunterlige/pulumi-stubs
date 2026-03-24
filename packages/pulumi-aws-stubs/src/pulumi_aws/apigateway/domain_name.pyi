import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainNameArgs", "DomainName"]

@pulumi.input_type
class DomainNameArgs:
    def __init__(
        __self__,
        *,
        domain_name: pulumi.Input[_builtins.str],
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_body: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[DomainNameEndpointConfigurationArgs]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[DomainNameMutualTlsAuthenticationArgs]
        ] = ...,
        ownership_verification_certificate_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]: ...
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_body.setter
    def certificate_body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificatePrivateKey")
    def certificate_private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_private_key.setter
    def certificate_private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointAccessMode")
    def endpoint_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_access_mode.setter
    def endpoint_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> Optional[pulumi.Input[DomainNameEndpointConfigurationArgs]]: ...
    @endpoint_configuration.setter
    def endpoint_configuration(
        self, value: Optional[pulumi.Input[DomainNameEndpointConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]: ...
    @mutual_tls_authentication.setter
    def mutual_tls_authentication(
        self, value: Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_certificate_arn.setter
    def regional_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateName")
    def regional_certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_certificate_name.setter
    def regional_certificate_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _DomainNameState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_body: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_upload_date: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfront_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfront_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[DomainNameEndpointConfigurationArgs]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[DomainNameMutualTlsAuthenticationArgs]
        ] = ...,
        ownership_verification_certificate_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_body.setter
    def certificate_body(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_chain.setter
    def certificate_chain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificatePrivateKey")
    def certificate_private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_private_key.setter
    def certificate_private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateUploadDate")
    def certificate_upload_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_upload_date.setter
    def certificate_upload_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontDomainName")
    def cloudfront_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudfront_domain_name.setter
    def cloudfront_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontZoneId")
    def cloudfront_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloudfront_zone_id.setter
    def cloudfront_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name_id.setter
    def domain_name_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointAccessMode")
    def endpoint_access_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_access_mode.setter
    def endpoint_access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> Optional[pulumi.Input[DomainNameEndpointConfigurationArgs]]: ...
    @endpoint_configuration.setter
    def endpoint_configuration(
        self, value: Optional[pulumi.Input[DomainNameEndpointConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]: ...
    @mutual_tls_authentication.setter
    def mutual_tls_authentication(
        self, value: Optional[pulumi.Input[DomainNameMutualTlsAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_certificate_arn.setter
    def regional_certificate_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateName")
    def regional_certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_certificate_name.setter
    def regional_certificate_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_domain_name.setter
    def regional_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regionalZoneId")
    def regional_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_zone_id.setter
    def regional_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routing_mode.setter
    def routing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:apigateway/domainName:DomainName")
class DomainName(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_body: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    DomainNameEndpointConfigurationArgs,
                    DomainNameEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[
                Union[
                    DomainNameMutualTlsAuthenticationArgs,
                    DomainNameMutualTlsAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        ownership_verification_certificate_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainNameArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_body: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_chain: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_upload_date: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfront_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cloudfront_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name_id: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_access_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_configuration: Optional[
            pulumi.Input[
                Union[
                    DomainNameEndpointConfigurationArgs,
                    DomainNameEndpointConfigurationArgsDict,
                ]
            ]
        ] = ...,
        mutual_tls_authentication: Optional[
            pulumi.Input[
                Union[
                    DomainNameMutualTlsAuthenticationArgs,
                    DomainNameMutualTlsAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        ownership_verification_certificate_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        regional_zone_id: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> DomainName: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateBody")
    def certificate_body(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateChain")
    def certificate_chain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificatePrivateKey")
    def certificate_private_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="certificateUploadDate")
    def certificate_upload_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontDomainName")
    def cloudfront_domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cloudfrontZoneId")
    def cloudfront_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainNameId")
    def domain_name_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointAccessMode")
    def endpoint_access_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> pulumi.Output[outputs.DomainNameEndpointConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainNameMutualTlsAuthentication]]: ...
    @_builtins.property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(
        self,
    ) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="regionalCertificateName")
    def regional_certificate_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regionalZoneId")
    def regional_zone_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingMode")
    def routing_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
