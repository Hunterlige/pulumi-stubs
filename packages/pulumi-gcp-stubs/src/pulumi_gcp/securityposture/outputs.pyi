

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PosturePolicySet', 'PosturePolicySetPolicy', 'PosturePolicySetPolicyComplianceStandard', 'PosturePolicySetPolicyConstraint', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...]
@pulumi.output_type
class PosturePolicySet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policies: Sequence[outputs.PosturePolicySetPolicy], policy_set_id: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Sequence[outputs.PosturePolicySetPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policySetId")
    def policy_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, constraint: outputs.PosturePolicySetPolicyConstraint, policy_id: _builtins.str, compliance_standards: Optional[Sequence[outputs.PosturePolicySetPolicyComplianceStandard]] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def constraint(self) -> outputs.PosturePolicySetPolicyConstraint:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStandards")
    def compliance_standards(self) -> Optional[Sequence[outputs.PosturePolicySetPolicyComplianceStandard]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyComplianceStandard(dict):
    def __init__(__self__, *, control: Optional[_builtins.str] = ..., standard: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def control(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def standard(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, org_policy_constraint: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraint] = ..., org_policy_constraint_custom: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustom] = ..., security_health_analytics_custom_module: Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModule] = ..., security_health_analytics_module: Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgPolicyConstraint")
    def org_policy_constraint(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgPolicyConstraintCustom")
    def org_policy_constraint_custom(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustom]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityHealthAnalyticsCustomModule")
    def security_health_analytics_custom_module(self) -> Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityHealthAnalyticsModule")
    def security_health_analytics_module(self) -> Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModule]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, canned_constraint_id: _builtins.str, policy_rules: Sequence[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRule]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cannedConstraintId")
    def canned_constraint_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRules")
    def policy_rules(self) -> Sequence[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRule]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustom(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_rules: Sequence[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRule], custom_constraint: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraint] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyRules")
    def policy_rules(self) -> Sequence[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customConstraint")
    def custom_constraint(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraint]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomCustomConstraint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_type: _builtins.str, condition: _builtins.str, method_types: Sequence[_builtins.str], name: _builtins.str, resource_types: Sequence[_builtins.str], description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="methodTypes")
    def method_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all: Optional[_builtins.bool] = ..., condition: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleCondition] = ..., deny_all: Optional[_builtins.bool] = ..., enforce: Optional[_builtins.bool] = ..., values: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValues]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintCustomPolicyRuleValues(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[Sequence[_builtins.str]] = ..., denied_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_all: Optional[_builtins.bool] = ..., condition: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleCondition] = ..., deny_all: Optional[_builtins.bool] = ..., enforce: Optional[_builtins.bool] = ..., values: Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAll")
    def allow_all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="denyAll")
    def deny_all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforce(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[outputs.PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValues]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintOrgPolicyConstraintPolicyRuleValues(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[Sequence[_builtins.str]] = ..., denied_values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deniedValues")
    def denied_values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, config: outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfig, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., module_enablement_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moduleEnablementState")
    def module_enablement_state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, predicate: outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicate, resource_selector: outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelector, severity: _builtins.str, custom_output: Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutput] = ..., description: Optional[_builtins.str] = ..., recommendation: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def predicate(self) -> outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicate:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelector")
    def resource_selector(self) -> outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelector:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customOutput")
    def custom_output(self) -> Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutput]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def recommendation(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutput(dict):
    def __init__(__self__, *, properties: Optional[Sequence[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputProperty]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[Sequence[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputProperty]]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value_expression: Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpression] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueExpression")
    def value_expression(self) -> Optional[outputs.PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpression]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigCustomOutputPropertyValueExpression(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigPredicate(dict):
    def __init__(__self__, *, expression: _builtins.str, description: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsCustomModuleConfigResourceSelector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_types: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PosturePolicySetPolicyConstraintSecurityHealthAnalyticsModule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, module_name: _builtins.str, module_enablement_state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moduleName")
    def module_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="moduleEnablementState")
    def module_enablement_state(self) -> Optional[_builtins.str]:
        
        ...
    


