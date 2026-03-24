

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
__all__ = ['TlsInspectionConfigurationArgs', 'TlsInspectionConfiguration']
@pulumi.input_type
class TlsInspectionConfigurationArgs:
    def __init__(__self__, *, tls_inspection_configuration: pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs], description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfiguration")
    def tls_inspection_configuration(self) -> pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs]:
        
        ...
    
    @tls_inspection_configuration.setter
    def tls_inspection_configuration(self, value: pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]]): # -> None:
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _TlsInspectionConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authorities: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateAuthorityArgs]]]] = ..., certificates: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_associations: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]] = ..., tls_inspection_configuration: Optional[pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs]] = ..., tls_inspection_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., update_token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorities")
    def certificate_authorities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateAuthorityArgs]]]]:
        
        ...
    
    @certificate_authorities.setter
    def certificate_authorities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateAuthorityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateArgs]]]]:
        
        ...
    
    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationCertificateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]]:
        
        ...
    
    @encryption_configurations.setter
    def encryption_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TlsInspectionConfigurationEncryptionConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfAssociations")
    def number_of_associations(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_associations.setter
    def number_of_associations(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[TlsInspectionConfigurationTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfiguration")
    def tls_inspection_configuration(self) -> Optional[pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs]]:
        
        ...
    
    @tls_inspection_configuration.setter
    def tls_inspection_configuration(self, value: Optional[pulumi.Input[TlsInspectionConfigurationTlsInspectionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfigurationId")
    def tls_inspection_configuration_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tls_inspection_configuration_id.setter
    def tls_inspection_configuration_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_token.setter
    def update_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TlsInspectionConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TlsInspectionConfigurationEncryptionConfigurationArgs, TlsInspectionConfigurationEncryptionConfigurationArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[TlsInspectionConfigurationTimeoutsArgs, TlsInspectionConfigurationTimeoutsArgsDict]]] = ..., tls_inspection_configuration: Optional[pulumi.Input[Union[TlsInspectionConfigurationTlsInspectionConfigurationArgs, TlsInspectionConfigurationTlsInspectionConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TlsInspectionConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., certificate_authorities: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TlsInspectionConfigurationCertificateAuthorityArgs, TlsInspectionConfigurationCertificateAuthorityArgsDict]]]]] = ..., certificates: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TlsInspectionConfigurationCertificateArgs, TlsInspectionConfigurationCertificateArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., encryption_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TlsInspectionConfigurationEncryptionConfigurationArgs, TlsInspectionConfigurationEncryptionConfigurationArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., number_of_associations: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[TlsInspectionConfigurationTimeoutsArgs, TlsInspectionConfigurationTimeoutsArgsDict]]] = ..., tls_inspection_configuration: Optional[pulumi.Input[Union[TlsInspectionConfigurationTlsInspectionConfigurationArgs, TlsInspectionConfigurationTlsInspectionConfigurationArgsDict]]] = ..., tls_inspection_configuration_id: Optional[pulumi.Input[_builtins.str]] = ..., update_token: Optional[pulumi.Input[_builtins.str]] = ...) -> TlsInspectionConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorities")
    def certificate_authorities(self) -> pulumi.Output[Sequence[outputs.TlsInspectionConfigurationCertificateAuthority]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def certificates(self) -> pulumi.Output[Sequence[outputs.TlsInspectionConfigurationCertificate]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(self) -> pulumi.Output[Sequence[outputs.TlsInspectionConfigurationEncryptionConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfAssociations")
    def number_of_associations(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.TlsInspectionConfigurationTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfiguration")
    def tls_inspection_configuration(self) -> pulumi.Output[outputs.TlsInspectionConfigurationTlsInspectionConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsInspectionConfigurationId")
    def tls_inspection_configuration_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateToken")
    def update_token(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


