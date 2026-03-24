

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DomainConfigurationArgs', 'DomainConfiguration']
@pulumi.input_type
class DomainConfigurationArgs:
    def __init__(__self__, *, application_protocol: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_config: Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_config: Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]] = ..., validation_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProtocol")
    def application_protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_protocol.setter
    def application_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfig")
    def authorizer_config(self) -> Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]]:
        
        ...
    
    @authorizer_config.setter
    def authorizer_config(self, value: Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificateArns")
    def server_certificate_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @server_certificate_arns.setter
    def server_certificate_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationCertificateArn")
    def validation_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @validation_certificate_arn.setter
    def validation_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _DomainConfigurationState:
    def __init__(__self__, *, application_protocol: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_config: Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_config: Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]] = ..., validation_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProtocol")
    def application_protocol(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_protocol.setter
    def application_protocol(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfig")
    def authorizer_config(self) -> Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]]:
        
        ...
    
    @authorizer_config.setter
    def authorizer_config(self, value: Optional[pulumi.Input[DomainConfigurationAuthorizerConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainType")
    def domain_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_type.setter
    def domain_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificateArns")
    def server_certificate_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @server_certificate_arns.setter
    def server_certificate_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_type.setter
    def service_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[DomainConfigurationTlsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationCertificateArn")
    def validation_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @validation_certificate_arn.setter
    def validation_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:iot/domainConfiguration:DomainConfiguration")
class DomainConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., application_protocol: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_config: Optional[pulumi.Input[Union[DomainConfigurationAuthorizerConfigArgs, DomainConfigurationAuthorizerConfigArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_config: Optional[pulumi.Input[Union[DomainConfigurationTlsConfigArgs, DomainConfigurationTlsConfigArgsDict]]] = ..., validation_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[DomainConfigurationArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., application_protocol: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., authorizer_config: Optional[pulumi.Input[Union[DomainConfigurationAuthorizerConfigArgs, DomainConfigurationAuthorizerConfigArgsDict]]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_type: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_certificate_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., service_type: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tls_config: Optional[pulumi.Input[Union[DomainConfigurationTlsConfigArgs, DomainConfigurationTlsConfigArgsDict]]] = ..., validation_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> DomainConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationProtocol")
    def application_protocol(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizerConfig")
    def authorizer_config(self) -> pulumi.Output[Optional[outputs.DomainConfigurationAuthorizerConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainType")
    def domain_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverCertificateArns")
    def server_certificate_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceType")
    def service_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> pulumi.Output[outputs.DomainConfigurationTlsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationCertificateArn")
    def validation_certificate_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


