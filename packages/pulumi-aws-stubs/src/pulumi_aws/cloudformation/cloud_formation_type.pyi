import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CloudFormationTypeArgs", "CloudFormationType"]

@pulumi.input_type
class CloudFormationTypeArgs:
    def __init__(
        __self__,
        *,
        schema_handler_package: pulumi.Input[_builtins.str],
        type_name: pulumi.Input[_builtins.str],
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[CloudFormationTypeLoggingConfigArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> pulumi.Input[_builtins.str]: ...
    @schema_handler_package.setter
    def schema_handler_package(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Input[_builtins.str]: ...
    @type_name.setter
    def type_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[CloudFormationTypeLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[CloudFormationTypeLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CloudFormationTypeState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecated_status: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        logging_config: Optional[
            pulumi.Input[CloudFormationTypeLoggingConfigArgs]
        ] = ...,
        provisioning_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_handler_package: Optional[pulumi.Input[_builtins.str]] = ...,
        source_url: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultVersionId")
    def default_version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_version_id.setter
    def default_version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deprecatedStatus")
    def deprecated_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deprecated_status.setter
    def deprecated_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation_url.setter
    def documentation_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_version.setter
    def is_default_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> Optional[pulumi.Input[CloudFormationTypeLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[CloudFormationTypeLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_type.setter
    def provisioning_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_handler_package.setter
    def schema_handler_package(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_url.setter
    def source_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeArn")
    def type_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_arn.setter
    def type_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_name.setter
    def type_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class CloudFormationType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    CloudFormationTypeLoggingConfigArgs,
                    CloudFormationTypeLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_handler_package: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CloudFormationTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        default_version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        deprecated_status: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[
                    CloudFormationTypeLoggingConfigArgs,
                    CloudFormationTypeLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        provisioning_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_handler_package: Optional[pulumi.Input[_builtins.str]] = ...,
        source_url: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        type_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        visibility: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CloudFormationType: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultVersionId")
    def default_version_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deprecatedStatus")
    def deprecated_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(
        self,
    ) -> pulumi.Output[Optional[outputs.CloudFormationTypeLoggingConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningType")
    def provisioning_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaHandlerPackage")
    def schema_handler_package(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeArn")
    def type_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="typeName")
    def type_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[_builtins.str]: ...
