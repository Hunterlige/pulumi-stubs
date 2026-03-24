import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["OutboundConnectionArgs", "OutboundConnection"]

@pulumi.input_type
class OutboundConnectionArgs:
    def __init__(
        __self__,
        *,
        connection_alias: pulumi.Input[_builtins.str],
        local_domain_info: pulumi.Input[OutboundConnectionLocalDomainInfoArgs],
        remote_domain_info: pulumi.Input[OutboundConnectionRemoteDomainInfoArgs],
        accept_connection: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_properties: Optional[
            pulumi.Input[OutboundConnectionConnectionPropertiesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionAlias")
    def connection_alias(self) -> pulumi.Input[_builtins.str]: ...
    @connection_alias.setter
    def connection_alias(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localDomainInfo")
    def local_domain_info(
        self,
    ) -> pulumi.Input[OutboundConnectionLocalDomainInfoArgs]: ...
    @local_domain_info.setter
    def local_domain_info(
        self, value: pulumi.Input[OutboundConnectionLocalDomainInfoArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remoteDomainInfo")
    def remote_domain_info(
        self,
    ) -> pulumi.Input[OutboundConnectionRemoteDomainInfoArgs]: ...
    @remote_domain_info.setter
    def remote_domain_info(
        self, value: pulumi.Input[OutboundConnectionRemoteDomainInfoArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="acceptConnection")
    def accept_connection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @accept_connection.setter
    def accept_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_mode.setter
    def connection_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(
        self,
    ) -> Optional[pulumi.Input[OutboundConnectionConnectionPropertiesArgs]]: ...
    @connection_properties.setter
    def connection_properties(
        self, value: Optional[pulumi.Input[OutboundConnectionConnectionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _OutboundConnectionState:
    def __init__(
        __self__,
        *,
        accept_connection: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_properties: Optional[
            pulumi.Input[OutboundConnectionConnectionPropertiesArgs]
        ] = ...,
        connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        local_domain_info: Optional[
            pulumi.Input[OutboundConnectionLocalDomainInfoArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_domain_info: Optional[
            pulumi.Input[OutboundConnectionRemoteDomainInfoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acceptConnection")
    def accept_connection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @accept_connection.setter
    def accept_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionAlias")
    def connection_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_alias.setter
    def connection_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_mode.setter
    def connection_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(
        self,
    ) -> Optional[pulumi.Input[OutboundConnectionConnectionPropertiesArgs]]: ...
    @connection_properties.setter
    def connection_properties(
        self, value: Optional[pulumi.Input[OutboundConnectionConnectionPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_status.setter
    def connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localDomainInfo")
    def local_domain_info(
        self,
    ) -> Optional[pulumi.Input[OutboundConnectionLocalDomainInfoArgs]]: ...
    @local_domain_info.setter
    def local_domain_info(
        self, value: Optional[pulumi.Input[OutboundConnectionLocalDomainInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteDomainInfo")
    def remote_domain_info(
        self,
    ) -> Optional[pulumi.Input[OutboundConnectionRemoteDomainInfoArgs]]: ...
    @remote_domain_info.setter
    def remote_domain_info(
        self, value: Optional[pulumi.Input[OutboundConnectionRemoteDomainInfoArgs]]
    ): ...

@pulumi.type_token(...)
class OutboundConnection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_connection: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_properties: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionConnectionPropertiesArgs,
                    OutboundConnectionConnectionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        local_domain_info: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionLocalDomainInfoArgs,
                    OutboundConnectionLocalDomainInfoArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_domain_info: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionRemoteDomainInfoArgs,
                    OutboundConnectionRemoteDomainInfoArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: OutboundConnectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        accept_connection: Optional[pulumi.Input[_builtins.bool]] = ...,
        connection_alias: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_properties: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionConnectionPropertiesArgs,
                    OutboundConnectionConnectionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        local_domain_info: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionLocalDomainInfoArgs,
                    OutboundConnectionLocalDomainInfoArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_domain_info: Optional[
            pulumi.Input[
                Union[
                    OutboundConnectionRemoteDomainInfoArgs,
                    OutboundConnectionRemoteDomainInfoArgsDict,
                ]
            ]
        ] = ...,
    ) -> OutboundConnection: ...
    @_builtins.property
    @pulumi.getter(name="acceptConnection")
    def accept_connection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionAlias")
    def connection_alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionProperties")
    def connection_properties(
        self,
    ) -> pulumi.Output[outputs.OutboundConnectionConnectionProperties]: ...
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localDomainInfo")
    def local_domain_info(
        self,
    ) -> pulumi.Output[outputs.OutboundConnectionLocalDomainInfo]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="remoteDomainInfo")
    def remote_domain_info(
        self,
    ) -> pulumi.Output[outputs.OutboundConnectionRemoteDomainInfo]: ...
