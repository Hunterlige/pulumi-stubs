

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, autoscaling_group_name: pulumi.Input[_builtins.str], adjustment_type: Optional[pulumi.Input[_builtins.str]] = ..., cooldown: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., metric_aggregation_type: Optional[pulumi.Input[_builtins.str]] = ..., min_adjustment_magnitude: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type: Optional[pulumi.Input[_builtins.str]] = ..., predictive_scaling_configuration: Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_adjustment: Optional[pulumi.Input[_builtins.int]] = ..., step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]] = ..., target_tracking_configuration: Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]]:
        
        ...
    
    @predictive_scaling_configuration.setter
    def predictive_scaling_configuration(self, value: Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scaling_adjustment.setter
    def scaling_adjustment(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]]:
        
        ...
    
    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]]:
        
        ...
    
    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, adjustment_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., cooldown: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., metric_aggregation_type: Optional[pulumi.Input[_builtins.str]] = ..., min_adjustment_magnitude: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type: Optional[pulumi.Input[_builtins.str]] = ..., predictive_scaling_configuration: Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_adjustment: Optional[pulumi.Input[_builtins.int]] = ..., step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]] = ..., target_tracking_configuration: Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adjustment_type.setter
    def adjustment_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autoscaling_group_name.setter
    def autoscaling_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @cooldown.setter
    def cooldown(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]]:
        
        ...
    
    @predictive_scaling_configuration.setter
    def predictive_scaling_configuration(self, value: Optional[pulumi.Input[PolicyPredictiveScalingConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @scaling_adjustment.setter
    def scaling_adjustment(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]]:
        
        ...
    
    @step_adjustments.setter
    def step_adjustments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyStepAdjustmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]]:
        
        ...
    
    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: Optional[pulumi.Input[PolicyTargetTrackingConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:autoscaling/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., adjustment_type: Optional[pulumi.Input[_builtins.str]] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., cooldown: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., metric_aggregation_type: Optional[pulumi.Input[_builtins.str]] = ..., min_adjustment_magnitude: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type: Optional[pulumi.Input[_builtins.str]] = ..., predictive_scaling_configuration: Optional[pulumi.Input[Union[PolicyPredictiveScalingConfigurationArgs, PolicyPredictiveScalingConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_adjustment: Optional[pulumi.Input[_builtins.int]] = ..., step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyStepAdjustmentArgs, PolicyStepAdjustmentArgsDict]]]]] = ..., target_tracking_configuration: Optional[pulumi.Input[Union[PolicyTargetTrackingConfigurationArgs, PolicyTargetTrackingConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., adjustment_type: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., autoscaling_group_name: Optional[pulumi.Input[_builtins.str]] = ..., cooldown: Optional[pulumi.Input[_builtins.int]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ..., metric_aggregation_type: Optional[pulumi.Input[_builtins.str]] = ..., min_adjustment_magnitude: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_type: Optional[pulumi.Input[_builtins.str]] = ..., predictive_scaling_configuration: Optional[pulumi.Input[Union[PolicyPredictiveScalingConfigurationArgs, PolicyPredictiveScalingConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., scaling_adjustment: Optional[pulumi.Input[_builtins.int]] = ..., step_adjustments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyStepAdjustmentArgs, PolicyStepAdjustmentArgsDict]]]]] = ..., target_tracking_configuration: Optional[pulumi.Input[Union[PolicyTargetTrackingConfigurationArgs, PolicyTargetTrackingConfigurationArgsDict]]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingGroupName")
    def autoscaling_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cooldown(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> pulumi.Output[Optional[outputs.PolicyPredictiveScalingConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> pulumi.Output[Optional[Sequence[outputs.PolicyStepAdjustment]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> pulumi.Output[Optional[outputs.PolicyTargetTrackingConfiguration]]:
        
        ...
    


