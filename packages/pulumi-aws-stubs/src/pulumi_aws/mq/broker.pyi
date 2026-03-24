

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
__all__ = ['BrokerArgs', 'Broker']
@pulumi.input_type
class BrokerArgs:
    def __init__(__self__, *, engine_type: pulumi.Input[_builtins.str], engine_version: pulumi.Input[_builtins.str], host_instance_type: pulumi.Input[_builtins.str], users: pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]], apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., authentication_strategy: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[BrokerConfigurationArgs]] = ..., data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., data_replication_primary_broker_arn: Optional[pulumi.Input[_builtins.str]] = ..., deployment_mode: Optional[pulumi.Input[_builtins.str]] = ..., encryption_options: Optional[pulumi.Input[BrokerEncryptionOptionsArgs]] = ..., ldap_server_metadata: Optional[pulumi.Input[BrokerLdapServerMetadataArgs]] = ..., logs: Optional[pulumi.Input[BrokerLogsArgs]] = ..., maintenance_window_start_time: Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @engine_type.setter
    def engine_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_instance_type.setter
    def host_instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]]:
        
        ...
    
    @users.setter
    def users(self, value: pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_strategy.setter
    def authentication_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @broker_name.setter
    def broker_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[BrokerConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[BrokerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationMode")
    def data_replication_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_replication_mode.setter
    def data_replication_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationPrimaryBrokerArn")
    def data_replication_primary_broker_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_replication_primary_broker_arn.setter
    def data_replication_primary_broker_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_mode.setter
    def deployment_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> Optional[pulumi.Input[BrokerEncryptionOptionsArgs]]:
        
        ...
    
    @encryption_options.setter
    def encryption_options(self, value: Optional[pulumi.Input[BrokerEncryptionOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapServerMetadata")
    def ldap_server_metadata(self) -> Optional[pulumi.Input[BrokerLdapServerMetadataArgs]]:
        
        ...
    
    @ldap_server_metadata.setter
    def ldap_server_metadata(self, value: Optional[pulumi.Input[BrokerLdapServerMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[BrokerLogsArgs]]:
        
        ...
    
    @logs.setter
    def logs(self, value: Optional[pulumi.Input[BrokerLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]]:
        
        ...
    
    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self, value: Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]]): # -> None:
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
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _BrokerState:
    def __init__(__self__, *, apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_strategy: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[BrokerConfigurationArgs]] = ..., data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., data_replication_primary_broker_arn: Optional[pulumi.Input[_builtins.str]] = ..., deployment_mode: Optional[pulumi.Input[_builtins.str]] = ..., encryption_options: Optional[pulumi.Input[BrokerEncryptionOptionsArgs]] = ..., engine_type: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., host_instance_type: Optional[pulumi.Input[_builtins.str]] = ..., instances: Optional[pulumi.Input[Sequence[pulumi.Input[BrokerInstanceArgs]]]] = ..., ldap_server_metadata: Optional[pulumi.Input[BrokerLdapServerMetadataArgs]] = ..., logs: Optional[pulumi.Input[BrokerLogsArgs]] = ..., maintenance_window_start_time: Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]] = ..., pending_data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., users: Optional[pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_strategy.setter
    def authentication_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @broker_name.setter
    def broker_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[BrokerConfigurationArgs]]:
        
        ...
    
    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[BrokerConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationMode")
    def data_replication_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_replication_mode.setter
    def data_replication_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationPrimaryBrokerArn")
    def data_replication_primary_broker_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_replication_primary_broker_arn.setter
    def data_replication_primary_broker_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_mode.setter
    def deployment_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> Optional[pulumi.Input[BrokerEncryptionOptionsArgs]]:
        
        ...
    
    @encryption_options.setter
    def encryption_options(self, value: Optional[pulumi.Input[BrokerEncryptionOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_type.setter
    def engine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_instance_type.setter
    def host_instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BrokerInstanceArgs]]]]:
        
        ...
    
    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BrokerInstanceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapServerMetadata")
    def ldap_server_metadata(self) -> Optional[pulumi.Input[BrokerLdapServerMetadataArgs]]:
        
        ...
    
    @ldap_server_metadata.setter
    def ldap_server_metadata(self, value: Optional[pulumi.Input[BrokerLdapServerMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[BrokerLogsArgs]]:
        
        ...
    
    @logs.setter
    def logs(self, value: Optional[pulumi.Input[BrokerLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]]:
        
        ...
    
    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self, value: Optional[pulumi.Input[BrokerMaintenanceWindowStartTimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingDataReplicationMode")
    def pending_data_replication_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pending_data_replication_mode.setter
    def pending_data_replication_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]]]:
        
        ...
    
    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BrokerUserArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:mq/broker:Broker")
class Broker(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., authentication_strategy: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[Union[BrokerConfigurationArgs, BrokerConfigurationArgsDict]]] = ..., data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., data_replication_primary_broker_arn: Optional[pulumi.Input[_builtins.str]] = ..., deployment_mode: Optional[pulumi.Input[_builtins.str]] = ..., encryption_options: Optional[pulumi.Input[Union[BrokerEncryptionOptionsArgs, BrokerEncryptionOptionsArgsDict]]] = ..., engine_type: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., host_instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ldap_server_metadata: Optional[pulumi.Input[Union[BrokerLdapServerMetadataArgs, BrokerLdapServerMetadataArgsDict]]] = ..., logs: Optional[pulumi.Input[Union[BrokerLogsArgs, BrokerLogsArgsDict]]] = ..., maintenance_window_start_time: Optional[pulumi.Input[Union[BrokerMaintenanceWindowStartTimeArgs, BrokerMaintenanceWindowStartTimeArgsDict]]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., users: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BrokerUserArgs, BrokerUserArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BrokerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., authentication_strategy: Optional[pulumi.Input[_builtins.str]] = ..., auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ..., broker_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration: Optional[pulumi.Input[Union[BrokerConfigurationArgs, BrokerConfigurationArgsDict]]] = ..., data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., data_replication_primary_broker_arn: Optional[pulumi.Input[_builtins.str]] = ..., deployment_mode: Optional[pulumi.Input[_builtins.str]] = ..., encryption_options: Optional[pulumi.Input[Union[BrokerEncryptionOptionsArgs, BrokerEncryptionOptionsArgsDict]]] = ..., engine_type: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., host_instance_type: Optional[pulumi.Input[_builtins.str]] = ..., instances: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BrokerInstanceArgs, BrokerInstanceArgsDict]]]]] = ..., ldap_server_metadata: Optional[pulumi.Input[Union[BrokerLdapServerMetadataArgs, BrokerLdapServerMetadataArgsDict]]] = ..., logs: Optional[pulumi.Input[Union[BrokerLogsArgs, BrokerLogsArgsDict]]] = ..., maintenance_window_start_time: Optional[pulumi.Input[Union[BrokerMaintenanceWindowStartTimeArgs, BrokerMaintenanceWindowStartTimeArgsDict]]] = ..., pending_data_replication_mode: Optional[pulumi.Input[_builtins.str]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., users: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BrokerUserArgs, BrokerUserArgsDict]]]]] = ...) -> Broker:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationStrategy")
    def authentication_strategy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerName")
    def broker_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[outputs.BrokerConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationMode")
    def data_replication_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataReplicationPrimaryBrokerArn")
    def data_replication_primary_broker_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionOptions")
    def encryption_options(self) -> pulumi.Output[Optional[outputs.BrokerEncryptionOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostInstanceType")
    def host_instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence[outputs.BrokerInstance]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ldapServerMetadata")
    def ldap_server_metadata(self) -> pulumi.Output[Optional[outputs.BrokerLdapServerMetadata]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Optional[outputs.BrokerLogs]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> pulumi.Output[outputs.BrokerMaintenanceWindowStartTime]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pendingDataReplicationMode")
    def pending_data_replication_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    def users(self) -> pulumi.Output[Sequence[outputs.BrokerUser]]:
        
        ...
    


