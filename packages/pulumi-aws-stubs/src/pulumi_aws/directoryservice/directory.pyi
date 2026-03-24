

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
__all__ = ['DirectoryArgs', 'Directory']
@pulumi.input_type
class DirectoryArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], password: pulumi.Input[_builtins.str], alias: Optional[pulumi.Input[_builtins.str]] = ..., connect_settings: Optional[pulumi.Input[DirectoryConnectSettingsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., enable_sso: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_settings: Optional[pulumi.Input[DirectoryVpcSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectSettings")
    def connect_settings(self) -> Optional[pulumi.Input[DirectoryConnectSettingsArgs]]:
        
        ...
    
    @connect_settings.setter
    def connect_settings(self, value: Optional[pulumi.Input[DirectoryConnectSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_number_of_domain_controllers.setter
    def desired_number_of_domain_controllers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSso")
    def enable_sso(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_sso.setter
    def enable_sso(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> Optional[pulumi.Input[DirectoryVpcSettingsArgs]]:
        
        ...
    
    @vpc_settings.setter
    def vpc_settings(self, value: Optional[pulumi.Input[DirectoryVpcSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DirectoryState:
    def __init__(__self__, *, access_url: Optional[pulumi.Input[_builtins.str]] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., connect_settings: Optional[pulumi.Input[DirectoryConnectSettingsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., dns_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., enable_sso: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_settings: Optional[pulumi.Input[DirectoryVpcSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrl")
    def access_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_url.setter
    def access_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectSettings")
    def connect_settings(self) -> Optional[pulumi.Input[DirectoryConnectSettingsArgs]]:
        
        ...
    
    @connect_settings.setter
    def connect_settings(self, value: Optional[pulumi.Input[DirectoryConnectSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_number_of_domain_controllers.setter
    def desired_number_of_domain_controllers(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @dns_ip_addresses.setter
    def dns_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSso")
    def enable_sso(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_sso.setter
    def enable_sso(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @short_name.setter
    def short_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> Optional[pulumi.Input[DirectoryVpcSettingsArgs]]:
        
        ...
    
    @vpc_settings.setter
    def vpc_settings(self, value: Optional[pulumi.Input[DirectoryVpcSettingsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:directoryservice/directory:Directory")
class Directory(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., connect_settings: Optional[pulumi.Input[Union[DirectoryConnectSettingsArgs, DirectoryConnectSettingsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., enable_sso: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_settings: Optional[pulumi.Input[Union[DirectoryVpcSettingsArgs, DirectoryVpcSettingsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DirectoryArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_url: Optional[pulumi.Input[_builtins.str]] = ..., alias: Optional[pulumi.Input[_builtins.str]] = ..., connect_settings: Optional[pulumi.Input[Union[DirectoryConnectSettingsArgs, DirectoryConnectSettingsArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., desired_number_of_domain_controllers: Optional[pulumi.Input[_builtins.int]] = ..., dns_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., enable_sso: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., short_name: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_settings: Optional[pulumi.Input[Union[DirectoryVpcSettingsArgs, DirectoryVpcSettingsArgsDict]]] = ...) -> Directory:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessUrl")
    def access_url(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectSettings")
    def connect_settings(self) -> pulumi.Output[Optional[outputs.DirectoryConnectSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredNumberOfDomainControllers")
    def desired_number_of_domain_controllers(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsIpAddresses")
    def dns_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSso")
    def enable_sso(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shortName")
    def short_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[_builtins.str]:
        
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
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSettings")
    def vpc_settings(self) -> pulumi.Output[Optional[outputs.DirectoryVpcSettings]]:
        
        ...
    


