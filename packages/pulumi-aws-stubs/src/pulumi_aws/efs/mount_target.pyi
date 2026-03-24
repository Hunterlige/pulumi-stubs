

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MountTargetArgs', 'MountTarget']
@pulumi.input_type
class MountTargetArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], subnet_id: pulumi.Input[_builtins.str], ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _MountTargetState:
    def __init__(__self__, *, availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., mount_target_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_id.setter
    def availability_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone_name.setter
    def availability_zone_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_arn.setter
    def file_system_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountTargetDnsName")
    def mount_target_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_target_dns_name.setter
    def mount_target_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:efs/mountTarget:MountTarget")
class MountTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MountTargetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., availability_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ..., dns_name: Optional[pulumi.Input[_builtins.str]] = ..., file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., ip_address_type: Optional[pulumi.Input[_builtins.str]] = ..., ipv6_address: Optional[pulumi.Input[_builtins.str]] = ..., mount_target_dns_name: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> MountTarget:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountTargetDnsName")
    def mount_target_dns_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


