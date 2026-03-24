import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IamAuditConfigArgs", "IamAuditConfig"]

@pulumi.input_type
class IamAuditConfigArgs:
    def __init__(
        __self__,
        *,
        audit_log_configs: pulumi.Input[
            Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]
        ],
        org_id: pulumi.Input[_builtins.str],
        service: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]]: ...
    @audit_log_configs.setter
    def audit_log_configs(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _IamAuditConfigState:
    def __init__(
        __self__,
        *,
        audit_log_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]]
    ]: ...
    @audit_log_configs.setter
    def audit_log_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IamAuditConfigAuditLogConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:organizations/iamAuditConfig:IamAuditConfig")
class IamAuditConfig(pulumi.CustomResource):
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
                            IamAuditConfigAuditLogConfigArgs,
                            IamAuditConfigAuditLogConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IamAuditConfigArgs,
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
                            IamAuditConfigAuditLogConfigArgs,
                            IamAuditConfigAuditLogConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> IamAuditConfig: ...
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.IamAuditConfigAuditLogConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Output[_builtins.str]: ...
