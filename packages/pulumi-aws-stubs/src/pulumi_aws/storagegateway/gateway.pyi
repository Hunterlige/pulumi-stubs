

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
__all__ = ['GatewayArgs', 'Gateway']
@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *, gateway_name: pulumi.Input[_builtins.str], gateway_timezone: pulumi.Input[_builtins.str], activation_key: Optional[pulumi.Input[_builtins.str]] = ..., average_download_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., average_upload_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., gateway_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_vpc_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_start_time: Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]] = ..., medium_changer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., smb_active_directory_settings: Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]] = ..., smb_file_share_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., smb_guest_password: Optional[pulumi.Input[_builtins.str]] = ..., smb_security_strategy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tape_drive_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayTimezone")
    def gateway_timezone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @gateway_timezone.setter
    def gateway_timezone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_key.setter
    def activation_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageDownloadRateLimitInBitsPerSec")
    def average_download_rate_limit_in_bits_per_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @average_download_rate_limit_in_bits_per_sec.setter
    def average_download_rate_limit_in_bits_per_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageUploadRateLimitInBitsPerSec")
    def average_upload_rate_limit_in_bits_per_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @average_upload_rate_limit_in_bits_per_sec.setter
    def average_upload_rate_limit_in_bits_per_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_ip_address.setter
    def gateway_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_type.setter
    def gateway_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_vpc_endpoint.setter
    def gateway_vpc_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceStartTime")
    def maintenance_start_time(self) -> Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]]:
        
        ...
    
    @maintenance_start_time.setter
    def maintenance_start_time(self, value: Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediumChangerType")
    def medium_changer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @medium_changer_type.setter
    def medium_changer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbActiveDirectorySettings")
    def smb_active_directory_settings(self) -> Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]]:
        
        ...
    
    @smb_active_directory_settings.setter
    def smb_active_directory_settings(self, value: Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbFileShareVisibility")
    def smb_file_share_visibility(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smb_file_share_visibility.setter
    def smb_file_share_visibility(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbGuestPassword")
    def smb_guest_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_guest_password.setter
    def smb_guest_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSecurityStrategy")
    def smb_security_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_security_strategy.setter
    def smb_security_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tapeDriveType")
    def tape_drive_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tape_drive_type.setter
    def tape_drive_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GatewayState:
    def __init__(__self__, *, activation_key: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., average_download_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., average_upload_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., ec2_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[GatewayGatewayNetworkInterfaceArgs]]]] = ..., gateway_timezone: Optional[pulumi.Input[_builtins.str]] = ..., gateway_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_vpc_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., host_environment: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_start_time: Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]] = ..., medium_changer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., smb_active_directory_settings: Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]] = ..., smb_file_share_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., smb_guest_password: Optional[pulumi.Input[_builtins.str]] = ..., smb_security_strategy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tape_drive_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_key.setter
    def activation_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageDownloadRateLimitInBitsPerSec")
    def average_download_rate_limit_in_bits_per_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @average_download_rate_limit_in_bits_per_sec.setter
    def average_download_rate_limit_in_bits_per_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageUploadRateLimitInBitsPerSec")
    def average_upload_rate_limit_in_bits_per_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @average_upload_rate_limit_in_bits_per_sec.setter
    def average_upload_rate_limit_in_bits_per_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceId")
    def ec2_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ec2_instance_id.setter
    def ec2_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_ip_address.setter
    def gateway_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayNetworkInterfaces")
    def gateway_network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GatewayGatewayNetworkInterfaceArgs]]]]:
        
        ...
    
    @gateway_network_interfaces.setter
    def gateway_network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GatewayGatewayNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayTimezone")
    def gateway_timezone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_timezone.setter
    def gateway_timezone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_type.setter
    def gateway_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gateway_vpc_endpoint.setter
    def gateway_vpc_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostEnvironment")
    def host_environment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_environment.setter
    def host_environment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceStartTime")
    def maintenance_start_time(self) -> Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]]:
        
        ...
    
    @maintenance_start_time.setter
    def maintenance_start_time(self, value: Optional[pulumi.Input[GatewayMaintenanceStartTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediumChangerType")
    def medium_changer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @medium_changer_type.setter
    def medium_changer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbActiveDirectorySettings")
    def smb_active_directory_settings(self) -> Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]]:
        
        ...
    
    @smb_active_directory_settings.setter
    def smb_active_directory_settings(self, value: Optional[pulumi.Input[GatewaySmbActiveDirectorySettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbFileShareVisibility")
    def smb_file_share_visibility(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @smb_file_share_visibility.setter
    def smb_file_share_visibility(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbGuestPassword")
    def smb_guest_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_guest_password.setter
    def smb_guest_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSecurityStrategy")
    def smb_security_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @smb_security_strategy.setter
    def smb_security_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="tapeDriveType")
    def tape_drive_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tape_drive_type.setter
    def tape_drive_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:storagegateway/gateway:Gateway")
class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., activation_key: Optional[pulumi.Input[_builtins.str]] = ..., average_download_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., average_upload_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_timezone: Optional[pulumi.Input[_builtins.str]] = ..., gateway_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_vpc_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_start_time: Optional[pulumi.Input[Union[GatewayMaintenanceStartTimeArgs, GatewayMaintenanceStartTimeArgsDict]]] = ..., medium_changer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., smb_active_directory_settings: Optional[pulumi.Input[Union[GatewaySmbActiveDirectorySettingsArgs, GatewaySmbActiveDirectorySettingsArgsDict]]] = ..., smb_file_share_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., smb_guest_password: Optional[pulumi.Input[_builtins.str]] = ..., smb_security_strategy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tape_drive_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GatewayArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., activation_key: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., average_download_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., average_upload_rate_limit_in_bits_per_sec: Optional[pulumi.Input[_builtins.int]] = ..., cloudwatch_log_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., ec2_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_id: Optional[pulumi.Input[_builtins.str]] = ..., gateway_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., gateway_network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[Union[GatewayGatewayNetworkInterfaceArgs, GatewayGatewayNetworkInterfaceArgsDict]]]]] = ..., gateway_timezone: Optional[pulumi.Input[_builtins.str]] = ..., gateway_type: Optional[pulumi.Input[_builtins.str]] = ..., gateway_vpc_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., host_environment: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_start_time: Optional[pulumi.Input[Union[GatewayMaintenanceStartTimeArgs, GatewayMaintenanceStartTimeArgsDict]]] = ..., medium_changer_type: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., smb_active_directory_settings: Optional[pulumi.Input[Union[GatewaySmbActiveDirectorySettingsArgs, GatewaySmbActiveDirectorySettingsArgsDict]]] = ..., smb_file_share_visibility: Optional[pulumi.Input[_builtins.bool]] = ..., smb_guest_password: Optional[pulumi.Input[_builtins.str]] = ..., smb_security_strategy: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tape_drive_type: Optional[pulumi.Input[_builtins.str]] = ...) -> Gateway:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationKey")
    def activation_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageDownloadRateLimitInBitsPerSec")
    def average_download_rate_limit_in_bits_per_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="averageUploadRateLimitInBitsPerSec")
    def average_upload_rate_limit_in_bits_per_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2InstanceId")
    def ec2_instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayNetworkInterfaces")
    def gateway_network_interfaces(self) -> pulumi.Output[Sequence[outputs.GatewayGatewayNetworkInterface]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayTimezone")
    def gateway_timezone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gatewayVpcEndpoint")
    def gateway_vpc_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostEnvironment")
    def host_environment(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceStartTime")
    def maintenance_start_time(self) -> pulumi.Output[outputs.GatewayMaintenanceStartTime]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediumChangerType")
    def medium_changer_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbActiveDirectorySettings")
    def smb_active_directory_settings(self) -> pulumi.Output[Optional[outputs.GatewaySmbActiveDirectorySettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbFileShareVisibility")
    def smb_file_share_visibility(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbGuestPassword")
    def smb_guest_password(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smbSecurityStrategy")
    def smb_security_strategy(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="tapeDriveType")
    def tape_drive_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


