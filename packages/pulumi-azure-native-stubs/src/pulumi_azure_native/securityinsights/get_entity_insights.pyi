import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetEntityInsightsResult",
    "AwaitableGetEntityInsightsResult",
    "get_entity_insights",
    "get_entity_insights_output",
]

@pulumi.output_type
class GetEntityInsightsResult:
    def __init__(__self__, meta_data=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> Optional[outputs.GetInsightsResultsMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.EntityInsightItemResponse]]: ...

class AwaitableGetEntityInsightsResult(GetEntityInsightsResult):
    def __await__(self): ...

def get_entity_insights(
    add_default_extended_time_range: Optional[_builtins.bool] = ...,
    end_time: Optional[_builtins.str] = ...,
    entity_id: Optional[_builtins.str] = ...,
    insight_query_ids: Optional[Sequence[_builtins.str]] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    start_time: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetEntityInsightsResult: ...
def get_entity_insights_output(
    add_default_extended_time_range: Optional[
        pulumi.Input[Optional[_builtins.bool]]
    ] = ...,
    end_time: Optional[pulumi.Input[_builtins.str]] = ...,
    entity_id: Optional[pulumi.Input[_builtins.str]] = ...,
    insight_query_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetEntityInsightsResult]: ...
