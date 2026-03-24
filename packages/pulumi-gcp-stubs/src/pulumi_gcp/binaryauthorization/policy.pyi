

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
    def __init__(__self__, *, default_admission_rule: pulumi.Input[PolicyDefaultAdmissionRuleArgs], admission_whitelist_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]] = ..., cluster_admission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_policy_evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAdmissionRule")
    def default_admission_rule(self) -> pulumi.Input[PolicyDefaultAdmissionRuleArgs]:
        
        ...
    
    @default_admission_rule.setter
    def default_admission_rule(self, value: pulumi.Input[PolicyDefaultAdmissionRuleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="admissionWhitelistPatterns")
    def admission_whitelist_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]]:
        
        ...
    
    @admission_whitelist_patterns.setter
    def admission_whitelist_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAdmissionRules")
    def cluster_admission_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]]:
        
        ...
    
    @cluster_admission_rules.setter
    def cluster_admission_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalPolicyEvaluationMode")
    def global_policy_evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_policy_evaluation_mode.setter
    def global_policy_evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, admission_whitelist_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]] = ..., cluster_admission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]] = ..., default_admission_rule: Optional[pulumi.Input[PolicyDefaultAdmissionRuleArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_policy_evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="admissionWhitelistPatterns")
    def admission_whitelist_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]]:
        
        ...
    
    @admission_whitelist_patterns.setter
    def admission_whitelist_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyAdmissionWhitelistPatternArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAdmissionRules")
    def cluster_admission_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]]:
        
        ...
    
    @cluster_admission_rules.setter
    def cluster_admission_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PolicyClusterAdmissionRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAdmissionRule")
    def default_admission_rule(self) -> Optional[pulumi.Input[PolicyDefaultAdmissionRuleArgs]]:
        
        ...
    
    @default_admission_rule.setter
    def default_admission_rule(self, value: Optional[pulumi.Input[PolicyDefaultAdmissionRuleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalPolicyEvaluationMode")
    def global_policy_evaluation_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @global_policy_evaluation_mode.setter
    def global_policy_evaluation_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:binaryauthorization/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admission_whitelist_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyAdmissionWhitelistPatternArgs, PolicyAdmissionWhitelistPatternArgsDict]]]]] = ..., cluster_admission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyClusterAdmissionRuleArgs, PolicyClusterAdmissionRuleArgsDict]]]]] = ..., default_admission_rule: Optional[pulumi.Input[Union[PolicyDefaultAdmissionRuleArgs, PolicyDefaultAdmissionRuleArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_policy_evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admission_whitelist_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyAdmissionWhitelistPatternArgs, PolicyAdmissionWhitelistPatternArgsDict]]]]] = ..., cluster_admission_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyClusterAdmissionRuleArgs, PolicyClusterAdmissionRuleArgsDict]]]]] = ..., default_admission_rule: Optional[pulumi.Input[Union[PolicyDefaultAdmissionRuleArgs, PolicyDefaultAdmissionRuleArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., global_policy_evaluation_mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="admissionWhitelistPatterns")
    def admission_whitelist_patterns(self) -> pulumi.Output[Optional[Sequence[outputs.PolicyAdmissionWhitelistPattern]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAdmissionRules")
    def cluster_admission_rules(self) -> pulumi.Output[Optional[Sequence[outputs.PolicyClusterAdmissionRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultAdmissionRule")
    def default_admission_rule(self) -> pulumi.Output[outputs.PolicyDefaultAdmissionRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalPolicyEvaluationMode")
    def global_policy_evaluation_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


