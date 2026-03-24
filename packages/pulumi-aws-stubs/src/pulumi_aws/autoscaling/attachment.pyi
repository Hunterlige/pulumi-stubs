import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AttachmentArgs", "Attachment"]

@pulumi.input_type
class AttachmentArgs:
    def __init__(
        __self__,
        *,
        autoscaling_group_name: pulumi.Input[_builtins.str],
        elb: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def elb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elb.setter
    def elb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lbTargetGroupArn")
    def lb_target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lb_target_group_arn.setter
    def lb_target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AttachmentState:
    def __init__(
        __self__,
        *,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elb: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def elb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elb.setter
    def elb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lbTargetGroupArn")
    def lb_target_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lb_target_group_arn.setter
    def lb_target_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:autoscaling/attachment:Attachment")
class Attachment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elb: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AttachmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elb: Optional[pulumi.Input[_builtins.str]] = ...,
        lb_target_group_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Attachment: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def elb(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lbTargetGroupArn")
    def lb_target_group_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
