import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuntimeTemplateArgs", "RuntimeTemplate"]

@pulumi.input_type
class RuntimeTemplateArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        data_persistent_disk_spec: Optional[
            pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[
            pulumi.Input[RuntimeTemplateEncryptionSpecArgs]
        ] = ...,
        euc_config: Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]] = ...,
        idle_shutdown_config: Optional[
            pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        machine_spec: Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_spec: Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_vm_config: Optional[
            pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]
        ] = ...,
        software_config: Optional[
            pulumi.Input[RuntimeTemplateSoftwareConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataPersistentDiskSpec")
    def data_persistent_disk_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]]: ...
    @data_persistent_disk_spec.setter
    def data_persistent_disk_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eucConfig")
    def euc_config(self) -> Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]]: ...
    @euc_config.setter
    def euc_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleShutdownConfig")
    def idle_shutdown_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]]: ...
    @idle_shutdown_config.setter
    def idle_shutdown_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]]
    ): ...
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
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]]: ...
    @machine_spec.setter
    def machine_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSpec")
    def network_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]]: ...
    @network_spec.setter
    def network_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shieldedVmConfig")
    def shielded_vm_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]]: ...
    @shielded_vm_config.setter
    def shielded_vm_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateSoftwareConfigArgs]]
    ): ...

@pulumi.input_type
class _RuntimeTemplateState:
    def __init__(
        __self__,
        *,
        data_persistent_disk_spec: Optional[
            pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[
            pulumi.Input[RuntimeTemplateEncryptionSpecArgs]
        ] = ...,
        euc_config: Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]] = ...,
        idle_shutdown_config: Optional[
            pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_spec: Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_spec: Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_vm_config: Optional[
            pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]
        ] = ...,
        software_config: Optional[
            pulumi.Input[RuntimeTemplateSoftwareConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataPersistentDiskSpec")
    def data_persistent_disk_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]]: ...
    @data_persistent_disk_spec.setter
    def data_persistent_disk_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateDataPersistentDiskSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eucConfig")
    def euc_config(self) -> Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]]: ...
    @euc_config.setter
    def euc_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateEucConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idleShutdownConfig")
    def idle_shutdown_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]]: ...
    @idle_shutdown_config.setter
    def idle_shutdown_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateIdleShutdownConfigArgs]]
    ): ...
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
    @pulumi.getter(name="machineSpec")
    def machine_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]]: ...
    @machine_spec.setter
    def machine_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateMachineSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkSpec")
    def network_spec(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]]: ...
    @network_spec.setter
    def network_spec(
        self, value: Optional[pulumi.Input[RuntimeTemplateNetworkSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @network_tags.setter
    def network_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shieldedVmConfig")
    def shielded_vm_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]]: ...
    @shielded_vm_config.setter
    def shielded_vm_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateShieldedVmConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> Optional[pulumi.Input[RuntimeTemplateSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[RuntimeTemplateSoftwareConfigArgs]]
    ): ...

@pulumi.type_token("gcp:colab/runtimeTemplate:RuntimeTemplate")
class RuntimeTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_persistent_disk_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateDataPersistentDiskSpecArgs,
                    RuntimeTemplateDataPersistentDiskSpecArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateEncryptionSpecArgs,
                    RuntimeTemplateEncryptionSpecArgsDict,
                ]
            ]
        ] = ...,
        euc_config: Optional[
            pulumi.Input[
                Union[RuntimeTemplateEucConfigArgs, RuntimeTemplateEucConfigArgsDict]
            ]
        ] = ...,
        idle_shutdown_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateIdleShutdownConfigArgs,
                    RuntimeTemplateIdleShutdownConfigArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateMachineSpecArgs, RuntimeTemplateMachineSpecArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateNetworkSpecArgs, RuntimeTemplateNetworkSpecArgsDict
                ]
            ]
        ] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        shielded_vm_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateShieldedVmConfigArgs,
                    RuntimeTemplateShieldedVmConfigArgsDict,
                ]
            ]
        ] = ...,
        software_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateSoftwareConfigArgs,
                    RuntimeTemplateSoftwareConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuntimeTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_persistent_disk_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateDataPersistentDiskSpecArgs,
                    RuntimeTemplateDataPersistentDiskSpecArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateEncryptionSpecArgs,
                    RuntimeTemplateEncryptionSpecArgsDict,
                ]
            ]
        ] = ...,
        euc_config: Optional[
            pulumi.Input[
                Union[RuntimeTemplateEucConfigArgs, RuntimeTemplateEucConfigArgsDict]
            ]
        ] = ...,
        idle_shutdown_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateIdleShutdownConfigArgs,
                    RuntimeTemplateIdleShutdownConfigArgsDict,
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateMachineSpecArgs, RuntimeTemplateMachineSpecArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_spec: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateNetworkSpecArgs, RuntimeTemplateNetworkSpecArgsDict
                ]
            ]
        ] = ...,
        network_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        shielded_vm_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateShieldedVmConfigArgs,
                    RuntimeTemplateShieldedVmConfigArgsDict,
                ]
            ]
        ] = ...,
        software_config: Optional[
            pulumi.Input[
                Union[
                    RuntimeTemplateSoftwareConfigArgs,
                    RuntimeTemplateSoftwareConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> RuntimeTemplate: ...
    @_builtins.property
    @pulumi.getter(name="dataPersistentDiskSpec")
    def data_persistent_disk_spec(
        self,
    ) -> pulumi.Output[outputs.RuntimeTemplateDataPersistentDiskSpec]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.RuntimeTemplateEncryptionSpec]]: ...
    @_builtins.property
    @pulumi.getter(name="eucConfig")
    def euc_config(self) -> pulumi.Output[outputs.RuntimeTemplateEucConfig]: ...
    @_builtins.property
    @pulumi.getter(name="idleShutdownConfig")
    def idle_shutdown_config(
        self,
    ) -> pulumi.Output[outputs.RuntimeTemplateIdleShutdownConfig]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineSpec")
    def machine_spec(self) -> pulumi.Output[outputs.RuntimeTemplateMachineSpec]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkSpec")
    def network_spec(self) -> pulumi.Output[outputs.RuntimeTemplateNetworkSpec]: ...
    @_builtins.property
    @pulumi.getter(name="networkTags")
    def network_tags(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shieldedVmConfig")
    def shielded_vm_config(
        self,
    ) -> pulumi.Output[outputs.RuntimeTemplateShieldedVmConfig]: ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(
        self,
    ) -> pulumi.Output[outputs.RuntimeTemplateSoftwareConfig]: ...
