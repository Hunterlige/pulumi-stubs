

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
__all__ = ['ReplicationInstanceArgs', 'ReplicationInstance']
@pulumi.input_type
class ReplicationInstanceArgs:
    def __init__(__self__, *, replication_instance_class: pulumi.Input[_builtins.str], replication_instance_id: pulumi.Input[_builtins.str], allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., dns_name_servers: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kerberos_authentication_settings: Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replication_instance_class.setter
    def replication_instance_class(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceId")
    def replication_instance_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @replication_instance_id.setter
    def replication_instance_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNameServers")
    def dns_name_servers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name_servers.setter
    def dns_name_servers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosAuthenticationSettings")
    def kerberos_authentication_settings(self) -> Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]]:
        
        ...
    
    @kerberos_authentication_settings.setter
    def kerberos_authentication_settings(self, value: Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ReplicationInstanceState:
    def __init__(__self__, *, allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., dns_name_servers: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kerberos_authentication_settings: Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_class: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_instance_public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNameServers")
    def dns_name_servers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_name_servers.setter
    def dns_name_servers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosAuthenticationSettings")
    def kerberos_authentication_settings(self) -> Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]]:
        
        ...
    
    @kerberos_authentication_settings.setter
    def kerberos_authentication_settings(self, value: Optional[pulumi.Input[ReplicationInstanceKerberosAuthenticationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_instance_arn.setter
    def replication_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_instance_class.setter
    def replication_instance_class(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceId")
    def replication_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_instance_id.setter
    def replication_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstancePrivateIps")
    def replication_instance_private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replication_instance_private_ips.setter
    def replication_instance_private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstancePublicIps")
    def replication_instance_public_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replication_instance_public_ips.setter
    def replication_instance_public_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @replication_subnet_group_id.setter
    def replication_subnet_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:dms/replicationInstance:ReplicationInstance")
class ReplicationInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., dns_name_servers: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kerberos_authentication_settings: Optional[pulumi.Input[Union[ReplicationInstanceKerberosAuthenticationSettingsArgs, ReplicationInstanceKerberosAuthenticationSettingsArgsDict]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_class: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ReplicationInstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., allow_major_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., dns_name_servers: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kerberos_authentication_settings: Optional[pulumi.Input[Union[ReplicationInstanceKerberosAuthenticationSettingsArgs, ReplicationInstanceKerberosAuthenticationSettingsArgsDict]]] = ..., kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., multi_az: Optional[pulumi.Input[_builtins.bool]] = ..., network_type: Optional[pulumi.Input[_builtins.str]] = ..., preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_class: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., replication_instance_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_instance_public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., replication_subnet_group_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> ReplicationInstance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsNameServers")
    def dns_name_servers(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kerberosAuthenticationSettings")
    def kerberos_authentication_settings(self) -> pulumi.Output[Optional[outputs.ReplicationInstanceKerberosAuthenticationSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceArn")
    def replication_instance_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceClass")
    def replication_instance_class(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstanceId")
    def replication_instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstancePrivateIps")
    def replication_instance_private_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationInstancePublicIps")
    def replication_instance_public_ips(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSubnetGroupId")
    def replication_subnet_group_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


