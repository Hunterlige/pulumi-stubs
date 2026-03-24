import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BranchRuleArgs", "BranchRule"]

@pulumi.input_type
class BranchRuleArgs:
    def __init__(
        __self__,
        *,
        branch_rule_id: pulumi.Input[_builtins.str],
        include_pattern: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        repository_id: pulumi.Input[_builtins.str],
        allow_stale_reviews: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        minimum_approvals_count: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_reviews_count: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        require_comments_resolved: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_linear_history: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_pull_request: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchRuleId")
    def branch_rule_id(self) -> pulumi.Input[_builtins.str]: ...
    @branch_rule_id.setter
    def branch_rule_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="includePattern")
    def include_pattern(self) -> pulumi.Input[_builtins.str]: ...
    @include_pattern.setter
    def include_pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Input[_builtins.str]: ...
    @repository_id.setter
    def repository_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowStaleReviews")
    def allow_stale_reviews(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_stale_reviews.setter
    def allow_stale_reviews(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumApprovalsCount")
    def minimum_approvals_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_approvals_count.setter
    def minimum_approvals_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumReviewsCount")
    def minimum_reviews_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_reviews_count.setter
    def minimum_reviews_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireCommentsResolved")
    def require_comments_resolved(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_comments_resolved.setter
    def require_comments_resolved(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireLinearHistory")
    def require_linear_history(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_linear_history.setter
    def require_linear_history(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requirePullRequest")
    def require_pull_request(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_pull_request.setter
    def require_pull_request(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _BranchRuleState:
    def __init__(
        __self__,
        *,
        allow_stale_reviews: Optional[pulumi.Input[_builtins.bool]] = ...,
        branch_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_approvals_count: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_reviews_count: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        require_comments_resolved: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_linear_history: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_pull_request: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowStaleReviews")
    def allow_stale_reviews(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_stale_reviews.setter
    def allow_stale_reviews(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="branchRuleId")
    def branch_rule_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_rule_id.setter
    def branch_rule_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includePattern")
    def include_pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_pattern.setter
    def include_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumApprovalsCount")
    def minimum_approvals_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_approvals_count.setter
    def minimum_approvals_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumReviewsCount")
    def minimum_reviews_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum_reviews_count.setter
    def minimum_reviews_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_id.setter
    def repository_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requireCommentsResolved")
    def require_comments_resolved(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_comments_resolved.setter
    def require_comments_resolved(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireLinearHistory")
    def require_linear_history(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_linear_history.setter
    def require_linear_history(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="requirePullRequest")
    def require_pull_request(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_pull_request.setter
    def require_pull_request(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:securesourcemanager/branchRule:BranchRule")
class BranchRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_stale_reviews: Optional[pulumi.Input[_builtins.bool]] = ...,
        branch_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_approvals_count: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_reviews_count: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        require_comments_resolved: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_linear_history: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_pull_request: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: BranchRuleArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_stale_reviews: Optional[pulumi.Input[_builtins.bool]] = ...,
        branch_rule_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_pattern: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_approvals_count: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum_reviews_count: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
        require_comments_resolved: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_linear_history: Optional[pulumi.Input[_builtins.bool]] = ...,
        require_pull_request: Optional[pulumi.Input[_builtins.bool]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> BranchRule: ...
    @_builtins.property
    @pulumi.getter(name="allowStaleReviews")
    def allow_stale_reviews(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="branchRuleId")
    def branch_rule_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="includePattern")
    def include_pattern(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumApprovalsCount")
    def minimum_approvals_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="minimumReviewsCount")
    def minimum_reviews_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requireCommentsResolved")
    def require_comments_resolved(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="requireLinearHistory")
    def require_linear_history(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="requirePullRequest")
    def require_pull_request(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
