import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RuntimeArgs", "Runtime"]

@pulumi.input_type
class RuntimeArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        access_config: Optional[pulumi.Input[RuntimeAccessConfigArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        software_config: Optional[pulumi.Input[RuntimeSoftwareConfigArgs]] = ...,
        virtual_machine: Optional[pulumi.Input[RuntimeVirtualMachineArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input[RuntimeAccessConfigArgs]]: ...
    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input[RuntimeAccessConfigArgs]]): ...
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[pulumi.Input[RuntimeSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[RuntimeSoftwareConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input[RuntimeVirtualMachineArgs]]: ...
    @virtual_machine.setter
    def virtual_machine(
        self, value: Optional[pulumi.Input[RuntimeVirtualMachineArgs]]
    ): ...

@pulumi.input_type
class _RuntimeState:
    def __init__(
        __self__,
        *,
        access_config: Optional[pulumi.Input[RuntimeAccessConfigArgs]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        health_state: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[RuntimeMetricArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        software_config: Optional[pulumi.Input[RuntimeSoftwareConfigArgs]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[pulumi.Input[RuntimeVirtualMachineArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input[RuntimeAccessConfigArgs]]: ...
    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input[RuntimeAccessConfigArgs]]): ...
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
    @pulumi.getter(name="healthState")
    def health_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_state.setter
    def health_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def metrics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeMetricArgs]]]]: ...
    @metrics.setter
    def metrics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RuntimeMetricArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> Optional[pulumi.Input[RuntimeSoftwareConfigArgs]]: ...
    @software_config.setter
    def software_config(
        self, value: Optional[pulumi.Input[RuntimeSoftwareConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(self) -> Optional[pulumi.Input[RuntimeVirtualMachineArgs]]: ...
    @virtual_machine.setter
    def virtual_machine(
        self, value: Optional[pulumi.Input[RuntimeVirtualMachineArgs]]
    ): ...

@pulumi.type_token("gcp:notebooks/runtime:Runtime")
class Runtime(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_config: Optional[
            pulumi.Input[Union[RuntimeAccessConfigArgs, RuntimeAccessConfigArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        software_config: Optional[
            pulumi.Input[
                Union[RuntimeSoftwareConfigArgs, RuntimeSoftwareConfigArgsDict]
            ]
        ] = ...,
        virtual_machine: Optional[
            pulumi.Input[
                Union[RuntimeVirtualMachineArgs, RuntimeVirtualMachineArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RuntimeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_config: Optional[
            pulumi.Input[Union[RuntimeAccessConfigArgs, RuntimeAccessConfigArgsDict]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        health_state: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        metrics: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[RuntimeMetricArgs, RuntimeMetricArgsDict]]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        software_config: Optional[
            pulumi.Input[
                Union[RuntimeSoftwareConfigArgs, RuntimeSoftwareConfigArgsDict]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        virtual_machine: Optional[
            pulumi.Input[
                Union[RuntimeVirtualMachineArgs, RuntimeVirtualMachineArgsDict]
            ]
        ] = ...,
    ) -> Runtime: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> pulumi.Output[Optional[outputs.RuntimeAccessConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="healthState")
    def health_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Sequence[outputs.RuntimeMetric]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="softwareConfig")
    def software_config(self) -> pulumi.Output[outputs.RuntimeSoftwareConfig]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualMachine")
    def virtual_machine(
        self,
    ) -> pulumi.Output[Optional[outputs.RuntimeVirtualMachine]]: ...
