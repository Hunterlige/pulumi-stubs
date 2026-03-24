

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
__all__ = ['MigrationJobArgs', 'MigrationJob']
@pulumi.input_type
class MigrationJobArgs:
    def __init__(__self__, *, destination: pulumi.Input[_builtins.str], migration_job_id: pulumi.Input[_builtins.str], source: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ..., dump_flags: Optional[pulumi.Input[MigrationJobDumpFlagsArgs]] = ..., dump_path: Optional[pulumi.Input[_builtins.str]] = ..., dump_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., performance_config: Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reverse_ssh_connectivity: Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]] = ..., static_ip_connectivity: Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]] = ..., vpc_peering_connectivity: Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationJobId")
    def migration_job_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @migration_job_id.setter
    def migration_job_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFlags")
    def dump_flags(self) -> Optional[pulumi.Input[MigrationJobDumpFlagsArgs]]:
        
        ...
    
    @dump_flags.setter
    def dump_flags(self, value: Optional[pulumi.Input[MigrationJobDumpFlagsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpPath")
    def dump_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_path.setter
    def dump_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpType")
    def dump_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_type.setter
    def dump_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]]:
        
        ...
    
    @performance_config.setter
    def performance_config(self, value: Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseSshConnectivity")
    def reverse_ssh_connectivity(self) -> Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]]:
        
        ...
    
    @reverse_ssh_connectivity.setter
    def reverse_ssh_connectivity(self, value: Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpConnectivity")
    def static_ip_connectivity(self) -> Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]]:
        
        ...
    
    @static_ip_connectivity.setter
    def static_ip_connectivity(self, value: Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectivity")
    def vpc_peering_connectivity(self) -> Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]]:
        
        ...
    
    @vpc_peering_connectivity.setter
    def vpc_peering_connectivity(self, value: Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _MigrationJobState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., dump_flags: Optional[pulumi.Input[MigrationJobDumpFlagsArgs]] = ..., dump_path: Optional[pulumi.Input[_builtins.str]] = ..., dump_type: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobErrorArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., migration_job_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., performance_config: Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]] = ..., phase: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reverse_ssh_connectivity: Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_connectivity: Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connectivity: Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFlags")
    def dump_flags(self) -> Optional[pulumi.Input[MigrationJobDumpFlagsArgs]]:
        
        ...
    
    @dump_flags.setter
    def dump_flags(self, value: Optional[pulumi.Input[MigrationJobDumpFlagsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpPath")
    def dump_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_path.setter
    def dump_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpType")
    def dump_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dump_type.setter
    def dump_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobErrorArgs]]]]:
        
        ...
    
    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MigrationJobErrorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationJobId")
    def migration_job_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_job_id.setter
    def migration_job_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]]:
        
        ...
    
    @performance_config.setter
    def performance_config(self, value: Optional[pulumi.Input[MigrationJobPerformanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phase(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phase.setter
    def phase(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseSshConnectivity")
    def reverse_ssh_connectivity(self) -> Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]]:
        
        ...
    
    @reverse_ssh_connectivity.setter
    def reverse_ssh_connectivity(self, value: Optional[pulumi.Input[MigrationJobReverseSshConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpConnectivity")
    def static_ip_connectivity(self) -> Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]]:
        
        ...
    
    @static_ip_connectivity.setter
    def static_ip_connectivity(self, value: Optional[pulumi.Input[MigrationJobStaticIpConnectivityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectivity")
    def vpc_peering_connectivity(self) -> Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]]:
        
        ...
    
    @vpc_peering_connectivity.setter
    def vpc_peering_connectivity(self, value: Optional[pulumi.Input[MigrationJobVpcPeeringConnectivityArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MigrationJob(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., dump_flags: Optional[pulumi.Input[Union[MigrationJobDumpFlagsArgs, MigrationJobDumpFlagsArgsDict]]] = ..., dump_path: Optional[pulumi.Input[_builtins.str]] = ..., dump_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., migration_job_id: Optional[pulumi.Input[_builtins.str]] = ..., performance_config: Optional[pulumi.Input[Union[MigrationJobPerformanceConfigArgs, MigrationJobPerformanceConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., reverse_ssh_connectivity: Optional[pulumi.Input[Union[MigrationJobReverseSshConnectivityArgs, MigrationJobReverseSshConnectivityArgsDict]]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_connectivity: Optional[pulumi.Input[Union[MigrationJobStaticIpConnectivityArgs, MigrationJobStaticIpConnectivityArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connectivity: Optional[pulumi.Input[Union[MigrationJobVpcPeeringConnectivityArgs, MigrationJobVpcPeeringConnectivityArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MigrationJobArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., dump_flags: Optional[pulumi.Input[Union[MigrationJobDumpFlagsArgs, MigrationJobDumpFlagsArgsDict]]] = ..., dump_path: Optional[pulumi.Input[_builtins.str]] = ..., dump_type: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., errors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MigrationJobErrorArgs, MigrationJobErrorArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., migration_job_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., performance_config: Optional[pulumi.Input[Union[MigrationJobPerformanceConfigArgs, MigrationJobPerformanceConfigArgsDict]]] = ..., phase: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reverse_ssh_connectivity: Optional[pulumi.Input[Union[MigrationJobReverseSshConnectivityArgs, MigrationJobReverseSshConnectivityArgsDict]]] = ..., source: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_connectivity: Optional[pulumi.Input[Union[MigrationJobStaticIpConnectivityArgs, MigrationJobStaticIpConnectivityArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., vpc_peering_connectivity: Optional[pulumi.Input[Union[MigrationJobVpcPeeringConnectivityArgs, MigrationJobVpcPeeringConnectivityArgsDict]]] = ...) -> MigrationJob:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpFlags")
    def dump_flags(self) -> pulumi.Output[Optional[outputs.MigrationJobDumpFlags]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpPath")
    def dump_path(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dumpType")
    def dump_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.MigrationJobError]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationJobId")
    def migration_job_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="performanceConfig")
    def performance_config(self) -> pulumi.Output[Optional[outputs.MigrationJobPerformanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phase(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseSshConnectivity")
    def reverse_ssh_connectivity(self) -> pulumi.Output[Optional[outputs.MigrationJobReverseSshConnectivity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpConnectivity")
    def static_ip_connectivity(self) -> pulumi.Output[Optional[outputs.MigrationJobStaticIpConnectivity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConnectivity")
    def vpc_peering_connectivity(self) -> pulumi.Output[Optional[outputs.MigrationJobVpcPeeringConnectivity]]:
        
        ...
    


