import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StreamingJobArgs", "StreamingJob"]

@pulumi.input_type
class StreamingJobArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        cluster: Optional[pulumi.Input[ClusterInfoArgs]] = ...,
        compatibility_level: Optional[
            pulumi.Input[Union[_builtins.str, CompatibilityLevel]]
        ] = ...,
        content_storage_policy: Optional[
            pulumi.Input[Union[_builtins.str, ContentStoragePolicy]]
        ] = ...,
        data_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        events_late_arrival_max_delay_in_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        events_out_of_order_max_delay_in_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        events_out_of_order_policy: Optional[
            pulumi.Input[Union[_builtins.str, EventsOutOfOrderPolicy]]
        ] = ...,
        functions: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionArgs]]]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        inputs: Optional[pulumi.Input[Sequence[pulumi.Input[InputArgs]]]] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_storage_account: Optional[pulumi.Input[JobStorageAccountArgs]] = ...,
        job_type: Optional[pulumi.Input[Union[_builtins.str, JobType]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        output_error_policy: Optional[
            pulumi.Input[Union[_builtins.str, OutputErrorPolicy]]
        ] = ...,
        output_start_mode: Optional[
            pulumi.Input[Union[_builtins.str, OutputStartMode]]
        ] = ...,
        output_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[pulumi.Input[Sequence[pulumi.Input[OutputArgs]]]] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transformation: Optional[pulumi.Input[TransformationArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[ClusterInfoArgs]]: ...
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[ClusterInfoArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CompatibilityLevel]]]: ...
    @compatibility_level.setter
    def compatibility_level(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CompatibilityLevel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentStoragePolicy")
    def content_storage_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ContentStoragePolicy]]]: ...
    @content_storage_policy.setter
    def content_storage_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ContentStoragePolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataLocale")
    def data_locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_locale.setter
    def data_locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventsLateArrivalMaxDelayInSeconds")
    def events_late_arrival_max_delay_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @events_late_arrival_max_delay_in_seconds.setter
    def events_late_arrival_max_delay_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventsOutOfOrderMaxDelayInSeconds")
    def events_out_of_order_max_delay_in_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @events_out_of_order_max_delay_in_seconds.setter
    def events_out_of_order_max_delay_in_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="eventsOutOfOrderPolicy")
    def events_out_of_order_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EventsOutOfOrderPolicy]]]: ...
    @events_out_of_order_policy.setter
    def events_out_of_order_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EventsOutOfOrderPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def functions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FunctionArgs]]]]: ...
    @functions.setter
    def functions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FunctionArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[InputArgs]]]]: ...
    @inputs.setter
    def inputs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InputArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_name.setter
    def job_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobStorageAccount")
    def job_storage_account(self) -> Optional[pulumi.Input[JobStorageAccountArgs]]: ...
    @job_storage_account.setter
    def job_storage_account(
        self, value: Optional[pulumi.Input[JobStorageAccountArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[Union[_builtins.str, JobType]]]: ...
    @job_type.setter
    def job_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, JobType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputErrorPolicy")
    def output_error_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputErrorPolicy]]]: ...
    @output_error_policy.setter
    def output_error_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputErrorPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputStartMode")
    def output_start_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutputStartMode]]]: ...
    @output_start_mode.setter
    def output_start_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutputStartMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputStartTime")
    def output_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_start_time.setter
    def output_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OutputArgs]]]]: ...
    @outputs.setter
    def outputs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OutputArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def transformation(self) -> Optional[pulumi.Input[TransformationArgs]]: ...
    @transformation.setter
    def transformation(self, value: Optional[pulumi.Input[TransformationArgs]]): ...

@pulumi.type_token("azure-native:streamanalytics:StreamingJob")
class StreamingJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster: Optional[
            pulumi.Input[Union[ClusterInfoArgs, ClusterInfoArgsDict]]
        ] = ...,
        compatibility_level: Optional[
            pulumi.Input[Union[_builtins.str, CompatibilityLevel]]
        ] = ...,
        content_storage_policy: Optional[
            pulumi.Input[Union[_builtins.str, ContentStoragePolicy]]
        ] = ...,
        data_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        events_late_arrival_max_delay_in_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        events_out_of_order_max_delay_in_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        events_out_of_order_policy: Optional[
            pulumi.Input[Union[_builtins.str, EventsOutOfOrderPolicy]]
        ] = ...,
        functions: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[FunctionArgs, FunctionArgsDict]]]]
        ] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[InputArgs, InputArgsDict]]]]
        ] = ...,
        job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        job_storage_account: Optional[
            pulumi.Input[Union[JobStorageAccountArgs, JobStorageAccountArgsDict]]
        ] = ...,
        job_type: Optional[pulumi.Input[Union[_builtins.str, JobType]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        output_error_policy: Optional[
            pulumi.Input[Union[_builtins.str, OutputErrorPolicy]]
        ] = ...,
        output_start_mode: Optional[
            pulumi.Input[Union[_builtins.str, OutputStartMode]]
        ] = ...,
        output_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        outputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[OutputArgs, OutputArgsDict]]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transformation: Optional[
            pulumi.Input[Union[TransformationArgs, TransformationArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StreamingJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> StreamingJob: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[Optional[outputs.ClusterInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentStoragePolicy")
    def content_storage_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataLocale")
    def data_locale(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="eventsLateArrivalMaxDelayInSeconds")
    def events_late_arrival_max_delay_in_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="eventsOutOfOrderMaxDelayInSeconds")
    def events_out_of_order_max_delay_in_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="eventsOutOfOrderPolicy")
    def events_out_of_order_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def functions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.FunctionResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Optional[Sequence[outputs.InputResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobState")
    def job_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobStorageAccount")
    def job_storage_account(
        self,
    ) -> pulumi.Output[Optional[outputs.JobStorageAccountResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastOutputEventTime")
    def last_output_event_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputErrorPolicy")
    def output_error_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputStartMode")
    def output_start_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputStartTime")
    def output_start_time(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Optional[Sequence[outputs.OutputResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def transformation(
        self,
    ) -> pulumi.Output[Optional[outputs.TransformationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
