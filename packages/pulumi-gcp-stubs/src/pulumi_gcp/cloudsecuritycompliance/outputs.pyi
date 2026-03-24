

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CloudControlParameterSpec', 'CloudControlParameterSpecDefaultValue', 'CloudControlParameterSpecDefaultValueOneofValue', ..., ..., ..., 'CloudControlParameterSpecSubParameter', 'CloudControlParameterSpecSubParameterDefaultValue', ..., ..., ..., ..., ..., ..., ..., 'CloudControlParameterSpecSubParameterValidation', ..., ..., ..., ..., ..., ..., ..., ..., 'CloudControlParameterSpecSubstitutionRule', ..., ..., 'CloudControlParameterSpecValidation', 'CloudControlParameterSpecValidationAllowedValues', ..., ..., ..., ..., ..., 'CloudControlParameterSpecValidationIntRange', 'CloudControlParameterSpecValidationRegexpPattern', 'CloudControlRule', 'CloudControlRuleCelExpression', 'CloudControlRuleCelExpressionResourceTypesValues', 'FrameworkCloudControlDetail', 'FrameworkCloudControlDetailParameter', 'FrameworkCloudControlDetailParameterParameterValue', ..., ..., ..., ..., 'FrameworkDeploymentCloudControlDeploymentReference', 'FrameworkDeploymentCloudControlMetadata', ..., ..., ..., ..., ..., ..., ..., 'FrameworkDeploymentFramework', 'FrameworkDeploymentTargetResourceConfig', ..., ..., ...]
@pulumi.output_type
class CloudControlParameterSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_required: _builtins.bool, name: _builtins.str, value_type: _builtins.str, default_value: Optional[outputs.CloudControlParameterSpecDefaultValue] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., sub_parameters: Optional[Sequence[outputs.CloudControlParameterSpecSubParameter]] = ..., substitution_rules: Optional[Sequence[outputs.CloudControlParameterSpecSubstitutionRule]] = ..., validation: Optional[outputs.CloudControlParameterSpecValidation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[outputs.CloudControlParameterSpecDefaultValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subParameters")
    def sub_parameters(self) -> Optional[Sequence[outputs.CloudControlParameterSpecSubParameter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="substitutionRules")
    def substitution_rules(self) -> Optional[Sequence[outputs.CloudControlParameterSpecSubstitutionRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.CloudControlParameterSpecValidation]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecDefaultValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.CloudControlParameterSpecDefaultValueOneofValue] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecDefaultValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.CloudControlParameterSpecDefaultValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecDefaultValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecDefaultValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.CloudControlParameterSpecDefaultValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.CloudControlParameterSpecDefaultValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecDefaultValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecDefaultValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecDefaultValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, is_required: _builtins.bool, name: _builtins.str, value_type: _builtins.str, default_value: Optional[outputs.CloudControlParameterSpecSubParameterDefaultValue] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., substitution_rules: Optional[Sequence[outputs.CloudControlParameterSpecSubParameterSubstitutionRule]] = ..., validation: Optional[outputs.CloudControlParameterSpecSubParameterValidation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterDefaultValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="substitutionRules")
    def substitution_rules(self) -> Optional[Sequence[outputs.CloudControlParameterSpecSubParameterSubstitutionRule]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidation]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterDefaultValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValue] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterDefaultValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterDefaultValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterSubstitutionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_substitution_rule: Optional[outputs.CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRule] = ..., placeholder_substitution_rule: Optional[outputs.CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeSubstitutionRule")
    def attribute_substitution_rule(self) -> Optional[outputs.CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placeholderSubstitutionRule")
    def placeholder_substitution_rule(self) -> Optional[outputs.CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRule]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterSubstitutionRuleAttributeSubstitutionRule(dict):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterSubstitutionRulePlaceholderSubstitutionRule(dict):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValues] = ..., int_range: Optional[outputs.CloudControlParameterSpecSubParameterValidationIntRange] = ..., regexp_pattern: Optional[outputs.CloudControlParameterSpecSubParameterValidationRegexpPattern] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValues]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intRange")
    def int_range(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationIntRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexpPattern")
    def regexp_pattern(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationRegexpPattern]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValues(dict):
    def __init__(__self__, *, values: Sequence[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValue]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValue] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationAllowedValuesValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationIntRange(dict):
    def __init__(__self__, *, max: _builtins.str, min: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubParameterValidationRegexpPattern(dict):
    def __init__(__self__, *, pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubstitutionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_substitution_rule: Optional[outputs.CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRule] = ..., placeholder_substitution_rule: Optional[outputs.CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeSubstitutionRule")
    def attribute_substitution_rule(self) -> Optional[outputs.CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placeholderSubstitutionRule")
    def placeholder_substitution_rule(self) -> Optional[outputs.CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRule]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubstitutionRuleAttributeSubstitutionRule(dict):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecSubstitutionRulePlaceholderSubstitutionRule(dict):
    def __init__(__self__, *, attribute: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allowed_values: Optional[outputs.CloudControlParameterSpecValidationAllowedValues] = ..., int_range: Optional[outputs.CloudControlParameterSpecValidationIntRange] = ..., regexp_pattern: Optional[outputs.CloudControlParameterSpecValidationRegexpPattern] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[outputs.CloudControlParameterSpecValidationAllowedValues]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intRange")
    def int_range(self) -> Optional[outputs.CloudControlParameterSpecValidationIntRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexpPattern")
    def regexp_pattern(self) -> Optional[outputs.CloudControlParameterSpecValidationRegexpPattern]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValues(dict):
    def __init__(__self__, *, values: Sequence[outputs.CloudControlParameterSpecValidationAllowedValuesValue]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[outputs.CloudControlParameterSpecValidationAllowedValuesValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValuesValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValue] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValuesValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationAllowedValuesValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationIntRange(dict):
    def __init__(__self__, *, max: _builtins.str, min: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudControlParameterSpecValidationRegexpPattern(dict):
    def __init__(__self__, *, pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class CloudControlRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rule_action_types: Sequence[_builtins.str], cel_expression: Optional[outputs.CloudControlRuleCelExpression] = ..., description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleActionTypes")
    def rule_action_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="celExpression")
    def cel_expression(self) -> Optional[outputs.CloudControlRuleCelExpression]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class CloudControlRuleCelExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression: _builtins.str, resource_types_values: Optional[outputs.CloudControlRuleCelExpressionResourceTypesValues] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypesValues")
    def resource_types_values(self) -> Optional[outputs.CloudControlRuleCelExpressionResourceTypesValues]:
        
        ...
    


@pulumi.output_type
class CloudControlRuleCelExpressionResourceTypesValues(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, major_revision_id: _builtins.str, name: _builtins.str, parameters: Optional[Sequence[outputs.FrameworkCloudControlDetailParameter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.FrameworkCloudControlDetailParameter]]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, parameter_value: outputs.FrameworkCloudControlDetailParameterParameterValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> outputs.FrameworkCloudControlDetailParameterParameterValue:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameterParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValue] = ..., string_list_value: Optional[outputs.FrameworkCloudControlDetailParameterParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.FrameworkCloudControlDetailParameterParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameterParameterValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameterParameterValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkCloudControlDetailParameterParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlDeploymentReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_control_deployment: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlDeployment")
    def cloud_control_deployment(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadata(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_control_details: outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetails, enforcement_mode: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudControlDetails")
    def cloud_control_details(self) -> outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetails:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, major_revision_id: _builtins.str, name: _builtins.str, parameters: Optional[Sequence[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameter]]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, parameter_value: outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValue:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., oneof_value: Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValue] = ..., string_list_value: Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oneofValue")
    def oneof_value(self) -> Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., parameter_value: Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValue]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bool_value: Optional[_builtins.bool] = ..., number_value: Optional[_builtins.float] = ..., string_list_value: Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValue] = ..., string_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberValue")
    def number_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringListValue")
    def string_list_value(self) -> Optional[outputs.FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueOneofValueParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentCloudControlMetadataCloudControlDetailsParameterParameterValueStringListValue(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentFramework(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, framework: _builtins.str, major_revision_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def framework(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="majorRevisionId")
    def major_revision_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentTargetResourceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, existing_target_resource: Optional[_builtins.str] = ..., target_resource_creation_config: Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="existingTargetResource")
    def existing_target_resource(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceCreationConfig")
    def target_resource_creation_config(self) -> Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfig]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, folder_creation_config: Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfig] = ..., project_creation_config: Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderCreationConfig")
    def folder_creation_config(self) -> Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectCreationConfig")
    def project_creation_config(self) -> Optional[outputs.FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfig]:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigFolderCreationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, folder_display_name: _builtins.str, parent: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderDisplayName")
    def folder_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class FrameworkDeploymentTargetResourceConfigTargetResourceCreationConfigProjectCreationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, billing_account_id: _builtins.str, parent: _builtins.str, project_display_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectDisplayName")
    def project_display_name(self) -> _builtins.str:
        
        ...
    


