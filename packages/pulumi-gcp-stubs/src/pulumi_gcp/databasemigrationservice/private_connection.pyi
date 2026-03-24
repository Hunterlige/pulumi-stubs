import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PrivateConnectionArgs", "PrivateConnection"]

@pulumi.input_type
class PrivateConnectionArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        private_connection_id: pulumi.Input[_builtins.str],
        vpc_peering_config: pulumi.Input[PrivateConnectionVpcPeeringConfigArgs],
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="privateConnectionId")
    def private_connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @private_connection_id.setter
    def private_connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConfig")
    def vpc_peering_config(
        self,
    ) -> pulumi.Input[PrivateConnectionVpcPeeringConfigArgs]: ...
    @vpc_peering_config.setter
    def vpc_peering_config(
        self, value: pulumi.Input[PrivateConnectionVpcPeeringConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PrivateConnectionState:
    def __init__(
        __self__,
        *,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateConnectionErrorArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_config: Optional[
            pulumi.Input[PrivateConnectionVpcPeeringConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_without_validation.setter
    def create_without_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
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
    @pulumi.getter
    def errors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PrivateConnectionErrorArgs]]]]: ...
    @errors.setter
    def errors(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateConnectionErrorArgs]]]
        ],
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateConnectionId")
    def private_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_connection_id.setter
    def private_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConfig")
    def vpc_peering_config(
        self,
    ) -> Optional[pulumi.Input[PrivateConnectionVpcPeeringConfigArgs]]: ...
    @vpc_peering_config.setter
    def vpc_peering_config(
        self, value: Optional[pulumi.Input[PrivateConnectionVpcPeeringConfigArgs]]
    ): ...

@pulumi.type_token(...)
class PrivateConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        private_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_config: Optional[
            pulumi.Input[
                Union[
                    PrivateConnectionVpcPeeringConfigArgs,
                    PrivateConnectionVpcPeeringConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PrivateConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_without_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PrivateConnectionErrorArgs, PrivateConnectionErrorArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_peering_config: Optional[
            pulumi.Input[
                Union[
                    PrivateConnectionVpcPeeringConfigArgs,
                    PrivateConnectionVpcPeeringConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> PrivateConnection: ...
    @_builtins.property
    @pulumi.getter(name="createWithoutValidation")
    def create_without_validation(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[outputs.PrivateConnectionError]]: ...
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
    @pulumi.getter(name="privateConnectionId")
    def private_connection_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcPeeringConfig")
    def vpc_peering_config(
        self,
    ) -> pulumi.Output[outputs.PrivateConnectionVpcPeeringConfig]: ...
