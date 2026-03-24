import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IAMAuditConfigArgs", "IAMAuditConfig"]

@pulumi.input_type
class IAMAuditConfigArgs:
    def __init__(
        __self__,
        *,
        audit_log_configs: pulumi.Input[
            Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]
        ],
        project: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]]: ...
    @audit_log_configs.setter
    def audit_log_configs(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _IAMAuditConfigState:
    def __init__(
        __self__,
        *,
        audit_log_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]]
    ]: ...
    @audit_log_configs.setter
    def audit_log_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IAMAuditConfigAuditLogConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:projects/iAMAuditConfig:IAMAuditConfig")
class IAMAuditConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_log_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IAMAuditConfigAuditLogConfigArgs,
                            IAMAuditConfigAuditLogConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IAMAuditConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_log_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IAMAuditConfigAuditLogConfigArgs,
                            IAMAuditConfigAuditLogConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IAMAuditConfig: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.IAMAuditConfigAuditLogConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]: ...
