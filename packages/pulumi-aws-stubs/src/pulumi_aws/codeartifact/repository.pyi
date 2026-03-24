import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryArgs", "Repository"]

@pulumi.input_type
class RepositoryArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        repository: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_connections: Optional[
            pulumi.Input[RepositoryExternalConnectionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upstreams: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_owner.setter
    def domain_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalConnections")
    def external_connections(
        self,
    ) -> Optional[pulumi.Input[RepositoryExternalConnectionsArgs]]: ...
    @external_connections.setter
    def external_connections(
        self, value: Optional[pulumi.Input[RepositoryExternalConnectionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def upstreams(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]]: ...
    @upstreams.setter
    def upstreams(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]],
    ): ...

@pulumi.input_type
class _RepositoryState:
    def __init__(
        __self__,
        *,
        administrator_account: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_connections: Optional[
            pulumi.Input[RepositoryExternalConnectionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        upstreams: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorAccount")
    def administrator_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @administrator_account.setter
    def administrator_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_owner.setter
    def domain_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="externalConnections")
    def external_connections(
        self,
    ) -> Optional[pulumi.Input[RepositoryExternalConnectionsArgs]]: ...
    @external_connections.setter
    def external_connections(
        self, value: Optional[pulumi.Input[RepositoryExternalConnectionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def upstreams(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]]: ...
    @upstreams.setter
    def upstreams(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[RepositoryUpstreamArgs]]]],
    ): ...

@pulumi.type_token("aws:codeartifact/repository:Repository")
class Repository(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_connections: Optional[
            pulumi.Input[
                Union[
                    RepositoryExternalConnectionsArgs,
                    RepositoryExternalConnectionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        upstreams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RepositoryUpstreamArgs, RepositoryUpstreamArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RepositoryArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        administrator_account: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        external_connections: Optional[
            pulumi.Input[
                Union[
                    RepositoryExternalConnectionsArgs,
                    RepositoryExternalConnectionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        upstreams: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[RepositoryUpstreamArgs, RepositoryUpstreamArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> Repository: ...
    @_builtins.property
    @pulumi.getter(name="administratorAccount")
    def administrator_account(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="externalConnections")
    def external_connections(
        self,
    ) -> pulumi.Output[Optional[outputs.RepositoryExternalConnections]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def upstreams(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RepositoryUpstream]]]: ...
