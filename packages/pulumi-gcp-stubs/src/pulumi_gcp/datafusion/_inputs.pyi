import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceAcceleratorArgs",
    "InstanceAcceleratorArgsDict",
    "InstanceCryptoKeyConfigArgs",
    "InstanceCryptoKeyConfigArgsDict",
    "InstanceEventPublishConfigArgs",
    "InstanceEventPublishConfigArgsDict",
    "InstanceNetworkConfigArgs",
    "InstanceNetworkConfigArgsDict",
    ...,
    ...,
]

class InstanceAcceleratorArgsDict(TypedDict):
    accelerator_type: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceAcceleratorArgs:
    def __init__(
        __self__,
        *,
        accelerator_type: pulumi.Input[_builtins.str],
        state: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator_type.setter
    def accelerator_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]: ...
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): ...

class InstanceCryptoKeyConfigArgsDict(TypedDict):
    key_reference: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceCryptoKeyConfigArgs:
    def __init__(__self__, *, key_reference: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyReference")
    def key_reference(self) -> pulumi.Input[_builtins.str]: ...
    @key_reference.setter
    def key_reference(self, value: pulumi.Input[_builtins.str]): ...

class InstanceEventPublishConfigArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceEventPublishConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        topic: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...

class InstanceNetworkConfigArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    ip_allocation: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    private_service_connect_config: NotRequired[
        pulumi.Input[InstanceNetworkConfigPrivateServiceConnectConfigArgsDict]
    ]
    ...

@pulumi.input_type
class InstanceNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_allocation: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[InstanceNetworkConfigPrivateServiceConnectConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAllocation")
    def ip_allocation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_allocation.setter
    def ip_allocation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[
        pulumi.Input[InstanceNetworkConfigPrivateServiceConnectConfigArgs]
    ]: ...
    @private_service_connect_config.setter
    def private_service_connect_config(
        self,
        value: Optional[
            pulumi.Input[InstanceNetworkConfigPrivateServiceConnectConfigArgs]
        ],
    ): ...

class InstanceNetworkConfigPrivateServiceConnectConfigArgsDict(TypedDict):
    effective_unreachable_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    network_attachment: NotRequired[pulumi.Input[_builtins.str]]
    unreachable_cidr_block: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceNetworkConfigPrivateServiceConnectConfigArgs:
    def __init__(
        __self__,
        *,
        effective_unreachable_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
        network_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
        unreachable_cidr_block: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectiveUnreachableCidrBlock")
    def effective_unreachable_cidr_block(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_unreachable_cidr_block.setter
    def effective_unreachable_cidr_block(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkAttachment")
    def network_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_attachment.setter
    def network_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unreachableCidrBlock")
    def unreachable_cidr_block(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unreachable_cidr_block.setter
    def unreachable_cidr_block(self, value: Optional[pulumi.Input[_builtins.str]]): ...
