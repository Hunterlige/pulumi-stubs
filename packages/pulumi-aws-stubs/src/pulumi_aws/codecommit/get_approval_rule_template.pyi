import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetApprovalRuleTemplateResult",
    "AwaitableGetApprovalRuleTemplateResult",
    "get_approval_rule_template",
    "get_approval_rule_template_output",
]

@pulumi.output_type
class GetApprovalRuleTemplateResult:
    def __init__(
        __self__,
        approval_rule_template_id=...,
        content=...,
        creation_date=...,
        description=...,
        id=...,
        last_modified_date=...,
        last_modified_user=...,
        name=...,
        region=...,
        rule_content_sha256=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRuleTemplateId")
    def approval_rule_template_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedUser")
    def last_modified_user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleContentSha256")
    def rule_content_sha256(self) -> _builtins.str: ...

class AwaitableGetApprovalRuleTemplateResult(GetApprovalRuleTemplateResult):
    def __await__(self): ...

def get_approval_rule_template(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetApprovalRuleTemplateResult: ...
def get_approval_rule_template_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetApprovalRuleTemplateResult]: ...
