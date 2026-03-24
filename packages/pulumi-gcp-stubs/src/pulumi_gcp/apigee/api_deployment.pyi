import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiDeploymentArgs", "ApiDeployment"]

@pulumi.input_type
class ApiDeploymentArgs:
    def __init__(
        __self__,
        *,
        environment: pulumi.Input[_builtins.str],
        org_id: pulumi.Input[_builtins.str],
        proxy_id: pulumi.Input[_builtins.str],
        revision: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Input[_builtins.str]: ...
    @environment.setter
    def environment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Input[_builtins.str]: ...
    @org_id.setter
    def org_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Input[_builtins.str]: ...
    @proxy_id.setter
    def proxy_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Input[_builtins.str]: ...
    @revision.setter
    def revision(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _ApiDeploymentState:
    def __init__(
        __self__,
        *,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @proxy_id.setter
    def proxy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:apigee/apiDeployment:ApiDeployment")
class ApiDeployment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiDeploymentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        environment: Optional[pulumi.Input[_builtins.str]] = ...,
        org_id: Optional[pulumi.Input[_builtins.str]] = ...,
        proxy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ApiDeployment: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="proxyId")
    def proxy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.str]: ...
