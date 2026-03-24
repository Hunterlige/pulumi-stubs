import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecretVersionArgs", "SecretVersion"]

@pulumi.input_type
class SecretVersionArgs:
    def __init__(
        __self__,
        *,
        secret_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_binary: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        version_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[_builtins.str]: ...
    @secret_id.setter
    def secret_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretBinary")
    def secret_binary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_binary.setter
    def secret_binary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_string.setter
    def secret_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStringWo")
    def secret_string_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_string_wo.setter
    def secret_string_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStringWoVersion")
    def secret_string_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secret_string_wo_version.setter
    def secret_string_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionStages")
    def version_stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @version_stages.setter
    def version_stages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _SecretVersionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        has_secret_string_wo: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_binary: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hasSecretStringWo")
    def has_secret_string_wo(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_secret_string_wo.setter
    def has_secret_string_wo(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretBinary")
    def secret_binary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_binary.setter
    def secret_binary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_string.setter
    def secret_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStringWo")
    def secret_string_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_string_wo.setter
    def secret_string_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretStringWoVersion")
    def secret_string_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @secret_string_wo_version.setter
    def secret_string_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version_id.setter
    def version_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="versionStages")
    def version_stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @version_stages.setter
    def version_stages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:secretsmanager/secretVersion:SecretVersion")
class SecretVersion(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_binary: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        version_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecretVersionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        has_secret_string_wo: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_binary: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_string_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        version_id: Optional[pulumi.Input[_builtins.str]] = ...,
        version_stages: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> SecretVersion: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hasSecretStringWo")
    def has_secret_string_wo(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretBinary")
    def secret_binary(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretStringWo")
    def secret_string_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretStringWoVersion")
    def secret_string_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="versionStages")
    def version_stages(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
