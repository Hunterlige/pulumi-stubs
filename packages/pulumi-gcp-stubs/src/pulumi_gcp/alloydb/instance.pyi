

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
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, cluster: pulumi.Input[_builtins.str], instance_id: pulumi.Input[_builtins.str], instance_type: pulumi.Input[_builtins.str], activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., availability_type: Optional[pulumi.Input[_builtins.str]] = ..., client_connection_config: Optional[pulumi.Input[InstanceClientConnectionConfigArgs]] = ..., connection_pool_config: Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]] = ..., database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., gce_zone: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_config: Optional[pulumi.Input[InstanceMachineConfigArgs]] = ..., network_config: Optional[pulumi.Input[InstanceNetworkConfigArgs]] = ..., observability_config: Optional[pulumi.Input[InstanceObservabilityConfigArgs]] = ..., psc_instance_config: Optional[pulumi.Input[InstancePscInstanceConfigArgs]] = ..., query_insights_config: Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]] = ..., read_pool_config: Optional[pulumi.Input[InstanceReadPoolConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_policy.setter
    def activation_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_type.setter
    def availability_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConnectionConfig")
    def client_connection_config(self) -> Optional[pulumi.Input[InstanceClientConnectionConfigArgs]]:
        
        ...
    
    @client_connection_config.setter
    def client_connection_config(self, value: Optional[pulumi.Input[InstanceClientConnectionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]]:
        
        ...
    
    @connection_pool_config.setter
    def connection_pool_config(self, value: Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_flags.setter
    def database_flags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceZone")
    def gce_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gce_zone.setter
    def gce_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineConfig")
    def machine_config(self) -> Optional[pulumi.Input[InstanceMachineConfigArgs]]:
        
        ...
    
    @machine_config.setter
    def machine_config(self, value: Optional[pulumi.Input[InstanceMachineConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[InstanceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[InstanceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityConfig")
    def observability_config(self) -> Optional[pulumi.Input[InstanceObservabilityConfigArgs]]:
        
        ...
    
    @observability_config.setter
    def observability_config(self, value: Optional[pulumi.Input[InstanceObservabilityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscInstanceConfig")
    def psc_instance_config(self) -> Optional[pulumi.Input[InstancePscInstanceConfigArgs]]:
        
        ...
    
    @psc_instance_config.setter
    def psc_instance_config(self, value: Optional[pulumi.Input[InstancePscInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsConfig")
    def query_insights_config(self) -> Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]]:
        
        ...
    
    @query_insights_config.setter
    def query_insights_config(self, value: Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolConfig")
    def read_pool_config(self) -> Optional[pulumi.Input[InstanceReadPoolConfigArgs]]:
        
        ...
    
    @read_pool_config.setter
    def read_pool_config(self, value: Optional[pulumi.Input[InstanceReadPoolConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., availability_type: Optional[pulumi.Input[_builtins.str]] = ..., client_connection_config: Optional[pulumi.Input[InstanceClientConnectionConfigArgs]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_config: Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gce_zone: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_config: Optional[pulumi.Input[InstanceMachineConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[InstanceNetworkConfigArgs]] = ..., observability_config: Optional[pulumi.Input[InstanceObservabilityConfigArgs]] = ..., outbound_public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., psc_instance_config: Optional[pulumi.Input[InstancePscInstanceConfigArgs]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., query_insights_config: Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]] = ..., read_pool_config: Optional[pulumi.Input[InstanceReadPoolConfigArgs]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @activation_policy.setter
    def activation_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_type.setter
    def availability_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConnectionConfig")
    def client_connection_config(self) -> Optional[pulumi.Input[InstanceClientConnectionConfigArgs]]:
        
        ...
    
    @client_connection_config.setter
    def client_connection_config(self, value: Optional[pulumi.Input[InstanceClientConnectionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]]:
        
        ...
    
    @connection_pool_config.setter
    def connection_pool_config(self, value: Optional[pulumi.Input[InstanceConnectionPoolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @database_flags.setter
    def database_flags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceZone")
    def gce_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gce_zone.setter
    def gce_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineConfig")
    def machine_config(self) -> Optional[pulumi.Input[InstanceMachineConfigArgs]]:
        
        ...
    
    @machine_config.setter
    def machine_config(self, value: Optional[pulumi.Input[InstanceMachineConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[InstanceNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[InstanceNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityConfig")
    def observability_config(self) -> Optional[pulumi.Input[InstanceObservabilityConfigArgs]]:
        
        ...
    
    @observability_config.setter
    def observability_config(self, value: Optional[pulumi.Input[InstanceObservabilityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundPublicIpAddresses")
    def outbound_public_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @outbound_public_ip_addresses.setter
    def outbound_public_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscInstanceConfig")
    def psc_instance_config(self) -> Optional[pulumi.Input[InstancePscInstanceConfigArgs]]:
        
        ...
    
    @psc_instance_config.setter
    def psc_instance_config(self, value: Optional[pulumi.Input[InstancePscInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsConfig")
    def query_insights_config(self) -> Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]]:
        
        ...
    
    @query_insights_config.setter
    def query_insights_config(self, value: Optional[pulumi.Input[InstanceQueryInsightsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolConfig")
    def read_pool_config(self) -> Optional[pulumi.Input[InstanceReadPoolConfigArgs]]:
        
        ...
    
    @read_pool_config.setter
    def read_pool_config(self, value: Optional[pulumi.Input[InstanceReadPoolConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:alloydb/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., availability_type: Optional[pulumi.Input[_builtins.str]] = ..., client_connection_config: Optional[pulumi.Input[Union[InstanceClientConnectionConfigArgs, InstanceClientConnectionConfigArgsDict]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_config: Optional[pulumi.Input[Union[InstanceConnectionPoolConfigArgs, InstanceConnectionPoolConfigArgsDict]]] = ..., database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., gce_zone: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_config: Optional[pulumi.Input[Union[InstanceMachineConfigArgs, InstanceMachineConfigArgsDict]]] = ..., network_config: Optional[pulumi.Input[Union[InstanceNetworkConfigArgs, InstanceNetworkConfigArgsDict]]] = ..., observability_config: Optional[pulumi.Input[Union[InstanceObservabilityConfigArgs, InstanceObservabilityConfigArgsDict]]] = ..., psc_instance_config: Optional[pulumi.Input[Union[InstancePscInstanceConfigArgs, InstancePscInstanceConfigArgsDict]]] = ..., query_insights_config: Optional[pulumi.Input[Union[InstanceQueryInsightsConfigArgs, InstanceQueryInsightsConfigArgsDict]]] = ..., read_pool_config: Optional[pulumi.Input[Union[InstanceReadPoolConfigArgs, InstanceReadPoolConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., activation_policy: Optional[pulumi.Input[_builtins.str]] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., availability_type: Optional[pulumi.Input[_builtins.str]] = ..., client_connection_config: Optional[pulumi.Input[Union[InstanceClientConnectionConfigArgs, InstanceClientConnectionConfigArgsDict]]] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., connection_pool_config: Optional[pulumi.Input[Union[InstanceConnectionPoolConfigArgs, InstanceConnectionPoolConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., database_flags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gce_zone: Optional[pulumi.Input[_builtins.str]] = ..., instance_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., machine_config: Optional[pulumi.Input[Union[InstanceMachineConfigArgs, InstanceMachineConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[InstanceNetworkConfigArgs, InstanceNetworkConfigArgsDict]]] = ..., observability_config: Optional[pulumi.Input[Union[InstanceObservabilityConfigArgs, InstanceObservabilityConfigArgsDict]]] = ..., outbound_public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., psc_instance_config: Optional[pulumi.Input[Union[InstancePscInstanceConfigArgs, InstancePscInstanceConfigArgsDict]]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., query_insights_config: Optional[pulumi.Input[Union[InstanceQueryInsightsConfigArgs, InstanceQueryInsightsConfigArgsDict]]] = ..., read_pool_config: Optional[pulumi.Input[Union[InstanceReadPoolConfigArgs, InstanceReadPoolConfigArgsDict]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activationPolicy")
    def activation_policy(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityType")
    def availability_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientConnectionConfig")
    def client_connection_config(self) -> pulumi.Output[outputs.InstanceClientConnectionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionPoolConfig")
    def connection_pool_config(self) -> pulumi.Output[Optional[outputs.InstanceConnectionPoolConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseFlags")
    def database_flags(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceZone")
    def gce_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineConfig")
    def machine_config(self) -> pulumi.Output[outputs.InstanceMachineConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.InstanceNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityConfig")
    def observability_config(self) -> pulumi.Output[outputs.InstanceObservabilityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundPublicIpAddresses")
    def outbound_public_ip_addresses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pscInstanceConfig")
    def psc_instance_config(self) -> pulumi.Output[outputs.InstancePscInstanceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryInsightsConfig")
    def query_insights_config(self) -> pulumi.Output[outputs.InstanceQueryInsightsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readPoolConfig")
    def read_pool_config(self) -> pulumi.Output[Optional[outputs.InstanceReadPoolConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


