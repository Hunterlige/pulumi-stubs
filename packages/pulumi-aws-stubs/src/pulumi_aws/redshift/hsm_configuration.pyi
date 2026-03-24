

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HsmConfigurationArgs', 'HsmConfiguration']
@pulumi.input_type
class HsmConfigurationArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], hsm_configuration_identifier: pulumi.Input[_builtins.str], hsm_ip_address: pulumi.Input[_builtins.str], hsm_partition_name: pulumi.Input[_builtins.str], hsm_partition_password: pulumi.Input[_builtins.str], hsm_server_public_certificate: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hsm_configuration_identifier.setter
    def hsm_configuration_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmIpAddress")
    def hsm_ip_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hsm_ip_address.setter
    def hsm_ip_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionName")
    def hsm_partition_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hsm_partition_name.setter
    def hsm_partition_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionPassword")
    def hsm_partition_password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hsm_partition_password.setter
    def hsm_partition_password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmServerPublicCertificate")
    def hsm_server_public_certificate(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hsm_server_public_certificate.setter
    def hsm_server_public_certificate(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


@pulumi.input_type
class _HsmConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., hsm_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ..., hsm_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_name: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_password: Optional[pulumi.Input[_builtins.str]] = ..., hsm_server_public_certificate: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hsm_configuration_identifier.setter
    def hsm_configuration_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmIpAddress")
    def hsm_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hsm_ip_address.setter
    def hsm_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionName")
    def hsm_partition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hsm_partition_name.setter
    def hsm_partition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionPassword")
    def hsm_partition_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hsm_partition_password.setter
    def hsm_partition_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmServerPublicCertificate")
    def hsm_server_public_certificate(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hsm_server_public_certificate.setter
    def hsm_server_public_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:redshift/hsmConfiguration:HsmConfiguration")
class HsmConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., hsm_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ..., hsm_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_name: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_password: Optional[pulumi.Input[_builtins.str]] = ..., hsm_server_public_certificate: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: HsmConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., hsm_configuration_identifier: Optional[pulumi.Input[_builtins.str]] = ..., hsm_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_name: Optional[pulumi.Input[_builtins.str]] = ..., hsm_partition_password: Optional[pulumi.Input[_builtins.str]] = ..., hsm_server_public_certificate: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> HsmConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmConfigurationIdentifier")
    def hsm_configuration_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmIpAddress")
    def hsm_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionName")
    def hsm_partition_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmPartitionPassword")
    def hsm_partition_password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hsmServerPublicCertificate")
    def hsm_server_public_certificate(self) -> pulumi.Output[_builtins.str]:
        
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
    


