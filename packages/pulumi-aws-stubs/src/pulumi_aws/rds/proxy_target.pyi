import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProxyTargetArgs", "ProxyTarget"]

@pulumi.input_type
class ProxyTargetArgs:
    def __init__(
        __self__,
        *,
        db_proxy_name: pulumi.Input[_builtins.str],
        target_group_name: pulumi.Input[_builtins.str],
        db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Input[_builtins.str]: ...
    @db_proxy_name.setter
    def db_proxy_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupName")
    def target_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @target_group_name.setter
    def target_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_identifier.setter
    def db_instance_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ProxyTargetState:
    def __init__(
        __self__,
        *,
        db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        rds_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tracked_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_cluster_identifier.setter
    def db_cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_instance_identifier.setter
    def db_instance_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @db_proxy_name.setter
    def db_proxy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rdsResourceId")
    def rds_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rds_resource_id.setter
    def rds_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_arn.setter
    def target_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetGroupName")
    def target_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_group_name.setter
    def target_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trackedClusterId")
    def tracked_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tracked_cluster_id.setter
    def tracked_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:rds/proxyTarget:ProxyTarget")
class ProxyTarget(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ProxyTargetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        db_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        db_proxy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        rds_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        target_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        target_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tracked_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ProxyTarget: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbProxyName")
    def db_proxy_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rdsResourceId")
    def rds_resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetGroupName")
    def target_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackedClusterId")
    def tracked_cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
