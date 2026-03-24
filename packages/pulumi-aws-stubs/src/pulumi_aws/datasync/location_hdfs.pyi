import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["LocationHdfsArgs", "LocationHdfs"]

@pulumi.input_type
class LocationHdfsArgs:
    def __init__(
        __self__,
        *,
        agent_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        name_nodes: pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]],
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kerberos_keytab: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_keytab_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_provider_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        qop_configuration: Optional[
            pulumi.Input[LocationHdfsQopConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_factor: Optional[pulumi.Input[_builtins.int]] = ...,
        simple_user: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nameNodes")
    def name_nodes(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]]: ...
    @name_nodes.setter
    def name_nodes(
        self, value: pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_size.setter
    def block_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytab")
    def kerberos_keytab(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_keytab.setter
    def kerberos_keytab(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytabBase64")
    def kerberos_keytab_base64(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_keytab_base64.setter
    def kerberos_keytab_base64(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_krb5_conf.setter
    def kerberos_krb5_conf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5ConfBase64")
    def kerberos_krb5_conf_base64(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_krb5_conf_base64.setter
    def kerberos_krb5_conf_base64(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kerberosPrincipal")
    def kerberos_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_principal.setter
    def kerberos_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_provider_uri.setter
    def kms_key_provider_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qopConfiguration")
    def qop_configuration(
        self,
    ) -> Optional[pulumi.Input[LocationHdfsQopConfigurationArgs]]: ...
    @qop_configuration.setter
    def qop_configuration(
        self, value: Optional[pulumi.Input[LocationHdfsQopConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="simpleUser")
    def simple_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @simple_user.setter
    def simple_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _LocationHdfsState:
    def __init__(
        __self__,
        *,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kerberos_keytab: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_keytab_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_provider_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]]
        ] = ...,
        qop_configuration: Optional[
            pulumi.Input[LocationHdfsQopConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_factor: Optional[pulumi.Input[_builtins.int]] = ...,
        simple_user: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @agent_arns.setter
    def agent_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_size.setter
    def block_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytab")
    def kerberos_keytab(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_keytab.setter
    def kerberos_keytab(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytabBase64")
    def kerberos_keytab_base64(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_keytab_base64.setter
    def kerberos_keytab_base64(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_krb5_conf.setter
    def kerberos_krb5_conf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5ConfBase64")
    def kerberos_krb5_conf_base64(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_krb5_conf_base64.setter
    def kerberos_krb5_conf_base64(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kerberosPrincipal")
    def kerberos_principal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kerberos_principal.setter
    def kerberos_principal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_provider_uri.setter
    def kms_key_provider_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nameNodes")
    def name_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]]]: ...
    @name_nodes.setter
    def name_nodes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LocationHdfsNameNodeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="qopConfiguration")
    def qop_configuration(
        self,
    ) -> Optional[pulumi.Input[LocationHdfsQopConfigurationArgs]]: ...
    @qop_configuration.setter
    def qop_configuration(
        self, value: Optional[pulumi.Input[LocationHdfsQopConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="simpleUser")
    def simple_user(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @simple_user.setter
    def simple_user(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:datasync/locationHdfs:LocationHdfs")
class LocationHdfs(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kerberos_keytab: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_keytab_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_provider_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name_nodes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LocationHdfsNameNodeArgs, LocationHdfsNameNodeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        qop_configuration: Optional[
            pulumi.Input[
                Union[
                    LocationHdfsQopConfigurationArgs,
                    LocationHdfsQopConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_factor: Optional[pulumi.Input[_builtins.int]] = ...,
        simple_user: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: LocationHdfsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        authentication_type: Optional[pulumi.Input[_builtins.str]] = ...,
        block_size: Optional[pulumi.Input[_builtins.int]] = ...,
        kerberos_keytab: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_keytab_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_krb5_conf_base64: Optional[pulumi.Input[_builtins.str]] = ...,
        kerberos_principal: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_provider_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name_nodes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[LocationHdfsNameNodeArgs, LocationHdfsNameNodeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        qop_configuration: Optional[
            pulumi.Input[
                Union[
                    LocationHdfsQopConfigurationArgs,
                    LocationHdfsQopConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_factor: Optional[pulumi.Input[_builtins.int]] = ...,
        simple_user: Optional[pulumi.Input[_builtins.str]] = ...,
        subdirectory: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> LocationHdfs: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="blockSize")
    def block_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytab")
    def kerberos_keytab(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosKeytabBase64")
    def kerberos_keytab_base64(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5Conf")
    def kerberos_krb5_conf(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosKrb5ConfBase64")
    def kerberos_krb5_conf_base64(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosPrincipal")
    def kerberos_principal(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyProviderUri")
    def kms_key_provider_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="nameNodes")
    def name_nodes(self) -> pulumi.Output[Sequence[outputs.LocationHdfsNameNode]]: ...
    @_builtins.property
    @pulumi.getter(name="qopConfiguration")
    def qop_configuration(
        self,
    ) -> pulumi.Output[outputs.LocationHdfsQopConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="simpleUser")
    def simple_user(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]: ...
