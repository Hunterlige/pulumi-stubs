

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], org_id: pulumi.Input[_builtins.str], access_logging_config: Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_range: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., peering_cidr_range: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLoggingConfig")
    def access_logging_config(self) -> Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]]:
        
        ...
    
    @access_logging_config.setter
    def access_logging_config(self, value: Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_accept_lists.setter
    def consumer_accept_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKeyName")
    def disk_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_key_name.setter
    def disk_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_range.setter
    def ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringCidrRange")
    def peering_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_cidr_range.setter
    def peering_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, access_logging_config: Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., ip_range: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., peering_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLoggingConfig")
    def access_logging_config(self) -> Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]]:
        
        ...
    
    @access_logging_config.setter
    def access_logging_config(self, value: Optional[pulumi.Input[InstanceAccessLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @consumer_accept_lists.setter
    def consumer_accept_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKeyName")
    def disk_encryption_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_encryption_key_name.setter
    def disk_encryption_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_range.setter
    def ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringCidrRange")
    def peering_cidr_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @peering_cidr_range.setter
    def peering_cidr_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:apigee/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_logging_config: Optional[pulumi.Input[Union[InstanceAccessLoggingConfigArgs, InstanceAccessLoggingConfigArgsDict]]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_range: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., peering_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_logging_config: Optional[pulumi.Input[Union[InstanceAccessLoggingConfigArgs, InstanceAccessLoggingConfigArgsDict]]] = ..., consumer_accept_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., host: Optional[pulumi.Input[_builtins.str]] = ..., ip_range: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., org_id: Optional[pulumi.Input[_builtins.str]] = ..., peering_cidr_range: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLoggingConfig")
    def access_logging_config(self) -> pulumi.Output[Optional[outputs.InstanceAccessLoggingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerAcceptLists")
    def consumer_accept_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKeyName")
    def disk_encryption_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringCidrRange")
    def peering_cidr_range(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


