import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainPermissionsArgs", "DomainPermissions"]

@pulumi.input_type
class DomainPermissionsArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_owner.setter
    def domain_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_revision.setter
    def policy_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _DomainPermissionsState:
    def __init__(
        __self__,
        *,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_revision.setter
    def policy_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_arn.setter
    def resource_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class DomainPermissions(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainPermissionsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_document: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> DomainPermissions: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyRevision")
    def policy_revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[_builtins.str]: ...
