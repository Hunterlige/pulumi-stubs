import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CertificateObjectGlobalRulestackArgs", "CertificateObjectGlobalRulestack"]

@pulumi.input_type
class CertificateObjectGlobalRulestackArgs:
    def __init__(
        __self__,
        *,
        certificate_self_signed: pulumi.Input[Union[_builtins.str, BooleanEnum]],
        global_rulestack_name: pulumi.Input[_builtins.str],
        audit_comment: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_signer_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(
        self,
    ) -> pulumi.Input[Union[_builtins.str, BooleanEnum]]: ...
    @certificate_self_signed.setter
    def certificate_self_signed(
        self, value: pulumi.Input[Union[_builtins.str, BooleanEnum]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalRulestackName")
    def global_rulestack_name(self) -> pulumi.Input[_builtins.str]: ...
    @global_rulestack_name.setter
    def global_rulestack_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_signer_resource_id.setter
    def certificate_signer_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class CertificateObjectGlobalRulestack(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        audit_comment: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate_self_signed: Optional[
            pulumi.Input[Union[_builtins.str, BooleanEnum]]
        ] = ...,
        certificate_signer_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        global_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CertificateObjectGlobalRulestackArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> CertificateObjectGlobalRulestack: ...
    @_builtins.property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
