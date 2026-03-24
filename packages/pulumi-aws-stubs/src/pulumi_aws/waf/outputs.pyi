

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ByteMatchSetByteMatchTuple', 'ByteMatchSetByteMatchTupleFieldToMatch', 'GeoMatchSetGeoMatchConstraint', 'IpSetIpSetDescriptor', 'RateBasedRulePredicate', 'RegexMatchSetRegexMatchTuple', 'RegexMatchSetRegexMatchTupleFieldToMatch', 'RuleGroupActivatedRule', 'RuleGroupActivatedRuleAction', 'RulePredicate', 'SizeConstraintSetSizeConstraint', 'SizeConstraintSetSizeConstraintFieldToMatch', 'SqlInjectionMatchSetSqlInjectionMatchTuple', ..., 'WebAclDefaultAction', 'WebAclLoggingConfiguration', 'WebAclLoggingConfigurationRedactedFields', ..., 'WebAclRule', 'WebAclRuleAction', 'WebAclRuleOverrideAction', 'XssMatchSetXssMatchTuple', 'XssMatchSetXssMatchTupleFieldToMatch']
@pulumi.output_type
class ByteMatchSetByteMatchTuple(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_to_match: outputs.ByteMatchSetByteMatchTupleFieldToMatch, positional_constraint: _builtins.str, text_transformation: _builtins.str, target_string: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> outputs.ByteMatchSetByteMatchTupleFieldToMatch:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetString")
    def target_string(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ByteMatchSetByteMatchTupleFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GeoMatchSetGeoMatchConstraint(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IpSetIpSetDescriptor(dict):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RateBasedRulePredicate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_id: _builtins.str, negated: _builtins.bool, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def negated(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegexMatchSetRegexMatchTuple(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_to_match: outputs.RegexMatchSetRegexMatchTupleFieldToMatch, regex_pattern_set_id: _builtins.str, text_transformation: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> outputs.RegexMatchSetRegexMatchTupleFieldToMatch:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetId")
    def regex_pattern_set_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegexMatchSetRegexMatchTupleFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupActivatedRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: outputs.RuleGroupActivatedRuleAction, priority: _builtins.int, rule_id: _builtins.str, type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RuleGroupActivatedRuleAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupActivatedRuleAction(dict):
    def __init__(__self__, *, type: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class RulePredicate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_id: _builtins.str, negated: _builtins.bool, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def negated(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SizeConstraintSetSizeConstraint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, field_to_match: outputs.SizeConstraintSetSizeConstraintFieldToMatch, size: _builtins.int, text_transformation: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> outputs.SizeConstraintSetSizeConstraintFieldToMatch:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SizeConstraintSetSizeConstraintFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SqlInjectionMatchSetSqlInjectionMatchTuple(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_to_match: outputs.SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatch, text_transformation: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> outputs.SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatch:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultAction(dict):
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_destination: _builtins.str, redacted_fields: Optional[outputs.WebAclLoggingConfigurationRedactedFields] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[outputs.WebAclLoggingConfigurationRedactedFields]:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFields(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_to_matches: Sequence[outputs.WebAclLoggingConfigurationRedactedFieldsFieldToMatch]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatches")
    def field_to_matches(self) -> Sequence[outputs.WebAclLoggingConfigurationRedactedFieldsFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFieldsFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, priority: _builtins.int, rule_id: _builtins.str, action: Optional[outputs.WebAclRuleAction] = ..., override_action: Optional[outputs.WebAclRuleOverrideAction] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.WebAclRuleAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> Optional[outputs.WebAclRuleOverrideAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleAction(dict):
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleOverrideAction(dict):
    def __init__(__self__, *, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class XssMatchSetXssMatchTuple(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_to_match: outputs.XssMatchSetXssMatchTupleFieldToMatch, text_transformation: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> outputs.XssMatchSetXssMatchTupleFieldToMatch:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class XssMatchSetXssMatchTupleFieldToMatch(dict):
    def __init__(__self__, *, type: _builtins.str, data: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    


