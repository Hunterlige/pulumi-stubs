import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CloudVmClusterArgs", "CloudVmCluster"]

@pulumi.input_type
class CloudVmClusterArgs:
    def __init__(
        __self__,
        *,
        cloud_vm_cluster_id: pulumi.Input[_builtins.str],
        exadata_infrastructure: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        backup_odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[CloudVmClusterPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @cloud_vm_cluster_id.setter
    def cloud_vm_cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructure")
    def exadata_infrastructure(self) -> pulumi.Input[_builtins.str]: ...
    @exadata_infrastructure.setter
    def exadata_infrastructure(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="backupOdbSubnet")
    def backup_odb_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_odb_subnet.setter
    def backup_odb_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_subnet_cidr.setter
    def backup_subnet_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @odb_network.setter
    def odb_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @odb_subnet.setter
    def odb_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[CloudVmClusterPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[CloudVmClusterPropertiesArgs]]
    ): ...

@pulumi.input_type
class _CloudVmClusterState:
    def __init__(
        __self__,
        *,
        backup_odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        exadata_infrastructure: Optional[pulumi.Input[_builtins.str]] = ...,
        gcp_oracle_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[CloudVmClusterPropertiesArgs]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backupOdbSubnet")
    def backup_odb_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_odb_subnet.setter
    def backup_odb_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_subnet_cidr.setter
    def backup_subnet_cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_vm_cluster_id.setter
    def cloud_vm_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructure")
    def exadata_infrastructure(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exadata_infrastructure.setter
    def exadata_infrastructure(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcp_oracle_zone.setter
    def gcp_oracle_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @odb_network.setter
    def odb_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @odb_subnet.setter
    def odb_subnet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[CloudVmClusterPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[CloudVmClusterPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:oracledatabase/cloudVmCluster:CloudVmCluster")
class CloudVmCluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        exadata_infrastructure: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[CloudVmClusterPropertiesArgs, CloudVmClusterPropertiesArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CloudVmClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        backup_odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        backup_subnet_cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cidr: Optional[pulumi.Input[_builtins.str]] = ...,
        cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        exadata_infrastructure: Optional[pulumi.Input[_builtins.str]] = ...,
        gcp_oracle_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_network: Optional[pulumi.Input[_builtins.str]] = ...,
        odb_subnet: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[CloudVmClusterPropertiesArgs, CloudVmClusterPropertiesArgsDict]
            ]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> CloudVmCluster: ...
    @_builtins.property
    @pulumi.getter(name="backupOdbSubnet")
    def backup_odb_subnet(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="backupSubnetCidr")
    def backup_subnet_cidr(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exadataInfrastructure")
    def exadata_infrastructure(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcpOracleZone")
    def gcp_oracle_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="odbNetwork")
    def odb_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="odbSubnet")
    def odb_subnet(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[Optional[outputs.CloudVmClusterProperties]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
