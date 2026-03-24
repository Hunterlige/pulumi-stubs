import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BitbucketServerConfigArgs", "BitbucketServerConfig"]

@pulumi.input_type
class BitbucketServerConfigArgs:
    def __init__(
        __self__,
        *,
        api_key: pulumi.Input[_builtins.str],
        config_id: pulumi.Input[_builtins.str],
        host_uri: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        secrets: pulumi.Input[BitbucketServerConfigSecretsArgs],
        username: pulumi.Input[_builtins.str],
        connected_repositories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
            ]
        ] = ...,
        peered_network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[_builtins.str]: ...
    @api_key.setter
    def api_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Input[_builtins.str]: ...
    @config_id.setter
    def config_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Input[_builtins.str]: ...
    @host_uri.setter
    def host_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Input[BitbucketServerConfigSecretsArgs]: ...
    @secrets.setter
    def secrets(self, value: pulumi.Input[BitbucketServerConfigSecretsArgs]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectedRepositories")
    def connected_repositories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
        ]
    ]: ...
    @connected_repositories.setter
    def connected_repositories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="peeredNetwork")
    def peered_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peered_network.setter
    def peered_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca.setter
    def ssl_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _BitbucketServerConfigState:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connected_repositories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
            ]
        ] = ...,
        host_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peered_network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[pulumi.Input[BitbucketServerConfigSecretsArgs]] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectedRepositories")
    def connected_repositories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
        ]
    ]: ...
    @connected_repositories.setter
    def connected_repositories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[BitbucketServerConfigConnectedRepositoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_uri.setter
    def host_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="peeredNetwork")
    def peered_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @peered_network.setter
    def peered_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input[BitbucketServerConfigSecretsArgs]]: ...
    @secrets.setter
    def secrets(
        self, value: Optional[pulumi.Input[BitbucketServerConfigSecretsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_ca.setter
    def ssl_ca(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_key.setter
    def webhook_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class BitbucketServerConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connected_repositories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BitbucketServerConfigConnectedRepositoryArgs,
                            BitbucketServerConfigConnectedRepositoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        host_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        peered_network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[
            pulumi.Input[
                Union[
                    BitbucketServerConfigSecretsArgs,
                    BitbucketServerConfigSecretsArgsDict,
                ]
            ]
        ] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BitbucketServerConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connected_repositories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BitbucketServerConfigConnectedRepositoryArgs,
                            BitbucketServerConfigConnectedRepositoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        host_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        peered_network: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        secrets: Optional[
            pulumi.Input[
                Union[
                    BitbucketServerConfigSecretsArgs,
                    BitbucketServerConfigSecretsArgsDict,
                ]
            ]
        ] = ...,
        ssl_ca: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BitbucketServerConfig: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectedRepositories")
    def connected_repositories(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.BitbucketServerConfigConnectedRepository]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hostUri")
    def host_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peeredNetwork")
    def peered_network(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> pulumi.Output[outputs.BitbucketServerConfigSecrets]: ...
    @_builtins.property
    @pulumi.getter(name="sslCa")
    def ssl_ca(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webhookKey")
    def webhook_key(self) -> pulumi.Output[_builtins.str]: ...
