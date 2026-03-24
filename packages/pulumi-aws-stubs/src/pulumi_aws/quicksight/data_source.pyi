import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataSourceArgs", "DataSource"]

@pulumi.input_type
class DataSourceArgs:
    def __init__(
        __self__,
        *,
        data_source_id: pulumi.Input[_builtins.str],
        parameters: pulumi.Input[DataSourceParametersArgs],
        type: pulumi.Input[_builtins.str],
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[DataSourceCredentialsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_properties: Optional[pulumi.Input[DataSourceSslPropertiesArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_connection_properties: Optional[
            pulumi.Input[DataSourceVpcConnectionPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_id.setter
    def data_source_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[DataSourceParametersArgs]: ...
    @parameters.setter
    def parameters(self, value: pulumi.Input[DataSourceParametersArgs]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[DataSourceCredentialsArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[DataSourceCredentialsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]]: ...
    @permissions.setter
    def permissions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslProperties")
    def ssl_properties(self) -> Optional[pulumi.Input[DataSourceSslPropertiesArgs]]: ...
    @ssl_properties.setter
    def ssl_properties(
        self, value: Optional[pulumi.Input[DataSourceSslPropertiesArgs]]
    ): ...
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
    @pulumi.getter(name="vpcConnectionProperties")
    def vpc_connection_properties(
        self,
    ) -> Optional[pulumi.Input[DataSourceVpcConnectionPropertiesArgs]]: ...
    @vpc_connection_properties.setter
    def vpc_connection_properties(
        self, value: Optional[pulumi.Input[DataSourceVpcConnectionPropertiesArgs]]
    ): ...

@pulumi.input_type
class _DataSourceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[pulumi.Input[DataSourceCredentialsArgs]] = ...,
        data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[DataSourceParametersArgs]] = ...,
        permissions: Optional[
            pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_properties: Optional[pulumi.Input[DataSourceSslPropertiesArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connection_properties: Optional[
            pulumi.Input[DataSourceVpcConnectionPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[DataSourceCredentialsArgs]]: ...
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[DataSourceCredentialsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source_id.setter
    def data_source_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[DataSourceParametersArgs]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[DataSourceParametersArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]]: ...
    @permissions.setter
    def permissions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DataSourcePermissionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslProperties")
    def ssl_properties(self) -> Optional[pulumi.Input[DataSourceSslPropertiesArgs]]: ...
    @ssl_properties.setter
    def ssl_properties(
        self, value: Optional[pulumi.Input[DataSourceSslPropertiesArgs]]
    ): ...
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectionProperties")
    def vpc_connection_properties(
        self,
    ) -> Optional[pulumi.Input[DataSourceVpcConnectionPropertiesArgs]]: ...
    @vpc_connection_properties.setter
    def vpc_connection_properties(
        self, value: Optional[pulumi.Input[DataSourceVpcConnectionPropertiesArgs]]
    ): ...

@pulumi.type_token("aws:quicksight/dataSource:DataSource")
class DataSource(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[
            pulumi.Input[
                Union[DataSourceCredentialsArgs, DataSourceCredentialsArgsDict]
            ]
        ] = ...,
        data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Union[DataSourceParametersArgs, DataSourceParametersArgsDict]]
        ] = ...,
        permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DataSourcePermissionArgs, DataSourcePermissionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_properties: Optional[
            pulumi.Input[
                Union[DataSourceSslPropertiesArgs, DataSourceSslPropertiesArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connection_properties: Optional[
            pulumi.Input[
                Union[
                    DataSourceVpcConnectionPropertiesArgs,
                    DataSourceVpcConnectionPropertiesArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataSourceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        aws_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        credentials: Optional[
            pulumi.Input[
                Union[DataSourceCredentialsArgs, DataSourceCredentialsArgsDict]
            ]
        ] = ...,
        data_source_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Union[DataSourceParametersArgs, DataSourceParametersArgsDict]]
        ] = ...,
        permissions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DataSourcePermissionArgs, DataSourcePermissionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_properties: Optional[
            pulumi.Input[
                Union[DataSourceSslPropertiesArgs, DataSourceSslPropertiesArgsDict]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connection_properties: Optional[
            pulumi.Input[
                Union[
                    DataSourceVpcConnectionPropertiesArgs,
                    DataSourceVpcConnectionPropertiesArgsDict,
                ]
            ]
        ] = ...,
    ) -> DataSource: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[outputs.DataSourceCredentials]]: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceId")
    def data_source_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[outputs.DataSourceParameters]: ...
    @_builtins.property
    @pulumi.getter
    def permissions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DataSourcePermission]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslProperties")
    def ssl_properties(self) -> pulumi.Output[outputs.DataSourceSslProperties]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectionProperties")
    def vpc_connection_properties(
        self,
    ) -> pulumi.Output[Optional[outputs.DataSourceVpcConnectionProperties]]: ...
