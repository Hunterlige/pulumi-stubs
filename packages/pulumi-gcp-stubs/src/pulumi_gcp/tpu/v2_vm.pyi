

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
__all__ = ['V2VmArgs', 'V2Vm']
@pulumi.input_type
class V2VmArgs:
    def __init__(__self__, *, runtime_version: pulumi.Input[_builtins.str], accelerator_config: Optional[pulumi.Input[V2VmAcceleratorConfigArgs]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[V2VmNetworkConfigArgs]] = ..., network_configs: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_config: Optional[pulumi.Input[V2VmSchedulingConfigArgs]] = ..., service_account: Optional[pulumi.Input[V2VmServiceAccountArgs]] = ..., shielded_instance_config: Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(self) -> Optional[pulumi.Input[V2VmAcceleratorConfigArgs]]:
        
        ...
    
    @accelerator_config.setter
    def accelerator_config(self, value: Optional[pulumi.Input[V2VmAcceleratorConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def network_config(self) -> Optional[pulumi.Input[V2VmNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[V2VmNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]]:
        
        ...
    
    @network_configs.setter
    def network_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingConfig")
    def scheduling_config(self) -> Optional[pulumi.Input[V2VmSchedulingConfigArgs]]:
        
        ...
    
    @scheduling_config.setter
    def scheduling_config(self, value: Optional[pulumi.Input[V2VmSchedulingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[V2VmServiceAccountArgs]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[V2VmServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]]:
        
        ...
    
    @shielded_instance_config.setter
    def shielded_instance_config(self, value: Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _V2VmState:
    def __init__(__self__, *, accelerator_config: Optional[pulumi.Input[V2VmAcceleratorConfigArgs]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., api_version: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., health: Optional[pulumi.Input[_builtins.str]] = ..., health_description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., multislice_node: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[V2VmNetworkConfigArgs]] = ..., network_configs: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]] = ..., network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., queued_resource: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_config: Optional[pulumi.Input[V2VmSchedulingConfigArgs]] = ..., service_account: Optional[pulumi.Input[V2VmServiceAccountArgs]] = ..., shielded_instance_config: Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., symptoms: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmSymptomArgs]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(self) -> Optional[pulumi.Input[V2VmAcceleratorConfigArgs]]:
        
        ...
    
    @accelerator_config.setter
    def accelerator_config(self, value: Optional[pulumi.Input[V2VmAcceleratorConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]]:
        
        ...
    
    @data_disks.setter
    def data_disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmDataDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def health(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health.setter
    def health(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthDescription")
    def health_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @health_description.setter
    def health_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multisliceNode")
    def multislice_node(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @multislice_node.setter
    def multislice_node(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    def network_config(self) -> Optional[pulumi.Input[V2VmNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[V2VmNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]]:
        
        ...
    
    @network_configs.setter
    def network_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpoints")
    def network_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointArgs]]]]:
        
        ...
    
    @network_endpoints.setter
    def network_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointArgs]]]]): # -> None:
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
    @pulumi.getter(name="queuedResource")
    def queued_resource(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @queued_resource.setter
    def queued_resource(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingConfig")
    def scheduling_config(self) -> Optional[pulumi.Input[V2VmSchedulingConfigArgs]]:
        
        ...
    
    @scheduling_config.setter
    def scheduling_config(self, value: Optional[pulumi.Input[V2VmSchedulingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[V2VmServiceAccountArgs]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[V2VmServiceAccountArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]]:
        
        ...
    
    @shielded_instance_config.setter
    def shielded_instance_config(self, value: Optional[pulumi.Input[V2VmShieldedInstanceConfigArgs]]): # -> None:
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
    def symptoms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmSymptomArgs]]]]:
        
        ...
    
    @symptoms.setter
    def symptoms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmSymptomArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:tpu/v2Vm:V2Vm")
class V2Vm(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accelerator_config: Optional[pulumi.Input[Union[V2VmAcceleratorConfigArgs, V2VmAcceleratorConfigArgsDict]]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmDataDiskArgs, V2VmDataDiskArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[V2VmNetworkConfigArgs, V2VmNetworkConfigArgsDict]]] = ..., network_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmNetworkConfigArgs, V2VmNetworkConfigArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_config: Optional[pulumi.Input[Union[V2VmSchedulingConfigArgs, V2VmSchedulingConfigArgsDict]]] = ..., service_account: Optional[pulumi.Input[Union[V2VmServiceAccountArgs, V2VmServiceAccountArgsDict]]] = ..., shielded_instance_config: Optional[pulumi.Input[Union[V2VmShieldedInstanceConfigArgs, V2VmShieldedInstanceConfigArgsDict]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: V2VmArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accelerator_config: Optional[pulumi.Input[Union[V2VmAcceleratorConfigArgs, V2VmAcceleratorConfigArgsDict]]] = ..., accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., api_version: Optional[pulumi.Input[_builtins.str]] = ..., cidr_block: Optional[pulumi.Input[_builtins.str]] = ..., data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmDataDiskArgs, V2VmDataDiskArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., health: Optional[pulumi.Input[_builtins.str]] = ..., health_description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., multislice_node: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[V2VmNetworkConfigArgs, V2VmNetworkConfigArgsDict]]] = ..., network_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmNetworkConfigArgs, V2VmNetworkConfigArgsDict]]]]] = ..., network_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmNetworkEndpointArgs, V2VmNetworkEndpointArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., queued_resource: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version: Optional[pulumi.Input[_builtins.str]] = ..., scheduling_config: Optional[pulumi.Input[Union[V2VmSchedulingConfigArgs, V2VmSchedulingConfigArgsDict]]] = ..., service_account: Optional[pulumi.Input[Union[V2VmServiceAccountArgs, V2VmServiceAccountArgsDict]]] = ..., shielded_instance_config: Optional[pulumi.Input[Union[V2VmShieldedInstanceConfigArgs, V2VmShieldedInstanceConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., symptoms: Optional[pulumi.Input[Sequence[pulumi.Input[Union[V2VmSymptomArgs, V2VmSymptomArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> V2Vm:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorConfig")
    def accelerator_config(self) -> pulumi.Output[outputs.V2VmAcceleratorConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> pulumi.Output[Optional[Sequence[outputs.V2VmDataDisk]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def health(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthDescription")
    def health_description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multisliceNode")
    def multislice_node(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[outputs.V2VmNetworkConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(self) -> pulumi.Output[Optional[Sequence[outputs.V2VmNetworkConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkEndpoints")
    def network_endpoints(self) -> pulumi.Output[Sequence[outputs.V2VmNetworkEndpoint]]:
        
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
    @pulumi.getter(name="queuedResource")
    def queued_resource(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schedulingConfig")
    def scheduling_config(self) -> pulumi.Output[Optional[outputs.V2VmSchedulingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Output[outputs.V2VmServiceAccount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> pulumi.Output[Optional[outputs.V2VmShieldedInstanceConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def symptoms(self) -> pulumi.Output[Sequence[outputs.V2VmSymptom]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


