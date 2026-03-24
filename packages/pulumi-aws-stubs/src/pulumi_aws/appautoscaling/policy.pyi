import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyArgs", "Policy"]

@pulumi.input_type
class PolicyArgs:
    def __init__(
        __self__,
        *,
        resource_id: pulumi.Input[_builtins.str],
        scalable_dimension: pulumi.Input[_builtins.str],
        service_namespace: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predictive_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        step_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]
        ] = ...,
        target_tracking_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Input[_builtins.str]: ...
    @scalable_dimension.setter
    def scalable_dimension(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Input[_builtins.str]: ...
    @service_namespace.setter
    def service_namespace(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingPolicyConfiguration")
    def predictive_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]]: ...
    @predictive_scaling_policy_configuration.setter
    def predictive_scaling_policy_configuration(
        self,
        value: Optional[pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]]: ...
    @step_scaling_policy_configuration.setter
    def step_scaling_policy_configuration(
        self, value: Optional[pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]]: ...
    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(
        self,
        value: Optional[
            pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]
        ],
    ): ...

@pulumi.input_type
class _PolicyState:
    def __init__(
        __self__,
        *,
        alarm_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predictive_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        step_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]
        ] = ...,
        target_tracking_scaling_policy_configuration: Optional[
            pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alarmArns")
    def alarm_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @alarm_arns.setter
    def alarm_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingPolicyConfiguration")
    def predictive_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]]: ...
    @predictive_scaling_policy_configuration.setter
    def predictive_scaling_policy_configuration(
        self,
        value: Optional[pulumi.Input[PolicyPredictiveScalingPolicyConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scalable_dimension.setter
    def scalable_dimension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_namespace.setter
    def service_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]]: ...
    @step_scaling_policy_configuration.setter
    def step_scaling_policy_configuration(
        self, value: Optional[pulumi.Input[PolicyStepScalingPolicyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> Optional[pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]]: ...
    @target_tracking_scaling_policy_configuration.setter
    def target_tracking_scaling_policy_configuration(
        self,
        value: Optional[
            pulumi.Input[PolicyTargetTrackingScalingPolicyConfigurationArgs]
        ],
    ): ...

@pulumi.type_token("aws:appautoscaling/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predictive_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyPredictiveScalingPolicyConfigurationArgs,
                    PolicyPredictiveScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        step_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyStepScalingPolicyConfigurationArgs,
                    PolicyStepScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        target_tracking_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyTargetTrackingScalingPolicyConfigurationArgs,
                    PolicyTargetTrackingScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alarm_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_type: Optional[pulumi.Input[_builtins.str]] = ...,
        predictive_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyPredictiveScalingPolicyConfigurationArgs,
                    PolicyPredictiveScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        scalable_dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        service_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        step_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyStepScalingPolicyConfigurationArgs,
                    PolicyStepScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        target_tracking_scaling_policy_configuration: Optional[
            pulumi.Input[
                Union[
                    PolicyTargetTrackingScalingPolicyConfigurationArgs,
                    PolicyTargetTrackingScalingPolicyConfigurationArgsDict,
                ]
            ]
        ] = ...,
    ) -> Policy: ...
    @_builtins.property
    @pulumi.getter(name="alarmArns")
    def alarm_arns(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="predictiveScalingPolicyConfiguration")
    def predictive_scaling_policy_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.PolicyPredictiveScalingPolicyConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalableDimension")
    def scalable_dimension(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNamespace")
    def service_namespace(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stepScalingPolicyConfiguration")
    def step_scaling_policy_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.PolicyStepScalingPolicyConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingPolicyConfiguration")
    def target_tracking_scaling_policy_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.PolicyTargetTrackingScalingPolicyConfiguration]
    ]: ...
