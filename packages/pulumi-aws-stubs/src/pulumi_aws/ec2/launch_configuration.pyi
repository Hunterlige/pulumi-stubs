

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
__all__ = ['LaunchConfigurationArgs', 'LaunchConfiguration']
@pulumi.input_type
class LaunchConfigurationArgs:
    def __init__(__self__, *, image_id: pulumi.Input[_builtins.str], instance_type: pulumi.Input[_builtins.str], associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_options: Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_tenancy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image_id.setter
    def image_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]]:
        
        ...
    
    @ebs_block_devices.setter
    def ebs_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMonitoring")
    def enable_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_monitoring.setter
    def enable_monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]]:
        
        ...
    
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_tenancy.setter
    def placement_tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]]:
        
        ...
    
    @root_block_device.setter
    def root_block_device(self, value: Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _LaunchConfigurationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_options: Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_tenancy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]]:
        
        ...
    
    @ebs_block_devices.setter
    def ebs_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEbsBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMonitoring")
    def enable_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_monitoring.setter
    def enable_monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]]:
        
        ...
    
    @ephemeral_block_devices.setter
    def ephemeral_block_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LaunchConfigurationEphemeralBlockDeviceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_instance_profile.setter
    def iam_instance_profile(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]]:
        
        ...
    
    @metadata_options.setter
    def metadata_options(self, value: Optional[pulumi.Input[LaunchConfigurationMetadataOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_tenancy.setter
    def placement_tenancy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]]:
        
        ...
    
    @root_block_device.setter
    def root_block_device(self, value: Optional[pulumi.Input[LaunchConfigurationRootBlockDeviceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_price.setter
    def spot_price(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_data_base64.setter
    def user_data_base64(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/launchConfiguration:LaunchConfiguration")
class LaunchConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchConfigurationEbsBlockDeviceArgs, LaunchConfigurationEbsBlockDeviceArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchConfigurationEphemeralBlockDeviceArgs, LaunchConfigurationEphemeralBlockDeviceArgsDict]]]]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_options: Optional[pulumi.Input[Union[LaunchConfigurationMetadataOptionsArgs, LaunchConfigurationMetadataOptionsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_tenancy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[Union[LaunchConfigurationRootBlockDeviceArgs, LaunchConfigurationRootBlockDeviceArgsDict]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LaunchConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., associate_public_ip_address: Optional[pulumi.Input[_builtins.bool]] = ..., ebs_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchConfigurationEbsBlockDeviceArgs, LaunchConfigurationEbsBlockDeviceArgsDict]]]]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., enable_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., ephemeral_block_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LaunchConfigurationEphemeralBlockDeviceArgs, LaunchConfigurationEphemeralBlockDeviceArgsDict]]]]] = ..., iam_instance_profile: Optional[pulumi.Input[_builtins.str]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., key_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata_options: Optional[pulumi.Input[Union[LaunchConfigurationMetadataOptionsArgs, LaunchConfigurationMetadataOptionsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., name_prefix: Optional[pulumi.Input[_builtins.str]] = ..., placement_tenancy: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_block_device: Optional[pulumi.Input[Union[LaunchConfigurationRootBlockDeviceArgs, LaunchConfigurationRootBlockDeviceArgsDict]]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., spot_price: Optional[pulumi.Input[_builtins.str]] = ..., user_data: Optional[pulumi.Input[_builtins.str]] = ..., user_data_base64: Optional[pulumi.Input[_builtins.str]] = ...) -> LaunchConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsBlockDevices")
    def ebs_block_devices(self) -> pulumi.Output[Sequence[outputs.LaunchConfigurationEbsBlockDevice]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMonitoring")
    def enable_monitoring(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralBlockDevices")
    def ephemeral_block_devices(self) -> pulumi.Output[Optional[Sequence[outputs.LaunchConfigurationEphemeralBlockDevice]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamInstanceProfile")
    def iam_instance_profile(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataOptions")
    def metadata_options(self) -> pulumi.Output[outputs.LaunchConfigurationMetadataOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementTenancy")
    def placement_tenancy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootBlockDevice")
    def root_block_device(self) -> pulumi.Output[outputs.LaunchConfigurationRootBlockDevice]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDataBase64")
    def user_data_base64(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


