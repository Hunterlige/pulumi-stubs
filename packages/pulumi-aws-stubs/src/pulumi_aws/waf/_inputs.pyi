

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ByteMatchSetByteMatchTupleArgs', 'ByteMatchSetByteMatchTupleArgsDict', 'ByteMatchSetByteMatchTupleFieldToMatchArgs', 'ByteMatchSetByteMatchTupleFieldToMatchArgsDict', 'GeoMatchSetGeoMatchConstraintArgs', 'GeoMatchSetGeoMatchConstraintArgsDict', 'IpSetIpSetDescriptorArgs', 'IpSetIpSetDescriptorArgsDict', 'RateBasedRulePredicateArgs', 'RateBasedRulePredicateArgsDict', 'RegexMatchSetRegexMatchTupleArgs', 'RegexMatchSetRegexMatchTupleArgsDict', 'RegexMatchSetRegexMatchTupleFieldToMatchArgs', 'RegexMatchSetRegexMatchTupleFieldToMatchArgsDict', 'RuleGroupActivatedRuleArgs', 'RuleGroupActivatedRuleArgsDict', 'RuleGroupActivatedRuleActionArgs', 'RuleGroupActivatedRuleActionArgsDict', 'RulePredicateArgs', 'RulePredicateArgsDict', 'SizeConstraintSetSizeConstraintArgs', 'SizeConstraintSetSizeConstraintArgsDict', 'SizeConstraintSetSizeConstraintFieldToMatchArgs', ..., 'SqlInjectionMatchSetSqlInjectionMatchTupleArgs', 'SqlInjectionMatchSetSqlInjectionMatchTupleArgsDict', ..., ..., 'WebAclDefaultActionArgs', 'WebAclDefaultActionArgsDict', 'WebAclLoggingConfigurationArgs', 'WebAclLoggingConfigurationArgsDict', 'WebAclLoggingConfigurationRedactedFieldsArgs', 'WebAclLoggingConfigurationRedactedFieldsArgsDict', ..., ..., 'WebAclRuleArgs', 'WebAclRuleArgsDict', 'WebAclRuleActionArgs', 'WebAclRuleActionArgsDict', 'WebAclRuleOverrideActionArgs', 'WebAclRuleOverrideActionArgsDict', 'XssMatchSetXssMatchTupleArgs', 'XssMatchSetXssMatchTupleArgsDict', 'XssMatchSetXssMatchTupleFieldToMatchArgs', 'XssMatchSetXssMatchTupleFieldToMatchArgsDict']
class ByteMatchSetByteMatchTupleArgsDict(TypedDict):
    field_to_match: pulumi.Input[ByteMatchSetByteMatchTupleFieldToMatchArgsDict]
    positional_constraint: pulumi.Input[_builtins.str]
    text_transformation: pulumi.Input[_builtins.str]
    target_string: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ByteMatchSetByteMatchTupleArgs:
    def __init__(__self__, *, field_to_match: pulumi.Input[ByteMatchSetByteMatchTupleFieldToMatchArgs], positional_constraint: pulumi.Input[_builtins.str], text_transformation: pulumi.Input[_builtins.str], target_string: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> pulumi.Input[ByteMatchSetByteMatchTupleFieldToMatchArgs]:
        
        ...
    
    @field_to_match.setter
    def field_to_match(self, value: pulumi.Input[ByteMatchSetByteMatchTupleFieldToMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @positional_constraint.setter
    def positional_constraint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_transformation.setter
    def text_transformation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetString")
    def target_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_string.setter
    def target_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ByteMatchSetByteMatchTupleFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ByteMatchSetByteMatchTupleFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeoMatchSetGeoMatchConstraintArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class GeoMatchSetGeoMatchConstraintArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IpSetIpSetDescriptorArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class IpSetIpSetDescriptorArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RateBasedRulePredicateArgsDict(TypedDict):
    data_id: pulumi.Input[_builtins.str]
    negated: pulumi.Input[_builtins.bool]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class RateBasedRulePredicateArgs:
    def __init__(__self__, *, data_id: pulumi.Input[_builtins.str], negated: pulumi.Input[_builtins.bool], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_id.setter
    def data_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def negated(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @negated.setter
    def negated(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RegexMatchSetRegexMatchTupleArgsDict(TypedDict):
    field_to_match: pulumi.Input[RegexMatchSetRegexMatchTupleFieldToMatchArgsDict]
    regex_pattern_set_id: pulumi.Input[_builtins.str]
    text_transformation: pulumi.Input[_builtins.str]


@pulumi.input_type
class RegexMatchSetRegexMatchTupleArgs:
    def __init__(__self__, *, field_to_match: pulumi.Input[RegexMatchSetRegexMatchTupleFieldToMatchArgs], regex_pattern_set_id: pulumi.Input[_builtins.str], text_transformation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> pulumi.Input[RegexMatchSetRegexMatchTupleFieldToMatchArgs]:
        
        ...
    
    @field_to_match.setter
    def field_to_match(self, value: pulumi.Input[RegexMatchSetRegexMatchTupleFieldToMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetId")
    def regex_pattern_set_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @regex_pattern_set_id.setter
    def regex_pattern_set_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_transformation.setter
    def text_transformation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RegexMatchSetRegexMatchTupleFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegexMatchSetRegexMatchTupleFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleGroupActivatedRuleArgsDict(TypedDict):
    action: pulumi.Input[RuleGroupActivatedRuleActionArgsDict]
    priority: pulumi.Input[_builtins.int]
    rule_id: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RuleGroupActivatedRuleArgs:
    def __init__(__self__, *, action: pulumi.Input[RuleGroupActivatedRuleActionArgs], priority: pulumi.Input[_builtins.int], rule_id: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[RuleGroupActivatedRuleActionArgs]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[RuleGroupActivatedRuleActionArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RuleGroupActivatedRuleActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class RuleGroupActivatedRuleActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RulePredicateArgsDict(TypedDict):
    data_id: pulumi.Input[_builtins.str]
    negated: pulumi.Input[_builtins.bool]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class RulePredicateArgs:
    def __init__(__self__, *, data_id: pulumi.Input[_builtins.str], negated: pulumi.Input[_builtins.bool], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataId")
    def data_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_id.setter
    def data_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def negated(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @negated.setter
    def negated(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SizeConstraintSetSizeConstraintArgsDict(TypedDict):
    comparison_operator: pulumi.Input[_builtins.str]
    field_to_match: pulumi.Input[SizeConstraintSetSizeConstraintFieldToMatchArgsDict]
    size: pulumi.Input[_builtins.int]
    text_transformation: pulumi.Input[_builtins.str]


@pulumi.input_type
class SizeConstraintSetSizeConstraintArgs:
    def __init__(__self__, *, comparison_operator: pulumi.Input[_builtins.str], field_to_match: pulumi.Input[SizeConstraintSetSizeConstraintFieldToMatchArgs], size: pulumi.Input[_builtins.int], text_transformation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @comparison_operator.setter
    def comparison_operator(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> pulumi.Input[SizeConstraintSetSizeConstraintFieldToMatchArgs]:
        
        ...
    
    @field_to_match.setter
    def field_to_match(self, value: pulumi.Input[SizeConstraintSetSizeConstraintFieldToMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_transformation.setter
    def text_transformation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SizeConstraintSetSizeConstraintFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SizeConstraintSetSizeConstraintFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SqlInjectionMatchSetSqlInjectionMatchTupleArgsDict(TypedDict):
    field_to_match: pulumi.Input[SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgsDict]
    text_transformation: pulumi.Input[_builtins.str]


@pulumi.input_type
class SqlInjectionMatchSetSqlInjectionMatchTupleArgs:
    def __init__(__self__, *, field_to_match: pulumi.Input[SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgs], text_transformation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> pulumi.Input[SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgs]:
        
        ...
    
    @field_to_match.setter
    def field_to_match(self, value: pulumi.Input[SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_transformation.setter
    def text_transformation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SqlInjectionMatchSetSqlInjectionMatchTupleFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebAclDefaultActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WebAclDefaultActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WebAclLoggingConfigurationArgsDict(TypedDict):
    log_destination: pulumi.Input[_builtins.str]
    redacted_fields: NotRequired[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsArgsDict]]


@pulumi.input_type
class WebAclLoggingConfigurationArgs:
    def __init__(__self__, *, log_destination: pulumi.Input[_builtins.str], redacted_fields: Optional[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @log_destination.setter
    def log_destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactedFields")
    def redacted_fields(self) -> Optional[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsArgs]]:
        
        ...
    
    @redacted_fields.setter
    def redacted_fields(self, value: Optional[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsArgs]]): # -> None:
        ...
    


class WebAclLoggingConfigurationRedactedFieldsArgsDict(TypedDict):
    field_to_matches: pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgsDict]]]


@pulumi.input_type
class WebAclLoggingConfigurationRedactedFieldsArgs:
    def __init__(__self__, *, field_to_matches: pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatches")
    def field_to_matches(self) -> pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs]]]:
        
        ...
    
    @field_to_matches.setter
    def field_to_matches(self, value: pulumi.Input[Sequence[pulumi.Input[WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs]]]): # -> None:
        ...
    


class WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebAclRuleArgsDict(TypedDict):
    priority: pulumi.Input[_builtins.int]
    rule_id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[WebAclRuleActionArgsDict]]
    override_action: NotRequired[pulumi.Input[WebAclRuleOverrideActionArgsDict]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebAclRuleArgs:
    def __init__(__self__, *, priority: pulumi.Input[_builtins.int], rule_id: pulumi.Input[_builtins.str], action: Optional[pulumi.Input[WebAclRuleActionArgs]] = ..., override_action: Optional[pulumi.Input[WebAclRuleOverrideActionArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_id.setter
    def rule_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[WebAclRuleActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[WebAclRuleActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> Optional[pulumi.Input[WebAclRuleOverrideActionArgs]]:
        
        ...
    
    @override_action.setter
    def override_action(self, value: Optional[pulumi.Input[WebAclRuleOverrideActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebAclRuleActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WebAclRuleActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WebAclRuleOverrideActionArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WebAclRuleOverrideActionArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class XssMatchSetXssMatchTupleArgsDict(TypedDict):
    field_to_match: pulumi.Input[XssMatchSetXssMatchTupleFieldToMatchArgsDict]
    text_transformation: pulumi.Input[_builtins.str]


@pulumi.input_type
class XssMatchSetXssMatchTupleArgs:
    def __init__(__self__, *, field_to_match: pulumi.Input[XssMatchSetXssMatchTupleFieldToMatchArgs], text_transformation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> pulumi.Input[XssMatchSetXssMatchTupleFieldToMatchArgs]:
        
        ...
    
    @field_to_match.setter
    def field_to_match(self, value: pulumi.Input[XssMatchSetXssMatchTupleFieldToMatchArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformation")
    def text_transformation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_transformation.setter
    def text_transformation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class XssMatchSetXssMatchTupleFieldToMatchArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    data: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class XssMatchSetXssMatchTupleFieldToMatchArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], data: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


